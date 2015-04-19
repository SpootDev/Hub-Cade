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

# open db
conn = connect('game_database.db')
curs = conn.cursor()

# read the category file and insert of update records
cat_file = open("Category.ini","rb")
while 1:
    line = cat_file.readline()
    if not line:
        break;
    if line.find("[") == 0:
        category = line.replace("[","").replace("]","").replace(" ","").rstrip('\n').rstrip('\r') # wipe out space to make the category table
        sql_args = category.strip(),
        curs.execute("select count(*) from game_category where gc_category = ?",sql_args)
        if int(curs.fetchone()[0]) == 0:
            curs.execute("insert into game_category (gc_id, gc_category) values (NULL,?)",sql_args)
# check to see if zero record exists and add if not
curs.execute("select count(*) from game_category where gc_id = 0")
if int(curs.fetchone()[0]) == 0:
    curs.execute("insert into game_category (gc_id, gc_category) values (0,'NA')")
# close db files
conn.commit()
conn.close