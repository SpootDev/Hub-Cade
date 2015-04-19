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
import os,string,sys

# import built in sqlite3 support
from sqlite3 import *

# open the database
conn = connect('game_database.db')
curs = conn.cursor()
conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")

def parse_files(files,path):
    crc32_value = None
    sha1_value = None
    game_name_value = None
    game_long_name_value = None
    game_status_value = None
    game_year_value = None
    game_man_value = None
    for fname in files:
        #print "fname:",fname
        sys_id_to_store = None
        # find system id from mess
        file_name, ext = os.path.splitext(fname)
        # file_name needs to _flop, _cart etc cut off
        # can't do this as some systems have a _ in the name - file_name = file_name.rsplit("_",1)[0]
        file_name = file_name.replace("_cart","").replace("_cass","").replace("_flop","").replace("_rom","").replace("_disk","").replace("_hdd","")
        if ext == ".hsi" or ext == ".xml":
            sql_args = file_name,
            curs.execute("select gs_id from game_systems where gs_system_name = ?",sql_args)
            row = curs.fetchone()
            if row == None:
                #print "file:",file_name
                sys_id_to_store = None
            else:
                sys_id_to_store = str(row[0])
            hash_file = None
            if str.upper(sys.platform[0:3])=='WIN' \
            or str.upper(sys.platform[0:3])=='CYG':
                hash_file = open(path + "\\" + fname,"rb")
            else:
                hash_file = open(path + "/" + fname,"rb")
            while 1:
                line = hash_file.readline()
                if not line:
                    break;
                crc32_local = line.find("crc32=\"")
                if crc32_local > 0:
##                    sha1_value = "NULL"
##                    game_name_value = "NULL"
##                    game_status_value = "NULL"
##                    game_year_value = "NULL"
##                    game_man_value = "NULL"
                    end_pos = line.find("\"",(crc32_local + 7))
                    crc32_value = line[(crc32_local + 7):end_pos]
                    #print "crc:",crc32_value
                else:
                    crc32_local = line.find("crc=\"")
                    if crc32_local > 0:
                        #print "line:",line
##                        sha1_value = "NULL"
##                        game_name_value = "NULL"
##                        game_status_value = "NULL"
##                        game_year_value = "NULL"
##                        game_man_value = "NULL"
                        end_pos = line.find("\"",(crc32_local + 5))
                        crc32_value = line[(crc32_local + 5):end_pos]
                #print "crc:",crc32_value
                sha1_local = line.find("sha1=\"")
                if sha1_local > 0:
                    end_pos = line.find("\"",(sha1_local + 6))
                    sha1_value = line[(sha1_local + 6):end_pos]

                if line.find("<description>") > 0:
                    game_long_name_value = line.replace("<description>","").replace("</description>","").strip()

                if line.find("<year>") > 0:
                    game_year_value = line.replace("<year>","").replace("</year>","").strip()

                if line.find("<manufacturer>") > 0:
                    game_man_value = line.replace("<manufacturer>","").replace("</manufacturer>","").strip()
                else:
                    if line.find("<publisher>") > 0:
                        game_man_value = line.replace("<publisher>","").replace("</publisher>","").strip()

                name_local = line.find("name=\"")
                if name_local > 0:
                    end_pos = line.find("\"",(name_local + 6))
                    game_name_value = line[(name_local + 6):end_pos]
                    # lookup/store the manufacturer/publisher
##                    if game_man_value != "NULL":
##                        print "man1:",game_man_value
                    if game_man_value != None and len(game_man_value) > 0:
                        quick_sql_args = game_man_value,
                        result_value = "0"
                        curs.execute('''select gsp_id from game_systems_publisher where gsp_publisher = ?''',quick_sql_args)
                        result_value = curs.fetchone()
                        if result_value == None:
                            curs.execute('''insert into game_systems_publisher (gsp_id,gsp_publisher) values (NULL,?);''',quick_sql_args)
                            # grab id from new record and insert the publisher
                            curs.execute('''SELECT last_insert_rowid()''')
                            game_man_value = str(curs.fetchone()[0])
                        else:
                            game_man_value = str(result_value[0])
                    else:
                        game_man_value = "0"

                    # build args and insert the record
                    sql_args = sys_id_to_store,game_name_value,game_long_name_value,game_status_value,game_year_value,game_man_value
                    curs.execute("insert into game_info (gi_id,gi_system_id,gi_short_name,gi_long_name,gi_status,gi_year,gi_publisher,gi_gc_category) values (NULL,?,?,?,?,?,?,0)",sql_args)
                    # grab id from new record and insert the roms
                    curs.execute('''SELECT last_insert_rowid()''')
                    # insert the roms info
                    last_id = curs.fetchone()[0]
                    # insert the roms for the game
                    sql_args = last_id,crc32_value,sha1_value
                    curs.execute("insert into game_info_roms (gir_id,gir_gi_id,gir_crc32,gir_sha1) values (NULL,?,?,?)",sql_args)
                    sha1_value = None
                    game_name_value = None
                    game_long_name_value = None
                    game_status_value = None
                    game_year_value = None
                    game_man_value = None


# find hashes to load
files = []
path="./hash"  # insert the path to the directory of interest
dirList=os.listdir(path)
for file_name in dirList:
    files.append(file_name)
parse_files(files,path)

# find hashes to load from mess xmls from wiki
files = []
path = "./mess_software_list_xml"
dirList=os.listdir(path)
for file_name in dirList:
    files.append(file_name)
parse_files(files,path)

# close db files
conn.commit()
conn.close