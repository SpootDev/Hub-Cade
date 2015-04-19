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

# open the database
conn = connect('game_database.db')
curs = conn.cursor()
curs_cat = conn.cursor()
curs_cat_update = conn.cursor()
curs_cat_update.execute('PRAGMA temp_store=MEMORY;')
curs_cat_update.execute('PRAGMA journal_mode=MEMORY;')
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")

# read the category file and create dict/list for it
cat_file = open("Category.ini","rb")
cat_dictionary = {}
category = ""
while 1:
    line = cat_file.readline()
    #print "line: ",line
    if not line:
        break;
    if line.find("[") == 0:
        category = line.replace("[","").replace("]","").replace(" ","").rstrip('\n').rstrip('\r') # wipe out space to make the category table
    elif len(line) > 1:
        quick_sql_args = category,
        curs.execute('''select gc_id from game_category where gc_category = ?''',quick_sql_args)
        for sql_row in curs:
            result_value = sql_row[0]
            if result_value == None:
                result_value = "0"
            cat_dictionary[line.strip()] = result_value
            break

# grab all system 0 in db as those are mame
curs.execute("select gi_id,gi_short_name from game_info where gi_system_id = 0 and gi_gc_category = 0")
for sql_row in curs.fetchall():
    # since not all games have cat's go a try/catch
    try:
        sql_args = cat_dictionary[sql_row[1]],sql_row[0]
        curs.execute("update game_info set gi_gc_category = ? where gi_id = ?",sql_args)
    except:
        pass

# grab all the non parent roms that aren't set
curs.execute("select gi_id,gi_cloneof from game_info where gi_system_id = 0 and gi_cloneof IS NOT NULL and gi_gc_category = 0")
for sql_row in curs.fetchall():
    sql_args = sql_row[1],
    curs_cat.execute("select gi_gc_category from game_info where gi_short_name = ?",sql_args)
    for sql_cat_row in curs_cat:
        sql_args = sql_cat_row[0],sql_row[0]
        curs_cat_update.execute("update game_info set gi_gc_category = ? where gi_id = ?",sql_args)
        break

# close db files
conn.commit()
conn.close