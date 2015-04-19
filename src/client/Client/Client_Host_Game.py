# import globals
import Client_GlobalData

# import code
import Client_MainFrame

# import template
from Client_Template_Host_Game_Dialog import *

class HostGameDialog(HostGameDialogTemplate):
    def initDialog(self, event):
        gameList = Client_GlobalData.auditData.getNames("")
        Client_MainFrame.updateListIfDirty(
        self.gameList,
        gameList
        )

    def launch( self, event ):
        event.Skip()
        if len(self.roomName.GetLineText(0))==0:
            mdial = wx.MessageDialog(None, 'You must enter a room name.', 'Enter a room name', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
        elif Client_GlobalData.mamePopen is not None:
            mdial = wx.MessageDialog(None, 'You already have an instance of CSMAME running. Please close it first.', 'Close CSMAME First', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
        elif ' ' in self.roomName.GetLineText(0):
            mdial = wx.MessageDialog(None, 'No spaces in the room name please.', 'No spaces in the room name please', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
        else:
            romFile,cartPath = Client_GlobalData.auditData.getRomAndCartFileFromName(self.gameList.GetStringSelection().encode("utf8"))
            if len(romFile)==0:
                mdial = wx.MessageDialog(None, "Rom "+gameInstance.romFilename+" cannot be found.", 'ROM not found', wx.OK | wx.ICON_ERROR)
                mdial.ShowModal()
                mdial.Destroy()
            else:
                if self.publicCheckbox.IsChecked():
                    Client_GlobalData.database.createGameInstance(
                    self.gameList.GetStringSelection().encode("utf8"),
                    self.roomName.GetLineText(0).encode("utf8"),
                    '',
                    Client_GlobalData.player.ID,
                    self.maxPlayerSlider.GetValue(),
                    self.maxObserverSlider.GetValue()
                    )
                else:
                    Client_GlobalData.database.changePlayerStatus(Player.STATUS_PLAYING,-1)
                Client_GlobalData.hostedFiles = Client_GlobalData.auditData.getAllMAMEFilesFromName(self.gameList.GetStringSelection().encode("utf8"))
                if Client_GlobalData.os_video_playback == True:
                    Client_GlobalData.app.mainFrame.vid_playback_control.Pause()
                    Client_GlobalData.app.mainFrame.timer_slider.Stop()
                launchGame(romFile,cartPath,True,"",Client_GlobalData.selfPort,Client_GlobalData.selfPort)
                self.Close()

    def cancel( self, event ):
        event.Skip()
        self.Close()