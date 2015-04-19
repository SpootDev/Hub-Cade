# import globals
import Client_GlobalData

# import python mods
import sys, os

# import code
from Client_INIParser import *
import Client_MainFrame

# import template
from Client_Template_Set_Directories import *

# global for adding all rom directories
rom_dirs = []

# grab mdd from agw
try:
    from agw import multidirdialog as MDD
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.multidirdialog as MDD

class SetDirectoriesDialog(SetDirectoriesDialogTemplate):
    def initDialog(self, event):
        iniParser = INIParser("mame.ini")
        romPaths = iniParser.getRomPaths()
        #print romPaths
        self.directoryListbox.Freeze()
        for x in xrange(0,len(romPaths)):
            self.directoryListbox.Append(romPaths[x].decode("utf8"))
        self.directoryListbox.Thaw()

    def closeDialog(self,event):
        event.Skip()
        iniParser = INIParser("mame.ini")
        romPaths = iniParser.getRomPaths()
        if romPaths != self.directoryListbox.GetItems():
            Client_GlobalData.needAudit=True
        newDirectories = str(';').join(self.directoryListbox.GetItems()).replace("\\","/").encode("utf8")
        if '../roms' not in newDirectories:
            newDirectories = '../roms;' + newDirectories
            Client_GlobalData.needAudit=True
        iniParser.setRomPaths(newDirectories)
        iniParser = INIParser("mess.ini")
        iniParser.setRomPaths(newDirectories)

    def OnSetFolder_Button( self, event ):
        event.Skip()
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.directoryListbox.Append(dlg.GetPath().replace("\\","/"))
        dlg.Destroy()

    def addNewDirectory( self, event ):
        event.Skip()
        if len(self.setfolder_text_control.GetValue()):
            self.directoryListbox.Append(self.setfolder_text_control.GetValue().replace("\\","/"))
            self.setfolder_text_control.SetValue("")

    def OnMultiDirButton( self, event ):
        dlg = MDD.MultiDirDialog(None, title="Browse for Folder(s)", defaultPath=os.getcwd(),agwStyle=MDD.DD_MULTIPLE|MDD.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() != wx.ID_OK:
            dlg.Destroy()
            return
        paths = dlg.GetPaths()
        self.directoryListbox.Freeze()
        for indx, path in enumerate(paths):
            #print "path: ",path
            if str.upper(sys.platform[0:3])=='WIN' \
            or str.upper(sys.platform[0:3])=='CYG':
                path = path.split("(")[1].replace(")","")
            self.directoryListbox.Append(path.replace("\\","/"))
        self.directoryListbox.Thaw()
        dlg.Destroy()

    def removeSelectedDirectory(self,event):
        # must do in reverse as the index will be removed on delete
        self.directoryListbox.Freeze()
        for index in sorted(self.directoryListbox.GetSelections(), reverse=True):
            self.directoryListbox.Delete(index)
        self.directoryListbox.Thaw()
        event.Skip()

    def OnAutoAddDirButton( self, event ):
        global rom_dirs
        rom_dirs = []
        dialog = wx.DirDialog(None, "Choose Main Directory to Parse:", style=1 )
        if dialog.ShowModal() == wx.ID_OK:
            self.find_rom_dirs(dialog.GetPath())
        dialog.Destroy()
        if len(rom_dirs) > 0:
            self.directoryListbox.Freeze()
            for rom_path in rom_dirs:
                if self.directoryListbox.FindString(rom_path.replace("\\","/")) < 0:
                    self.directoryListbox.Append(rom_path.replace("\\","/"))
            self.directoryListbox.Thaw()

    def find_rom_dirs(self,base_directory):
        global rom_dirs
        for file_name in os.listdir(base_directory):
            path = os.path.join(base_directory, file_name)
            if os.path.isdir(path):
                if file_name.lower() == "roms" or file_name.lower() == "rom"  or file_name.lower() == "bios":
                    rom_dirs.append(path)
                self.find_rom_dirs(path)