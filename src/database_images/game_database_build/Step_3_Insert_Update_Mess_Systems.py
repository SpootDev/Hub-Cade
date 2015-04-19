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
import os

# import built in sqlite3 support
from sqlite3 import *

# load xml parse mod
from xml.dom import minidom
doc = minidom.parse('mess_xml_systems.txt')

# open the db files
conn = connect('game_database.db')
curs = conn.cursor()

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

def handleMessSystems(systems):
    for mess_system in systems:
        # reset all sql data fields
        sql_system_name = None
        sql_system_source_file = None
        sql_system_long_name = None
        sql_system_description = None
        sql_system_year = None
        sql_system_manufacturer = None
        # emulation status
        sql_system_status = None
        sql_system_emulation = None
        sql_system_color = None
        sql_system_sound = None
        sql_system_graphic = None
        sql_system_savestate = None
        sql_system_cart_interface = None
        sql_system_palettesize = None
        # display type
        sql_system_display_type = None
        sql_system_display_rotate = None
        sql_system_display_width = None
        sql_system_display_height = None
        sql_system_display_refresh = None
        # roms and hash
        sql_system_rom_name = []
        sql_string_rom_bios = []
        sql_string_rom_size = []
        sql_string_rom_crc32 = []
        sql_string_rom_sha1 = []
        # load data into the fields
        sql_system_name = mess_system.getAttribute("name")
        try:
            sql_system_source_file = mess_system.getAttribute("sourcefile")
            if len(sql_system_source_file) <= 1:
                sql_system_source_file = None
        except:
            sql_system_source_file = None
        # grab values for the system
        sql_system_long_name,sql_system_year,sql_system_manufacturer,sql_system_display_type,sql_system_display_rotate,sql_system_display_width,sql_system_display_height,sql_system_display_refresh,sql_system_status,sql_system_emulation,sql_system_color,sql_system_sound,sql_system_graphic,sql_system_savestate,sql_system_palettesize,sql_system_cart_interface = handleMessSystem(mess_system)
        # lookup/store the monitor id
        sql_system_monitor_id = "0"
        global curs
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
        # lookup/store the manufacturer/publisher
        if sql_system_manufacturer != None and len(sql_system_manufacturer) > 0:
            quick_sql_args = sql_system_manufacturer,
            result_value = "0"
            curs.execute('''select gsp_id from game_systems_publisher where gsp_publisher = ?''',quick_sql_args)
            result_value = curs.fetchone()
            if result_value == None:
                curs.execute('''insert into game_systems_publisher (gsp_id,gsp_publisher) values (NULL,?);''',quick_sql_args)
                # grab id from new record and insert the publisher
                curs.execute('''SELECT last_insert_rowid()''')
                sql_system_manufacturer = str(curs.fetchone()[0])
            else:
                sql_system_manufacturer = str(result_value[0])
        else:
            sql_system_manufacturer = "0"
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

        # build the sql args
        sql_args = sql_system_name,sql_system_source_file,sql_system_long_name,sql_system_description,sql_system_year,sql_system_manufacturer,sql_system_status,sql_system_emulation,sql_system_color,sql_system_sound,sql_system_graphic,sql_system_savestate,sql_system_cart_interface,sql_system_palettesize,sql_system_monitor_id
        # insert/update the values into the database
        #print "sql:",sql_args
        # see if exists then need to update
        quick_sql_args = sql_system_name,
        curs.execute('''select count(*) from game_systems where gs_system_name = ?''',quick_sql_args)
        if int(curs.fetchone()[0]) > 0:
            sql_args = sql_system_name,sql_system_source_file,sql_system_long_name,sql_system_description,sql_system_year,sql_system_manufacturer,sql_system_status,sql_system_emulation,sql_system_color,sql_system_sound,sql_system_graphic,sql_system_savestate,sql_system_cart_interface,sql_system_palettesize,sql_system_monitor_id,sql_system_name
            curs.execute('''update game_systems set gs_system_name = ?,gs_system_source_file = ?,gs_system_long_name = ?,gs_system_description = ?,gs_system_year = ?,gs_system_manufacturer = ?,gs_system_status = ?,gs_system_emulation = ?,gs_system_color = ?,gs_system_sound = ?,gs_system_graphic = ?,gs_system_savestate = ?,gs_system_cart_interface = ?,gs_system_palette = ?,gs_system_monitor_id = ? where gs_system_name = ?;''',sql_args)
        else:
            curs.execute('''insert into game_systems (gs_id,gs_system_name,gs_system_source_file,gs_system_long_name,gs_system_description,gs_system_year,gs_system_manufacturer,gs_system_status,gs_system_emulation,gs_system_color,gs_system_sound,gs_system_graphic,gs_system_savestate,gs_system_cart_interface,gs_system_palette,gs_system_monitor_id) values (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',sql_args)
            # grab id from new record and insert the roms
            curs.execute('''SELECT last_insert_rowid()''')
            # insert the roms info
            last_id = curs.fetchone()[0]
            for rom_info in handleMessRoms(mess_system):
                quick_sql_args = last_id,rom_info[0],rom_info[1],rom_info[2],rom_info[3],rom_info[4]
                curs.execute('''insert into game_systems_roms (gsr_id,gsr_gs_id,gsr_rom_name,gsr_crc32,gsr_sha1,gsr_size,gsr_offset) values (NULL,?,?,?,?,?,?);''',quick_sql_args)
            # insert the expanded cart info


##def handleMessCartType(mess_system):
##    try:
##        sql_system_rom_name.append(getElement(mess_system.getElementsByTagName("device")[0]))
##    except:
##        sql_system_rom_name.append("NULL")

def handleMessRoms(mess_system):
    roms_list = []
    first_rom = True
    rom_info_list = mess_system.getElementsByTagName("rom")
    for sql_system_rom_name in rom_info_list:
        try:
            roms_list_data = (sql_system_rom_name.getAttribute("name"),sql_system_rom_name.getAttribute("crc"),sql_system_rom_name.getAttribute("sha1"),sql_system_rom_name.getAttribute("size"),sql_system_rom_name.getAttribute("offset"))
            roms_list.append(roms_list_data)
            first_rom = False
        except:
            # store the NULL's so the join will work
            if first_rom == False:
                roms_list_data = None,None,None,None,None
                roms_list.append(roms_list_data)
            break;
    return roms_list

def handleMessSystem(mess_system):
    sql_system_long_name = getElement(mess_system.getElementsByTagName("description")[0])
    try:
        sql_system_year = getElement(mess_system.getElementsByTagName("year")[0])
    except:
        sql_system_year = None
    try:
        sql_system_manufacturer = getElement(mess_system.getElementsByTagName("manufacturer")[0])
    except:
        sql_system_manufacturer = None
    try:
        display_details = mess_system.getElementsByTagName("display")[0]
        sql_system_display_type = display_details.getAttribute("type")
        sql_system_display_rotate = display_details.getAttribute("rotate")
        sql_system_display_width = display_details.getAttribute("width")
        sql_system_display_height = display_details.getAttribute("height")
        sql_system_display_refresh = display_details.getAttribute("refresh")
    except:
        sql_system_display_type = None
        sql_system_display_rotate = None
        sql_system_display_width = None
        sql_system_display_height = None
        sql_system_display_refresh = None
    try:
        display_details = mess_system.getElementsByTagName("driver")[0]
        sql_system_status = display_details.getAttribute("status")
        sql_system_emulation = display_details.getAttribute("emulation")
        sql_system_color = display_details.getAttribute("color")
        sql_system_sound = display_details.getAttribute("sound")
        sql_system_graphic = display_details.getAttribute("graphic")
        if display_details.getAttribute("savestate") == "supported":
            sql_system_savestate = 1
        else:
            sql_system_savestate = 0
        sql_system_palettesize = display_details.getAttribute("palettesize")
    except:
        sql_system_status = None
        sql_system_emulation = None
        sql_system_color = None
        sql_system_sound = None
        sql_system_graphic = None
        sql_system_savestate = None
        sql_system_palettesize = None
    try:
        device_interface = mess_system.getElementsByTagName("device")[0]
        instance_interface = device_interface.getElementsByTagName("instance")[0]
        sql_system_cart_interface = instance_interface.getAttribute("briefname")
    except:
        sql_system_cart_interface = None
    return sql_system_long_name,sql_system_year,sql_system_manufacturer,sql_system_display_type,sql_system_display_rotate,sql_system_display_width,sql_system_display_height,sql_system_display_refresh,sql_system_status,sql_system_emulation,sql_system_color,sql_system_sound,sql_system_graphic,sql_system_savestate,sql_system_palettesize,sql_system_cart_interface

# create machine list
mess_system_list = doc.getElementsByTagName("machine")
handleMessSystems(mess_system_list)

# close db files
conn.commit()
conn.close