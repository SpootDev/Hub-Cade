# import templates
from Client_Template_MOTD import *

# import globals
import Client_GlobalData

class MOTDDialog ( MOTDTemplate ):

    def OnMOTDSaveText( self, event ):
        Client_GlobalData.motd_value = self.m_textCtrl12.GetValue()
        event.Skip()

    def OnMOTDDialogInit( self, event ):
        self.m_textCtrl12.SetValue(Client_GlobalData.motd_value)
        event.Skip()