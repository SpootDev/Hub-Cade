# import python mods
import sys

# import globals
import Client_GlobalData
import Client_GlobalData_Config

#import template
from Client_Template_Config import *

class ConfigDialog ( ConfigTemplate ):
    def onConfigDiagInit( self, event ):
        self.cfg = wx.Config('hubcade_gui_config')
        # font
        if self.cfg.Exists('chat_font'):
            Client_GlobalData_Config.chat_font = self.cfg.Read('chat_font')
        if self.cfg.Exists('chat_font_size'):
            Client_GlobalData_Config.chat_font_size = self.cfg.ReadInt('chat_font_size')
        if self.cfg.Exists('chat_font_color'):
            Client_GlobalData_Config.chat_font_color = self.cfg.Read('chat_font_color')
        self.chatfontExample.SetLabel(Client_GlobalData_Config.chat_font + ":" + str(Client_GlobalData_Config.chat_font_size))  #  color.Get()  need GetFont. in front?
        self.chatfontExampleColor.SetLabel(Client_GlobalData_Config.chat_font_color)
        if self.cfg.Exists('user_list_font'):
            Client_GlobalData_Config.user_list_font = self.cfg.Read('user_list_font')
        if self.cfg.Exists('user_list_font_size'):
            Client_GlobalData_Config.user_list_font_size = self.cfg.ReadInt('user_list_font_size')
        if self.cfg.Exists('user_list_font_color'):
            Client_GlobalData_Config.user_list_font_color = self.cfg.Read('user_list_font_color')
        self.userfontExample.SetLabel(Client_GlobalData_Config.user_list_font + ":" + str(Client_GlobalData_Config.user_list_font_size))  #  color.Get()  need GetFont. in front?
        self.userfontExampleColor.SetLabel(Client_GlobalData_Config.user_list_font_color)
        if self.cfg.Exists('gamelist_font'):
            Client_GlobalData_Config.gamelist_font = self.cfg.Read('gamelist_font')
        if self.cfg.Exists('gamelist_font_size'):
            Client_GlobalData_Config.gamelist_font_size = self.cfg.ReadInt('gamelist_font_size')
        if self.cfg.Exists('gamelist_font_color'):
            Client_GlobalData_Config.gamelist_font_color = self.cfg.Read('gamelist_font_color')
        self.gamelistfontExample.SetLabel(Client_GlobalData_Config.gamelist_font + ":" + str(Client_GlobalData_Config.gamelist_font_size))  #  color.Get()  need GetFont. in front?
        self.gamelistfontExampleColor.SetLabel(Client_GlobalData_Config.gamelist_font_color)
        if self.cfg.Exists('gameinfo_font'):
            Client_GlobalData_Config.gameinfo_font = self.cfg.Read('gameinfo_font')
        if self.cfg.Exists('gameinfo_font_size'):
            Client_GlobalData_Config.gameinfo_font_size = self.cfg.ReadInt('gameinfo_font_size')
        if self.cfg.Exists('gameinfo_font_color'):
            Client_GlobalData_Config.gameinfo_font_color = self.cfg.Read('gameinfo_font_color')
        self.gameinfofontExample.SetLabel(Client_GlobalData_Config.gameinfo_font + ":" + str(Client_GlobalData_Config.gameinfo_font_size))  #  color.Get()  need GetFont. in front?
        self.gameinfofontExampleColor.SetLabel(Client_GlobalData_Config.gameinfo_font_color)
        # image settings
        # don't need to code the else as it's True in the global configs for images
        if self.cfg.Exists('autodown_image'):
            Client_GlobalData_Config.autodown_image = self.cfg.ReadInt('autodown_image')
            self.auto_download_checkbox.SetValue(Client_GlobalData_Config.autodown_image)
        else:
            self.auto_download_checkbox.SetValue(1)
        if self.cfg.Exists('mame_info_display_tab'):
            Client_GlobalData_Config.mame_info_display_tab = self.cfg.ReadInt('mame_info_display_tab')
            self.mame_info_checkbox.SetValue(Client_GlobalData_Config.mame_info_display_tab)
        else:
            self.mame_info_checkbox.SetValue(1)
        if self.cfg.Exists('mame_title_snap_display_tab'):
            Client_GlobalData_Config.mame_title_snap_display_tab = self.cfg.ReadInt('mame_title_snap_display_tab')
            self.mame_title_snap_checkbox.SetValue(Client_GlobalData_Config.mame_title_snap_display_tab)
        else:
            self.mame_title_snap_checkbox.SetValue(1)
        if self.cfg.Exists('mame_title_display_tab'):
            Client_GlobalData_Config.mame_title_display_tab = self.cfg.ReadInt('mame_title_display_tab')
            self.mame_title_checkbox.SetValue(Client_GlobalData_Config.mame_title_display_tab)
        else:
            self.mame_title_checkbox.SetValue(0)
        if self.cfg.Exists('mame_snap_display_tab'):
            Client_GlobalData_Config.mame_snap_display_tab = self.cfg.ReadInt('mame_snap_display_tab')
            self.mame_snap_checkbox.SetValue(Client_GlobalData_Config.mame_snap_display_tab)
        else:
            self.mame_snap_checkbox.SetValue(0)
        if self.cfg.Exists('mame_cabinet_display_tab'):
            Client_GlobalData_Config.mame_cabinet_display_tab = self.cfg.ReadInt('mame_cabinet_display_tab')
            self.mame_cabinet_checkbox.SetValue(Client_GlobalData_Config.mame_cabinet_display_tab)
        else:
            self.mame_cabinet_checkbox.SetValue(0)
        if self.cfg.Exists('mame_control_panel_display_tab'):
            Client_GlobalData_Config.mame_control_panel_display_tab = self.cfg.ReadInt('mame_control_panel_display_tab')
            self.mame_control_panel_checkbox.SetValue(Client_GlobalData_Config.mame_control_panel_display_tab)
        else:
            self.mame_control_panel_checkbox.SetValue(0)
        if self.cfg.Exists('mame_marque_display_tab'):
            Client_GlobalData_Config.mame_marque_display_tab = self.cfg.ReadInt('mame_marque_display_tab')
            self.mame_marque_checkbox.SetValue(Client_GlobalData_Config.mame_marque_display_tab)
        else:
            self.mame_marque_checkbox.SetValue(0)
        if self.cfg.Exists('mame_pcb_display_tab'):
            Client_GlobalData_Config.mame_pcb_display_tab = self.cfg.ReadInt('mame_pcb_display_tab')
            self.mame_pcb_checkbox.SetValue(Client_GlobalData_Config.mame_pcb_display_tab)
        else:
            self.mame_pcb_checkbox.SetValue(0)
        if self.cfg.Exists('mame_video_playback_tab'):
            Client_GlobalData_Config.mame_video_playback_display_tab = self.cfg.ReadInt('mame_video_playback_tab')
            self.mame_video_playback_checkbox.SetValue(Client_GlobalData_Config.mame_video_playback_display_tab)
        else:
            self.mame_video_playback_checkbox.SetValue(0)
        if self.cfg.Exists('mame_manual_display_tab'):
            Client_GlobalData_Config.mame_manual_display_tab = self.cfg.ReadInt('mame_manual_display_tab')
            self.mame_manual_checkbox.SetValue(Client_GlobalData_Config.mame_manual_display_tab)
        else:
            self.mame_manual_checkbox.SetValue(0)
        if self.cfg.Exists('mess_info_display_tab'):
            Client_GlobalData_Config.mess_info_display_tab = self.cfg.ReadInt('mess_info_display_tab')
            self.mess_info_checkbox.SetValue(Client_GlobalData_Config.mess_info_display_tab)
        else:
            self.mess_info_checkbox.SetValue(1)
        if self.cfg.Exists('mess_title_snap_display_tab'):
            Client_GlobalData_Config.mess_title_snap_display_tab = self.cfg.ReadInt('mess_title_snap_display_tab')
            self.mess_title_snap_checkbox.SetValue(Client_GlobalData_Config.mess_title_snap_display_tab)
        else:
            self.mess_title_snap_checkbox.SetValue(1)
        if self.cfg.Exists('mess_title_display_tab'):
            Client_GlobalData_Config.mess_title_display_tab = self.cfg.ReadInt('mess_title_display_tab')
            self.mess_title_checkbox.SetValue(Client_GlobalData_Config.mess_title_display_tab)
        else:
            self.mess_title_checkbox.SetValue(0)
        if self.cfg.Exists('mess_snap_display_tab'):
            Client_GlobalData_Config.mess_snap_display_tab = self.cfg.ReadInt('mess_snap_display_tab')
            self.mess_snap_checkbox.SetValue(Client_GlobalData_Config.mess_snap_display_tab)
        else:
            self.mess_snap_checkbox.SetValue(0)
        if self.cfg.Exists('mess_box_display_tab'):
            Client_GlobalData_Config.mess_box_display_tab = self.cfg.ReadInt('mess_box_display_tab')
            self.mess_box_checkbox.SetValue(Client_GlobalData_Config.mess_box_display_tab)
        else:
            self.mess_box_checkbox.SetValue(1)
        if self.cfg.Exists('mess_cart_display_tab'):
            Client_GlobalData_Config.mess_cart_display_tab = self.cfg.ReadInt('mess_cart_display_tab')
            self.mess_cart_checkbox.SetValue(Client_GlobalData_Config.mess_cart_display_tab)
        else:
            self.mess_cart_checkbox.SetValue(0)
        if self.cfg.Exists('mess_label_display_tab'):
            Client_GlobalData_Config.mess_label_display_tab = self.cfg.ReadInt('mess_label_display_tab')
            self.mess_label_checkbox.SetValue(Client_GlobalData_Config.mess_label_display_tab)
        else:
            self.mess_label_checkbox.SetValue(0)
        if self.cfg.Exists('mess_cart_top_display_tab'):
            Client_GlobalData_Config.mess_cart_top_display_tab = self.cfg.ReadInt('mess_cart_top_display_tab')
            self.mess_cart_top_checkbox.SetValue(Client_GlobalData_Config.mess_cart_top_display_tab)
        else:
            self.mess_cart_top_checkbox.SetValue(0)
        if self.cfg.Exists('mess_video_playback_tab'):
            Client_GlobalData_Config.mess_video_playback_display_tab = self.cfg.ReadInt('mess_video_playback_tab')
            self.mess_video_playback_checkbox.SetValue(Client_GlobalData_Config.mess_video_playback_display_tab)
        else:
            self.mess_video_playback_checkbox.SetValue(0)
        if self.cfg.Exists('mess_manual_display_tab'):
            Client_GlobalData_Config.mess_manual_display_tab = self.cfg.ReadInt('mess_manual_display_tab')
            self.mess_manual_checkbox.SetValue(Client_GlobalData_Config.mess_manual_display_tab)
        else:
            self.mess_manual_checkbox.SetValue(0)
        # video options
        if self.cfg.Exists('video_download'):
            Client_GlobalData_Config.video_download = self.cfg.ReadInt('video_download')
            self.video_download_checkbox.SetValue(Client_GlobalData_Config.video_download)
        else:
            self.video_download_checkbox.SetValue(1)
        if self.cfg.Exists('video_mute'):
            Client_GlobalData_Config.video_mute = self.cfg.ReadInt('video_mute')
            self.video_mute_checkbox.SetValue(Client_GlobalData_Config.video_mute)
        else:
            self.video_mute_checkbox.SetValue(1)
        if self.cfg.Exists('video_repeat'):
            Client_GlobalData_Config.video_repeat = self.cfg.ReadInt('video_repeat')
            self.video_repeat_checkbox.SetValue(Client_GlobalData_Config.video_repeat)
        else:
            self.video_repeat_checkbox.SetValue(1)
        if self.cfg.Exists('video_volume'):
            Client_GlobalData_Config.video_volume = self.cfg.ReadInt('video_volume')
            self.video_volume_spinner.SetValue(Client_GlobalData_Config.video_volume)
        else:
            self.video_volume_spinner.SetValue(10)
        # theme/app settings
        if self.cfg.Exists('start_screen_option'):
            self.app_start_choice.SetSelection(self.cfg.ReadInt('start_screen_option'))
        else:
            self.app_start_choice.SetSelection(0)
        #if self.cfg.Exists('theme_name'):
        #    self.theme_choice.SetSelection(self.cfg.Read('theme_name'))
        #else:
        #    self.theme_choice.SetText("Not Yet")
        if self.cfg.Exists('html_chat_window_lines'):
            self.chat_window_lines_combobox.SetSelection(self.cfg.ReadInt('html_chat_window_lines'))
        else:
            self.chat_window_lines_combobox.SetSelection(0)
        if self.cfg.Exists('user_list_sort'):
            self.user_list_sort_choice.SetSelection(self.cfg.ReadInt('user_list_sort'))
        else:
            self.user_list_sort_choice.SetSelection(1)
        if self.cfg.Exists('hubcad_layout'):
            Client_GlobalData_Config.hubcad_layout = self.cfg.Read('hubcad_layout')
        else:
            Client_GlobalData_Config.hubcad_layout = "NA"

        if self.cfg.Exists('display_emote_in_chat'):
            self.chat_window_display_emote_checkbox.SetValue(self.cfg.ReadInt('display_emote_in_chat'))
        else:
            self.chat_window_display_emote_checkbox.SetValue(0)
        if self.cfg.Exists('allow_client_downloads'):
            self.allow_client_downloads_checkbox.SetValue(self.cfg.ReadInt('allow_client_downloads'))
        else:
            self.allow_client_downloads_checkbox.SetValue(1)
        if self.cfg.Exists('file_save_method'):
            self.image_save_option_choice.SetSelection(self.cfg.ReadInt('file_save_method'))
        else:
            self.image_save_option_choice.SetSelection(0)
        if self.cfg.Exists('Mute_Chat_Sounds'):
            self.mute_chat_sounds_checkbox.SetValue(self.cfg.ReadInt('Mute_Chat_Sounds'))
        else:
            self.mute_chat_sounds_checkbox.SetValue(0)
        if self.cfg.Exists('chime_on_chat_name'):
            self.chime_on_chat_name_checkbox.SetValue(self.cfg.ReadInt('chime_on_chat_name'))
        else:
            self.chime_on_chat_name_checkbox.SetValue(0)
        if self.cfg.Exists('use_miniupnpc'):
            self.unpnc_checkbox.SetValue(self.cfg.ReadInt('use_miniupnpc'))
        else:
            self.unpnc_checkbox.SetValue(1)
        if self.cfg.Exists('chime_on_friend'):
            self.chime_on_friend_checkbox.SetValue(self.cfg.ReadInt('chime_on_friend'))
        else:
            self.chime_on_friend_checkbox.SetValue(0)
        # misc settings tab
        if self.cfg.Exists('chat_save_to_db'):
            self.chat_save_to_db_checkbox.SetValue(self.cfg.ReadInt('chat_save_to_db'))
        else:
            self.chat_save_to_db_checkbox.SetValue(0)
        if self.cfg.Exists('chat_export_on_disco'):
            self.chat_export_on_disco_checkbox.SetValue(self.cfg.ReadInt('chat_export_on_disco'))
        else:
            self.chat_export_on_disco_checkbox.SetValue(0)
        if self.cfg.Exists('display_clock_24'):
            self.display_clock_24_checkbox.SetValue(self.cfg.ReadInt('display_clock_24'))
        else:
            self.display_clock_24_checkbox.SetValue(1)
        if self.cfg.Exists('record_inp_on_mame'):
            self.record_inp_checkbox.SetValue(self.cfg.ReadInt('record_inp_on_mame'))
        else:
            self.record_inp_checkbox.SetValue(0)
        if self.cfg.Exists('ping_timeframe'):
            self.ping_timeframe_combo.SetValue(self.cfg.ReadInt('ping_timeframe'))
        else:
            self.ping_timeframe_combo.SetValue(0)
        # audit options tab
        if self.cfg.Exists('skip_mechanical'):
            self.skip_mech_checkbox.SetValue(self.cfg.ReadInt('skip_mechanical'))
        else:
            self.skip_mech_checkbox.SetValue(1)
        if self.cfg.Exists('skip_adult'):
            self.skip_adult_checkbox.SetValue(self.cfg.ReadInt('skip_adult'))
        else:
            self.skip_adult_checkbox.SetValue(0)
        if self.cfg.Exists('scan_choice'):
            self.config_audit_scan_choice.SetSelection(self.cfg.ReadInt('scan_choice'))
        else:
            self.config_audit_scan_choice.SetSelection(0)
        if self.cfg.Exists('skip_clones'):
            self.skip_audit_clone.SetValue(self.cfg.ReadInt('skip_clones'))
        else:
            self.skip_audit_clone.SetValue(1)
        if self.cfg.Exists('skip_gambling'):
            self.skip_gambling_checkbox.SetValue(self.cfg.ReadInt('skip_gambling'))
        else:
            self.skip_gambling_checkbox.SetValue(1)
        if self.cfg.Exists('skip_mahjong'):
            self.skip_mahjong_checkbox.SetValue(self.cfg.ReadInt('skip_mahjong'))
        else:
            self.skip_mahjong_checkbox.SetValue(1)
        if self.cfg.Exists('rename_files'):
            self.rename_files_checkbox.SetValue(self.cfg.ReadInt('rename_files'))
        else:
            self.rename_files_checkbox.SetValue(0)

    def OnSelectChatFontButton( self, event ):
        default_font = wx.Font(10, wx.SWISS , wx.NORMAL, wx.NORMAL, False, "Verdana")
        data = wx.FontData()
        if sys.platform == 'win32':
            data.EnableEffects(True)
        data.SetAllowSymbols(False)
        data.SetInitialFont(default_font)
        data.SetRange(10, 30)
        dlg = wx.FontDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
           data = dlg.GetFontData()
           font = data.GetChosenFont()
           color = data.GetColour()
           self.chatfontExample.SetLabel(font.GetFaceName() + ":" + str(font.GetPointSize()))
           self.chatfontExampleColor.SetLabel(str(color.Get()))
        dlg.Destroy()

    def OnSelectUserListFontButton( self, event ):
        default_font = wx.Font(10, wx.SWISS , wx.NORMAL, wx.NORMAL, False, "Verdana")
        data = wx.FontData()
        if sys.platform == 'win32':
            data.EnableEffects(True)
        data.SetAllowSymbols(False)
        data.SetInitialFont(default_font)
        data.SetRange(10, 30)
        dlg = wx.FontDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
           data = dlg.GetFontData()
           font = data.GetChosenFont()
           color = data.GetColour()
           self.userfontExample.SetLabel(font.GetFaceName() + ":" + str(font.GetPointSize()))
           self.userfontExampleColor.SetLabel(str(color.Get()))
        dlg.Destroy()

    def OnGameListFontButton( self, event ):
        default_font = wx.Font(10, wx.SWISS , wx.NORMAL, wx.NORMAL, False, "Verdana")
        data = wx.FontData()
        if sys.platform == 'win32':
            data.EnableEffects(True)
        data.SetAllowSymbols(False)
        data.SetInitialFont(default_font)
        data.SetRange(10, 30)
        dlg = wx.FontDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
           data = dlg.GetFontData()
           font = data.GetChosenFont()
           color = data.GetColour()
           self.gamelistfontExample.SetLabel(font.GetFaceName() + ":" + str(font.GetPointSize()))
           self.gamelistfontExampleColor.SetLabel(str(color.Get()))
        dlg.Destroy()

    def OnGameInfoFontButton( self, event ):
        default_font = wx.Font(10, wx.SWISS , wx.NORMAL, wx.NORMAL, False, "Verdana")
        data = wx.FontData()
        if sys.platform == 'win32':
            data.EnableEffects(True)
        data.SetAllowSymbols(False)
        data.SetInitialFont(default_font)
        data.SetRange(10, 30)
        dlg = wx.FontDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
           data = dlg.GetFontData()
           font = data.GetChosenFont()
           color = data.GetColour()
           self.gameinfofontExample.SetLabel(font.GetFaceName() + ":" + str(font.GetPointSize()))
           self.gameinfofontExampleColor.SetLabel(str(color.Get()))
        dlg.Destroy()

    def onConfigApply(self, event):
        # font options
        self.cfg.Write("chat_font", self.chatfontExample.GetLabel().split(":")[0])
        Client_GlobalData_Config.chat_font = self.chatfontExample.GetLabel().split(":")[0]
        self.cfg.WriteInt("chat_font_size", int(self.chatfontExample.GetLabel().split(":")[1]))
        Client_GlobalData_Config.chat_font_size = int(self.chatfontExample.GetLabel().split(":")[1])
        self.cfg.Write("chat_font_color", self.chatfontExampleColor.GetLabel())
        Client_GlobalData_Config.chat_font_color = self.chatfontExampleColor.GetLabel()
        self.cfg.Write("user_list_font", self.userfontExample.GetLabel().split(":")[0])
        Client_GlobalData_Config.user_list_font = self.userfontExample.GetLabel().split(":")[0]
        self.cfg.WriteInt("user_list_font_size", int(self.userfontExample.GetLabel().split(":")[1]))
        Client_GlobalData_Config.user_list_font_size = int(self.userfontExample.GetLabel().split(":")[1])
        self.cfg.Write("user_list_font_color", self.userfontExampleColor.GetLabel())
        Client_GlobalData_Config.user_list_font_color = self.userfontExampleColor.GetLabel()
        self.cfg.Write("gamelist_font", self.gamelistfontExample.GetLabel().split(":")[0])
        Client_GlobalData_Config.gamelist_font = self.gamelistfontExample.GetLabel().split(":")[0]
        self.cfg.WriteInt("gamelist_font_size", int(self.gamelistfontExample.GetLabel().split(":")[1]))
        Client_GlobalData_Config.gamelist_font_size = int(self.gamelistfontExample.GetLabel().split(":")[1])
        self.cfg.Write("gamelist_font_color", self.gamelistfontExampleColor.GetLabel())
        Client_GlobalData_Config.gamelist_font_color = self.gamelistfontExampleColor.GetLabel()
        self.cfg.Write("gameinfo_font", self.gameinfofontExample.GetLabel().split(":")[0])
        Client_GlobalData_Config.gameinfo_font = self.gameinfofontExample.GetLabel().split(":")[0]
        self.cfg.WriteInt("gameinfo_font_size", int(self.gameinfofontExample.GetLabel().split(":")[1]))
        Client_GlobalData_Config.gameinfo_font_size = int(self.gameinfofontExample.GetLabel().split(":")[1])
        self.cfg.Write("gameinfo_font_color", self.gameinfofontExampleColor.GetLabel())
        Client_GlobalData_Config.gameinfo_font_color = self.gameinfofontExampleColor.GetLabel()

        # image options
        self.cfg.WriteInt("autodown_image", self.auto_download_checkbox.IsChecked())
        Client_GlobalData_Config.autodown_image = self.auto_download_checkbox.IsChecked()
        self.cfg.WriteInt("mame_info_display_tab", self.mame_info_checkbox.IsChecked())
        Client_GlobalData_Config.mame_info_display_tab = self.mame_info_checkbox.IsChecked()
        self.cfg.WriteInt("mame_title_snap_display_tab", self.mame_title_snap_checkbox.IsChecked())
        Client_GlobalData_Config.mame_title_snap_display_tab = self.mame_title_snap_checkbox.IsChecked()
        self.cfg.WriteInt("mame_title_display_tab", self.mame_title_checkbox.IsChecked())
        Client_GlobalData_Config.mame_title_display_tab = self.mame_title_checkbox.IsChecked()
        self.cfg.WriteInt("mame_snap_display_tab", self.mame_snap_checkbox.IsChecked())
        Client_GlobalData_Config.mame_snap_display_tab = self.mame_snap_checkbox.IsChecked()
        self.cfg.WriteInt("mame_cabinet_display_tab", self.mame_cabinet_checkbox.IsChecked())
        Client_GlobalData_Config.mame_cabinet_display_tab = self.mame_cabinet_checkbox.IsChecked()
        self.cfg.WriteInt("mame_control_panel_display_tab", self.mame_control_panel_checkbox.IsChecked())
        Client_GlobalData_Config.mame_control_panel_display_tab = self.mame_control_panel_checkbox.IsChecked()
        self.cfg.WriteInt("mame_marque_display_tab", self.mame_marque_checkbox.IsChecked())
        Client_GlobalData_Config.mame_marque_display_tab =self. mame_marque_checkbox.IsChecked()
        self.cfg.WriteInt("mame_pcb_display_tab", self.mame_pcb_checkbox.IsChecked())
        Client_GlobalData_Config.mame_pcb_display_tab = self.mame_pcb_checkbox.IsChecked()
        self.cfg.WriteInt("mame_video_playback_tab", self.mame_video_playback_checkbox.IsChecked())
        Client_GlobalData_Config.mame_video_playback_display_tab = self.mame_video_playback_checkbox.IsChecked()
        self.cfg.WriteInt("mame_manual_display_tab", self.mame_manual_checkbox.IsChecked())
        Client_GlobalData_Config.mame_manual_display_tab = self.mame_manual_checkbox.IsChecked()

        self.cfg.WriteInt("mess_info_display_tab", self.mess_info_checkbox.IsChecked())
        Client_GlobalData_Config.mess_info_display_tab = self.mess_info_checkbox.IsChecked()
        self.cfg.WriteInt("mess_title_snap_display_tab", self.mess_title_snap_checkbox.IsChecked())
        Client_GlobalData_Config.mess_title_snap_display_tab = self.mess_title_snap_checkbox.IsChecked()
        self.cfg.WriteInt("mess_title_display_tab", self.mess_title_checkbox.IsChecked())
        Client_GlobalData_Config.mess_title_display_tab = self.mess_title_checkbox.IsChecked()
        self.cfg.WriteInt("mess_snap_display_tab", self.mess_snap_checkbox.IsChecked())
        Client_GlobalData_Config.mess_snap_display_tab = self.mess_snap_checkbox.IsChecked()
        self.cfg.WriteInt("mess_box_display_tab", self.mess_box_checkbox.IsChecked())
        Client_GlobalData_Config.mess_box_display_tab = self.mess_box_checkbox.IsChecked()
        self.cfg.WriteInt("mess_cart_display_tab", self.mess_cart_checkbox.IsChecked())
        Client_GlobalData_Config.mess_cart_display_tab = self.mess_cart_checkbox.IsChecked()
        self.cfg.WriteInt("mess_label_display_tab", self.mess_label_checkbox.IsChecked())
        Client_GlobalData_Config.mess_label_display_tab = self.mess_label_checkbox.IsChecked()
        self.cfg.WriteInt("mess_cart_top_display_tab", self.mess_cart_top_checkbox.IsChecked())
        Client_GlobalData_Config.mess_cart_top_display_tab = self.mess_cart_top_checkbox.IsChecked()
        self.cfg.WriteInt("mess_video_playback_tab", self.mess_video_playback_checkbox.IsChecked())
        Client_GlobalData_Config.mess_video_playback_display_tab = self.mess_video_playback_checkbox.IsChecked()
        self.cfg.WriteInt("mess_manual_display_tab", self.mess_manual_checkbox.IsChecked())
        Client_GlobalData_Config.mess_manual_display_tab = self.mess_manual_checkbox.IsChecked()
        # layout options
        self.cfg.WriteInt("start_screen_option", self.app_start_choice.GetCurrentSelection())
        #Client_GlobalData_Config.start_screen_option = self.app_start_choice.GetCurrentSelection()   # don't need to load live as it's done at begining
        # no sense writting them here......do at program exit
        #self.cfg.WriteInt("width", self.mainFrame.Size[0])
        #self.cfg.WriteInt("height", self.mainFrame.Size[1])
        #self.cfg.Write("theme_name", self.theme_choice.GetText())
        self.cfg.WriteInt("html_chat_window_lines", self.chat_window_lines_combobox.GetCurrentSelection())
        Client_GlobalData_Config.html_chat_window_lines = self.chat_window_lines_combobox.GetCurrentSelection()
        self.cfg.WriteInt("user_list_sort", self.user_list_sort_choice.GetCurrentSelection())
        Client_GlobalData_Config.user_list_sort = self.user_list_sort_choice.GetCurrentSelection()
        self.cfg.Write("hubcad_layout", Client_GlobalData_Config.hubcad_layout)

        self.cfg.WriteInt("display_emote_in_chat", self.chat_window_display_emote_checkbox.IsChecked())
        Client_GlobalData_Config.display_emote_in_chat = self.chat_window_display_emote_checkbox.IsChecked()
        self.cfg.WriteInt("allow_client_downloads", self.allow_client_downloads_checkbox.IsChecked())
        Client_GlobalData_Config.allow_client_downloads = self.allow_client_downloads_checkbox.IsChecked()
        self.cfg.WriteInt("file_save_method", self.image_save_option_choice.GetCurrentSelection())
        Client_GlobalData_Config.file_save_method = self.image_save_option_choice.GetCurrentSelection()
        self.cfg.WriteInt("Mute_Chat_Sounds", self.mute_chat_sounds_checkbox.IsChecked())
        Client_GlobalData_Config.Mute_Chat_Sounds = self.mute_chat_sounds_checkbox.IsChecked()
        self.cfg.WriteInt("chime_on_chat_name", self.chime_on_chat_name_checkbox.IsChecked())
        Client_GlobalData_Config.chime_on_chat_name = self.chime_on_chat_name_checkbox.IsChecked()
        self.cfg.WriteInt("use_miniupnpc", self.unpnc_checkbox.IsChecked())
        Client_GlobalData_Config.use_miniupnpc = self.unpnc_checkbox.IsChecked()
        self.cfg.WriteInt("chime_on_friend", self.chime_on_friend_checkbox.IsChecked())
        Client_GlobalData_Config.chime_on_friend = self.chime_on_friend_checkbox.IsChecked()
        # video playback options
        self.cfg.WriteInt("video_download", self.video_download_checkbox.IsChecked())
        Client_GlobalData_Config.video_download = self.video_download_checkbox.IsChecked()
        self.cfg.WriteInt("video_mute", self.video_mute_checkbox.IsChecked())
        Client_GlobalData_Config.video_mute = self.video_mute_checkbox.IsChecked()
        self.cfg.WriteInt("video_volume", self.video_volume_spinner.GetValue())
        Client_GlobalData_Config.video_volume = self.video_volume_spinner.GetValue()
        self.cfg.WriteInt("video_repeat", self.video_repeat_checkbox.IsChecked())
        Client_GlobalData_Config.video_repeat = self.video_repeat_checkbox.IsChecked()
        # misc settings options
        self.cfg.WriteInt("chat_save_to_db", self.chat_save_to_db_checkbox.IsChecked())
        Client_GlobalData_Config.chat_save_to_db = self.chat_save_to_db_checkbox.IsChecked()
        self.cfg.WriteInt("chat_export_on_disco", self.chat_export_on_disco_checkbox.IsChecked())
        Client_GlobalData_Config.chat_export_on_disco = self.chat_export_on_disco_checkbox.IsChecked()
        self.cfg.WriteInt("display_clock_24", self.display_clock_24_checkbox.IsChecked())
        Client_GlobalData_Config.display_clock_24 = self.display_clock_24_checkbox.IsChecked()
        self.cfg.WriteInt("record_inp_on_mame", self.record_inp_checkbox.IsChecked())
        Client_GlobalData_Config.record_inp_on_mame = self.record_inp_checkbox.IsChecked()
        # audit options
        self.cfg.WriteInt("skip_mechanical", self.skip_mech_checkbox.IsChecked())
        Client_GlobalData_Config.skip_mechanical = self.skip_mech_checkbox.IsChecked()
        self.cfg.WriteInt("skip_adult", self.skip_adult_checkbox.IsChecked())
        Client_GlobalData_Config.skip_adult = self.skip_adult_checkbox.IsChecked()
        self.cfg.WriteInt("scan_choice", self.config_audit_scan_choice.GetCurrentSelection())
        Client_GlobalData_Config.scan_choice = self.config_audit_scan_choice.GetCurrentSelection()
        self.cfg.WriteInt("skip_clones", self.skip_audit_clone.IsChecked())
        Client_GlobalData_Config.skip_clones = self.skip_audit_clone.IsChecked()
        self.cfg.WriteInt('skip_gambling', self.skip_gambling_checkbox.IsChecked())
        Client_GlobalData_Config.skip_gambling = self.skip_gambling_checkbox.IsChecked()
        self.cfg.WriteInt('skip_mahjong', self.skip_mahjong_checkbox.IsChecked())
        Client_GlobalData_Config.skip_mahjong = self.skip_mahjong_checkbox.IsChecked()
        self.cfg.WriteInt('rename_files', self.rename_files_checkbox.IsChecked())
        Client_GlobalData_Config.rename_files = self.rename_files_checkbox.IsChecked()
        self.cfg.Flush()
        # don't need to delete the rows as the forced refresh will do so.
        #Client_GlobalData.app.mainFrame.playerGridNew.DeleteRows(0,Client_GlobalData.app.mainFrame.playerGridNew.GetNumberRows())
        Client_GlobalData.gui_update_user_grid = True

    def onConfigOK( self, event ):
        self.onConfigApply( event )
        self.Destroy()
        event.Skip()

    def onConfigCancel( self, event ):
        self.Destroy()
        event.Skip()

    def OnHubCadLayoutButton( self, event ):
        event.Skip()

    # chat and video options
    def ResetDefaultTabOne( self ):
        self.chatfontExample.SetLabel("Verdana:6")
        self.chatfontExampleColor.SetLabel("(0,0,0)")
        self.userfontExample.SetLabel("Verdana:10")
        self.userfontExampleColor.SetLabel("(0,0,0)")
        self.gamelistfontExample.SetLabel("Verdana:8")
        self.gamelistfontExampleColor.SetLabel("(0,0,0)")
        self.gameinfofontExample.SetLabel("Verdana:8")
        self.gameinfofontExampleColor.SetLabel("(0,0,0)")
        self.video_download_checkbox.SetValue(0)
        self.video_mute_checkbox.SetValue(0)
        self.video_volume_spinner.SetValue(1)
        self.video_repeat_checkbox.SetValue(1)

    # images options
    def ResetDefaultTabTwo( self ):
        self.mame_info_checkbox.SetValue(1)
        self.mame_title_snap_checkbox.SetValue(1)
        self.mame_title_checkbox.SetValue(0)
        self.mame_snap_checkbox.SetValue(0)
        self.mame_cabinet_checkbox.SetValue(0)
        self.mame_control_panel_checkbox.SetValue(0)
        self.mame_marque_checkbox.SetValue(0)
        self.mame_pcb_checkbox.SetValue(0)
        self.mame_video_playback_checkbox.SetValue(0)
        self.mame_manual_checkbox.SetValue(0)
        self.mess_info_checkbox.SetValue(1)
        self.mess_title_snap_checkbox.SetValue(1)
        self.mess_title_checkbox.SetValue(0)
        self.mess_snap_checkbox.SetValue(0)
        self.mess_box_checkbox.SetValue(0)
        self.mess_cart_checkbox.SetValue(0)
        self.mess_label_checkbox.SetValue(0)
        self.mess_cart_top_checkbox.SetValue(0)
        self.mess_video_playback_checkbox.SetValue(0)
        self.mess_manual_display_tab.SetValue(0)
        self.auto_download_checkbox.SetValue(1)

    # layout/theme options
    def ResetDefaultTabThree( self ):
        self.app_start_choice.SetSelection(0)
        self.theme_choice.SetSelection(0)
        self.chat_window_lines_combobox.SetSelection(0)
        self.image_save_option_choice.SetSelection(0)
        self.user_list_sort_choice.SetSelection(1)

    # misc options
    def ResetDefaultTabFour( self ):
        self.chat_save_to_db_checkbox.SetValue(0)
        self.chat_export_on_disco_checkbox.SetValue(0)
        self.chat_window_display_emote_checkbox.SetValue(1)
        self.allow_client_downloads_checkbox.SetValue(1)
        self.mute_chat_sounds_checkbox.SetValue(0)
        self.chime_on_chat_name_checkbox.SetValue(0)
        self.unpnc_checkbox.SetValue(1)
        self.chime_on_friend_checkbox.SetValue(0)
        self.display_clock_24_checkbox.SetValue(1)
        self.record_inp_checkbox.SetValue(0)

    # audit options
    def ResetDefaultTabFive( self ):
        self.skip_mech_checkbox.SetValue(1)
        self.skip_adult_checkbox.SetValue(0)
        self.config_audit_scan_choice.SetSelection(0)
        self.skip_audit_clone.SetValue(0)
        self.skip_gambling_checkbox.SetValue(1)
        self.skip_mahjong_checkbox.SetValue(1)
        self.rename_files_checkbox.SetValue(0)

    def OnConfigDefaultButton( self, event ):
        if self.config_dialog_notebook.GetSelection() == 0:
            self.ResetDefaultTabOne()
        elif self.config_dialog_notebook.GetSelection() == 1:
            self.ResetDefaultTabTwo()
        elif self.config_dialog_notebook.GetSelection() == 2:
            self.ResetDefaultTabThree()
        elif self.config_dialog_notebook.GetSelection() == 3:
            self.ResetDefaultTabFour()
        else:
            self.ResetDefaultTabFive()
        event.Skip()

    def OnConfigDefaultAllButton( self, event ):
        self.ResetDefaultTabOne()
        self.ResetDefaultTabTwo()
        self.ResetDefaultTabThree()
        self.ResetDefaultTabFour()
        self.ResetDefaultTabFive()
        event.Skip()

