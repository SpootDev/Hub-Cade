# import div for "proper" no floor division which is REQUIRED for the image resize....ie remove and DIE
from __future__ import division

# import python mods
from time import time
import webbrowser,subprocess
import operator
from operator import itemgetter, attrgetter
import struct
import platform

# import code
from Client_Audit_Error import *
from Client_Ban_Dialog import *
from Client_Cade_Main import *
from Client_Host_Game import *
from Client_Program_Entry import *
##if str.upper(sys.platform[0:3])=='WIN' \
##or str.upper(sys.platform[0:3])=='CYG':
##    import wx.lib.iewin as iewin
##    from Client_ActiveX_PDF import *
##else:
##    from Client_Cairo_PDF import *
import Client_Game
from Client_Chat_View import *
from Client_ClientStats import *
import Client_Database
from Client_Config import *
from Client_Friend_Block import *
#from Client_Game_Audit import *
from Client_Game_Audit_newway import *
from Client_Host_Game import *
import Client_INIParser
from Client_MOTD import *
from Client_Set_Directories import *
#import Client_ServerStats
from Client_Youtube_Uploader import *

# import embedded files
import Client_EmbeddedFiles

# import custom render codes
import Client_CustomClass_Grid_Render

# import base/io for image embedded file manipulation
import base64
from io import BytesIO

# inport all the template files
from Client_TaskBar_Icon import *
from Client_Template_Main import *

# import globals
import Client_GlobalData
import Client_GlobalData_Config

# import localization
import locale
locale.setlocale(locale.LC_ALL, '')

# import PIL for image conversion
from PIL import Image

# import compression mods
import pylzma
if str.upper(sys.platform[0:3])=='WIN' \
or str.upper(sys.platform[0:3])=='CYG':
    from py7zlib import Archive7z
import zipfile
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED
modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED:   'stored',
          }
from StringIO import StringIO
#from zipfile_infolist import print_info

class MediaType(object):
    def __init__(self,name,extensions):
        self.name = name
        self.extensions = extensions

def updateTreeIfDirtyNoRoot(treeControl,newItems):
    Client_GlobalData.game_tree_id = {}
    treeControl.Freeze()
    treeControl.DeleteAllItems()
    root = treeControl.AddRoot('Root')
    fillTree(treeControl,root,newItems)
    treeControl.Thaw()

def fillTree(treeControl,root,newItems):
    if type(newItems)==dict:
        for key,value in sorted(newItems.items()):
            subRoot = treeControl.AppendItem(root,key)
            fillTree(treeControl,subRoot,value)
    elif type(newItems)==list:
        for value in sorted(newItems):
            # to add columns look in the frame template
            child = treeControl.AppendItem(root,str(value[0].encode("utf8"))) # game name
            Client_GlobalData.game_tree_id[value[1][4]] = child
            treeControl.SetItemText(child, locale.format("%.0f", int(value[1][0]), 1), 1) # times played
            seconds_running = int(value[1][1])
            if seconds_running < 86400:
                treeControl.SetItemText(child, time.strftime('%H:%M:%S', time.gmtime(seconds_running)), 2) # time played
            else:
                treeControl.SetItemText(child, time.strftime('%d Day(s) %H:%M:%S', time.gmtime(seconds_running)), 2) # time played
            treeControl.SetItemText(child, str(value[1][2]), 3) # monitor
            treeControl.SetItemText(child, locale.format("%.0f", int(value[1][3]), 1), 4) # players
            treeControl.SetItemText(child, str(value[1][4]), 5) # game id
            treeControl.SetItemText(child, str(value[1][5]), 6) # category
            treeControl.SetItemText(child, str(value[1][1]), 7) # seconds played
            treeControl.SetColumnShown(5,0) # hide the game id
            treeControl.SetColumnShown(7,0) # hide the seconds played
    else:
        treeControl.AppendItem(root,newItems.encode("utf8"))
    # build/display the numbers of games per system(s)
    item, cookie = treeControl.GetFirstChild(root)
    while item.IsOk():
        if treeControl.GetChildrenCount(item) != 0:
            treeControl.SetItemText(item,treeControl.GetItemText(item) + " - " + locale.format("%.0f", treeControl.GetChildrenCount(item), 1))
        item, cookie = treeControl.GetNextChild(root, cookie)

def updateLabelIfDirty(label,actualLabel):
    if label.GetLabel() != actualLabel:
        label.SetLabel(actualLabel)

def updateGameGrid(self,actualListNew,grid):
    if Client_GlobalData.gui_update_hosted_game_grid == True:
        Client_GlobalData.gui_update_hosted_game_grid = False
        #print 'Updating list'
##        newlist = []
##        for x in xrange(0,len(actualList)):
##            newlist.append(actualList[x].decode("utf8"))
##        print "new: ",newlist
        # set the game info grid
        newlist = []
        for x in xrange(0,len(actualListNew)):
            newlist.append(actualListNew[x].decode("utf8"))
        grid.Freeze()
        if grid.GetNumberRows() > 0:
            grid.DeleteRows(0,grid.GetNumberRows())
        player_list_font = wx.Font(Client_GlobalData_Config.user_list_font_size, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL, False, Client_GlobalData_Config.user_list_font)
        color_to_use = Client_GlobalData_Config.user_list_font_color
        color_to_use = color_to_use.replace('(','')
        color_to_use = color_to_use.replace(')','')
        color_to_use = color_to_use.replace('-1','0')
        player_list_color = wx.Colour(int(color_to_use.split(',')[0]),int(color_to_use.split(',')[1]),int(color_to_use.split(',')[2]))
        current_epoch = float(time.time())
        for x in xrange(0,len(newlist)):
            #print "game list:",newlist[x]
            grid.AppendRows(1)
            grid.SetCellTextColour(x, 0, player_list_color)
            grid.SetCellFont(x,0,player_list_font)
            grid.SetCellTextColour(x, 1, player_list_color)
            grid.SetCellFont(x,1,player_list_font)
            grid.SetCellTextColour(x, 2, player_list_color)
            grid.SetCellFont(x,2,player_list_font)
            grid.SetCellTextColour(x, 3, player_list_color)
            grid.SetCellFont(x,3,player_list_font)
            grid.SetCellTextColour(x, 4, player_list_color)
            grid.SetCellFont(x,4,player_list_font)
            grid.SetCellValue(x, 0, newlist[x].decode("utf8").split('|')[0])  # host
            grid.SetCellValue(x, 1, newlist[x].decode("utf8").split('|')[1])  # game
            grid.SetCellValue(x, 2, newlist[x].decode("utf8").split('|')[2])  # players
            grid.SetCellValue(x, 3,time.strftime('%H:%M:%S %m/%d/%Y',time.localtime(float(newlist[x].decode("utf8").split('|')[3]))))  # time started
            # meh the seconds thing is kinda lame, but leaving code just in case
##            seconds_running = current_epoch- float(newlist[x].decode("utf8").split(' ')[3])
##            if seconds_running < 86400:
##                grid.SetCellValue(x, 3, time.strftime('%H:%M:%S', time.gmtime(seconds_running)))  # time started
##            else:
##                grid.SetCellValue(x, 3, time.strftime('%d Day(s) %H:%M:%S', time.gmtime(seconds_running)))  # time started
            grid.SetCellValue(x, 4, newlist[x].decode("utf8").split('|')[4])  # system)
        grid.AutoSizeColumns(True)
        grid.AutoSizeRows(True)
        grid.Thaw()

def updatePlayerGrid(self,grid,actualList):
    if Client_GlobalData.gui_update_user_grid == True:
        Client_GlobalData.gui_update_user_grid = False
        #print "playergrid:",actualList
        if Client_GlobalData_Config.user_list_sort == 0:  # country code
            actualList = sorted(actualList)
        else:  # user name
            actualList = sorted(actualList, key=operator.itemgetter(1))
        player_list_font = wx.Font(Client_GlobalData_Config.user_list_font_size, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL, False, Client_GlobalData_Config.user_list_font)
        color_to_use = Client_GlobalData_Config.user_list_font_color
        color_to_use = color_to_use.replace('(','')
        color_to_use = color_to_use.replace(')','')
        color_to_use = color_to_use.replace('-1','0')
        player_list_color = wx.Colour(int(color_to_use.split(',')[0]),int(color_to_use.split(',')[1]),int(color_to_use.split(',')[2]))
        grid.Freeze()
        if grid.GetNumberRows() > 0:
            grid.DeleteRows(0,grid.GetNumberRows())
        # populate flags images
        for x in xrange(0,len(actualList)):
            grid.AppendRows(1)
            # grab the flag png name = actualList[x].decode("utf8").split(' ')[0][1:3]
            flag_letter = ""
            try:
                flag_letter = actualList[x][0].lower()
            except:
                pass
            if flag_letter == "uk":
                flag_letter = "gb"
            try:
                image_data = wx.ImageFromStream(BytesIO(base64.b64decode(Client_EmbeddedFiles.embed_image_data["flag_" + flag_letter])))
            except:
                image_data = wx.ImageFromStream(BytesIO(base64.b64decode(Client_EmbeddedFiles.embed_image_data['os_unk'])))
            imageRenderer = Client_CustomClass_Grid_Render.GridImageRenderer(wx.BitmapFromImage(image_data))
            grid.SetCellRenderer(x,0,imageRenderer)
            grid.SetCellTextColour(x, 1, player_list_color)
            grid.SetCellFont(x,1,player_list_font)
            grid.SetCellTextColour(x, 2, player_list_color)
            grid.SetCellFont(x,2,player_list_font)
            grid.SetCellTextColour(x, 3, player_list_color)
            grid.SetCellFont(x,3,player_list_font)
            grid.SetCellTextColour(x, 5, player_list_color)
            grid.SetCellFont(x,5,player_list_font)
            if actualList[x][1] != "*Unknown*":
                grid.SetCellValue(x, 1, actualList[x][0])
            grid.SetCellValue(x, 2, actualList[x][1])
            # os image
            os_file_name = 'os_unk'
            if actualList[x][3] == "1":
                os_file_name = 'os_windows'
            elif actualList[x][3] == "2":
                os_file_name = 'os_mac'
            elif actualList[x][3] == "3":
                os_file_name = 'os_tux'
            image_data = wx.ImageFromStream(BytesIO(base64.b64decode(Client_EmbeddedFiles.embed_image_data[os_file_name])))
            imageRenderer = Client_CustomClass_Grid_Render.GridImageRenderer(wx.BitmapFromImage(image_data))
            grid.SetCellRenderer(x,4,imageRenderer)
            try:
                grid.SetCellValue(x, 3, actualList[x][2])
            except:
                pass
            grid.SetCellValue(x, 5, "Idle")
        grid.AutoSizeColumns(True)
        grid.AutoSizeRows(True)
        grid.Thaw()

# scale images to control panel
def ResizeImageCalc(img,size0,size1):
    picWidth = img.GetWidth()
    picHeight = img.GetHeight()
    scaleWidth =  float(size0 / picWidth)
    scaleHeight = float(size1 / picHeight)
    if scaleWidth > scaleHeight:
        scale = scaleHeight
    else:
        scale = scaleWidth
    NewWidth = picWidth * scale
    NewHeight = picHeight * scale
    return NewWidth,NewHeight

