'''
  Copyright (C) 2015 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''

# include python mods
import os,string

# import built in sqlite3 support
from sqlite3 import *

# open the database
conn = connect('game_database.db')
curs = conn.cursor()
curs.execute('PRAGMA temp_store=MEMORY;')
curs.execute('PRAGMA journal_mode=MEMORY;')
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")

# load xml parse mod
from xml.dom import minidom
doc = minidom.parse('mame.xml')

def status_lookup(status_text):
    # lookup/store the system status_text
    global curs
    quick_sql_args = status_text,
    result_value = "0"
    if status_text != None:
        curs.execute('''select gses_id from game_systems_emulation_status where gses_status_text = ?''',quick_sql_args)
        result_value = curs.fetchone()
        if result_value == None:
            curs.execute('''insert into game_systems_emulation_status (gses_id,gses_status_text) values (NULL,?);''',quick_sql_args)
            # grab id from new record and insert the status
            curs.execute('''SELECT last_insert_rowid()''')
            status_text = str(curs.fetchone()[0])
        else:
            status_text = str(result_value[0])
    return status_text


def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

def getElement(element):
    return getText(element.childNodes)

def handleMameRoms(mame_game):
    roms_list = []
    first_rom = True
    rom_info_list = mame_game.getElementsByTagName("rom")
    for sql_system_rom_name in rom_info_list:
        try:
            roms_list_data = (sql_system_rom_name.getAttribute("name"),sql_system_rom_name.getAttribute("crc"),sql_system_rom_name.getAttribute("sha1"),sql_system_rom_name.getAttribute("size"),sql_system_rom_name.getAttribute("offset"),sql_system_rom_name.getAttribute("merge"))
            roms_list.append(roms_list_data)
            first_rom = False
        except:
            # store the NULL's so the join will work
            if first_rom == False:
                roms_list_data = None,None,None,None,None
                roms_list.append(roms_list_data)
            break;
    return roms_list

def handleMameGames(games):
    global cat_dictionary
    for mame_game in games:
        # reset all sql data fields
        sql_game_source_file = None
        sql_game_description = None
        sql_game_year = None
        sql_game_manufacturer = None
        sql_game_cloneof = None
        sql_game_romof = None
        sql_game_mech = "0"

        # load data into the fields
        sql_game_name = mame_game.getAttribute("name")
        try:
            sql_game_source_file = mame_game.getAttribute("sourcefile")
            if len(sql_game_source_file) <= 1:
                sql_game_source_file = None
        except:
            sql_game_source_file = None
        try:
            sql_game_cloneof = mame_game.getAttribute("cloneof")
            if len(sql_game_cloneof) <= 1:
                sql_game_cloneof = None
        except:
            sql_game_cloneof = None
        try:
            sql_game_romof = mame_game.getAttribute("romof")
            if len(sql_game_romof) <= 1:
                sql_game_romof = None
        except:
            sql_game_romof = None
        try:
            sql_game_mech = mame_game.getAttribute("ismechanical")
            if len(sql_game_mech) <= 1:
                sql_game_mech = "0"
        except:
            sql_game_mech = "0"
        if sql_game_mech == "yes":
            sql_game_mech = "1"

        try:
            sql_game_description = getElement(mame_game.getElementsByTagName("description")[0])
        except:
            pass
        try:
            sql_game_year = getElement(mame_game.getElementsByTagName("year")[0])
        except:
            pass
        try:
            sql_game_manufacturer = getElement(mame_game.getElementsByTagName("manufacturer")[0])
            # lookup/store the manufacturer/publisher
            if sql_game_manufacturer != None and len(sql_game_manufacturer) > 0:
                quick_sql_args = sql_game_manufacturer,
                result_value = "0"
                curs.execute('''select gsp_id from game_systems_publisher where gsp_publisher = ?''',quick_sql_args)
                result_value = curs.fetchone()
                if result_value == None:
                    curs.execute('''insert into game_systems_publisher (gsp_id,gsp_publisher) values (NULL,?);''',quick_sql_args)
                    # grab id from new record and insert the publisher
                    curs.execute('''SELECT last_insert_rowid()''')
                    sql_game_manufacturer = str(curs.fetchone()[0])
                else:
                    sql_game_manufacturer = str(result_value[0])
            else:
                sql_game_manufacturer = "0"
        except:
            pass
        # get input information
        try:
            sql_input_data = mame_game.getElementsByTagName("input")[0]
            sql_game_players = sql_input_data.getAttribute("players")
            sql_game_buttons = sql_input_data.getAttribute("buttons")
            sql_input_control = sql_input_data.getElementsByTagName("control")
            first_control = True
            sql_input_type = ""
            for control_type in sql_input_control:
                try:
                    if first_control == False:
                        sql_input_type += "|"
                    sql_input_type += (control_type.getAttribute("type") + ": " + control_type.getAttribute("ways"))
                    first_control = False
                except:
                    if first_control == True:
                        sql_input_type = None
                    break;
        except:
            sql_game_players = None
            sql_game_buttons = None
            sql_input_type = None
        try:
            sql_game_driver = mame_game.getElementsByTagName("driver")[0]
            sql_system_status = sql_game_driver.getAttribute("status")
            sql_system_emulation = sql_game_driver.getAttribute("emulation")
            sql_system_color = sql_game_driver.getAttribute("color")
            sql_system_sound = sql_game_driver.getAttribute("sound")
            sql_system_graphic = sql_game_driver.getAttribute("graphic")
            sql_system_savestate = sql_game_driver.getAttribute("savestate")
            if sql_system_savestate == "supported":
                sql_system_savestate = "1"
            else:
                sql_system_savestate = "0"
            sql_system_palettesize = sql_game_driver.getAttribute("palettesize")
            # lookup/store the system status
            sql_system_status = status_lookup(sql_system_status)
            # lookup/store the system emulation
            sql_system_emulation = status_lookup(sql_system_emulation)
            # lookup/store the system color
            sql_system_color = status_lookup(sql_system_color)
            # lookup/store the system sound
            sql_system_sound = status_lookup(sql_system_sound)
            # lookup/store the system graphics
            sql_system_graphic = status_lookup(sql_system_graphic)
        except:
            sql_system_status = None
            sql_system_emulation = None
            sql_system_color = None
            sql_system_sound = None
            sql_system_graphic = None
            sql_system_savestate = "0"
            sql_system_palettesize = None
        # find monitor type
        sql_num_monitors = mame_game.getElementsByTagName("display")
        sql_num_monitors = len(sql_num_monitors)
        if sql_num_monitors > 0:
            sql_game_display = mame_game.getElementsByTagName("display")[0]
            sql_system_display_type = sql_game_display.getAttribute("type")
            sql_system_display_rotate = sql_game_display.getAttribute("rotate")
            sql_system_display_width = sql_game_display.getAttribute("width")
            sql_system_display_height = sql_game_display.getAttribute("height")
            sql_system_display_refresh = sql_game_display.getAttribute("refresh")
        else:
            sql_system_display_type = None
            sql_system_display_rotate = None
            sql_system_display_width = None
            sql_system_display_height = None
            sql_system_display_refresh = None
        quick_sql_args = sql_system_display_type,sql_system_display_rotate,sql_system_display_width,sql_system_display_height,sql_system_display_refresh
        if sql_system_display_type != None:
            quick_sql_args = sql_system_display_type,sql_system_display_rotate,sql_system_display_width,sql_system_display_height,sql_system_display_refresh
            result_value = "0"
            curs.execute('''select gm_id from game_monitor where gm_type = ? and gm_rotate = ? and gm_width = ? and gm_height = ? and gm_refresh = ?''',quick_sql_args)
            result_value = curs.fetchone()
            if result_value == None:
                curs.execute('''insert into game_monitor (gm_id,gm_type,gm_rotate,gm_width,gm_height,gm_refresh) values (NULL,?,?,?,?,?);''',quick_sql_args)
                # grab id from new record and insert the monitor
                curs.execute('''SELECT last_insert_rowid()''')
                sql_system_monitor_id = str(curs.fetchone()[0])
            else:
                sql_system_monitor_id = str(result_value[0])
        else:
            sql_system_display_type = "0"
        # set cat value to 0 so can have other program update/insert the categoryies
        cat_value = 0
        # see if exists then need to update
        quick_sql_args = sql_game_name,
        curs.execute('''select count(*) from game_info where gi_short_name = ? and gi_system_id = 0''',quick_sql_args)
        if int(curs.fetchone()[0]) > 0:
            sql_args = sql_game_name,sql_game_description,sql_game_cloneof,sql_game_romof,sql_game_year,sql_game_manufacturer,cat_value,sql_game_mech,sql_num_monitors,sql_system_monitor_id,sql_game_players,sql_game_buttons,sql_input_type,sql_system_status,sql_system_emulation,sql_system_color,sql_system_sound,sql_system_graphic,sql_system_palettesize,sql_system_savestate,sql_game_name
            curs.execute('''update game_info set gi_short_name = ?, gi_long_name = ?, gi_cloneof = ?, gi_romof = ?, gi_year = ?, gi_publisher = ?, gi_gc_category = ?, gi_is_mech = ?, gi_num_monitors = ?, gi_monitor_id = ?, gi_players = ?, gi_buttons = ?, gi_joy_way = ?, gi_status = ?, gi_emulation = ?, gi_color = ?, gi_sound = ?, gi_graphic = ?, gi_palettesize = ?, gi_savestate = ? where gi_short_name = ? and gi_system_id = 0;''',sql_args)
# should prob check crc32/sha1...but no those could change.....remove ALL rom rows and add new ones on an update.....it'll be easier
        else:
            sql_args = "0",sql_game_name,sql_game_description,sql_game_cloneof,sql_game_romof,sql_game_year,sql_game_manufacturer,cat_value,sql_game_mech,sql_num_monitors,sql_system_monitor_id,sql_game_players,sql_game_buttons,sql_input_type,sql_system_status,sql_system_emulation,sql_system_color,sql_system_sound,sql_system_graphic,sql_system_palettesize,sql_system_savestate
            curs.execute('''insert into game_info (gi_id, gi_system_id, gi_short_name, gi_long_name, gi_cloneof, gi_romof, gi_year, gi_publisher, gi_gc_category, gi_is_mech, gi_num_monitors, gi_monitor_id, gi_players, gi_buttons, gi_joy_way, gi_status, gi_emulation, gi_color, gi_sound, gi_graphic, gi_palettesize, gi_savestate) values (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',sql_args)
            # grab id from new record and insert the roms
            curs.execute('''SELECT last_insert_rowid()''')
            # insert the roms info
            last_id = curs.fetchone()[0]
            for rom_info in handleMameRoms(mame_game):
                quick_sql_args = last_id,rom_info[0],rom_info[1],rom_info[2],rom_info[3],rom_info[4],rom_info[5]
                curs.execute('''insert into game_info_roms (gir_id, gir_gi_id, gir_rom_name, gir_crc32, gir_sha1, gir_size, gir_offset,gir_merged_rom_name) values (NULL,?,?,?,?,?,?,?);''',quick_sql_args)

# create mame game list
mame_game_list = doc.getElementsByTagName("game")
handleMameGames(mame_game_list)

# close db files
conn.commit()
conn.close