# setup the aui notbook list global data
def OnSetAUINotebookPageList( ):
    # mame table
    if Client_GlobalData_Config.mame_title_snap_display_tab == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(1)
    if Client_GlobalData_Config.mame_title_display_tab == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(2)
    if Client_GlobalData_Config.mame_snap_display_tab == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(3)
    if Client_GlobalData_Config.mame_cabinet_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(4)
    if Client_GlobalData_Config.mame_control_panel_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(5)
    if Client_GlobalData_Config.mame_marque_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(6)
    if Client_GlobalData_Config.mame_pcb_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(7)
    if Client_GlobalData_Config.mame_video_playback_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(8)
    if Client_GlobalData_Config.mame_manual_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mame_list.append(9)
    # mess table
    if Client_GlobalData_Config.mess_title_snap_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(1)
    if Client_GlobalData_Config.mess_title_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(2)
    if Client_GlobalData_Config.mess_snap_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(3)
    if Client_GlobalData_Config.mess_box_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(4)
    if Client_GlobalData_Config.mess_cart_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(5)
    if Client_GlobalData_Config.mess_label_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(6)
    if Client_GlobalData_Config.mess_cart_top_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(7)
    if Client_GlobalData_Config.mess_video_playback_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(8)
    if Client_GlobalData_Config.mess_manual_display_tab  == 1:
        Client_GlobalData_Config.auinotebook_mess_list.append(9)

    #for row in Client_GlobalData_Config.auinotebook_mame_list:
        #print row
