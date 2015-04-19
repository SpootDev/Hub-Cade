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

# create db
try:
    os.remove('game_database.db')
except:
    pass
conn = connect('game_database.db')
curs = conn.cursor()
#conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")

# create table game_category
curs.execute('''create table game_category (gc_id integer primary key, gc_category text)''')
curs.execute('''CREATE INDEX gc_category_ndx on game_category (gc_category)''')  # so can build category faster

# create table game_info
curs.execute('''create table game_info (gi_id integer primary key, gi_system_id numeric, gi_short_name text, gi_long_name text, gi_alternate_title text, gi_description text, gi_cloneof text, gi_romof text, gi_cart_interface text, gi_serial text, gi_year text, gi_release text, gi_publisher integer, gi_author text, gi_gc_category integer, gi_is_mech integer, gi_num_monitors integer, gi_monitor_id integer, gi_players integer, gi_buttons integer, gi_joy_way text, gi_status integer, gi_emulation integer, gi_color integer, gi_sound integer, gi_graphic integer, gi_palettesize integer, gi_savestate integer)''')
curs.execute('''CREATE INDEX gi_system_id_ndx on game_info (gi_system_id);''')  # so can match systems quickly
curs.execute('''CREATE INDEX gi_is_mech_ndx on game_info (gi_is_mech);''')  # to be able to throw out mechanicals from audit
curs.execute('''CREATE INDEX gi_gc_category_ndx on game_info (gi_gc_category);''')  # to filter by category
curs.execute('''CREATE INDEX gi_monitor_ndx on game_info (gi_monitor_id);''')  # to match with monitor tye

# create table game_info_roms
curs.execute('''create table game_info_roms (gir_id integer primary key, gir_gi_id integer, gir_rom_name text, gir_merged_rom_name text, gir_crc32 text, gir_sha1 text, gir_size numeric, gir_offset numeric)''')
curs.execute('''CREATE INDEX gir_gi_id_ndx on game_info_roms (gir_gi_id);''')  # to match the roms to the games
curs.execute('''CREATE INDEX gir_crc32_ndx on game_info_roms (gir_crc32);''')  # to match crc32
curs.execute('''CREATE INDEX gir_sha1_ndx on game_info_roms (gir_sha1);''')  # to match sha1

# create table game_systems
curs.execute('''create table game_systems (gs_id integer primary key, gs_system_name text,gs_system_source_file text,gs_system_long_name text,gs_system_description text,gs_system_year text,gs_system_manufacturer integer,gs_system_status integer,gs_system_emulation integer,gs_system_color integer,gs_system_sound integer,gs_system_graphic integer,gs_system_savestate integer,gs_system_cart_interface text,gs_system_palette integer,gs_system_monitor_id)''')
curs.execute('''CREATE INDEX gs_system_name_ndx on game_systems (gs_system_name);''')  # to match the system names

# create table game_systems_roms
curs.execute('''create table game_systems_roms (gsr_id integer primary key, gsr_gs_id integer, gsr_rom_name text, gsr_crc32 text, gsr_sha1 text, gsr_size numeric, gsr_offset text)''')
curs.execute('''CREATE INDEX gsr_gs_id_ndx on game_systems_roms (gsr_gs_id);''')  # to match the roms to the systems
curs.execute('''CREATE INDEX gsr_crc32_ndx on game_systems_roms (gsr_crc32);''')  # to match crc32
curs.execute('''CREATE INDEX gsr_sha1_ndx on game_systems_roms (gsr_sha1);''')  # to match sha1

# create table game_systems_publisher
curs.execute('''create table game_systems_publisher (gsp_id integer primary key, gsp_publisher text)''')
curs.execute('''CREATE INDEX gsp_publisher_ndx on game_systems_publisher (gsp_publisher);''')  # to match the roms/systems to publishers

# create table game_systems_author
curs.execute('''create table game_systems_author (gsa_id integer primary key, gsa_author text)''')
curs.execute('''CREATE INDEX gsa_author_ndx on game_systems_author (gsa_author);''')  # to match the roms/systems to authors

# create table game_systems_emulation_status
curs.execute('''create table game_systems_emulation_status (gses_id integer primary key, gses_status_text text)''')
curs.execute('''CREATE INDEX gses_status_text_ndx on game_systems_emulation_status (gses_status_text);''')  # to match the roms/systems to emulation status

# create table game_systems_monitor
curs.execute('''create table game_monitor (gm_id integer primary key, gm_type text, gm_rotate integer, gm_width integer, gm_height integer, gm_refresh integer)''')
curs.execute('''CREATE INDEX gm_monitor_ndx on game_monitor (gm_type,gm_rotate,gm_width,gm_height,gm_refresh);''')  # to match the roms/systems to monitor

# close db files
conn.commit()
conn.close