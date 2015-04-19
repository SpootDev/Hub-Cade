# import div for "proper" no floor division
from __future__ import division

# import wxWidgets files
import wx
import wx.grid as gridlib
import wx.html as html
import wx.media

# import globals
import Client_GlobalData
import Client_GlobalData_Config

# inport all the template files
from Client_Template_Chat_View import *
from Client_Template_Config import *
from Client_Template_Friend_Block import *
from Client_Template_Game_Lobby import *
from Client_Template_Host_Game_Dialog import *
from Client_Template_Main import *
from Client_Template_Program_Entry import *
from Client_Template_Set_Directories import *
from Client_Template_Youtube_Uploader import *

# import code files
from Client_Chat_View import *
from Client_Config import *
from Client_Friend_Block import *
from Client_Game_Lobby import *
from Client_Host_Game import *
from Client_MainApp import *
from Client_Program_Entry import *
from Client_Set_Directories import *
from Client_TaskBar_Icon import *
from Client_Youtube import *
#import Client_IPCountryMap

# import localization
import locale
locale.setlocale(locale.LC_ALL, '')

# import PIL
import Image

# import python mods
import platform,sys
import multiprocessing
import multiprocessing.forking

# determine platform and setup upnpc
if platform.architecture()[0][0:2]=='32':
    Client_GlobalData.messName = "./csmess"
    Client_GlobalData.mameName = "./csmame"
else:
    Client_GlobalData.messName = "./csmess64"
    Client_GlobalData.mameName = "./csmame64"
if str.upper(sys.platform[0:3])=='WIN' \
or str.upper(sys.platform[0:3])=='CYG':
    import miniupnpc
    Client_GlobalData.u = miniupnpc.UPnP()
    Client_GlobalData.editorName = "notepad.exe "
    Client_GlobalData.computer_os = 1
elif str.upper(sys.platform[0:3])=='DAR':
    import miniupnpc
    Client_GlobalData.u = miniupnpc.UPnP()
    Client_GlobalData.editorName = "open -e "
    Client_GlobalData.computer_os = 2
else:
    Client_GlobalData.editorName = "gedit "
    if platform.architecture()[0][0:2]=='32':
        # keep following code in case 32bit comes back
        #import miniupnpclinux32 as miniupnpc
        #Client_GlobalData.u = miniupnpc.UPnP()
        raise Exception("32-Bit linux is not supported")
    else:
        import miniupnpclinux64 as miniupnpc
        Client_GlobalData.u = miniupnpc.UPnP()
    Client_GlobalData.computer_os = 3

# open the db files
OpenDatabase()

# following code is for pyinstaller multiprocessing fix for one file in Windows
class _Popen(multiprocessing.forking.Popen):
    def __init__(self, *args, **kw):
        if hasattr(sys, 'frozen'):
            # We have to set _MEIPASS2 to get
            # --onefile and --onedir mode working.
            os.putenv('_MEIPASS2', sys._MEIPASS) # last character is stripped in C-loader
        try:
            super(_Popen, self).__init__(*args, **kw)
        finally:
            if hasattr(sys, 'frozen'):
                os.unsetenv('_MEIPASS2')

class Process(multiprocessing.Process):
    _Popen = _Popen

class SendeventProcess(Process):
    def __init__(self, resultQueue):
        self.resultQueue = resultQueue

        multiprocessing.Process.__init__(self)
        self.start()

    def run(self):
        #print 'SendeventProcess'
        self.resultQueue.put((1, 2))
        #print 'SendeventProcess'

# main app start
def main():
##    if os.path.isfile('settings.dat'):
##        try:
##            Client_GlobalData.settings = pickle.load(open('settings.dat','rb'))
##        except:
##            Client_GlobalData.settings = {}
##    else:
##        Client_GlobalData.settings = {}
    Client_GlobalData.app = MainApp(False)
    Client_GlobalData.app.MainLoop()
##    pickle.dump(Client_GlobalData.settings,open('settings.dat','wb'))
    # close the db files
    CloseDatabase()
    sys.exit(0)

if __name__ == '__main__':
    multiprocessing.freeze_support()
##    # following code is for pyinstaller multiprocessing fix for one file in Windows
##    if str.upper(sys.platform[0:3])=='WIN' \
##    or str.upper(sys.platform[0:3])=='CYG':
##        resultQueue = multiprocessing.Queue()
##        SendeventProcess(resultQueue)
##        if hasattr(sys, 'frozen'):
##            # We need to wait for all child processes otherwise
##            # --onefile mode won't work.
##            while multiprocessing.active_children():
##                multiprocessing.active_children()[0].join()
    main()