def launchGameByID(hostGameId,isServer,ipAddress,selfport,port):
    romFilename,systemId = Client_Database.SQL_Retrieve_File_Path_SystemId(hostGameId)
    print 'Connecting with selfport',selfport,'to',ipAddress,':',port
    Client_GlobalData.emuLogFile = open("../MAMElog.txt","wb")
    Client_GlobalData.emuLogFile.write(platform.platform())
    # this means launch MESS
    if systemId != 0:
        # look up the system for interface option(s)
        devicetype = None
        system_name = None
        sql_args = systemId,
        Client_GlobalData.curs_game.execute("select gs_system_cart_interface,gs_system_name from game_systems where gs_id = ?",sql_args)
        for row in Client_GlobalData.curs_game:
            if len(row[0]) > 0:
                devicetype = "-" + row[0]
                system_name = row[1]
        # begin launch of game
        if isServer:
            if devicetype != None:
                if devicetype == "-cdrm":
                    print 'Calling1 '+Client_GlobalData.messName+' with parameters',system_name,'-server',devicetype+' '+romFilename,'-cdrm '+chdname
                    Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.messName, system_name, "-username",Client_GlobalData.playerName,"-server",devicetype,romFilename,"-cdrm",chdname,"-port",str(port)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
                else:
                    print 'Calling2 '+Client_GlobalData.messName+' with parameters',system_name,'-server',devicetype+' '+romFilename #,'-cass '+chdname
                    #Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.messName, system_name, "-username",Client_GlobalData.playerName,"-server",devicetype,romFilename,"-cass",chdname,"-port",str(port)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
                    Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.messName, system_name, "-username",Client_GlobalData.playerName,"-server",devicetype,romFilename,"-port",str(port)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
            else:
                print 'Calling3 '+Client_GlobalData.messName+' with parameters',system_name,'-server',devicetype+' '+romFilename
                Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.messName, system_name, "-username",Client_GlobalData.playerName,"-server",devicetype,romFilename,"-port",str(port)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
        else:
            if devicetype != None:
                if devicetype == "-cdrm":
                    print 'Calling4 '+Client_GlobalData.messName+' with parameters',system_name,'-client',devicetype+' '+romFilename,'-cdrm '+chdname,'-hostname '+ipAddress
                    Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.messName, system_name, "-username",Client_GlobalData.playerName,"-client",devicetype,romFilename,"-cdrm",chdname,"-hostname",ipAddress,"-port",str(port),"-selfport",str(selfport)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
                else:
                    print 'Calling5 '+Client_GlobalData.messName+' with parameters',system_name,'-client',devicetype+' '+romFilename,'-cass '+chdname,'-hostname '+ipAddress
                    Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.messName, system_name, "-username",Client_GlobalData.playerName,"-client",devicetype,romFilename,"-cass",chdname,"-hostname",ipAddress,"-port",str(port),"-selfport",str(selfport)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
            else:
                print 'Calling6 '+Client_GlobalData.messName+' with parameters',system_name,'-client',devicetype+' '+romFilename,'-hostname '+ipAddress
                Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.messName, system_name, "-username",Client_GlobalData.playerName,"-client",devicetype,romFilename,"-hostname",ipAddress,"-port",str(port),"-selfport",str(selfport)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
    else:
        # launch MAME
        if Client_GlobalData_Config.record_inp_on_mame == True:
            record_string_file_name = os.path.split(romFilename)[1].split('.')[0] +  "_" + time.strftime("%Y%m%d_%H%M%S") + ".inp"
            if isServer:
                print 'Calling '+Client_GlobalData.mameName+' with parameters',os.path.split(romFilename)[1],'-server'
                Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.mameName, os.path.split(romFilename)[1],"-record",record_string_file_name, "-username",Client_GlobalData.playerName,"-server","-port",str(port)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
            else:
                print 'Calling '+Client_GlobalData.mameName+' with parameters',os.path.split(romFilename)[1],'-client','-hostname',ipAddress
                Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.mameName, os.path.split(romFilename)[1],"-record",record_string_file_name, "-username",Client_GlobalData.playerName,"-client","-hostname",ipAddress,"-port",str(port),"-selfport",str(selfport)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
        # launch MAME without inp
        else:
            if isServer:
                print 'Calling '+Client_GlobalData.mameName+' with parameters',os.path.split(romFilename)[1],'-server'
                Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.mameName, os.path.split(romFilename)[1], "-username",Client_GlobalData.playerName,"-server","-port",str(port)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
            else:
                print 'Calling '+Client_GlobalData.mameName+' with parameters',os.path.split(romFilename)[1],'-client','-hostname',ipAddress
                Client_GlobalData.mamePopen = subprocess.Popen([Client_GlobalData.mameName, os.path.split(romFilename)[1], "-username",Client_GlobalData.playerName,"-client","-hostname",ipAddress,"-port",str(port),"-selfport",str(selfport)],bufsize=-1,stdin=subprocess.PIPE,stdout=Client_GlobalData.emuLogFile,stderr=subprocess.STDOUT)
    # update database with played instances and update globals for time started
    Client_Database.DB_Game_Played_Increase(hostGameId)
    Client_GlobalData.game_id = hostGameId
    Client_GlobalData.game_start_time = time.time()

class MainFrame(MainFrameTemplate):
    def __init__( self, parent ):
        MainFrameTemplate.__init__(self,parent)
        self.icon = wx.Icon('../images/HubCade.ico', wx.BITMAP_TYPE_ICO, 16, 16)
        self.SetIcon(self.icon)
        self.tbicon = HubCadeTaskBarIcon(None)
        self.tbicon.SetIcon(self.icon)
        TIMER_ID = wx.NewId()
        self.timer = wx.Timer(self,TIMER_ID)
        self.timer.Start(200,True)
        wx.EVT_TIMER(self,TIMER_ID,self.update)
        # timer for video slider update
        if Client_GlobalData.os_video_playback == True:
            timerid = wx.NewId()
            self.timer_slider = wx.Timer(self, timerid)
            wx.EVT_TIMER(self, timerid, self.OnVideoTimer)
        # timer for statusbar clock
        TIMER_ID = wx.NewId()
        self.clock_timer = wx.Timer(self,TIMER_ID)
        self.clock_timer.Start(1000)
        wx.EVT_TIMER(self,TIMER_ID,self.statusclockupdate)
        # timer for ping
        ping_seconds = 10
        if Client_GlobalData_Config.ping_timeframe == 0: # default 10 seconds
            pass
        elif Client_GlobalData_Config.ping_timeframe == 1: # 20 seconds
            ping_seconds = 20
        elif Client_GlobalData_Config.ping_timeframe == 2: # 30 seconds
            ping_seconds = 30
        elif Client_GlobalData_Config.ping_timeframe == 3: # 1 minute
            ping_seconds = 60
        else: # Client_GlobalData_Config.ping_timeframe == 4: # NONE
            ping_seconds = 0
        TIMER_ID = wx.NewId()
        self.ping_timer = wx.Timer(self,TIMER_ID)
        self.ping_timer.Start(ping_seconds * 1000)
        wx.EVT_TIMER(self,TIMER_ID,self.ping_update)

        self.auditing=False
        self.cyclesUntilFilter = 0
        self.gameSearchText.SetValue("")

    def closeFrame(self):
        try:
            self.tbicon.Destroy()
        except:
            pass
        Client_GlobalData.app.ExitMainLoop();

    def closeFrameEvent(self,evt):
        self.closeFrame()
        evt.Skip()

    def iconizeFrame(self,event):
        if str.upper(sys.platform[0:3])!='WIN':
            return #Mac/Linux doesn't support iconization
##        if 'iconizedBefore' not in Client_GlobalData.settings:
##            Client_GlobalData.settings['iconizedBefore'] = True
##            wx.MessageBox("Hub!Cade is now minimized to the system tray. To reopen hubcade, click the arcade machine icon in the system tray", "")
        print 'ICONIZING'
        self.Hide()
        #self.Show(False)
        #self.tbicon.SetIcon(self.icon)
        self.tbicon.ShowBalloonTip("Return to Hub!Cade","Click this icon to bring Hub!Cade back")

    def statusclockupdate (self,event):
        t = time.localtime(time.time())
        st = None
        if Client_GlobalData_Config.display_clock_24 == True:
            st = u"Current Time: " + time.strftime("%d-%b-%Y   %H:%M:%S", t).encode("utf8")
        else:
            st = u"Current Time: " + time.strftime("%d-%b-%Y   %I:%M:%S", t).encode("utf8")
        self.main_frame_status_bar.SetStatusText(st, 2)

    def ping_update (self,event):
        pass

    def update(self,event):
        while len(Client_GlobalData.messageBoxQueue):
            m = Client_GlobalData.messageBoxQueue[0]
            del Client_GlobalData.messageBoxQueue[0]
            wx.MessageBox(m[0],m[1])

        if Client_GlobalData.fileReceiverThread:
            if Client_GlobalData.fileReceiverThread.is_alive()==False:
                Client_GlobalData.fileReceiverThread = None
            else:
                if Client_GlobalData.fileReceiverProgressDialog is None:
                    Client_GlobalData.fileReceiverProgressDialog = \
                        wx.ProgressDialog("Download in progress","Please wait while files(s) are downloaded",100,None,0)
                Client_GlobalData.fileReceiverProgressDialog.Update(
                Client_GlobalData.fileReceiverThread.fileDone*100/Client_GlobalData.fileReceiverThread.fileSize
                )
        else:
            if Client_GlobalData.fileReceiverProgressDialog:
                Client_GlobalData.fileReceiverProgressDialog.Destroy()
                Client_GlobalData.fileReceiverProgressDialog = None
            #Don't audit while receiving
            if Client_GlobalData.needAudit:
                Client_GlobalData.needAudit=False
                self.performAudit()

        if Client_GlobalData.mamePopen is None:
            if Client_GlobalData.player:
                if Client_GlobalData.player.status == Client_Game.Player.STATUS_PLAYING:
                    print "here i am exiting the game"
                    Client_GlobalData.database.changePlayerStatus(Client_Game.Player.STATUS_LOBBY,-1)
                    total_play_time = (Client_GlobalData.game_start_time - time.time()) * -1
                    Client_Database.DB_Game_Played_Time_Increase(Client_GlobalData.game_id,total_play_time)
                    data = self.gameListTreeCtrl.GetItemText(Client_GlobalData.game_tree_id[Client_GlobalData.game_id],7)
                    seconds_running = float(data) + total_play_time
                    # now must refresh the time in the host tab
                    if seconds_running < 86400:
                        self.gameListTreeCtrl.SetItemText(Client_GlobalData.game_tree_id[Client_GlobalData.game_id], time.strftime('%H:%M:%S', time.gmtime(seconds_running)), 2)
                    else:
                        self.gameListTreeCtrl.SetItemText(Client_GlobalData.game_tree_id[Client_GlobalData.game_id], time.strftime('%d Day(s) %H:%M:%S', time.gmtime(seconds_running)), 2)
                    self.gameListTreeCtrl.SetItemText(Client_GlobalData.game_tree_id[Client_GlobalData.game_id], str(seconds_running), 7)
        else:
            retcode = Client_GlobalData.mamePopen.poll()
            if retcode is not None:
                if retcode==10:
                    mdial = wx.MessageDialog(None, 'The server didn\'t accept your connection.  Either you connected too early, the host has locked the game from new players, or there has been some other connection error.', 'Game is Locked', wx.OK | wx.ICON_ERROR)
                    mdial.ShowModal()
                    mdial.Destroy()
                elif retcode!=0:
                    mdial = wx.MessageDialog(None, 'An error has occurred.  Press ALT-L to view the log.', 'Error During Game', wx.OK | wx.ICON_ERROR)
                    mdial.ShowModal()
                    mdial.Destroy()
                Client_GlobalData.mamePopen = None
                Client_GlobalData.emuLogFile.close()
                Client_GlobalData.emuLogFile = None
                if Client_GlobalData.player.playingGameInstanceID>=0:
                    if Client_GlobalData.player.playingGameInstanceID in Client_GlobalData.database.gameInstances:
                        gameInstance = Client_GlobalData.database.gameInstances[Client_GlobalData.player.playingGameInstanceID]
                        logAsString = bz2.compress(str(open("../MAMElog.txt","rb").read()))
                        #print 'SENDING LOG WITH SIZE:',len(logAsString)
                        Client_GlobalData.networkProtocol.sendString("GAME_LOG " + str(gameInstance.db_game_id) + " |"+logAsString)
                    Client_GlobalData.database.removeGameInstance()
                Client_GlobalData.database.changePlayerStatus(Client_Game.Player.STATUS_LOBBY,-1)
                if Client_GlobalData.DEBUG_APP == True:
                    # don't throw error if does not exist
                    try:
                        os.system(Client_GlobalData.editorName + "../MAMElog.txt")
                    except:
                        pass

        if Client_GlobalData.gui_update_user_grid == True:
            playerNameList = []
            for player in Client_GlobalData.database.players.itervalues():
                haveGameInCommon = False
                if Client_GlobalData.player:
                    LFGList = Client_GlobalData.player.LFG.split('/')
                    #updateGameGrid(self,self.LFGList,LFGList)
                    tmpLFGList = player.LFG.split('/')
                    for LFG in LFGList:
                        if len(LFG) and LFG in tmpLFGList:
                            haveGameInCommon = True
                prependages = player.Country
                if player.status == Client_Game.Player.STATUS_PLAYING:
                    if player.playingGameInstanceID in Client_GlobalData.database.gameInstances:
                        player_data = prependages, player.username + " (" + Client_Database.SQL_Retrieve_Game_Name(Client_GlobalData.database.gameInstances[player.playingGameInstanceID].db_game_id) + ")", "", player.OperatingSystem
                        playerNameList.append(player_data)
                    else:
                        player_data = prependages, player.username, "*Unknown*", player.OperatingSystem
                        playerNameList.append(player_data)
                elif player.status == Client_Game.Player.STATUS_LOBBY:
                    appendages = ""
    ##                if haveGameInCommon:
    ##                    appendages += " <<<LFG"
                    if player.AFK:
                        appendages += " (AFK)"
                    player_data = prependages, player.username, appendages, player.OperatingSystem
                    playerNameList.append(player_data)
            updateLabelIfDirty(self.FindWindowById(wx.ID_PLAYERLISTSIZER),(locale.format("%.0f", len(playerNameList), 1) +" Current User(s)"))
            updatePlayerGrid(self,self.playerGridNew,playerNameList)

        if Client_GlobalData.gui_update_hosted_game_grid == True:
            gameInstanceNameListGrid = []
            for gameInstance in Client_GlobalData.database.gameInstances.itervalues():
                #print "derp:",gameInstance.ID,str(Client_GlobalData.database.getNumPlayersForGameInstance(gameInstance.ID)),gameInstance.host_name
                if Client_GlobalData.database.getNumPlayersForGameInstance(gameInstance.ID)>0:
                    game_entry = gameInstance.host_name + "|" + Client_Database.SQL_Retrieve_Game_Name(gameInstance.db_game_id) + "|" + str(Client_GlobalData.database.getNumPlayersForGameInstance(gameInstance.ID))
                    if gameInstance.locked:
                        game_entry += "-(locked)"
                    game_entry += "|" + str(gameInstance.time_started) + "|" + Client_Database.SQL_Retrieve_Game_System_Name(gameInstance.db_game_id)
                    gameInstanceNameListGrid.append(game_entry)
            updateGameGrid(self,gameInstanceNameListGrid,self.publicGameGrid)

        if self.manage_game_auinotebook.GetSelection() == 0:
            updateLabelIfDirty(self.FindWindowById(wx.ID_GAMELISTSIZER),("Join List - Double-Click a game to join (" + locale.format("%.0f", self.publicGameGrid.GetNumberRows(), 1) +" Hosted Games Found)"))

        if self.auditing:
            if Client_GlobalData.auditData.is_alive():
                if Client_GlobalData.auditData.hashScanner is not None and \
                    Client_GlobalData.auditData.hashScanner.percentComplete != self.lastPercent:
                        self.lastPercent = Client_GlobalData.auditData.hashScanner.percentComplete
                        #print 'REPORT:',self.lastPercent
                        if self.lastPercent==100:
                            self.auditProgress.Update(self.lastPercent,"Matching hashes to ROMs/Carts " + locale.format("%.0f", Client_GlobalData.matching_on_file, 1) + "/" + locale.format("%.0f", Client_GlobalData.matching_files_to_audit, 1))
                        else:
                            self.auditProgress.Update(self.lastPercent,"Calculating SHA1 " + locale.format("%.0f", Client_GlobalData.audit_on_file, 1) + "/" + locale.format("%.0f", Client_GlobalData.audit_files_to_audit, 1))
            else:
                print "End Audit Time: ",time.strftime("%Y:%m:%d_%H:%M:%S")
                self.auditing=False
                #gameList = Client_GlobalData.auditData.getNames("")

                # clear and then write the ids to the database for the client
                Client_GlobalData.curs_player.execute("delete from game_audit")
                item_ndx = 0
                for game_id in Client_GlobalData.found_rom_ids:
                    sql_args = game_id,Client_GlobalData.found_rom_paths[item_ndx]
                    item_ndx += 1
                    Client_GlobalData.curs_player.execute("insert into game_audit (ga_id,ga_game_id,ga_game_path) values (NULL,?,?)",sql_args)
                Client_GlobalData.conn_player.commit()

                # clear out the mech/adult/clones from the audit game database
                first_skip = False
                sql_query = ""
                if Client_GlobalData_Config.skip_mechanical == True:
                    sql_query = u"select gi_id from game_info where gi_is_mech = 1 or gc_category like 'XtraAGEMAME-Pin%'"
                    first_skip = True
                if Client_GlobalData_Config.skip_adult == True:
                    if first_skip == True:
                        sql_query += " union "
                    sql_query += u"select gi_id from game_info,game_category where gi_gc_category = gc_id and gc_category like 'Adult%'"
                    first_skip = True
                if Client_GlobalData_Config.skip_clones == True:
                    if first_skip == True:
                        sql_query += " union "
                    sql_query += u"select gi_id from game_info where gi_cloneof is not NULL"
                if Client_GlobalData_Config.skip_gambling == True:
                    if first_skip == True:
                        sql_query += " union "
                    sql_query += u"select gi_id from game_info,game_category where gi_gc_category = gc_id and gc_category like 'Gambling%'"
                if Client_GlobalData_Config.skip_mahjong == True:
                    if first_skip == True:
                        sql_query += " union "
                    sql_query += u"select gi_id from game_info,game_category where gi_gc_category = gc_id and gc_category like 'Logic/Mahjong%'"
                print "query:",sql_query
                Client_GlobalData.curs_game.execute(sql_query)
                sql_query = ""
                for sql_row in Client_GlobalData.curs_game:
                    sql_query += str(sql_row[0]) + ","
                sql_args = sql_query[:-1],
                Client_GlobalData.curs_game.execute("delete from game_audit where ga_game_id IN (?)",sql_args)
                Client_GlobalData.conn_game.commit()

                self.gameSearchText.SetValue("")
                self.auditProgress.Destroy()
                self.auditProgress = None
                if len(Client_GlobalData.skipped_files) > 0:
                    dialog = AuditErrorDialog(self)
                    dialog.ShowModal()
                    dialog.Destroy()
                else:
                    mdial = wx.MessageDialog(None, 'Audit Complete!', 'Audit Complete', wx.OK | wx.ICON_INFORMATION)
                    mdial.ShowModal()
                    mdial.Destroy()
                # load the new results
                Client_GlobalData.auditData.load_hash_map_from_database()
                gameListTreeData = Client_GlobalData.auditData.getNamesDictDB(self.gameSearchText.GetLineText(0).encode("utf8"))
                updateTreeIfDirtyNoRoot(self.gameListTreeCtrl,gameListTreeData)

        if self.cyclesUntilFilter>0:
            self.cyclesUntilFilter -= 1
            if self.cyclesUntilFilter==0:
                #gameList = Client_GlobalData.auditData.getNames(self.gameSearchText.GetLineText(0).encode("utf8"))
                # old way      gameListTree = Client_GlobalData.auditData.getNamesDict(self.gameSearchText.GetLineText(0).encode("utf8"))
                gameListTreeData = Client_GlobalData.auditData.getNamesDictDB(self.gameSearchText.GetLineText(0).encode("utf8"))
                #print "tree:",gameListTree
                #updateTreeIfDirtyNoRoot(self.gameListTree,gameListTreeData)
                updateTreeIfDirtyNoRoot(self.gameListTreeCtrl,gameListTreeData)
                if len(self.gameSearchText.GetLineText(0)):
                    self.gameListTreeCtrl.ExpandAll(self.gameListTreeCtrl.GetRootItem())
                if self.manage_game_auinotebook.GetSelection()==1:
                    self.FindWindowById(wx.ID_GAMELISTSIZER).SetLabel("Game List - Double-Click a game to host (" + locale.format("%.0f", Client_GlobalData.audited_games, 1) +" Games Found)")
        #print 'Updating main frame'
        self.timer.Start(200,True)
        event.Skip()

