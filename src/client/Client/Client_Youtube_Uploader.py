# import python mods
import threading,os

# import wxWidgets files
import wx

# inport all the template files
from Client_Template_Youtube_Uploader import *

# import globals
import Client_GlobalData

class YoutubeUploader( YoutubeUploaderTemplate, threading.Thread ):
    def padSpaces(self,string,length):
        while len(string)<length:
            string = string + " "
        return string

    def __init__( self, parent ):

        threading.Thread.__init__(self)
        YoutubeUploaderTemplate.__init__( self, parent )
        self.emailText.SetValue(Client_GlobalData.player.email)

        rootdir = "../snap"
        self.fileTextMap = {}
        for root, subFolders, files in os.walk(rootdir):
            for file in files:
                if file[-4:] == 'webm':
                    self.fileTextMap[self.padSpaces(root.replace("../snap\\",""),20) + str(time.ctime(os.path.getctime(os.path.join(root,file))))] = os.path.join(root,file)
        print self.fileTextMap

        if len(self.fileTextMap)==0:
            mdial = wx.MessageDialog(None, "You haven't recorded any videos yet, press shift-F12 while playing to start recording a video and then shift+F12 again to stop", 'No videos found', wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
            mdial.ShowModal()
            mdial.Destroy()
            self.Close(True)
            return

        self.videoChoice.AppendItems(self.fileTextMap.keys())

    def upload(self, event):
        self.exitButton.Enable(False)
        self.uploadButton.Enable(False)
        mdial = wx.MessageDialog(None, "This may take awhile to upload.  During the upload, you can't leave this dialog.  Be patient!", 'Be patient', wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
        mdial.ShowModal()
        mdial.Destroy()
        self.start()

    def run(self):
        try:
            if self.addKeywordsCheckbox.IsChecked():
                self.keywordsText.AppendText(" mamehub, mame, online")
            if self.addTitleCheckbox.IsChecked():
                self.titleText.AppendText(" - MAMEHub")
            print 'UPLOADING ',self.fileTextMap[self.videoChoice.GetStringSelection().encode('ascii','ignore')]
            parameters = [
                "--email="+self.emailText.GetValue().encode('ascii','ignore'),
                "--password="+self.passwordText.GetValue().encode('ascii','ignore'),
                "--title="+self.titleText.GetValue().encode('ascii','ignore'),
                "--description="+self.descriptionText.GetValue().encode('ascii','ignore'),
                "--category=Games",
                "--keywords="+self.keywordsText.GetValue().encode('ascii','ignore'),
                self.fileTextMap[self.videoChoice.GetStringSelection().encode('ascii','ignore')]
                ]
            if self.privateCheckBox.IsChecked():
                parameters.append("--private")
            url = youtube_upload.main_upload( parameters )
            if self.privateCheckBox.IsChecked()==False:
                Client_GlobalData.networkProtocol.sendString("CHAT_MESSAGE I just uploaded a video \""+self.titleText.GetValue().encode('ascii','ignore')+"\"!  Check it out here: "+url)
            mdial = wx.MessageDialog(None, "Video uploaded! Check the chat window for a link if the video was public", 'Video uploaded', wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
            mdial.ShowModal()
            mdial.Destroy()
        except Exception as e:
            mdial = wx.MessageDialog(None, "Error uploading video of type "+str(type(e))+": "+str(e)+" (args: "+str(e.args)+") stack: "+traceback.format_exc(), 'Error uploading video', wx.OK | wx.ICON_ERROR | wx.STAY_ON_TOP)
            mdial.ShowModal()
            mdial.Destroy()
        self.Close()

    def exit(self, event):
        self.Close()
