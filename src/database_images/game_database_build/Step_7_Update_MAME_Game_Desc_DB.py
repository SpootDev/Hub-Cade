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

game_titles = []
game_desc = ""
add_to_desc = False
history_file = open("history.dat","rb")
#curs.execute("BEGIN IMMEDIATE TRANSACTION");
while 1:
    line = history_file.readline()
    if not line:
        break;
    if line.find("$info=") == 0:
        game_titles = line.split("=",1)[1].split(",")
    elif line.find("$end") == 0:
        add_to_desc = False
        for game in game_titles:
            sql_args = game_desc,game
            curs.execute("update game_info set gi_description = ? where gi_short_name = ?",sql_args)
            game_desc = ""
    if add_to_desc == True:
        game_desc += line
    if line.find("$bio") == 0:
        add_to_desc = True
#curs.execute("COMMIT TRANSACTION");
# close db files
conn.commit()
conn.close