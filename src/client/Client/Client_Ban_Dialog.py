# import globals
import Client_GlobalData
try:
    import cPickle as pickle
except:
    import pickle

# import templates
from Client_Template_Ban_Dialog import *

# import sql mod
from sqlite3 import *

# store the ban ids'
ban_id_list = []

class BanDialog ( BanDialogTemplate ):

    def initBanDialog(self, event):
        global ban_id_list
        ban_id_list = []
        ndx = 0
        self.ban_dialog_ban_grid.Freeze()
        for sql_row in tuple(pickle.loads(Client_GlobalData.generic_string)):
            #print "boo: ",sql_row
            self.ban_dialog_ban_grid.AppendRows(1)
            self.ban_dialog_ban_grid.SetCellValue(ndx, 0, sql_row[0])
            self.ban_dialog_ban_grid.SetCellValue(ndx, 1, sql_row[1])
            self.ban_dialog_ban_grid.SetCellValue(ndx, 2, str(sql_row[2]))
            self.ban_dialog_ban_grid.SetCellValue(ndx, 3, sql_row[3])
            self.ban_dialog_ban_grid.SetCellValue(ndx, 4, sql_row[4])
            self.ban_dialog_ban_grid.SetCellValue(ndx, 5, sql_row[5])
            ban_id_list.append(sql_row[6])
        self.ban_dialog_ban_grid.AutoSizeColumns(True)
        self.ban_dialog_ban_grid.AutoSizeRows(True)
        self.ban_dialog_ban_grid.Thaw()

    def Ban_Grab_Highlighted( self, remove_upgrade ):
        global ban_id_list
        return_string = None
        # must do in reverse as the index will be removed on delete
        for index in sorted(self.ban_dialog_ban_grid.GetSelections(), reverse=True):
            return_string += ban_id_list(index) + ","
            if remove_upgrade == 0:
                self.ban_dialog_ban_grid.Delete(index)
                ban_id_list.remove(index)
        return return_string

    def OnBanDialog_Remove_Ban_Button( self, event ):
        Client_GlobalData.networkProtocol.sendString("ADMIN_BAN_REMOVE "+ Ban_Grab_Highlighted(0))
        event.Skip()

    def OnBanDialog_Upgrade_Ban_Button( self, event ):
        Client_GlobalData.networkProtocol.sendString("ADMIN_BAN_UPGRADE "+ Ban_Grab_Highlighted(1))
        event.Skip()

