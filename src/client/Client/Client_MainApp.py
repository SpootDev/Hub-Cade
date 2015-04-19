# import wxWidgets files
import wx

# import globals
import Client_GlobalData
import Client_GlobalData_Config

# import python mods
import sys,os

# import code
from Client_Database import *
from Client_Game import *
from Client_Game_Audit import *
from Client_Host_Game import *
from Client_INIParser import *
from Client_MainFrame import *
from Client_Network import *

class MainApp(wx.App):
    def OnInit(self):
        self.name = "HubCade-%s" % wx.GetUserId()
        self.instance = wx.SingleInstanceChecker(self.name)
        if '--multi' not in sys.argv and self.instance.IsAnotherRunning():
            mdial = wx.MessageDialog(None, 'Another instance of Hub!Cade is already running (maybe in the system tray?). If you want to run multiple copies of Hub!CAde on the same machine.','Already running Hub!Cade', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
            self.quit = True
            sys.exit(1)
        self.quit = False

        # set the working dir
        Client_GlobalData.application_launch_directory = os.getcwd().replace('\\','/')

        self.gameStartedSound = wx.Sound('../Sounds/GameStarted.wav')
        self.challengeSound = wx.Sound('../Sounds/Challenge.wav')
        self.playSound = wx.Sound('../Sounds/PlayGame.ogg')
        self.chimeSound = wx.Sound('../Sounds/chime.wav')
        self.friendEntrySound = wx.Sound('../Sounds/friendentry.wav')
        self.friendExitSound = wx.Sound('../Sounds/friendexit.wav')

        #Initialize system-media map
        sysMediaFile = open("Data/media.txt",'rU')
        for line in sysMediaFile.readlines()[2:]:
            if line[0]!=' ':
                #New system
                system = line.partition(' ')[0]
            mediaName = line.partition('(')[2].partition(')')[0]
            extensions = []
            for token in line.split():
                if token[0]=='.':
                    extensions.append(token)
            #print system,mediaName,extensions
            if line[0]!=' ':
                Client_GlobalData.systemMediaTypes[system] = [MediaType(mediaName,extensions)]
            else:
                Client_GlobalData.systemMediaTypes[system].append(MediaType(mediaName,extensions))

        Client_GlobalData.app = self
        self.clientFactory = MyClientFactory()
        self.hostGameDialog = None
        self.entryDialog = None

        reactor.startRunning()

        timerid = wx.NewId()
        self.timer = wx.Timer(self, timerid)
        wx.EVT_TIMER(self, timerid, self.reactorUpdate)
        self.timer.Start(150, True)

        Client_GlobalData.database = DatabaseClient()

        Client_GlobalData.auditData = GameAuditer()
        if Client_GlobalData.auditData.load_hash_map_from_database()==False:
            iniParser = INIParser("mame.ini")
            romPaths = iniParser.getRomPaths()
            Client_GlobalData.auditData.baseDirectories = romPaths
            Client_GlobalData.auditData.audit()

        self.mainFrame = MainFrame(None)
        self.hostGameDialog = HostGameDialog(self.mainFrame)
        self.entryDialog = ProgramEntryDialog(self.mainFrame)

        # set title
        self.mainFrame.SetTitle(u"Hub!Cade " + Client_GlobalData.software_rev)

        #self.mainFrame.playerGridNew.SetRowLabelSize(0)
        # setup form from config file
        self.cfg = wx.Config('hubcade_gui_config')
        # read config settings for program
        # font config
        if self.cfg.Exists('chat_font'):
             Client_GlobalData_Config.chat_font = self.cfg.Read('chat_font')
        if self.cfg.Exists('chat_font_size'):
             Client_GlobalData_Config.chat_font_size = self.cfg.ReadInt('chat_font_size')
        if self.cfg.Exists('chat_font_color'):
             Client_GlobalData_Config.chat_font_color = self.cfg.Read('chat_font_color')

        if self.cfg.Exists('user_list_font'):
             Client_GlobalData_Config.user_list_font = self.cfg.Read('user_list_font')
        if self.cfg.Exists('user_list_font_size'):
             Client_GlobalData_Config.user_list_font_size = self.cfg.ReadInt('user_list_font_size')
        if self.cfg.Exists('user_list_font_color'):
             Client_GlobalData_Config.user_list_font_color = self.cfg.Read('user_list_font_color')

        if self.cfg.Exists('gamelist_font'):
             Client_GlobalData_Config.gamelist_font = self.cfg.Read('gamelist_font')
        if self.cfg.Exists('gamelist_font_size'):
             Client_GlobalData_Config.gamelist_font_size = self.cfg.ReadInt('gamelist_font_size')
        if self.cfg.Exists('gamelist_font_color'):
             Client_GlobalData_Config.gamelist_font_color = self.cfg.Read('gamelist_font_color')

        if self.cfg.Exists('gameinfo_font'):
             Client_GlobalData_Config.gameinfo_font = self.cfg.Read('gameinfo_font')
        if self.cfg.Exists('gameinfo_font_size'):
             Client_GlobalData_Config.gameinfo_font_size = self.cfg.ReadInt('gameinfo_font_size')
        if self.cfg.Exists('gameinfo_font_color'):
             Client_GlobalData_Config.gameinfo_font_color = self.cfg.Read('gameinfo_font_color')

        # image config
        if self.cfg.Exists('autodown_image'):
             Client_GlobalData_Config.autodown_image = self.cfg.ReadInt('autodown_image')
        if self.cfg.Exists('file_save_method'):
             Client_GlobalData_Config.file_save_method = self.cfg.ReadInt('file_save_method')
        # mame image config
        if self.cfg.Exists('mame_info_display_tab'):
             Client_GlobalData_Config.mame_info_display_tab = self.cfg.ReadInt('mame_info_display_tab')
        if self.cfg.Exists('mame_title_snap_display_tab'):
             Client_GlobalData_Config.mame_title_snap_display_tab = self.cfg.ReadInt('mame_title_snap_display_tab')
        if self.cfg.Exists('mame_title_display_tab'):
             Client_GlobalData_Config.mame_title_display_tab = self.cfg.ReadInt('mame_title_display_tab')
        if self.cfg.Exists('mame_snap_display_tab'):
             Client_GlobalData_Config.mame_snap_display_tab = self.cfg.ReadInt('mame_snap_display_tab')
        if self.cfg.Exists('mame_cabinet_display_tab'):
             Client_GlobalData_Config.mame_cabinet_display_tab = self.cfg.ReadInt('mame_cabinet_display_tab')
        if self.cfg.Exists('mame_control_panel_display_tab'):
             Client_GlobalData_Config.mame_control_panel_display_tab = self.cfg.ReadInt('mame_control_panel_display_tab')
        if self.cfg.Exists('mame_marque_display_tab'):
             Client_GlobalData_Config.mame_marque_display_tab = self.cfg.ReadInt('mame_marque_display_tab')
        if self.cfg.Exists('mame_pcb_display_tab'):
             Client_GlobalData_Config.mame_pcb_display_tab = self.cfg.ReadInt('mame_pcb_display_tab')
        if self.cfg.Exists('mame_video_playback_tab'):
             Client_GlobalData_Config.mame_video_playback_display_tab = self.cfg.ReadInt('mame_video_playback_tab')
        if self.cfg.Exists('mame_manual_display_tab'):
             Client_GlobalData_Config.mame_manual_display_tab = self.cfg.ReadInt('mame_manual_display_tab')
        # mess image config
        if self.cfg.Exists('mess_info_display_tab'):
             Client_GlobalData_Config.mess_info_display_tab = self.cfg.ReadInt('mess_info_display_tab')
        if self.cfg.Exists('mess_title_snap_display_tab'):
             Client_GlobalData_Config.mess_title_snap_display_tab = self.cfg.ReadInt('mess_title_snap_display_tab')
        if self.cfg.Exists('mess_title_display_tab'):
             Client_GlobalData_Config.mess_title_display_tab = self.cfg.ReadInt('mess_title_display_tab')
        if self.cfg.Exists('mess_snap_display_tab'):
             Client_GlobalData_Config.mess_snap_display_tab = self.cfg.ReadInt('mess_snap_display_tab')
        if self.cfg.Exists('mess_box_display_tab'):
             Client_GlobalData_Config.mess_box_display_tab = self.cfg.ReadInt('mess_box_display_tab')
        if self.cfg.Exists('mess_cart_display_tab'):
             Client_GlobalData_Config.mess_cart_display_tab = self.cfg.ReadInt('mess_cart_display_tab')
        if self.cfg.Exists('mess_label_display_tab'):
             Client_GlobalData_Config.mess_label_display_tab = self.cfg.ReadInt('mess_label_display_tab')
        if self.cfg.Exists('mess_cart_top_display_tab'):
             Client_GlobalData_Config.mess_cart_top_display_tab = self.cfg.ReadInt('mess_cart_top_display_tab')
        if self.cfg.Exists('mess_video_playback_tab'):
             Client_GlobalData_Config.mess_video_playback_display_tab = self.cfg.ReadInt('mess_video_playback_tab')
        if self.cfg.Exists('mess_manual_display_tab'):
             Client_GlobalData_Config.mess_manual_display_tab = self.cfg.ReadInt('mess_manual_display_tab')
        # theme/app settigns
        if self.cfg.Exists('html_chat_window_lines'):
             Client_GlobalData_Config.html_chat_window_lines = self.cfg.ReadInt('html_chat_window_lines')
        if self.cfg.Exists('user_list_sort'):
             Client_GlobalData_Config.user_list_sort = self.cfg.ReadInt('user_list_sort')
        if self.cfg.Exists('display_emote_in_chat'):
             Client_GlobalData_Config.display_emote_in_chat = self.cfg.ReadInt('display_emote_in_chat')
        if self.cfg.Exists('allow_client_downloads'):
             Client_GlobalData_Config.allow_client_downloads = self.cfg.ReadInt('allow_client_downloads')
        if self.cfg.Exists('mute_chat_sounds'):
             Client_GlobalData_Config.mute_chat_sounds = self.cfg.ReadInt('mute_chat_sounds')
        if self.cfg.Exists('chime_on_chat_name'):
             Client_GlobalData_Config.chime_on_chat_name = self.cfg.ReadInt('chime_on_chat_name')
        if self.cfg.Exists('use_miniupnpc'):
             Client_GlobalData_Config.use_miniupnpc = self.cfg.ReadInt('use_miniupnpc')
        if self.cfg.Exists('chime_on_friend'):
             Client_GlobalData_Config.chime_on_friend = self.cfg.ReadInt('chime_on_friend')
        # video playback settigns
        if self.cfg.Exists('video_download'):
             Client_GlobalData_Config.video_download = self.cfg.ReadInt('video_download')
        if self.cfg.Exists('video_mute'):
             Client_GlobalData_Config.video_mute = self.cfg.ReadInt('video_mute')
        if self.cfg.Exists('video_volume'):
             Client_GlobalData_Config.video_volume = self.cfg.ReadInt('video_volume')
        if self.cfg.Exists('video_repeat'):
             Client_GlobalData_Config.video_repeat = self.cfg.ReadInt('video_repeat')
        # misc settings tab
        if self.cfg.Exists('chat_save_to_db'):
            Client_GlobalData_Config.chat_save_to_db = self.cfg.ReadInt('chat_save_to_db')
        if self.cfg.Exists('chat_export_on_disco'):
            Client_GlobalData_Config.chat_export_on_disco = self.cfg.ReadInt('chat_export_on_disco')
        if self.cfg.Exists('display_clock_24'):
            Client_GlobalData_Config.display_clock_24 = self.cfg.ReadInt('display_clock_24')
        if self.cfg.Exists('record_inp_on_mame'):
            Client_GlobalData_Config.record_inp_on_mame = self.cfg.ReadInt('record_inp_on_mame')
        if self.cfg.Exists('ping_timeframe'):
            Client_GlobalData_Config.ping_timeframe.SetValue(self.cfg.ReadInt('ping_timeframe'))
        # audit settings tab
        if self.cfg.Exists('skip_mechanical'):
            Client_GlobalData_Config.skip_mechanical = self.cfg.ReadInt('skip_mechanical')
        if self.cfg.Exists('skip_adult'):
            Client_GlobalData_Config.skip_adult = self.cfg.ReadInt('skip_adult')
        if self.cfg.Exists('scan_choice'):
            Client_GlobalData_Config.scan_choice = self.cfg.ReadInt('scan_choice')
        if self.cfg.Exists('skip_clones'):
            Client_GlobalData_Config.skip_clones = self.cfg.ReadInt('skip_clones')
        if self.cfg.Exists('skip_gambling'):
            Client_GlobalData_Config.skip_gambling = self.cfg.ReadInt('skip_gambling')
        if self.cfg.Exists('skip_mahjong'):
            Client_GlobalData_Config.skip_mahjong = self.cfg.ReadInt('skip_mahjong')
        if self.cfg.Exists('rename_files'):
            Client_GlobalData_Config.rename_files = self.cfg.ReadInt('rename_files')
        # connect to server
        self.entryDialog.Show()
        # populate the bitmap combo for emotes
        img = wx.Image( u"../images/emotes/Ashamed.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(ashamed)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/BangWall.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bangwall)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/beerwez.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(beer)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Biggin.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bgrin)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/BigLaugh.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(lol)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/bslap.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bslap)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/ChairHit.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(chair)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Clap.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(clap)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Confused3.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(con)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/cool_smiley.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(cool)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/First.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(first)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/GreenAlien.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(alien)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Hammer3.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(hammer)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Irritated.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(irr)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/nono4.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(nono)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Rock.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(rock)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Shades.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(shade)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Sorry56fdg.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(sorry)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Tongue2.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(tongue)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Uzi.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(uzi)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/VeryAngry.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(mad)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/Whistle.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(whistle)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/drinking08.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(cheers)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/beta1.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(beta)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/feedtroll.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(troll)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/lame.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(lame)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/pics.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(pics)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/jerry.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(jerry)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/drool.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(drool)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/bat.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bat)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/stupid.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(stupid)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/hissy.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(hissy)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/404.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(404)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/blah2.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(blah)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/bow2.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bow)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/laught16.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(rofl)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/soapbox2.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(soap)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/sleep1.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(zzz)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/sick.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(sick)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/pirate.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(pirate)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/surrender.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(surrender)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/shuriken.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(nstar)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/thumbup.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(ok)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/happybday.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bday)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/innocent.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(angel)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/nuke.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(nuke)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/oops.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(oops)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/offtopic.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(off)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/w00t.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(wow)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/drink.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(drink)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/doh1.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(doh)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/yawn.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(yawn)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/help.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(help)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/eek.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(eek)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/ambulance.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(ambulance)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/peek.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(peek)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/blind.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(blind)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/crazy.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(crazy)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/blush.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(blush)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/circles.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(circles)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/yeah.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(yeah)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/wtf.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(wtf)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/master.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(master)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/hi.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(hi)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/cold.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(cold)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/booboo.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(booboo)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/tmi.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(tmi)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/welcome.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(welcome)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/assimilate.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(borg)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/ballnchain.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(ballnchain)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/bravo.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bravo)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/phone.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(phone)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/rip.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(rip)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/bye.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(bye)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/pray.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(pray)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/kids.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(kids)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/nn.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(nn)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/shock.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(shock)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/gaming.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(gaming)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/party.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(party)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/smoke.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(smoke)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/sad.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(sad)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/deadhorse.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(horse)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/inoob.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(inoob)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/waterski.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(wski)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/woot.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(woot)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/flamewar.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(flame)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/lawn.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(lawn)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/owned.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(owned)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/inet_punch.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(punch)', img.ConvertToBitmap())
        img = wx.Image( u"../images/emotes/facepalm.gif", wx.BITMAP_TYPE_ANY)
        img.Rescale(30,30)
        self.mainFrame.emote_bitmapcombo.Append('(palm)', img.ConvertToBitmap())
        self.mainFrame.emote_bitmapcombo.SetSelection(0)
        # load category choice in host
        self.mainFrame.filterjoincategorychoice.Append("All")
        #Client_GlobalData.category_id.Append(category_id).Append(0)  # don't do this, just subtract from index to save a bit of memory
        for category_id,category in SQL_Fetch_Category():
            if category_id != 0:
                self.mainFrame.filterjoincategorychoice.Append(category)
                #Client_GlobalData.category_id.append(category_id)
        self.mainFrame.filterjoincategorychoice.SetSelection(0)
        # show main frame after doing settings
        self.mainFrame.Show()
        if self.cfg.Exists('left_splitter_location'):
            self.mainFrame.sash_left.SetSashPosition(self.cfg.ReadInt('left_splitter_location'),True)
        else:
            self.mainFrame.sash_left.SetSashPosition(Client_GlobalData_Config.left_splitter_location,True)
        if self.cfg.Exists('right_splitter_location'):
            self.mainFrame.sash_right.SetSashPosition(self.cfg.ReadInt('right_splitter_location'),True)
        else:
            self.mainFrame.sash_right.SetSashPosition(Client_GlobalData_Config.right_splitter_location,True)
        if self.cfg.Exists('center_splitter_location'):
            self.mainFrame.sash_middle.SetSashPosition(self.cfg.ReadInt('center_splitter_location'),True)
        else:
            self.mainFrame.sash_middle.SetSashPosition(Client_GlobalData_Config.center_splitter_location,True)
        self.mainFrame.monitor_type_combo.SetSelection(0)
        self.mainFrame.main_frame_status_bar.SetStatusText("Welcome to Hub!Cade " + Client_GlobalData.software_rev + " for version " + Client_GlobalData.software_rom_rev + " roms", 0)

        start_option = 0
        if self.cfg.Exists('start_screen_option'):
            start_option = self.cfg.ReadInt('start_screen_option')
        if start_option == 0:  # maximuzed
            self.mainFrame.Maximize()
            self.SetTopWindow(self.mainFrame)
        elif start_option == 1:  # minimized
            self.mainFrame.Hide()
        elif start_option == 2:  # last open option
            if self.cfg.Exists('mainframe_position_x'):
                Client_GlobalData_Config.mainframe_position_x = self.cfg.ReadInt('mainframe_position_x')
            if self.cfg.Exists('mainframe_position_y'):
                Client_GlobalData_Config.mainframe_position_y = self.cfg.ReadInt('mainframe_position_y')
            if self.cfg.Exists('mainframe_width'):
                Client_GlobalData_Config.mainframe_width = self.cfg.ReadInt('mainframe_width')
            if self.cfg.Exists('mainframe_height'):
                Client_GlobalData_Config.mainframe_height = self.cfg.ReadInt('mainframe_height')
            frame_position = [Client_GlobalData_Config.mainframe_position_x,Client_GlobalData_Config.mainframe_position_y]
            frame_size = [Client_GlobalData_Config.mainframe_width,Client_GlobalData_Config.mainframe_height]
            self.mainFrame.SetPosition(frame_position)
            self.mainFrame.SetSize(frame_size)
            self.SetTopWindow(self.mainFrame)
##        self.mainFrame.chat_aui_notebook.SetCloseButton(0,false)
##        self.mainFrame.game_info_images_auinotebook.SetCloseButton(0,false)
        # setup the aui notebook tab tables with current settings
        OnSetAUINotebookPageList()
        self.mainFrame.Refresh()
        return True

    def OnExit(self):
        print "here i am exiting and saving settings"
        # write out window config options
        self.cfg = wx.Config('hubcade_gui_config')
        self.cfg.WriteInt("width", self.mainFrame.Size[0])
        self.cfg.WriteInt("height", self.mainFrame.Size[1])
        self.cfg.WriteInt("left_splitter_location", self.mainFrame.sash_left.GetSashPosition())
        self.cfg.WriteInt("right_splitter_location", self.mainFrame.sash_right.GetSashPosition())
        self.cfg.WriteInt("center_splitter_location", self.mainFrame.sash_middle.GetSashPosition())
        self.cfg.WriteInt("mainframe_position_x", self.mainFrame.GetPositionTuple()[0])
        self.cfg.WriteInt("mainframe_position_y", self.mainFrame.GetPositionTuple()[1])
        self.cfg.WriteInt("mainframe_width", self.mainFrame.Size[0])
        self.cfg.WriteInt("mainframe_height", self.mainFrame.Size[1])
        self.cfg.Flush()
        self.quit = True
        self.timer.Stop()
        self.mainFrame.clock_timer.Stop()
        self.mainFrame.ping_timer.Stop()
        if Client_GlobalData.os_video_playback == True:
            self.mainFrame.timer_slider.Stop()
        # close the sqlite3 db's
        #CloseDatabase()  - This is done in client_main.py and exit of program
        return 0

    def reactorUpdate(self,event):
        reactor.runUntilCurrent()
        reactor.doIteration(0)
        if '--override-port' in sys.argv:
            Client_GlobalData.hasPortForwarded = True
        if self.quit: return
        if self.clientFactory.protocol is None:
            #Wait until the protocol has started
            self.timer.Start(150, True)
            return
        if Client_GlobalData.networkProtocol:
            if time.time() > Client_GlobalData.networkProtocol.lastPingTime+5*60:
                Client_GlobalData.networkProtocol.pingServer()
            if time.time() > Client_GlobalData.networkProtocol.lastPongTime+20*60:
                mdial = wx.MessageDialog(None, 'No response from server.', 'No response from server.', wx.OK | wx.ICON_ERROR)
                mdial.ShowModal()
                mdial.Destroy()
                self.mainFrame.closeFrame()
        if self.clientFactory.failed \
        or self.clientFactory.protocol.connStatus==ClientProtocol.NOTSTARTED:
            mdial = wx.MessageDialog(None, 'Could not establish connection with Hub!Cade server. Ensure that the port entered is manually forwarded on your router and opened up on any firewalls.', 'Could not establish 2-way connection with server.', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
            self.mainFrame.closeFrame()
        elif self.clientFactory.protocol.connStatus==ClientProtocol.CLOSED:
            if Client_GlobalData_Config.chat_export_on_disco == True:
                self.onExportChatMenuItem(event)
            mdial = wx.MessageDialog(None, 'Disconnected from Hub!Cade server. Please try to reconnect.', 'Disconnected from Hub!Cade server.', wx.OK | wx.ICON_INFORMATION)
            mdial.ShowModal()
            mdial.Destroy()
            self.mainFrame.closeFrame()
        else:
            self.timer.Start(150, True)