##    def notifyIfInactive(self,title,text):
##        if self.IsActive()==False or self.IsShown()==False:
##            #self.tbicon.ShowBalloonTip(title,text.decode("utf8"))
##            pass

    def joinGameFromGames( self, event ):
        gameInstance = Client_GlobalData.database.getGameInstanceFromHostName(self.publicGameGrid.GetCellValue(Client_GlobalData.grid_cell_row, 0).encode("utf8"))
        print gameInstance.ID,self.publicGameGrid.GetCellValue(Client_GlobalData.grid_cell_row, 0)
        if Client_GlobalData.hasPortForwarded == False and Client_GlobalData.database.getNumPlayersForGameInstance(gameInstance.ID)>1:
            mdial = wx.MessageDialog(None, 'You do not have your port forwarded correctly!  You will not be able to be the 3rd, 4th, etc. person to join a games until you set up port forwarding.', 'Port Forward', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()
            return
        event.Skip()
        hostPlayer = Client_GlobalData.database.players[gameInstance.hostID]
        if gameInstance:
            if gameInstance.locked:
                mdial = wx.MessageDialog(None, 'This game has been locked by the host.', 'Game Locked', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
            elif Client_GlobalData.mamePopen is not None:
                mdial = wx.MessageDialog(None, 'You already have an instance of CSMAME running. Please close it first.', 'Close CSMAME First', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
            else:
                game_file_path,game_system_id = Client_Database.SQL_Retrieve_File_Path_SystemId(gameInstance.db_game_id)
                if game_file_path == "Unknown":
                    # qg12 must fix the path below for missing rom thingie
                    retval = wx.MessageBox("Rom \""+Client_Database.SQL_Retrieve_Game_Name(gameInstance.db_game_id)+"\" cannot be found. Can acquire from game host. Are you legally entitled to own a copy of this ROM?","ROM not found.",style=wx.YES_NO)
                    if retval==wx.YES:
                        Client_GlobalData.networkProtocol.sendString("REQUEST_ROM "+str(gameInstance.ID))
                else:
                    Client_GlobalData.database.changePlayerStatus(Client_Game.Player.STATUS_PLAYING,gameInstance.ID)
                    launchGameByID(gameInstance.db_game_id,False,hostPlayer.IPAddress,Client_GlobalData.selfPort,hostPlayer.port)
        else:
            mdial = wx.MessageDialog(None, 'Game no longer exists or cannot be found.', 'Game no longer exists', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()

    def performAudit(self):
        if self.auditing==False:
            iniParser = Client_INIParser.INIParser("./mame.ini")
            romPaths = iniParser.getRomPaths()
##            mdial = wx.MessageDialog(None, 'Auditing may take a long time if you have many roms, and the client may become unresponsive while auditing. Please be patient.', "Auditing "+';'.join(romPaths), wx.OK | wx.ICON_INFORMATION)
##            mdial.ShowModal()
##            mdial.Destroy()
            Client_GlobalData.auditData = GameAuditer()
            Client_GlobalData.auditData.baseDirectories = romPaths
            Client_GlobalData.auditData.start()
            self.auditing=True
            self.lastPercent = -1
            self.auditProgress = wx.ProgressDialog("Auditing in Progress","Please wait while audit is performed",110,None,0)
            self.auditProgress

    def auditGames( self, event ):
        # this is the alt-A command in the gui
        print "Start Audit Time: ",time.strftime("%Y:%m:%d_%H:%M:%S")
        self.performAudit()

    def OnCadeModeMenuItem( self, event ):
        cade_main()
        event.Skip()

    def OnViewMAMELog( self, event ):
        try:
            os.system(Client_GlobalData.editorName + "../MAMElog.txt")
        except:
            mdial = wx.MessageDialog(None, 'No MAMELog.txt file to open!', 'No Log to View', wx.OK | wx.ICON_INFORMATION)
            mdial.ShowModal()
            mdial.Destroy()

    def ToggleDebug( self, event ):
        if Client_GlobalData.DEBUG_APP == True:
            Client_GlobalData.DEBUG_APP = False
            self.SetTitle(u"Hub!Cade")
        else:
            Client_GlobalData.DEBUG_APP = True
            self.SetTitle(u"Hub!Cade - DEBUG_APP Mode")

    def setDirectories( self, event ):
        dialog = SetDirectoriesDialog(self)
        dialog.ShowModal()
        dialog.Destroy()

    def hostGameFromList( self, event ):
##        if Client_GlobalData.hasPortForwarded == False:
##            mdial = wx.MessageDialog(None, 'You do not have your port forwarded correctly!  You will not be able to host a game until you set up port forwarding, but you can still join games that other people host if you are the first person to join.', 'Port Forward', wx.OK | wx.ICON_EXCLAMATION)
##            mdial.ShowModal()
##            mdial.Destroy()
##            return
        if Client_GlobalData.mamePopen is not None:
            mdial = wx.MessageDialog(None, 'You already have an instance of CSMAME running. Please close it first.', 'Close CSMAME First', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()
        elif self.gameListTreeCtrl.GetChildrenCount(self.gameListTreeCtrl.GetSelection(),True)>0:  # system is selected
            pass
        else:
            hostGameId = self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection(),5).encode("utf8")
            Client_GlobalData.database.createGameInstance(hostGameId,Client_GlobalData.playerID,Client_GlobalData.host_game_max_players,Client_GlobalData.host_game_max_observers)
            #Client_GlobalData.hostedFiles = Client_GlobalData.auditData.getAllMAMEFilesFromName(hostGameName)
            if Client_GlobalData.os_video_playback == True:
                self.vid_playback_control.Pause()
                self.timer_slider.Stop()
            launchGameByID(hostGameId,True,"",Client_GlobalData.selfPort,Client_GlobalData.selfPort)
            times_played = int(self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection(),1).encode("utf8")) + 1
            self.gameListTreeCtrl.SetItemText(self.gameListTreeCtrl.GetSelection(),locale.format("%.0f", times_played),1)

    def Rebuild_Game_Info_Notebook_AddPage ( self, type_to_add ):
        if type_to_add == 1:  # title/snap
            self.game_info_images_auinotebook.AddPage( self.title_snap_panel, u"Title/Snap" )
        elif type_to_add == 2:  # title
            self.game_info_images_auinotebook.AddPage( self.title_panel, u"Title" )
        elif type_to_add == 3:  # snap
            self.game_info_images_auinotebook.AddPage( self.snap_panel, u"Snap" )
        elif type_to_add == 4:  # cabinet - box
            self.game_info_images_auinotebook.AddPage( self.cart_panel, u"Cabinet" )
            if  Client_GlobalData_Config.mame_mess == False:
                self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(4)+1, "Box")
        elif type_to_add == 5:  # cpanel - cart
            self.game_info_images_auinotebook.AddPage( self.box_panel, u"CPanel" )
            if  Client_GlobalData_Config.mame_mess == False:
                self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(5)+1, "Cart")
        elif type_to_add == 6:  # marque - label
            self.game_info_images_auinotebook.AddPage( self.label_panel, u"Marquee" )
            if  Client_GlobalData_Config.mame_mess == False:
                self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(6)+1, "Label")
        elif type_to_add == 7:  # pcb - cart top
            self.game_info_images_auinotebook.AddPage( self.cart_top_panel, u"PCB" )
            if  Client_GlobalData_Config.mame_mess == False:
                self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(7)+1, "Cart Top")
        elif type_to_add == 8:  # video
            self.game_info_images_auinotebook.AddPage( self.video_panel, u"Video" )
        elif type_to_add == 9:  # manual
            self.game_info_images_auinotebook.AddPage( self.pdf_panel, u"Manual" )

    def Rebuild_Game_Info_Notebook ( self ):
        # remove all the pages after info
        ndx = 1
        while ndx < self.game_info_images_auinotebook.GetPageCount():
            self.game_info_images_auinotebook.RemovePage(ndx)
        # readd the pages for mame/mess current pages
        if Client_GlobalData_Config.mame_mess == True:
            for type_to_add in Client_GlobalData_Config.auinotebook_mame_list:
                self.Rebuild_Game_Info_Notebook_AddPage(type_to_add)
        else:
            for type_to_add in Client_GlobalData_Config.auinotebook_mess_list:
                self.Rebuild_Game_Info_Notebook_AddPage(type_to_add)

    def GameImageDisplay ( self,romFilePath,game_system_id,hostGameId ):
        print "rompath:",romFilePath
        if romFilePath != "Unknown":
            if str.upper(sys.platform[0:3])=='WIN' \
            or str.upper(sys.platform[0:3])=='CYG':
                image_location_split = romFilePath.rsplit("\\",1)
            else:
                image_location_split = romFilePath.rsplit("/",1)
            print "image:",image_location_split
            image_name = image_location_split[1]
            image_path = image_location_split[0]
            if str.upper(sys.platform[0:3])=='WIN' \
            or str.upper(sys.platform[0:3])=='CYG':
                image_path = image_path.rsplit("\\",1)[0]
            else:
                image_path = image_path.rsplit("/",1)[0]
            print "image path:",image_path
            rom_name = image_name
            image_name = image_name.rsplit(".", 1)[0] + '.png'
            # set the global for image resize
            rebuild_pages = False
            if game_system_id==0:
                if (len(Client_GlobalData_Config.auinotebook_mame_list) != (self.game_info_images_auinotebook.GetPageCount() -1)):
                    rebuild_pages = True
                else:
                    page_count = 0
                    for data in Client_GlobalData_Config.auinotebook_mame_list:
                        page_count += 1
                        page_text = "Title/Snap"
                        if data == 2:
                            page_text = "Title"
                        elif data == 3:
                            page_text = "Snap"
                        elif data == 4:
                            page_text = "Cabinet"
                        elif data == 5:
                            page_text = "CPanel"
                        elif data == 6:
                            page_text = "Marquee"
                        elif data == 7:
                            page_text = "PCB"
                        elif data == 8:
                            page_text = "Video"
                        elif data == 9:
                            page_text = "Manual"
                        if page_text != self.game_info_images_auinotebook.GetPageText(page_count):
                            rebuild_pages = True
                Client_GlobalData_Config.mame_mess = True
            else:
                if (len(Client_GlobalData_Config.auinotebook_mess_list) != (self.game_info_images_auinotebook.GetPageCount() -1)):
                    rebuild_pages = True
                else:
                    page_count = 0
                    for data in Client_GlobalData_Config.auinotebook_mess_list:
                        page_count += 1
                        page_text = "Title/Snap"
                        if data == 2:
                            page_text = "Title"
                        elif data == 3:
                            page_text = "Snap"
                        elif data == 4:
                            page_text = "Box"
                        elif data == 5:
                            page_text = "Cart"
                        elif data == 6:
                            page_text = "Label"
                        elif data == 7:
                            page_text = "Cart Top"
                        elif data == 8:
                            page_text = "Video"
                        elif data == 9:
                            page_text = "Manual"
                        if page_text != self.game_info_images_auinotebook.GetPageText(page_count):
                            rebuild_pages = True
                Client_GlobalData_Config.mame_mess = False
            if rebuild_pages == True:
                self.Rebuild_Game_Info_Notebook()
            # do title/snap image
            if (game_system_id==0 and Client_GlobalData_Config.mame_title_snap_display_tab == True) or (game_system_id!=0 and Client_GlobalData_Config.mess_title_snap_display_tab == True):
                self.game_info_images_auinotebook.SetPageText(1, "Title/Snap")
                if Client_GlobalData_Config.file_save_method == False:
                    image_location = "../images/titles/" + image_name
                else:
                    image_location = image_path + "/titles/" + image_name
    ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
    ##                image_location = image_location.replace('/','\\')
                image_location = os.path.normpath(image_location)
                print "huh:",image_name, image_location,self.title_snap_title_bitmap.Size[0],self.title_snap_title_bitmap.Size[1]
                #do title image
                if os.path.exists(image_location):
                    img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                else:
                    if Client_GlobalData_Config.autodown_image == True:
                        download_image("http://www.spootsworld.com/arcade/title/" + image_name,image_location)
                        if os.path.exists(image_location):
                            img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                        else:
                           img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    else:
                       img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_snap_title_bitmap.Size[0],self.title_snap_title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.title_snap_title_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.title_snap_title_bitmap.Refresh()
                self.title_snap_title_bitmap.GetParent().Layout()
                # do snap image
                if Client_GlobalData_Config.file_save_method == False:
                    image_location = "../images/snap/" + image_name
                else:
                    image_location = image_path + "/snap/" + image_name
    ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
    ##                image_location = image_location.replace('/','\\')
                image_location = os.path.normpath(image_location)
                #print image_name, image_location
                if os.path.exists(image_location):
                    img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                else:
                    if Client_GlobalData_Config.autodown_image == True:
                        download_image("http://www.spootsworld.com/arcade/snap/" + image_name,image_location)
                        if os.path.exists(image_location):
                            img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                        else:
                           img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    else:
                       img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_snap_title_bitmap.Size[0],self.title_snap_title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.title_snap_snap_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.title_snap_snap_bitmap.Refresh()
                self.title_snap_snap_bitmap.GetParent().Layout()
            # do title image
            if (game_system_id==0 and Client_GlobalData_Config.mame_title_display_tab == True) or (game_system_id!=0 and Client_GlobalData_Config.mess_title_display_tab == True):
                if Client_GlobalData_Config.mame_mess == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(2)+1, "Title")
                else:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(2)+1, "Title")
                if Client_GlobalData_Config.file_save_method == False:
                    image_location = "../images/titles/" + image_name
                else:
                    image_location = image_path + "/titles/" + image_name
    ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
    ##                image_location = image_location.replace('/','\\')
                image_location = os.path.normpath(image_location)
                #print image_name, image_location
                #do title image
                if os.path.exists(image_location):
                    img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                else:
                    if Client_GlobalData_Config.autodown_image == True:
                        download_image("http://www.spootsworld.com/arcade/title/" + image_name,image_location)
                        if os.path.exists(image_location):
                            img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                        else:
                           img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    else:
                       img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.title_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.title_bitmap.Refresh()
                self.title_bitmap.GetParent().Layout()
            #do snap image
            if (game_system_id==0 and Client_GlobalData_Config.mame_snap_display_tab == True) or (game_system_id!=0 and Client_GlobalData_Config.mess_snap_display_tab == True):
                if Client_GlobalData_Config.mame_mess == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(3)+1, "Snap")
                else:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(3)+1, "Snap")
                #self.game_info_images_auinotebook.SetPageText(3, "Snap")
                if Client_GlobalData_Config.file_save_method == False:
                    image_location = "../images/snap/" + image_name
                else:
                    image_location = image_path + "/snap/" + image_name
    ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
    ##                image_location = image_location.replace('/','\\')
                image_location = os.path.normpath(image_location)
                #print image_name, image_location
                if os.path.exists(image_location):
                    img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                else:
                    if Client_GlobalData_Config.autodown_image == True:
                        download_image("http://www.spootsworld.com/arcade/snap/" + image_name,image_location)
                        if os.path.exists(image_location):
                            img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                        else:
                           img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    else:
                       img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.snap_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.snap_bitmap.Refresh()
                self.snap_bitmap.GetParent().Layout()
            # if mame rom
            if game_system_id==0:
                # info display
                if Client_GlobalData_Config.mame_info_display_tab == True:
                    html_page = "<html><font size=\"" + str(Client_GlobalData_Config.gameinfo_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.gameinfo_font_color + "\" face=\"" + Client_GlobalData_Config.gameinfo_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.gameinfo_font_size)+"pt;\"><B>Rom Name: </B> " + rom_name
                    sql_args = hostGameId,
                    Client_GlobalData.curs_game.execute("select gi_short_name,gi_cloneof,gi_romof,gi_description,gi_year, (select gsp_publisher from game_systems_publisher where gsp_id = gi_publisher),gi_players,gi_buttons,gi_joy_way,gi_savestate,gm_type,gm_rotate,gm_width,gm_height,gm_refresh from game_info, game_monitor where gi_id = ? and gi_monitor_id = gm_id",sql_args)
                    for row in Client_GlobalData.curs_game:
                        #print row[1],":"
                        if row[1] != None:
                            html_page += u"    <B>Clone Of:</b> " + str(row[1]).encode("utf8")
                        #print row[2],":"
                        if row[2] != None:
                            html_page += u"    <B>Parent Of:</B> " + str(row[2]).encode("utf8")
                        html_page += u"<BR><B>Year Released:</B> " + str(row[4]).encode("utf8") + u"<BR>"
                        html_page += u"<B>Manufacturer:</B> " + str(row[5]).encode("utf8") + u"<BR>"
                        if str(row[6]) == "0":
                            html_page += u"<B>Number of Player(s):</B> Unknown<BR>"
                        else:
                            html_page += u"<B>Number of Player(s):</B> " + str(row[6]).encode("utf8") + u"<BR>"
                        if str(row[7]) != "999":
                            html_page += u"<B>Button(s):</B> " + str(row[7]).encode("utf8") + u"<BR>"
                        else:
                            html_page += u"<B>Button(s):</B> Unlisted<BR>"
                        if len(row[8]) > 0:
                            html_page += u"<B>Controller Type(s):</B> " + str(row[8]).capitalize().encode("utf8") + u"<BR>"
                        if str(row[9]) == "0":
                            html_page += u"<B>Save State Status:</B><font color=\"red\"> Unsupported - Instajoin Disabled</font><BR>"
                        else:
                            html_page += u"<B>Save State Status:</B><font color=\"green\"> Supported - Instajoin/Resync Enabled</font><BR>"
                        if row[10] != None:
                            html_page += "<B>Monitor Type:</B> " + str(row[10]).capitalize().encode("utf8")
                        if row[11] != None:
                            mon_rotate = u"Horizontal"
                            if str(row[11]) != "0":
                                mon_rotate = u"Vertical"
                            html_page += u" <B>Orientation:</B> " + mon_rotate.encode("utf8")
                        # monitor width
                        if row[12] != None:
                            if str(row[12]) != "0":
                                html_page += u" <B>Width:</B> " + locale.format("%.0f", row[12], 1)
                            else:
                                html_page += u" <B>Width:</B> NA"
                        # monitor height
                        if row[13] != None:
                            if str(row[13]) != "0":
                                html_page += u" <B>Height:</B> " + locale.format("%.0f", row[13], 1)
                            else:
                                html_page += u" <B>Height:</B> NA"
                        # monitor refresh
                        if row[14] != None:
                            if str(row[13]) != "0":
                                html_page += u" <B>Refresh:</B> " + locale.format("%.6f", row[14], 1) + "<BR>"
                            else:
                                html_page += u" <B>Refresh:</B> NA<BR>"
                        if row[3] != None and len(row[3]) > 1:
                            html_page += u"<BR><B>Description:</B> " + row[3].replace('\n\n','<BR>').replace('\n','<BR>') + u"<BR>"
                    if Client_GlobalData.webkit_enabled == False:
                        self.gameinfo_htmlwindow.SetPage(html_page + "</span></font></html>")
                    else:
                        self.gameinfo_htmlwindow.SetPage(html_page + "</span></font></html>","")
                #do cabinets image
                if Client_GlobalData_Config.mame_cabinet_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(4)+1, "Cabinet")
                    #self.game_info_images_auinotebook.SetPageText(4, "Cabinet")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/cabinets/" + image_name
                    else:
                        image_location = image_path + "/cabinets/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/arcade/cabinets/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                                img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                            img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.cart_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.cart_bitmap.Refresh()
                    self.cart_bitmap.GetParent().Layout()
                #do control panel image
                if Client_GlobalData_Config.mame_control_panel_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(5)+1, "CPanel")
                    #self.game_info_images_auinotebook.SetPageText(5, "CPanel")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/cpanel/" + image_name
                    else:
                        image_location = image_path + "/cpanel/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/arcade/cpanel/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                                img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                            img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.box_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.box_bitmap.Refresh()
                    self.box_bitmap.GetParent().Layout()
                #do marque image
                if Client_GlobalData_Config.mame_marque_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(6)+1, "Marquee")
                    #self.game_info_images_auinotebook.SetPageText(6, "Marquee")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/marquees/" + image_name
                    else:
                        image_location = image_path + "/marquees/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/arcade/marquees/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                                img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                            img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.label_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.label_bitmap.Refresh()
                    self.label_bitmap.GetParent().Layout()
                #do pcb image
                if Client_GlobalData_Config.mame_pcb_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(7)+1, "PCB")
                    #self.game_info_images_auinotebook.SetPageText(7, "PCB")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/pcb/" + image_name
                    else:
                        image_location = image_path + "/pcb/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/arcade/pcb/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                                img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                            img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.cart_top_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.cart_top_bitmap.Refresh()
                    self.cart_top_bitmap.GetParent().Layout()
                # check to see if playback
                if Client_GlobalData.os_video_playback == True and Client_GlobalData_Config.mame_video_playback_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(8)+1, "Video")
                    # load avi file if exists
                    video_name = image_name.replace('.png','.avi')
                    if Client_GlobalData_Config.file_save_method == False:    # yes, kinda reverse since I'm using the combo index
                        image_location = "../videos/" + video_name
                    else:
                        image_location = image_path + "/videos/" + video_name
                    if os.path.exists(image_location):
                        if not self.vid_playback_control.Load(image_location):
                            mdial = wx.MessageDialog(None, 'Unable to load %s: Unsupported format?' % path, 'Playback Error', wx.OK | wx.ICON_ERROR)
                            mdial.ShowModal()
                            mdial.Destroy()
                    else:
                        self.vid_playback_control.Stop()
                        self.timer_slider.Stop()
                # check to see if pdf
                if Client_GlobalData_Config.mame_manual_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mame_list.index(9)+1, "Manual")
                    # load pdf if it exists
                    pdf_name = image_name.replace('.png','.pdf')
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../manuals/" + pdf_name
                    else:
                        image_location = image_path + "/manuals/" + pdf_name
                    print "pdf:",image_location
                    if os.path.exists(image_location):
                        print "here3"
                        if wx.Platform == '__WXMSW__':
                            self.pdf_panel.LoadUrl(image_location)
                        else:
                            self.pdf_panel.LoadDocument(image_location)
    ##                    if wx.Platform == '__WXMSW__':
    ##                        self.ie.LoadUrl(image_location)
                    else:
                        # wipe out "old" manual
                        if wx.Platform == '__WXMSW__':
                            self.pdf_panel.LoadUrl( Client_GlobalData.application_launch_directory.rsplit('/',1)[0] + "/images/hubcade.pdf" )
                        else:
                            self.pdf_panel.LoadDocument( Client_GlobalData.application_launch_directory.rsplit('/',1)[0] + "/images/hubcade.pdf" )
            else:
                # if mess rom
                #do box image
                if Client_GlobalData_Config.mess_box_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(4)+1, "Box")
                    #self.game_info_images_auinotebook.SetPageText(4, "Box")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/box/" + image_name
                    else:
                        image_location = image_path + "/box/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/boxart/box/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                               img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                           img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.box_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.box_bitmap.Refresh()
                    self.box_bitmap.GetParent().Layout()
                #do cart image
                if Client_GlobalData_Config.mess_cart_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(5)+1, "Cart")
                    #self.game_info_images_auinotebook.SetPageText(5, "Cart")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/cart/" + image_name
                    else:
                        image_location = image_path + "/cart/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/boxart/cart/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                               img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                           img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.cart_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.cart_bitmap.Refresh()
                    self.cart_bitmap.GetParent().Layout()
                #do label image
                if Client_GlobalData_Config.mess_label_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(6)+1, "Label")
                    #self.game_info_images_auinotebook.SetPageText(6, "Label")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/label/" + image_name
                    else:
                        image_location = image_path + "/label/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/boxart/label/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                               img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                           img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.label_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.label_bitmap.Refresh()
                    self.label_bitmap.GetParent().Layout()
                #do cart top image
                if Client_GlobalData_Config.mess_cart_top_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(7)+1, "Cart Top")
                    #self.game_info_images_auinotebook.SetPageText(7, "Cart Top")
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../images/carttop/" + image_name
                    else:
                        image_location = image_path + "/carttop/" + image_name
        ##            if str.upper(sys.platform[0:3])=='WIN' or str.upper(sys.platform[0:3])=='CYG':
        ##                image_location = image_location.replace('/','\\')
                    image_location = os.path.normpath(image_location)
                    #print image_name, image_location
                    if os.path.exists(image_location):
                        img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                    else:
                        if Client_GlobalData_Config.autodown_image == True:
                            download_image("http://www.spootsworld.com/boxart/carttop/" + image_name,image_location)
                            if os.path.exists(image_location):
                                img = wx.Image( image_location, wx.BITMAP_TYPE_ANY)
                            else:
                                img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                        else:
                            img = wx.Image( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY)
                    NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                    img = img.Scale(NewWidth,NewHeight)
                    self.cart_top_bitmap.SetBitmap(wx.BitmapFromImage(img))
                    self.cart_top_bitmap.Refresh()
                    self.cart_top_bitmap.GetParent().Layout()
                # check to see if pdf
                if Client_GlobalData_Config.mess_manual_display_tab == True:
                    self.game_info_images_auinotebook.SetPageText(Client_GlobalData_Config.auinotebook_mess_list.index(9)+1, "Manual")
                    # load pdf if it exists
                    pdf_name = image_name.replace('.png','.pdf')
                    if Client_GlobalData_Config.file_save_method == False:
                        image_location = "../manuals/" + pdf_name
                    else:
                        image_location = image_path + "/manuals/" + pdf_name
                    print "pdf:",image_location
                    if os.path.exists(image_location):
                        print "here5"
                        if wx.Platform == '__WXMSW__':
                            self.pdf_panel.LoadUrl(image_location)
                        else:
                            self.pdf_panel.LoadDocument(image_location)
    ##                    if wx.Platform == '__WXMSW__':
    ##                        self.ie.LoadUrl(image_location)
                    else:
                        # wipe out "old" manual
                        if wx.Platform == '__WXMSW__':
                            self.pdf_panel.LoadUrl( Client_GlobalData.application_launch_directory.rsplit('/',1)[0] + "/images/hubcade.pdf" )
                        else:
                            self.pdf_panel.LoadDocument( Client_GlobalData.application_launch_directory.rsplit('/',1)[0] + "/images/hubcade.pdf" )
                # info display
                if Client_GlobalData_Config.mess_info_display_tab == True:
                    html_page = "<html><font size=\"" + str(Client_GlobalData_Config.gameinfo_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.gameinfo_font_color + "\" face=\"" + Client_GlobalData_Config.gameinfo_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.gameinfo_font_size)+"pt;\"><B>Rom Name: </B> " + rom_name + "<BR>"
                    html_page += "<BR>Additional information for MESS roms is not supported yet.<BR>"
                    """
                    curs.execute("select game_name,cloneof,romof,description,game_year,manufacturer,players,buttons,joy_way,save_state_support from games where game_name =\"" + rom_name.replace(".zip","") + "\"")
                    for row in curs:
                        pass
                    """
                    if Client_GlobalData.webkit_enabled == False:
                        self.gameinfo_htmlwindow.SetPage(html_page + "</span></font></html>")
                    else:
                        self.gameinfo_htmlwindow.SetPage(html_page + "</span></font></html>","")

    def hostGameInformation( self, event ):
        if self.gameListTreeCtrl.GetChildrenCount(self.gameListTreeCtrl.GetSelection(),True)>0:
            html_page = "<html><font size=\"" + str(Client_GlobalData_Config.gameinfo_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.gameinfo_font_color + "\" face=\"" + Client_GlobalData_Config.gameinfo_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.gameinfo_font_size)+"pt;\">"
            if self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection()).encode("utf8").split(" ")[0] == "Arcade":
                html_page += "MAME stands for Multiple Arcade Machine Emulator. When used in conjunction with images of the original arcade game's ROM and disk data, MAME attempts to reproduce that game as faithfully as possible on a more modern general-purpose computer. MAME can currently emulate several thousand different classic arcade video games from the late 1970s through the modern era."
            else:
                info_page_text = "System not found in database."
                sql_args = self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection()).encode("utf8").rsplit("-")[0].strip(),
                Client_GlobalData.curs_game.execute ("SELECT gs_system_long_name,gsp_publisher,gs_system_year,gs_system_description,gs_system_savestate,gses_status_text,(select gses_status_text from game_systems_emulation_status where gses_id = gs_system_color),(select gses_status_text from game_systems_emulation_status where gses_id = gs_system_sound),(select gses_status_text from game_systems_emulation_status where gses_id = gs_system_graphic) FROM game_systems,game_systems_publisher,game_systems_emulation_status WHERE gs_system_long_name = ? and gs_system_manufacturer = gsp_id and gs_system_emulation = gses_id",sql_args)
                for row in Client_GlobalData.curs_game:
                    info_page_text = "<B>System Name: </B>" + row[0] + "<BR>" \
                        + "<B>Manufacturer: </B>" + row[1] + "<BR>" \
                        + "<B>Release Year: </B>" + row[2] + "<BR>"
                    if row[3] != None and len(row[3]) > 1:
                        info_page_text += "<B>Description: </B>" + row[3].replace('\n\n','<BR>').replace('\n','<BR>') + "<BR>"
                    if int(row[4]) == 0:
                        info_page_text += "<B>Save State Status:</B><font color=\"red\"> Unsupported - Instajoin Disabled</font><BR>"
                    else:
                        info_page_text += "<B>Save State Status:</B><font color=\"green\"> Supported - Instajoin/Resync Enabled</font><BR>"
                    info_page_text += "<B>Emulation: </B>" + row[5].capitalize() + "<BR>" \
                        + "<B>Color: </B>" + row[6].capitalize() + "<BR>" \
                        + "<B>Sound: </B>" + row[7].capitalize() + "<BR>" \
                        + "<B>Graphics: </B>" + row[8].capitalize() + "<BR>"
                html_page += info_page_text
            if Client_GlobalData.webkit_enabled == False:
                self.gameinfo_htmlwindow.SetPage(html_page + "</span></font></html>")
            else:
                self.gameinfo_htmlwindow.SetPage((html_page + "</span></font></html>"),"")
        else:
            #hostGameName = self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection()).encode("utf8")
            hostGameId = self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection(),5).encode("utf8")
            #print "host:",hostGameName,hostGameId
            gamePath, systemId = Client_Database.SQL_Retrieve_File_Path_SystemId(hostGameId)
            self.GameImageDisplay(gamePath,systemId,hostGameId)
