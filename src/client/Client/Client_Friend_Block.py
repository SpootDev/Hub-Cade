# import globals
import Client_GlobalData

# import templates
from Client_Template_Friend_Block import *

# import sql mod
from sqlite3 import *

class FriendBlockDialog ( FriendBlockTemplate ):

    def OnFriendBlockInit( self, event ):
        Client_GlobalData.curs_player.execute("select player_name,player_friend,player_block_chat from player_info order by player_name")
        for sql_row in Client_GlobalData.curs_player:
            if sql_row[1] == 1:
                self.friendblock_friend_listbox.Append(sql_row[0])
            if sql_row[2] == 1:
                self.friendblock_block_listbox.Append(sql_row[0])
        event.Skip()

    def OnFriendBlockRemoveFriendMenuItem( self, event ):
        for index in self.friendblock_friend_listbox.GetSelections():
            sql_statement = u"delete from player_info where player_name = \"" + self.friendblock_friend_listbox.GetString(index) + u"\" and player_friend = 1"
            Client_GlobalData.curs_player.execute(sql_statement)
            self.friendblock_friend_listbox.Delete(index)
        Client_GlobalData.conn_player.commit()
        event.Skip()

    def OnFriendBlockRemoveBlockMenuItem( self, event ):
        for index in self.friendblock_block_listbox.GetSelections():
            sql_statement = u"delete from player_info where player_name = \"" + self.friendblock_block_listbox.GetString(index) + u"\" and player_block_chat = 1"
            Client_GlobalData.curs_player.execute(sql_statement)
            self.friendblock_block_listbox.Delete(index)
        Client_GlobalData.conn_player.commit()
        event.Skip()
