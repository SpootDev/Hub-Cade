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

# import built in sqlite3 support
from sqlite3 import *

conn = connect('game_database.db')
curs = conn.cursor()
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")

infile = open("messinfo.dat","r")
start_system_read = False
skip_next_line = False
long_name_next = False
desc_next = False
wip_in_progress = False
romset_in_progress = False
# store args to sql
sys_shortname = ""
sys_longname = None
sys_manufacturer = None
sys_year = None
sys_desc = None
sys_emulation = None
sys_color = None
sys_sound = None
sys_graphics = None
sys_save_state = None
sys_wip = ""
sys_romset = None

sql_string = ""
while 1:
    line = infile.readline()
    if not line:
        break;
    if skip_next_line == True:
        skip_next_line = False
    else:
        if line.find("DRIVERS INFO") != -1:  # stop at drivers
            break;
        line = line.replace("    ","")
        if line[0] == "#" or len(line) < 4 or line.find("$mame") == 0:  # skip comments and blank lines
            if line.find("$mame") == 0:
                skip_next_line = True
                long_name_next = True
            pass
        elif line.find("$info") == 0:  # found so begin start system read
            start_system_read = True
            # load the short name
            sys_short_name = line.split('=')[1]
        elif line.find("Emulation:") == 0:  # found so begin start system read
            sys_emulation = line.split(' ')[1]
        elif line.find("Color:") == 0:  # found so begin start system read
            sys_color = line.split(' ')[1]
        elif line.find("Sound:") == 0:  # found so begin start system read
            sys_sound = line.split(' ')[1]
        elif line.find("Graphics:") == 0:  # found so begin start system read
            sys_graphics = line.split(' ')[1]
        elif line.find("Save State:") == 0:  # found so begin start system read
            if line.rsplit(' ',1)[1][:-1] == "Supported":
                sys_save_state = 1
            else:
                sys_save_state = 0
        elif line.find("WIP:") == 0:  # found so begin start system read
            wip_in_progress = True
        elif line.find("Romset:") == 0:  # found so begin start system read
            wip_in_progress = False
            romset_in_progress = True
        else:
            if wip_in_progress == True and line.find("Romset:") != 0:
                # sys_wip += line[:-1] + "<BR>"
                pass
            if romset_in_progress == True and line.find("$end") != 0:
                # sys_romset += line[:-1] + "<BR>"
                pass
            if desc_next == True:
                sys_desc = line
                desc_next = False
            if long_name_next == True:
                #print "huh:",len(line),line
                try:
                    sys_longname,sys_manufacturer,sys_year = line.split(',')
                except:
                    sys_longname,msys_manufacturer,sys_year = line.rsplit(',',2)
                long_name_next = False
                desc_next = True
            if line.find("$end") == 0:  # end of system info so store system into db
                romset_in_progress = False
                sql_args = sys_short_name[:-1],sys_longname,sys_manufacturer,sys_year[:-1],sys_desc[:-1],sys_emulation[:-1],sys_color[:-1],sys_sound[:-1],sys_graphics[:-1],sys_save_state
                #print sql_args
                quick_sql_args = sys_short_name[:-1],
                curs.execute("select count(*) from game_systems where gs_system_name = ?",quick_sql_args)
                if int(curs.fetchone()[0]) > 0:
                    if sys_desc[:-1] == "...":
                        sys_desc = None
                    else:
                        sys_desc = sys_desc[:-1]
                    quick_sql_args = sys_desc,sys_short_name[:-1]
                    curs.execute(u"update game_systems set gs_system_description = ? where gs_system_name = ?",quick_sql_args)
                else:
                    curs.execute(u"insert into game_systems (gs_id,gs_system_name,gs_system_long_name,gs_system_manufacturer,gs_system_year,gs_system_description,gs_system_emulation,gs_system_color,gs_system_sound,gs_system_graphic,gs_system_savestate) values (NULL,?,?,?,?,?,?,?,?,?,?)",sql_args)
                sys_wip = None
                sys_romset = None
conn.commit()
conn.close