##            #Need to find the file from the name
##            romFile,cartPath = Client_GlobalData.auditData.getRomAndCartFileFromName(hostGameName)
##            if len(romFile)==0:
##                mdial = wx.MessageDialog(None, "Rom "+hostGameName+" cannot be found.", 'ROM not found', wx.OK | wx.ICON_EXCLAMATION)
##                mdial.ShowModal()
##                mdial.Destroy()
##            else:
##                #print cartPath
##                #print romFile
##                if len(cartPath)==0:
##                    # means it's the Arcade/MAME selection
##                    gameRoomName = Client_GlobalData.player.username+'_'+hostGameName.replace(' ','_')
##                    image_location = romFile
##                else:
##                    # console selection which romfile will have the system type
##                    gameRoomName = Client_GlobalData.player.username+'_'+hostGameName.replace(' ','_')+' ['+romFile+']'
##                    image_location = cartPath
##                self.GameImageDisplay(romFile,cartPath,image_location)
        event.Skip()

    def joinGameInformation ( self, event):
        gameInstance = Client_GlobalData.database.getGameInstanceFromHostName(self.publicGameGrid.GetCellValue(Client_GlobalData.grid_cell_row, 0).encode("utf8"))
        game_file_path,game_system_id = Client_Database.SQL_Retrieve_File_Path_SystemId(gameInstance.db_game_id)
        self.GameImageDisplay(game_file_path,game_system_id,gameInstance.db_game_id)
        event.Skip()

    def Reload_Favorites_Grid(self):
        Client_GlobalData.favorite_game_id = []
        self.favorites_grid.Freeze()
        # union is for the fact mame is system 0 and doesnt' match anything
        Client_GlobalData.curs_game.execute("select gi_long_name,gi_short_name,game_times_played,game_time_played,game_rom_id,'Arcade','Arcade' from gui_db.game_info,game_info where game_favorite = 1 and game_rom_id = gi_id union all select gi_long_name,gi_short_name,game_times_played,game_time_played,game_rom_id,gs_system_name,gs_system_long_name from gui_db.game_info,game_info,game_systems where game_favorite = 1 and game_rom_id = gi_id and gi_system_id = gs_id order by game_times_played desc")
        row_count = 0
        for sql_row in Client_GlobalData.curs_game:
            self.favorites_grid.AppendRows(1)
            # in case of NULL
            if sql_row[0] != None:
                game_name = sql_row[0]
            else:
                game_name = sql_row[1]
            self.favorites_grid.SetCellValue(row_count, 0, game_name)
            self.favorites_grid.SetCellValue(row_count, 1, locale.format("%.0f", int(sql_row[2]), 1))
            current_epoch = float(time.time())
            seconds_running = current_epoch- float(sql_row[3])
            if seconds_running < 86400:
                self.favorites_grid.SetCellValue(row_count, 2, time.strftime('%H:%M:%S', time.gmtime(seconds_running)))  # time started
            else:
                self.favorites_grid.SetCellValue(row_count, 2, time.strftime('%d Day(s) %H:%M:%S', time.gmtime(seconds_running)))  # time started
            # pull system info of long/short name
            if len(sql_row[6]) > 0:
                self.favorites_grid.SetCellValue(row_count, 3, sql_row[6])
            else:
                self.favorites_grid.SetCellValue(row_count, 3, sql_row[5])
            Client_GlobalData.favorite_game_id.append(sql_row[4])
            row_count += 1
        self.favorites_grid.AutoSizeColumns(True)
        self.favorites_grid.AutoSizeRows(True)
        self.favorites_grid.Thaw()
        Client_GlobalData.gui_update_favorite = False

    def game_notebook_tab_change( self, event ):
        if event.GetSelection() == 0:
            self.FindWindowById(wx.ID_GAMELISTSIZER).SetLabel("Join List - Double-Click a game to join (" + locale.format("%.0f", self.publicGameGrid.GetNumberRows(), 1) +" Hosted Games Found)")
        elif event.GetSelection() == 1:
            self.FindWindowById(wx.ID_GAMELISTSIZER).SetLabel("Game List - Double-Click a game to host (" + locale.format("%.0f", Client_GlobalData.audited_games, 1) +" Games Found)")
        else:
            # check to see if changes to reload
            if Client_GlobalData.gui_update_favorite == True:
                Client_GlobalData.app.mainFrame.Reload_Favorites_Grid()
            self.FindWindowById(wx.ID_GAMELISTSIZER).SetLabel("Favorite List - Double-Click a game to host (" + locale.format("%.0f", self.favorites_grid.GetNumberRows(), 1) +" Games Found)")
        event.Skip()

    def joinGameFromUser( self, event ):
        event.Skip()
        selectedUsername = self.playerGridNew.GetCellValue(self.playerGridNew.GetGridCursorRow(), 2).split(" ")[0]
        print selectedUsername
        player = Client_GlobalData.database.getPlayerFromName(selectedUsername)
        if player:
            print "PLAYER ID",player.ID
            gameInstance = Client_GlobalData.database.getGameInstanceWithHostID(player.ID)
            if Client_GlobalData.hasPortForwarded == False and Client_GlobalData.database.getNumPlayersForGameInstance(gameInstance.ID)>1:
                mdial = wx.MessageDialog(None, 'You do not have your port forwarded correctly!  You will not be able to be the 3rd, 4th, etc. person to join a games until you set up port forwarding.', 'Port Forwared', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
                return
            if gameInstance:
                if Client_GlobalData.mamePopen is not None:
                    mdial = wx.MessageDialog(None, 'You already have an instance of CSMAME running. Please close it first.', 'Close CSMAME First', wx.OK | wx.ICON_EXCLAMATION)
                    mdial.ShowModal()
                    mdial.Destroy()
                else:
                    Client_GlobalData.database.changePlayerStatus(Client_Game.Player.STATUS_PLAYING,gameInstance.ID)
                    game_file_path,game_system_id = Client_Database.SQL_Retrieve_File_Path_SystemId(gameInstance.db_game_id)
                    if game_file_path == "Unknown":
                        # qg12 must fix the path below for missing rom thingie
                        retval = wx.MessageBox("Rom "+gameInstance.romFilename+" cannot be found. Can acquire from game host. Are you legally entitled to own a copy of this ROM?","ROM not found.",style=wx.YES_NO)
                        if retval==wx.YES:
                            Client_GlobalData.networkProtocol.sendString("REQUEST_ROM "+str(gameInstance.ID))
                    else:
                        launchGameByID(gameInstance.db_game_id,False,player.IPAddress,Client_GlobalData.selfPort,player.port)
            else:
                mdial = wx.MessageDialog(None, 'Game no longer exists or cannot be found.', 'Game no longer exists', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
        else:
            mdial = wx.MessageDialog(None, 'Player no longer exists or cannot be found', 'Player no longer exists', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()

    def hostGame( self, event ):
        if Client_GlobalData.hasPortForwarded == False:
            wx.MessageBox("You do not have your port forwarded correctly!  You will not be able to host games until you set up port forwarding.")
            return
        Client_GlobalData.app.hostGameDialog.ShowModal()

    def onAboutMenuItem( self, event ):
        info = wx.AboutDialogInfo()
        #info.SetIcon(wx.Icon('icons/hunter.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Hub!Cade')
        info.SetVersion(Client_GlobalData.software_rev)
        info.SetDescription("Hub!Cade is a frontend that helps users to arrange and play games on CSMAME and CSMESS.\nThis allows users to play older generation arcade, home console and computer games over the internet.")
        info.SetCopyright('(C) 2010-2012 Jason Gauci ')
        info.SetCopyright('(C) 2015 Quinn Granfor ')
        #info.SetWebSite('http://xxxxx')
        #info.SetLicence("license")
        info.AddDeveloper('DigitalGhost')
        info.AddDeveloper('SpootDev')
        info.AddDeveloper('Krusty')
        info.AddDocWriter('Krusty')
        #info.AddArtist('The Tango crew')
        #info.AddTranslator('Spoot')
        wx.AboutBox(info)

    def OnMainHubCadeSite( self, event ):
        webbrowser.open("https://sites.google.com/site/hubcade/Home/",1,True)

    def onConfigurationMenuItem( self, event ):
        dialog = ConfigDialog(self)
        dialog.ShowModal()
        dialog.Destroy()

    def onHubCadeMenuItem( self, event ):
        cade_main()
        print "boomer"
        event.Skip()

    def onHubCadeEditorMenuItem( self, event ):
        if str.upper(sys.platform[0:3])=='WIN' \
        or str.upper(sys.platform[0:3])=='CYG':
            subprocess.call(['./HubCade_Editor.exe'])
        else:
            subprocess.call(['./HubCade_Editor'])
        event.Skip()

    def OnChatArchiveViewMenuItem( self, event ):
        dialog = ChatViewDialog(self)
        dialog.Show()
        #dialog.Destroy()

    def OnFriendBlockMenuItem( self, event ):
        dialog = FriendBlockDialog(self)
        dialog.Show()
        #dialog.Destroy()

    def OnSliderResetMenuItem( self, event ):
        self.sash_left.SetSashPosition(self.m_panel29.Size[1]/2,True)
        self.sash_right.SetSashPosition(self.m_panel28.Size[1]/2,True)
        self.sash_middle.SetSashPosition(self.Size[0]/2,True)
        self.Refresh()
        wx.CallAfter(Client_GlobalData.app.mainFrame.OnChatResize, event )
        wx.CallAfter(Client_GlobalData.app.mainFrame.OnImageResize, event )
        event.Skip()

    def OnVidPlayButton( self, event ):
        # playback file if can
        if not self.vid_playback_control.Play():
            wx.MessageBox("Unable to Play media : Unsupported format?", "Playback Error", wx.ICON_ERROR | wx.OK)
        else:
            if Client_GlobalData_Config.video_mute == True:
                self.vid_playback_control.SetVolume(0)
            #print "length ",self.vid_playback_control.Length()
            self.timer_slider.Start(100)
            self.video_playback_slider.SetRange(0, self.vid_playback_control.Length())
            self.vid_playback_control.SetInitialSize()
            self.GetSizer().Layout()

    def OnVidPauseButton( self, event ):
        self.vid_playback_control.Pause()
        self.timer_slider.Stop()

    def OnVidStopButton( self, event ):
        self.vid_playback_control.Stop()
        self.timer_slider.Stop()

    def OnVidMuteToggleButton( self, event ):
        event.Skip()

    def OnVidVolumeDownButton( self, event ):
        volume = self.vid_playback_control.GetVolume() - 0.1
        if volume < 0:
            volume = 0
        self.vid_playback_control.SetVolume(volume)

    def OnVidVolumeUpButton( self, event ):
        volume = self.vid_playback_control.GetVolume() + 0.1
        if volume > 10:
            volume = 10
        self.vid_playback_control.SetVolume(volume)

    def OnMediaLoad(self, evt):
        # playback file if can
        if not self.vid_playback_control.Play():
            wx.MessageBox("Unable to Play media : Unsupported format?", "Playback Error", wx.ICON_ERROR | wx.OK)
        else:
            if Client_GlobalData_Config.video_mute == True:
                self.vid_playback_control.SetVolume(0)
            #print "length ",self.vid_playback_control.Length()
            self.timer_slider.Start(100)
            self.video_playback_slider.SetRange(0, self.vid_playback_control.Length())
            self.vid_playback_control.SetInitialSize()
            self.GetSizer().Layout()

    def OnVideoFinished(self, evt):
        if Client_GlobalData_Config.video_repeat == True:
            if not self.vid_playback_control.Play():
                wx.MessageBox("Unable to Play media : Unsupported format?", "Playback Error", wx.ICON_ERROR | wx.OK)
            else:
                if Client_GlobalData_Config.video_mute == True:
                    self.vid_playback_control.SetVolume(0)
                self.timer_slider.Start(100)
                #print "length ",self.vid_playback_control.Length()
                self.video_playback_slider.SetRange(0, self.vid_playback_control.Length())
                self.vid_playback_control.SetInitialSize()
                self.GetSizer().Layout()

    def OnSeek(self, evt):
        self.vid_playback_control.Seek(self.video_playback_slider.GetValue())

    def OnVideoTimer(self, evt):
        self.video_playback_slider.SetValue(self.vid_playback_control.Tell())
        #self.st_size.SetLabel('size: %s' % self.vid_playback_control.GetBestSize())
        #self.st_len.SetLabel('length: %d seconds' % (self.vid_playback_control.Length()/1000))
        #self.st_pos.SetLabel('position: %d' % offset)

    def openBlogPage( self, event ):
        webbrowser.open("http://xxxxxx/",1,True)

    def openForumPage( self, event ):
        webbrowser.open("http://xxxxxx",1,True)

    def openHelpPage( self, event ):
        webbrowser.open("http://xxxxxx",1,True)

    def OnBugReportMenuItem( self, event ):
        webbrowser.open("http://xxxxxx",1,True)

    def OnImageChatResize( self, event ):
        wx.CallAfter(Client_GlobalData.app.mainFrame.OnChatResize, event )
        wx.CallAfter(Client_GlobalData.app.mainFrame.OnImageResize, event )
        #event.Skip()

    def OnImageResize( self, event ):
        # resize all images that are displayed
        # the try block is to catch the errors from resize events that fire before images are loaded and causing 0 division
        try:
            # do title image
            if (Client_GlobalData_Config.mame_mess==True and Client_GlobalData_Config.mame_title_display_tab == True) or (Client_GlobalData_Config.mame_mess==False and Client_GlobalData_Config.mess_title_display_tab == True):
                img = self.title_bitmap.GetBitmap().ConvertToImage()
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.title_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.title_bitmap.Refresh()
                self.title_bitmap.GetParent().Layout()
            #do snap image
            if (Client_GlobalData_Config.mame_mess==True and Client_GlobalData_Config.mame_snap_display_tab == True) or (Client_GlobalData_Config.mame_mess==False and Client_GlobalData_Config.mess_snap_display_tab == True):
                img = self.snap_bitmap.GetBitmap().ConvertToImage()
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.snap_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.snap_bitmap.Refresh()
                self.snap_bitmap.GetParent().Layout()
            #do cabinets image
            if (Client_GlobalData_Config.mame_mess==True and Client_GlobalData_Config.mame_cabinet_display_tab == True) or (Client_GlobalData_Config.mame_mess==False and Client_GlobalData_Config.mess_box_display_tab == True):
                img = self.cart_bitmap.GetBitmap().ConvertToImage()
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.cart_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.cart_bitmap.Refresh()
                self.cart_bitmap.GetParent().Layout()
            #do control panel image
            if (Client_GlobalData_Config.mame_mess==True and Client_GlobalData_Config.mame_control_panel_display_tab == True) or (Client_GlobalData_Config.mame_mess==False and Client_GlobalData_Config.mess_cart_display_tab == True):
                img = self.box_bitmap.GetBitmap().ConvertToImage()
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.box_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.box_bitmap.Refresh()
                self.box_bitmap.GetParent().Layout()
            #do marque image
            if (Client_GlobalData_Config.mame_mess==True and Client_GlobalData_Config.mame_marque_display_tab == True) or (Client_GlobalData_Config.mame_mess==False and Client_GlobalData_Config.mess_label_display_tab == True):
                img = self.label_bitmap.GetBitmap().ConvertToImage()
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.label_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.label_bitmap.Refresh()
                self.label_bitmap.GetParent().Layout()
            #do pcb image
            if (Client_GlobalData_Config.mame_mess==True and Client_GlobalData_Config.mame_pcb_display_tab == True) or (Client_GlobalData_Config.mame_mess==False and Client_GlobalData_Config.mess_cart_top_display_tab == True):
                img = self.cart_top_bitmap.GetBitmap().ConvertToImage()
                NewWidth, NewHeight = ResizeImageCalc(img,self.title_bitmap.Size[0],self.title_bitmap.Size[1])
                img = img.Scale(NewWidth,NewHeight)
                self.cart_top_bitmap.SetBitmap(wx.BitmapFromImage(img))
                self.cart_top_bitmap.Refresh()
                self.cart_top_bitmap.GetParent().Layout()
        except:
            pass
        #event.Skip()

    def OnChatResize( self, event ):
        # so chat doesn't "pop"
##        scrollPosition = Client_GlobalData.app.mainFrame.chatLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1]
##        scrollBottomPosition = (Client_GlobalData.app.mainFrame.chatLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])+Client_GlobalData.app.mainFrame.chatLogHTML.GetClientSize()[1]
##        scroll_bottom = False
###        print scrollBottomPosition, Client_GlobalData.app.mainFrame.chatLogHTML.GetVirtualSize()[1]
##        if scrollBottomPosition+30 >= Client_GlobalData.app.mainFrame.chatLogHTML.GetVirtualSize()[1]:
##            scroll_bottom = True
##        Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>")
###        print scroll_bottom
##        if scroll_bottom == True:
##            Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(-1, scrollBottomPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
##        else:
##            Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(0, scrollPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
        #print "chat resize"
        Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(-1, Client_GlobalData.app.mainFrame.chatLogHTML.GetClientSize()[0])
        #wx.CallAfter(Client_GlobalData.app.mainFrame.chatlogHTML.Refresh())
##        wx.CallAfter(self.chatLogHTML.Scroll(-1, ((self.chatLogHTML.GetViewStart()[1]*self.chatLogHTML.GetScrollPixelsPerUnit()[1])+self.chatLogHTML.GetClientSize()[1])/self.chatLogHTML.GetScrollPixelsPerUnit()[1]))
##        #wx.CallAfter(self.chatLogHTML.Scroll(-1, self.chatLogHTML.GetClientSize()[0]))

    def onMainFrameSize( self, event ):
        event.Skip()  # must leave this otherwise the sizer doesn't kick in
        wx.CallAfter(Client_GlobalData.app.mainFrame.OnChatResize, event )
        wx.CallAfter(Client_GlobalData.app.mainFrame.OnImageResize, event )

    def OnHostGameAddToFavMenuItem( self, event ):
        sql_args = self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection(),5).encode("utf8"),
        Client_GlobalData.curs_player.execute(u"select count(*) from game_info where game_rom_id = ?",sql_args)
        if int(Client_GlobalData.curs_player.fetchone()[0]) > 0:
            sql_statement = u"update game_info set game_favorite = 1 where game_rom_id = ?"
        else:
            sql_statement = u"insert into game_info (id,game_rom_id,game_favorite,game_times_played,game_time_played) values (NULL,?,1,0,0)"
        Client_GlobalData.curs_player.execute(sql_statement,sql_args)
        Client_GlobalData.conn_player.commit()
        Client_GlobalData.favorite_game_id.append(sql_args[0])
        # reload grid to show new favs (set to true so only loads when tab actived)
        Client_GlobalData.gui_update_favorite = True
        event.Skip()

    def OnHostGameRemFromFavMenuItem( self, event ):
        sql_args = self.gameListTree.GetItemText(self.gameListTree.GetSelection(),5).encode("utf8"),
        Client_GlobalData.curs_player.execute(u"update game_info set game_favorite = 0 where game_rom_id = ?",sql_args)
        Client_GlobalData.conn_player.commit()
        # remove from fav table
        Client_GlobalData.favorite_game_id.remove(self.gameListTree.GetSelection())
        # remove from favorite grid
        self.favorites_grid.Freeze()
        self.favorites_grid.DeleteRows(self.gameListTree.GetSelection(),1)
        self.favorites_grid.AutoSizeColumns(True)
        self.favorites_grid.AutoSizeRows(True)
        self.favorites_grid.Thaw()
        event.Skip()

    def OnHostGameHostGameMenuItem( self, event ):
        self.hostGameFromList(event)
        event.Skip()

    def OnFavoriteGameViewData( self, event ):
        game_file_path,game_system_id = Client_Database.SQL_Retrieve_File_Path_SystemId(Client_GlobalData.favorite_game_id[Client_GlobalData.grid_cell_row])
        self.GameImageDisplay(game_file_path,game_system_id,Client_GlobalData.favorite_game_id[Client_GlobalData.grid_cell_row])
        event.Skip()

    def OnFavoriteRemFromFavMenuItem( self, event ):
        sql_args = Client_GlobalData.favorite_game_id[Client_GlobalData.grid_cell_row],
        Client_GlobalData.curs_player.execute(u"update game_info set game_favorite = 0 where game_rom_id = ?",sql_args)
        Client_GlobalData.conn_player.commit()
        # remove from favorite grid
        self.favorites_grid.Freeze()
        self.favorites_grid.DeleteRows(Client_GlobalData.grid_cell_row,1)
        self.favorites_grid.AutoSizeColumns(True)
        self.favorites_grid.AutoSizeRows(True)
        self.favorites_grid.Thaw()
        # remove from the table
        Client_GlobalData.favorite_game_id.remove(sql_args[0])
        event.Skip()

    def OnFavoriteHostGameMenuItem( self, event ):
##        if Client_GlobalData.hasPortForwarded == False:
##            mdial = wx.MessageDialog(None, 'You do not have your port forwarded correctly!  You will not be able to host a game until you set up port forwarding, but you can still join games that other people host if you are the first person to join.', 'Port Forward', wx.OK | wx.ICON_EXCLAMATION)
##            mdial.ShowModal()
##            mdial.Destroy()
##            return
        if Client_GlobalData.mamePopen is not None:
            mdial = wx.MessageDialog(None, 'You already have an instance of CSMAME running. Please close it first.', 'Close CSMAME First', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()
        else:
            hostGameId = str(Client_GlobalData.favorite_game_id[Client_GlobalData.grid_cell_row])
            Client_GlobalData.database.createGameInstance(hostGameId,Client_GlobalData.playerID,Client_GlobalData.host_game_max_players,Client_GlobalData.host_game_max_observers)
            if Client_GlobalData.os_video_playback == True:
                self.vid_playback_control.Pause()
                self.timer_slider.Stop()
            launchGameByID(hostGameId,True,"",Client_GlobalData.selfPort,Client_GlobalData.selfPort)
            # search for the index to be used in the treeview
            #times_played = int(self.gameListTreeCtrl.GetItemText(self.gameListTreeCtrl.GetSelection(),1).encode("utf8")) + 1
            #self.gameListTreeCtrl.SetItemText(self.gameListTreeCtrl.GetSelection(),locale.format("%.0f", times_played),1)
        event.Skip()

    def OnJoinGameAddToFavMenuItem( self, event ):
        gameInstance = Client_GlobalData.database.getGameInstanceFromHostName(self.publicGameGrid.GetCellValue(Client_GlobalData.grid_cell_row, 0).encode("utf8"))
        sql_args = gameInstance.db_game_id,
        Client_GlobalData.curs_player.execute(u"select count(*) from game_info where game_rom_id = ?",sql_args)
        if int(Client_GlobalData.curs_player.fetchone()[0]) > 0:
            sql_statement = u"update game_info set game_favorite = 1 where game_rom_id = ?"
        else:
            sql_statement = u"insert into game_info (id,game_rom_id,game_favorite,game_times_played,game_time_played) values (NULL,?,1,0,0)"
        Client_GlobalData.curs_player.execute(sql_statement,sql_args)
        Client_GlobalData.conn_player.commit()
        Client_GlobalData.favorite_game_id.append(sql_args[0])
        # reload grid to show new favs (set to true so only loads when tab actived)
        Client_GlobalData.gui_update_favorite = True
        event.Skip()

    def OnJoinGameRemoveFromFavMenuItem( self, event ):
        # todo
        event.Skip()

    def OnJoinGameJoinGameMenuItem( self, event ):
        self.joinGameFromGames(event)
        event.Skip()

    def onURLclick( self, event ):
        if Client_GlobalData.webkit_enabled == False:
            webbrowser.open(event.GetLinkInfo().GetHref(),1,True)
        else:
            webbrowser.open(event.GetURL(),1,True)

    def editMAMESettings( self, event ):
        os.system(Client_GlobalData.editorName + " mame.ini")
        #call(Client_GlobalData.editorName + " mame.ini")   - might be only python 2.7

    def editMESSSettings( self, event ):
        os.system(Client_GlobalData.editorName + " mess.ini")
        #call(Client_GlobalData.editorName + " mess.ini")   - might be only python 2.7

    # fired off by send button and called by sendChatOnEnter
    def sendChat( self, event ):
        if len(self.chatText.GetLineText(0).strip().encode("utf8"))>0:
            if self.chat_aui_notebook.GetPageText(self.chat_aui_notebook.GetSelection()) == "Global":
                Client_GlobalData.networkProtocol.sendString("CHAT_MESSAGE "+self.chatText.GetLineText(0).encode("utf8"))
            elif self.chat_aui_notebook.GetPageText(self.chat_aui_notebook.GetSelection()) == "Private":
                Client_GlobalData.networkProtocol.sendString("PRIV_CHAT "+self.chatText.GetLineText(0).encode("utf8"))
            elif self.chat_aui_notebook.GetPageText(self.chat_aui_notebook.GetSelection()) == "Admin":
                Client_GlobalData.networkProtocol.sendString("ADMIN_CHAT "+self.chatText.GetLineText(0).encode("utf8"))
            self.chatText.Clear()

    def OnClearChatButton( self, event ):
        if self.chat_aui_notebook.GetPageText(self.chat_aui_notebook.GetSelection()) == "Global":
            Client_GlobalData.chatHTML = ""
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>")
            else:
                Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>","")
        elif self.chat_aui_notebook.GetPageText(self.chat_aui_notebook.GetSelection()) == "Private":
            Client_GlobalData.privHTML = ""
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.privateLogHTML.SetPage("<html>" + Client_GlobalData.privHTML + "</html>")
            else:
                Client_GlobalData.app.mainFrame.privateLogHTML.SetPage("<html>" + Client_GlobalData.privHTML + "</html>","")
        elif self.chat_aui_notebook.GetPageText(self.chat_aui_notebook.GetSelection()) == "Admin":
            Client_GlobalData.adminHTML = ""
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.adminLogHTML.SetPage("<html>" + Client_GlobalData.adminHTML + "</html>")
            else:
                Client_GlobalData.app.mainFrame.adminLogHTML.SetPage("<html>" + Client_GlobalData.adminHTML + "</html>","")

    def OnEmoteBitmapCombo( self, event ):
        self.chatText.SetValue(self.chatText.GetValue() + " " + self.emote_bitmapcombo.GetString(event.GetInt()) + " ")

    def sendChatOnEnter( self, event ):
        if event.KeyCode == 13 or event.KeyCode == 370:
            if len(self.chatText.GetLineText(0).strip())>0:
                if len(self.chatText.GetLineText(0).strip().encode("utf8"))>0:
                    self.sendChat(None)
        elif event.KeyCode==9:
            restOfText,spacer,partialName = self.chatText.GetLineText(0).encode("utf8").rpartition(' ')
            self.chatText.SetValue(restOfText + spacer + Client_GlobalData.database.getAutocompleteName(partialName))
            self.chatText.SetInsertionPoint(self.chatText.GetLastPosition())
        else:
            event.Skip()

    def OnaddToFriendsMenuItem( self, event ):
        selectedUsername = self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2)
        sql_statement = u"insert into player_info (id,player_name,player_friend) values (NULL,\"" + selectedUsername + u"\",1)"
        Client_Database.SQL_HubCade_Arrange_GUI(sql_statement)
        event.Skip()

    def OnremoveFromFriendsMenuItem( self, event ):
        selectedUsername = self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2)
        sql_statement = u"delete from player_info where player_name = \"" + selectedUsername + u"\" and player_friend = 1"
        Client_Database.SQL_HubCade_Arrange_GUI(sql_statement)
        event.Skip()

    def onPlayerGridAdmin_KickUserMenuItem( self, event ):
        Client_GlobalData.networkProtocol.sendString("ADMIN_USER_KICK " + self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2).encode("utf8"))
        event.Skip()

    def OnPlayerGridAdminMuteUsermenuItem( self, event ):
        Client_GlobalData.networkProtocol.sendString("ADMIN_USER_MUTE " + self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2).encode("utf8"))
        event.Skip()

    def OnPlayerGridAdminBanTemp( self, event ):
        Client_GlobalData.networkProtocol.sendString("ADMIN_USER_BAN_TEMP " + self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2).encode("utf8"))
        event.Skip()

    def OnPlayerGridAdminBanFull( self, event ):
        Client_GlobalData.networkProtocol.sendString("ADMIN_USER_BAN_FULL " + self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2).encode("utf8"))
        event.Skip()

    def OnPlayerGridAdminBanUserEmail( self, event ):
        Client_GlobalData.networkProtocol.sendString("ADMIN_USER_BAN_EMAIL " + self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2).encode("utf8"))
        event.Skip()

    def OnChatBlockMenuItem( self, event ):
        selectedUsername = self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2)
        sql_statement = u"insert into player_info (id,player_name,player_block_chat) values (NULL,\"" + selectedUsername + u"\",1)"
        Client_Database.SQL_HubCade_Arrange_GUI(sql_statement)
        event.Skip()

    def OnremovechatblockMenuItem( self, event ):
        selectedUsername = self.playerGridNew.GetCellValue(Client_GlobalData.grid_cell_row, 2)
        sql_statement = u"delete from player_info where player_name = \"" + selectedUsername + u"\" and player_block_chat = 1"
        Client_Database.SQL_HubCade_Arrange_GUI(sql_statement)
        event.Skip()

    def filterGameTree( self, event ):
        self.cyclesUntilFilter = min(10,self.cyclesUntilFilter+5)
        event.Skip()

    def OnHostMonitorFilterComboChange( self, event ):
        wx.CommandEvent(wx.EVT_TEXT, self.gameSearchText)
        event.Skip()

    def OnFilterPlayerSpinner( self, event ):
        wx.CommandEvent(wx.EVT_TEXT, self.gameSearchText)
        event.Skip()

    def OnHostCategoryFilter( self, event ):
        wx.CommandEvent(wx.EVT_TEXT, self.gameSearchText)
        event.Skip()

    def ongamefilterResetButton( self, event ):
        self.gameSearchText.SetValue("")
        # don't need to manually call event below in windows at least
        #wx.CommandEvent(wx.EVT_TEXT, self.gameSearchText)
        event.Skip()

    def onExportChatMenuItem( self, event ):
        fileName = u"HubCade_Chat_Log_" + time.strftime("%Y%m%d_%H%M%S").encode("utf8") + ".html"
        outHandle = open ( fileName, 'w')
        outHandle.write("<html>" + Client_GlobalData.chatHTML.encode("utf8") + "</html>")
        outHandle.close()
        mdial = None
        if os.path.exists(fileName):
            path_flip = u"\\"
            if str.upper(sys.platform[0:3])=='WIN' \
            or str.upper(sys.platform[0:3])=='CYG':
                path_flip = u"/"
            mdial = wx.MessageDialog(None, "Chat file: " + os.getcwd() + path_flip + fileName + " saved successfully.", 'Chat saved', wx.OK | wx.ICON_INFORMATION)
        else:
            mdial = wx.MessageDialog(None, "Sorry, chat not saved properly.", 'Chat save failed', wx.OK | wx.ICON_EXCLAMATION)
        mdial.ShowModal()
        mdial.Destroy()

    def addLFG( self, event ):
        event.Skip()
        if self.LFGText.GetLineText(0).find(' ')!=-1:
            mdial = wx.MessageDialog(None, 'Sorry, spaces are not allowed.', 'Spaces not allowed', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()
        elif self.LFGText.GetLineText(0).find('/')!=-1:
            mdial = wx.MessageDialog(None, "Sorry, '/' is not allowed.", 'Slash not allowed', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()
        elif len(self.LFGText.GetLineText(0)):
            if(len(Client_GlobalData.player.LFG)):
                Client_GlobalData.database.setLFG(
                Client_GlobalData.player.LFG + "/" +
                self.LFGText.GetLineText(0).encode("utf8")
                )
            else:
                Client_GlobalData.database.setLFG(
                self.LFGText.GetLineText(0).encode("utf8")
                )
            self.LFGText.Clear()

    def removeLFG( self, event ):
        event.Skip()
        selections = self.LFGList.GetSelections()
        if len(selections)>0:
            selectedItem = selections[0]
            if selectedItem == -1:
                return
            selectedItem = self.LFGList.GetString(selectedItem).encode("utf8")
            #print selectedItem
            currentLFG = Client_GlobalData.player.LFG
            #print currentLFG,'->',
            currentLFG = currentLFG.replace(selectedItem,'',1)
            currentLFG = currentLFG.replace('//','/')
            currentLFG = currentLFG.lstrip('/').rstrip('/')
            #print currentLFG
            Client_GlobalData.database.setLFG(currentLFG)

    def uploadToYoutube(self, event):
        YoutubeUploader(self).Show()

    def OnEditMenuItem_Copy( self, event ):
        event.Skip()

    def OnEditMenuItem_Paste( self, event ):
        event.Skip()

    def OnChatPageChanged( self, event ):
        if self.chat_aui_notebook.GetSelection() == 0:
            self.chat_aui_notebook.SetWindowStyle(wx.aui.AUI_NB_SCROLL_BUTTONS)
        else:
            self.chat_aui_notebook.SetWindowStyle(wx.aui.AUI_NB_CLOSE_ON_ALL_TABS | wx.aui.AUI_NB_SCROLL_BUTTONS)
        event.Skip()

    def OnChatPageClosed( self, event ):
        event.Skip()

    def OnGameInfoImagesPageChanged( self, event ):
        #self.ToggleWindowStyle(wx.aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)
##        # removed the following as then can't close down tabs except in options
##        if self.game_info_images_auinotebook.GetSelection() == 0:
##            self.game_info_images_auinotebook.SetWindowStyle(wx.aui.AUI_NB_SCROLL_BUTTONS)
##        else:
##            #self.game_info_images_auinotebook.SetWindowStyle(wx.aui.AUI_NB_CLOSE_ON_ALL_TABS | wx.aui.AUI_NB_SCROLL_BUTTONS)
##            self.game_info_images_auinotebook.SetWindowStyle(wx.aui.AUI_NB_SCROLL_BUTTONS)
        event.Skip()

    def OnGameInfoImagesPageClosed( self, event ):
        removed_page = event.GetSelection() - 1  # do the -1 so it will match the list below as info page is 0 and can't be removed
        print "removed: ",removed_page
        #print "count: ",len(Client_GlobalData_Config.auinotebook_mame_list)
        self.cfg = wx.Config('hubcade_gui_config')
        if Client_GlobalData_Config.mame_mess == True:
            item_type = Client_GlobalData_Config.auinotebook_mame_list[removed_page]
            Client_GlobalData_Config.auinotebook_mame_list.pop(removed_page)
            if item_type == 1:
                Client_GlobalData_Config.mame_title_snap_display_tab = 0
                self.cfg.WriteInt("mame_title_snap_display_tab", 0)
            elif item_type == 2:
                Client_GlobalData_Config.mame_title_display_tab = 0
                self.cfg.WriteInt("mame_title_display_tab", 0)
            elif item_type == 3:
                Client_GlobalData_Config.mame_snap_display_tab = 0
                self.cfg.WriteInt("mame_snap_display_tab", 0)
            elif item_type == 4:
                Client_GlobalData_Config.mame_cabinet_display_tab = 0
                self.cfg.WriteInt("mame_cabinet_display_tab", 0)
            elif item_type == 5:
                Client_GlobalData_Config.mame_control_panel_display_tab = 0
                self.cfg.WriteInt("mame_control_panel_display_tab", 0)
            elif item_type == 6:
                Client_GlobalData_Config.mame_marque_display_tab = 0
                self.cfg.WriteInt("mame_marque_display_tab", 0)
            elif item_type == 7:
                Client_GlobalData_Config.mame_pcb_display_tab = 0
                self.cfg.WriteInt("mame_pcb_display_tab", 0)
            elif item_type == 8:
                Client_GlobalData_Config.mame_video_playback_display_tab = 0
                self.cfg.WriteInt("mame_video_playback_display_tab", 0)
            elif item_type == 9:
                Client_GlobalData_Config.mame_manual_display_tab = 0
                self.cfg.WriteInt("mame_manual_display_tab", 0)
        else:
            item_type = Client_GlobalData_Config.auinotebook_mess_list[removed_page]
            Client_GlobalData_Config.auinotebook_mess_list.pop(removed_page)
            if item_type == 1:
                Client_GlobalData_Config.mess_title_snap_display_tab = 0
                self.cfg.WriteInt("mess_title_snap_display_tab", 0)
            elif item_type == 2:
                Client_GlobalData_Config.mess_title_display_tab = 0
                self.cfg.WriteInt("mess_title_display_tab", 0)
            elif item_type == 3:
                Client_GlobalData_Config.mess_snap_display_tab = 0
                self.cfg.WriteInt("mess_snap_display_tab", 0)
            elif item_type == 4:
                Client_GlobalData_Config.mess_box_display_tab = 0
                self.cfg.WriteInt("mess_box_display_tab", 0)
            elif item_type == 5:
                Client_GlobalData_Config.mess_cart_display_tab = 0
                self.cfg.WriteInt("mess_cart_display_tab", 0)
            elif item_type == 6:
                Client_GlobalData_Config.mess_label_display_tab = 0
                self.cfg.WriteInt("mess_label_display_tab", 0)
            elif item_type == 7:
                Client_GlobalData_Config.mess_cart_top_display_tab = 0
                self.cfg.WriteInt("mess_cart_top_display_tab", 0)
            elif item_type == 8:
                Client_GlobalData_Config.mess_video_playback_display_tab = 0
                self.cfg.WriteInt("mess_video_playback_display_tab", 0)
            elif item_type == 9:
                Client_GlobalData_Config.mess_manual_display_tab = 0
                self.cfg.WriteInt("mess_manual_display_tab", 0)
        self.cfg.Flush()
##        for row in Client_GlobalData_Config.auinotebook_mame_list:
##            print row
        event.Skip()

    def OnImageConvertMenuItem( self, event ):
        wildcard = "Image (*.bmp; *.gif; *.jpeg;*.pcx;*.pnm;*.tiff;*.xpm;*.jpg)|*.bmp;*.gif;*.jpeg;*.pcx;*.pnm;*.tiff;*.xpm;*.jpg|" \
                 "Windows Bitamp (*.bmp)|*.bmp|" \
                 "Graphics Interchange Format (*.gif)|*.gif|" \
                 "Joint Photographic Experts Group (*.jpeg;*.jpg)|*.jpeg;*.jpg|" \
                 "PC Paintbrush (*.pcx)|*.pcx|" \
                 "Portable Any Map (*.pnm)|*.pnm|" \
                 "Tagged Image File Format (*.tiff)|*.tiff|" \
                 "X PixMap (*.xpm)|*.xpm|" \
                 "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Choose image(s)",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for file_path in paths:
                file_name, ext = os.path.splitext(file_path)
                if os.path.exists(file_name + ".png"):
                    pass
                else:
                    im = Image.open(file_path)
                    im.save(file_name + ".png", "PNG")
        dlg.Destroy()

    def OnArchiveZip7zConvertMenuItem( self, event ):
        wildcard = "ZIP (zip) (*.zip)|*.zip|" \
                 "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Choose archive(s)",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            #directory = dlg.GetPath();
            for archive_rom_name in paths:
                file_name, ext = os.path.splitext(archive_rom_name)
                if os.path.exists(file_name + ".7z"):
                    pass
                else:
                    # convert the zip

# multiple heaers or sumthing?
                    pass
        dlg.Destroy()

    def OnArchiveConvertMenuItem( self, event ):
        wildcard = "LZMA (7z) (*.7z)|*.7z|" \
                 "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Choose archive(s)",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            #directory = dlg.GetPath();
            for archive_rom_name in paths:
                file_name, ext = os.path.splitext(archive_rom_name)
                if os.path.exists(file_name + ".zip"):
                    pass
                else:
                    try:
                        # open the archive file
                        fp = open(archive_rom_name, 'rb')
                        archive = Archive7z(fp)
                        filenames = list(archive.getnames())
                        z = zipfile.ZipFile(file_name + ".zip", "w",compression)
                        # loop through all files in archive and write to zip
                        for archive_file_name in filenames:
                            try:
                                zip_IO_buffer = StringIO
                                cf = archive.getmember(archive_file_name)
                                zip_IO_buffer = cf.read()
                                z.writestr(archive_file_name, zip_IO_buffer)
                                #del zip_IO_buffer
                            except:
                                z.close()
                                os.remove(archive_file_name)
                                break;
                        z.close()
                    except:
                        print "7z read fail:",archive_rom_name
        dlg.Destroy()

    def OnRom7zConvertMenuItem( self, event ):
        wildcard = "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Choose rom(s)",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for rom_name in paths:
                file_name, ext = os.path.splitext(rom_name)
                if os.path.exists(file_name + ".7z"):
                    pass
                else:
                    iconfile = open(rom_name,"rb")
                    file_data = iconfile.read()
                    fin = open(file_name + ".7z", "wb")
                    archive_data = StringIO()
                    comp_data = pylzma.compressfile(StringIO(file_data))
                    # LZMA header
                    archive_header = comp_data.read(5)
                    # size of uncompressed data
                    archive_header += struct.pack('<Q', len(file_data))
                    # compressed data
                    archive_data.write(archive_header + comp_data.read())
                    fin.write(archive_data.getvalue())
                    archive_data.close()
                    fin.close()
                    iconfile.close()
        dlg.Destroy()

    def OnRomZipConvertMenuItem( self, event ):
        wildcard = "All files (*.*)|*.*"
        dlg = wx.FileDialog(
            self, message="Choose rom(s)",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for rom_name in paths:
                file_name, ext = os.path.splitext(rom_name)
                if os.path.exists(file_name + ".zip"):
                    pass
                else:
                    z = zipfile.ZipFile(file_name + ".zip", "w",compression)
                    try:
                        z.write(os.path.basename(file_name) + ext)
                    except:
                        z.close()
                        os.remove(os.path.basename(file_name) + ext)
                        break;
                    z.close()
        dlg.Destroy()

    def OnAdminMOTDMenuItem( self, event ):
        dialog = MOTDDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            # send the motd
            Client_GlobalData.networkProtocol.sendString("MOTD "+ Client_GlobalData.motd_value.encode("utf8"))
        dialog.Destroy()

    def OnAdminBanInquiryMenuItem( self, event ):
        Client_GlobalData.networkProtocol.sendString("REQ_BAN_LIST")

    def OnServerStatsMenuItem( self, event ):
        Client_GlobalData.networkProtocol.sendString("REQ_SRV_STATS")

    def Ontop10StatsMenuItem( self, event ):
        Client_GlobalData.networkProtocol.sendString("REQ_TOP10")

