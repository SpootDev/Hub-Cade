# import built in sqlite3 support
from sqlite3 import *

# import globals
import Client_GlobalData

# setup/open all the database files
def OpenDatabase():
    #Client_GlobalData.conn.text_factory = lambda x: unicode(x, "utf-8", "ignore")
    Client_GlobalData.conn_player = connect('db/hubcade_gui.db')
    Client_GlobalData.curs_player = Client_GlobalData.conn_player.cursor()
    Client_GlobalData.conn_chat = connect('db/hubcade_chat.db')
    Client_GlobalData.curs_chat = Client_GlobalData.conn_chat.cursor()
    Client_GlobalData.conn_game = connect('db/game_database.db')
    Client_GlobalData.curs_game = Client_GlobalData.conn_game.cursor()
    Client_GlobalData.conn_game.text_factory = lambda x: unicode(x, "utf-8", "ignore")
    Client_GlobalData.curs_game.execute("attach database 'db/hubcade_gui.db' as gui_db")

# close all the database files
def CloseDatabase():
##    Client_GlobalData.curs.close()
##    Client_GlobalData.conn.close()
    Client_GlobalData.curs_player.close()
    Client_GlobalData.conn_player.close()
    Client_GlobalData.curs_chat.close()
    Client_GlobalData.conn_chat.close()
##    Client_GlobalData.curs_mess.close()
##    Client_GlobalData.conn_mess.close()
    Client_GlobalData.curs_game.close()
    Client_GlobalData.conn_game.close()

# check database versions and update them if nessecary
def CheckDBVersions():
    pass

# perform sql on hubcade_gui.db
def SQL_HubCade_Arrange_GUI(sql_statement):
    Client_GlobalData.curs_player.execute(sql_statement)
    Client_GlobalData.conn_player.commit()

def SQL_HubCade_Arrange_GUI_Args(sql_statement,sql_args):
    Client_GlobalData.curs_player.execute(sql_statement,sql_args)
    Client_GlobalData.conn_player.commit()

# perfrom sql on hubcade_chat.db
def SQL_HubCade_Arrange_Chat(sql_statement,sql_args):
    Client_GlobalData.curs_chat.execute(sql_statement,sql_args)
    Client_GlobalData.conn_chat.commit()

# increase game played instances
def DB_Game_Played_Increase(gameID):
    sql_args = gameID,
    try:
        Client_GlobalData.curs_player.execute(u"insert into game_info (game_rom_id,game_times_played,game_time_played,game_favorite) values (?,0,0,0)",sql_args)
    except:
        pass
    Client_GlobalData.curs_player.execute(u"update game_info set game_times_played = game_times_played + 1 where game_rom_id = ?",sql_args)
    Client_GlobalData.conn_player.commit()

# increase game played time
def DB_Game_Played_Time_Increase(gameID,time_played_seconds):
    # since the game increase should create the record I should only have to updatee
    sql_args = time_played_seconds,gameID
    Client_GlobalData.curs_player.execute(u"update game_info set game_time_played = game_time_played + ? where game_rom_id = ?",sql_args)
    Client_GlobalData.conn_player.commit()

# fetch game name from id
def SQL_Retrieve_Game_Name(game_id):
    sql_args = game_id,
    Client_GlobalData.curs_game.execute(u"select gi_long_name,gi_short_name from game_info where gi_id = ?",sql_args)
    for sql_row in Client_GlobalData.curs_game:
        if sql_row == None:
            return u"Unknown"
        else:
            if sql_row[0] != None:
                return str(sql_row[0])
            else:
                return str(sql_row[1])
        break;
    # should never get here
    return u"Unknown"

# fetch system name from game id
def SQL_Retrieve_Game_System_Name(game_id):
    sql_args = game_id,
    Client_GlobalData.curs_game.execute(u"select gs_system_long_name,gs_system_name from game_info,game_systems where gi_system_id = gs_id and gi_id = ?",sql_args)
    for sql_row in Client_GlobalData.curs_game:
        if sql_row == None:
            return u"Arcade"
        else:
            if sql_row[0] != None:
                return str(sql_row[0])
            else:
                return str(sql_row[1])
        break;
    # should never get here
    return u"Arcade"

# fetch the file name/rom patch from game id
def SQL_Retrieve_File_Path_SystemId(game_id):
    sql_args = game_id,
    Client_GlobalData.curs_game.execute("select gui_db.game_audit.ga_game_path,gi_system_id from gui_db.game_audit,game_info where gui_db.game_audit.ga_game_id = ? and gui_db.game_audit.ga_game_id = gi_id",sql_args)
    for sql_row in Client_GlobalData.curs_game:
        if sql_row == None:
            return u"Unknown",0
        else:
            return str(sql_row[0]),int(sql_row[1])
        break;
    # should never get here
    return u"Unknown",0

# fetch the categorys
def SQL_Fetch_Category():
    Client_GlobalData.curs_game.execute("select gc_id,gc_category from game_category order by gc_category asc")
    return Client_GlobalData.curs_game
