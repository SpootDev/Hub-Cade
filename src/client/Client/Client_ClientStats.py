# import globals
import Client_GlobalData

from Client_Template_ClientStats import *
from sqlite3 import *

class ClientStatsDialog ( ClientStatsTemplate ):

    def OnClientStatsDialogInit( self, event ):
        event.Skip()