# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 10 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ConfigTemplate
###########################################################################

class ConfigTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuration Settings", pos = wx.DefaultPosition, size = wx.Size( 528,498 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.config_dialog_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel12 = wx.Panel( self.config_dialog_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel37 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 0, 4, 0, 0 )

		self.m_staticText5 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Chat Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.SelectChatFontButton = wx.Button( self.m_panel37, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.SelectChatFontButton, 0, wx.ALL, 5 )

		self.chatfontExample = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Example Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chatfontExample.Wrap( -1 )
		gSizer5.Add( self.chatfontExample, 0, wx.ALL, 5 )

		self.chatfontExampleColor = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chatfontExampleColor.Wrap( -1 )
		self.chatfontExampleColor.Hide()

		gSizer5.Add( self.chatfontExampleColor, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"User List Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.SelectUserFontButton = wx.Button( self.m_panel37, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.SelectUserFontButton, 0, wx.ALL, 5 )

		self.userfontExample = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Example Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.userfontExample.Wrap( -1 )
		gSizer5.Add( self.userfontExample, 0, wx.ALL, 5 )

		self.userfontExampleColor = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.userfontExampleColor.Wrap( -1 )
		self.userfontExampleColor.Hide()

		gSizer5.Add( self.userfontExampleColor, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Game List Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.SelectGameListFontButton = wx.Button( self.m_panel37, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.SelectGameListFontButton, 0, wx.ALL, 5 )

		self.gamelistfontExample = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Example Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gamelistfontExample.Wrap( -1 )
		gSizer5.Add( self.gamelistfontExample, 0, wx.ALL, 5 )

		self.gamelistfontExampleColor = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gamelistfontExampleColor.Wrap( -1 )
		self.gamelistfontExampleColor.Hide()

		gSizer5.Add( self.gamelistfontExampleColor, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Game Info Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer5.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.SelectGameInfoFontButton = wx.Button( self.m_panel37, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.SelectGameInfoFontButton, 0, wx.ALL, 5 )

		self.gameinfofontExample = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Example Font", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gameinfofontExample.Wrap( -1 )
		gSizer5.Add( self.gameinfofontExample, 0, wx.ALL, 5 )

		self.gameinfofontExampleColor = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gameinfofontExampleColor.Wrap( -1 )
		self.gameinfofontExampleColor.Hide()

		gSizer5.Add( self.gameinfofontExampleColor, 0, wx.ALL, 5 )


		self.m_panel37.SetSizer( gSizer5 )
		self.m_panel37.Layout()
		gSizer5.Fit( self.m_panel37 )
		bSizer42.Add( self.m_panel37, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel38 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer54 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel38, wx.ID_ANY, u"Video Playback Options" ), wx.HORIZONTAL )

		self.m_panel39 = wx.Panel( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.video_download_checkbox = wx.CheckBox( self.m_panel39, wx.ID_ANY, u"Video Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.video_download_checkbox.Enable( False )

		bSizer43.Add( self.video_download_checkbox, 0, wx.ALL, 5 )

		self.video_mute_checkbox = wx.CheckBox( self.m_panel39, wx.ID_ANY, u"Video Mute", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.video_mute_checkbox, 0, wx.ALL, 5 )

		self.video_repeat_checkbox = wx.CheckBox( self.m_panel39, wx.ID_ANY, u"Video Loop/Repeat", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.video_repeat_checkbox, 0, wx.ALL, 5 )


		self.m_panel39.SetSizer( bSizer43 )
		self.m_panel39.Layout()
		bSizer43.Fit( self.m_panel39 )
		sbSizer54.Add( self.m_panel39, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel40 = wx.Panel( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer44.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.video_volume_spinner = wx.SpinCtrl( self.m_panel40, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 0 )
		bSizer44.Add( self.video_volume_spinner, 0, wx.ALL, 5 )


		self.m_panel40.SetSizer( bSizer44 )
		self.m_panel40.Layout()
		bSizer44.Fit( self.m_panel40 )
		sbSizer54.Add( self.m_panel40, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel38.SetSizer( sbSizer54 )
		self.m_panel38.Layout()
		sbSizer54.Fit( self.m_panel38 )
		bSizer42.Add( self.m_panel38, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer42 )
		self.m_panel12.Layout()
		bSizer42.Fit( self.m_panel12 )
		self.config_dialog_notebook.AddPage( self.m_panel12, u"Fonts/Video Playback", True )
		self.m_panel13 = wx.Panel( self.config_dialog_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel21 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer33 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel21, wx.ID_ANY, u"MAME" ), wx.VERTICAL )

		self.mame_info_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Info Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_info_checkbox, 0, wx.ALL, 5 )

		self.mame_title_snap_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Title/Snap Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_title_snap_checkbox, 0, wx.ALL, 5 )

		self.mame_title_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Title Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_title_checkbox, 0, wx.ALL, 5 )

		self.mame_snap_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Snap Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_snap_checkbox, 0, wx.ALL, 5 )

		self.mame_cabinet_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Cabinet Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_cabinet_checkbox, 0, wx.ALL, 5 )

		self.mame_control_panel_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Control Panel Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_control_panel_checkbox, 0, wx.ALL, 5 )

		self.mame_marque_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Marque Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_marque_checkbox, 0, wx.ALL, 5 )

		self.mame_pcb_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"PCB Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_pcb_checkbox, 0, wx.ALL, 5 )

		self.mame_video_playback_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Video Playback", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_video_playback_checkbox, 0, wx.ALL, 5 )

		self.mame_manual_checkbox = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Display PDF Manual ", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer33.Add( self.mame_manual_checkbox, 0, wx.ALL, 5 )


		self.m_panel21.SetSizer( sbSizer33 )
		self.m_panel21.Layout()
		sbSizer33.Fit( self.m_panel21 )
		bSizer191.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel22 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer34 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel22, wx.ID_ANY, u"MESS" ), wx.VERTICAL )

		self.mess_info_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Info Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_info_checkbox, 0, wx.ALL, 5 )

		self.mess_title_snap_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Title/Snap Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_title_snap_checkbox, 0, wx.ALL, 5 )

		self.mess_title_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Title Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_title_checkbox, 0, wx.ALL, 5 )

		self.mess_snap_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Snap Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_snap_checkbox, 0, wx.ALL, 5 )

		self.mess_box_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Box Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_box_checkbox, 0, wx.ALL, 5 )

		self.mess_cart_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Cart Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_cart_checkbox, 0, wx.ALL, 5 )

		self.mess_label_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Label Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_label_checkbox, 0, wx.ALL, 5 )

		self.mess_cart_top_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Cart Top Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_cart_top_checkbox, 0, wx.ALL, 5 )

		self.mess_video_playback_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Video Playback", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_video_playback_checkbox, 0, wx.ALL, 5 )

		self.mess_manual_checkbox = wx.CheckBox( self.m_panel22, wx.ID_ANY, u"Display PDF Manual", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer34.Add( self.mess_manual_checkbox, 0, wx.ALL, 5 )


		self.m_panel22.SetSizer( sbSizer34 )
		self.m_panel22.Layout()
		sbSizer34.Fit( self.m_panel22 )
		bSizer191.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer18.Add( bSizer191, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel17 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.auto_download_checkbox = wx.CheckBox( self.m_panel17, wx.ID_ANY, u"Auto download image(s) if no local copy", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.auto_download_checkbox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel17.SetSizer( bSizer20 )
		self.m_panel17.Layout()
		bSizer20.Fit( self.m_panel17 )
		bSizer18.Add( self.m_panel17, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer18 )
		self.m_panel13.Layout()
		bSizer18.Fit( self.m_panel13 )
		self.config_dialog_notebook.AddPage( self.m_panel13, u"Image/Video Display", False )
		self.m_panel14 = wx.Panel( self.config_dialog_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText11 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Application Start Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		app_start_choiceChoices = [ u"Maximized", u"Minimized", u"Last Setting" ]
		self.app_start_choice = wx.Choice( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, app_start_choiceChoices, 0 )
		self.app_start_choice.SetSelection( 0 )
		gSizer3.Add( self.app_start_choice, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Theme to use", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		theme_choiceChoices = [ u"Not yet", u"In due time" ]
		self.theme_choice = wx.Choice( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, theme_choiceChoices, 0 )
		self.theme_choice.SetSelection( 0 )
		gSizer3.Add( self.theme_choice, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Chat Window Lines", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		chat_window_lines_comboboxChoices = [ u"Unlimited", u"50", u"100", u"250", u"500", u"750", u"1.000", u"5.000", u"10,000", u"25,000" ]
		self.chat_window_lines_combobox = wx.Choice( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chat_window_lines_comboboxChoices, 0 )
		self.chat_window_lines_combobox.SetSelection( 0 )
		self.chat_window_lines_combobox.SetToolTipString( u"Number of chat lines to keep" )

		gSizer3.Add( self.chat_window_lines_combobox, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Image Save/Load Option", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )

		image_save_option_choiceChoices = [ u"Central Method", u"System Method" ]
		self.image_save_option_choice = wx.Choice( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, image_save_option_choiceChoices, 0 )
		self.image_save_option_choice.SetSelection( 0 )
		self.image_save_option_choice.SetToolTipString( u"Central Method = All located in MAMEHub Images\nSystem Method = Parent directory of system/roms" )

		gSizer3.Add( self.image_save_option_choice, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Sort User List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer3.Add( self.m_staticText23, 0, wx.ALL, 5 )

		user_list_sort_choiceChoices = [ u"Country Code", u"Username" ]
		self.user_list_sort_choice = wx.Choice( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, user_list_sort_choiceChoices, 0 )
		self.user_list_sort_choice.SetSelection( 0 )
		gSizer3.Add( self.user_list_sort_choice, 0, wx.ALL, 5 )

		self.m_staticText251 = wx.StaticText( self.m_panel14, wx.ID_ANY, u"Hub!Cad Layout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )
		gSizer3.Add( self.m_staticText251, 0, wx.ALL, 5 )

		self.hubcad_layout_button = wx.Button( self.m_panel14, wx.ID_ANY, u"Select Layout", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.hubcad_layout_button, 0, wx.ALL, 5 )


		self.m_panel14.SetSizer( gSizer3 )
		self.m_panel14.Layout()
		gSizer3.Fit( self.m_panel14 )
		self.config_dialog_notebook.AddPage( self.m_panel14, u"Layout/Theme", False )
		self.m_panel371 = wx.Panel( self.config_dialog_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel53 = wx.Panel( self.m_panel371, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		config_misc_sizer = wx.GridSizer( 0, 2, 0, 0 )

		self.chat_save_to_db_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Save chat to DB", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_misc_sizer.Add( self.chat_save_to_db_checkbox, 0, wx.ALL, 5 )

		self.chat_export_on_disco_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Export Chat on Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_misc_sizer.Add( self.chat_export_on_disco_checkbox, 0, wx.ALL, 5 )

		self.chat_window_display_emote_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Display emotes in chat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chat_window_display_emote_checkbox.SetToolTipString( u"Turn emote tags into GIFS" )

		config_misc_sizer.Add( self.chat_window_display_emote_checkbox, 0, wx.ALL, 5 )

		self.allow_client_downloads_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Allow Client Rom Downloads", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.allow_client_downloads_checkbox.SetValue(True)
		self.allow_client_downloads_checkbox.Enable( False )

		config_misc_sizer.Add( self.allow_client_downloads_checkbox, 0, wx.ALL, 5 )

		self.mute_chat_sounds_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Mute Chat Sounds", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_misc_sizer.Add( self.mute_chat_sounds_checkbox, 0, wx.ALL, 5 )

		self.chime_on_chat_name_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Chime on name in Chat", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_misc_sizer.Add( self.chime_on_chat_name_checkbox, 0, wx.ALL, 5 )

		self.unpnc_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Enable Unpnc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.unpnc_checkbox.SetToolTipString( u"Enable this option to autoforward your network port." )

		config_misc_sizer.Add( self.unpnc_checkbox, 0, wx.ALL, 5 )

		self.chime_on_friend_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Chime on friend Log/Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_misc_sizer.Add( self.chime_on_friend_checkbox, 0, wx.ALL, 5 )

		self.display_clock_24_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Display clock as 24hr", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_misc_sizer.Add( self.display_clock_24_checkbox, 0, wx.ALL, 5 )

		self.record_inp_checkbox = wx.CheckBox( self.m_panel53, wx.ID_ANY, u"Auto-Record INP (Mame only)", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_misc_sizer.Add( self.record_inp_checkbox, 0, wx.ALL, 5 )


		self.m_panel53.SetSizer( config_misc_sizer )
		self.m_panel53.Layout()
		config_misc_sizer.Fit( self.m_panel53 )
		bSizer58.Add( self.m_panel53, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel54 = wx.Panel( self.m_panel371, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText252 = wx.StaticText( self.m_panel54, wx.ID_ANY, u"Ping Option", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText252.Wrap( -1 )
		bSizer61.Add( self.m_staticText252, 0, wx.ALL, 5 )

		ping_timeframe_comboChoices = [ u"None", u"10 Seconds", u"30 Seconds", u"1 Minute", u"5 Minutes" ]
		self.ping_timeframe_combo = wx.Choice( self.m_panel54, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ping_timeframe_comboChoices, 0 )
		self.ping_timeframe_combo.SetSelection( 0 )
		bSizer61.Add( self.ping_timeframe_combo, 0, wx.ALL, 5 )


		self.m_panel54.SetSizer( bSizer61 )
		self.m_panel54.Layout()
		bSizer61.Fit( self.m_panel54 )
		bSizer58.Add( self.m_panel54, 0, wx.EXPAND |wx.ALL, 5 )


		self.m_panel371.SetSizer( bSizer58 )
		self.m_panel371.Layout()
		bSizer58.Fit( self.m_panel371 )
		self.config_dialog_notebook.AddPage( self.m_panel371, u"Misc", False )
		self.m_panel47 = wx.Panel( self.config_dialog_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		config_audit_sizer = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText25 = wx.StaticText( self.m_panel47, wx.ID_ANY, u"Audit Scan Option", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		config_audit_sizer.Add( self.m_staticText25, 0, wx.ALL, 5 )

		config_audit_scan_choiceChoices = [ u"Quick Scan", u"CRC32 File Check", u"Full Verification CRC32/SHA1" ]
		self.config_audit_scan_choice = wx.Choice( self.m_panel47, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, config_audit_scan_choiceChoices, 0 )
		self.config_audit_scan_choice.SetSelection( 0 )
		config_audit_sizer.Add( self.config_audit_scan_choice, 0, wx.ALL, 5 )

		self.skip_adult_checkbox = wx.CheckBox( self.m_panel47, wx.ID_ANY, u"Skip Adult in Audit", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_audit_sizer.Add( self.skip_adult_checkbox, 0, wx.ALL, 5 )

		self.skip_audit_clone = wx.CheckBox( self.m_panel47, wx.ID_ANY, u"Skip Clone(s) in Audit", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_audit_sizer.Add( self.skip_audit_clone, 0, wx.ALL, 5 )

		self.skip_mech_checkbox = wx.CheckBox( self.m_panel47, wx.ID_ANY, u"Skip Mechanical in Audit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.skip_mech_checkbox.SetValue(True)
		config_audit_sizer.Add( self.skip_mech_checkbox, 0, wx.ALL, 5 )

		self.skip_gambling_checkbox = wx.CheckBox( self.m_panel47, wx.ID_ANY, u"Skip Gambling", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_audit_sizer.Add( self.skip_gambling_checkbox, 0, wx.ALL, 5 )

		self.skip_mahjong_checkbox = wx.CheckBox( self.m_panel47, wx.ID_ANY, u"Skip Mahjong", wx.DefaultPosition, wx.DefaultSize, 0 )
		config_audit_sizer.Add( self.skip_mahjong_checkbox, 0, wx.ALL, 5 )

		self.rename_files_checkbox = wx.CheckBox( self.m_panel47, wx.ID_ANY, u"Remame Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rename_files_checkbox.SetToolTipString( u"Allow rename of roms to help match with images" )

		config_audit_sizer.Add( self.rename_files_checkbox, 0, wx.ALL, 5 )


		self.m_panel47.SetSizer( config_audit_sizer )
		self.m_panel47.Layout()
		config_audit_sizer.Fit( self.m_panel47 )
		self.config_dialog_notebook.AddPage( self.m_panel47, u"Auditing", False )

		bSizer16.Add( self.config_dialog_notebook, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel381 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer431 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel391 = wx.Panel( self.m_panel381, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer432 = wx.BoxSizer( wx.HORIZONTAL )

		self.config_default_button = wx.Button( self.m_panel391, wx.ID_ANY, u"Reset Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.config_default_button.SetToolTipString( u"Use this button to reset all options on the selected tab/page." )

		bSizer432.Add( self.config_default_button, 0, wx.ALL, 3 )

		self.config_default_all_button = wx.Button( self.m_panel391, wx.ID_ANY, u"Reset GUI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.config_default_all_button.SetToolTipString( u"Use this button to set the entire application back to default options." )

		bSizer432.Add( self.config_default_all_button, 0, wx.ALL, 3 )


		self.m_panel391.SetSizer( bSizer432 )
		self.m_panel391.Layout()
		bSizer432.Fit( self.m_panel391 )
		bSizer431.Add( self.m_panel391, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self.m_panel381, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Apply = wx.Button( self.m_panel381, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		self.m_sdbSizer1Cancel = wx.Button( self.m_panel381, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer431.Add( m_sdbSizer1, 0, wx.ALL|wx.EXPAND, 8 )


		self.m_panel381.SetSizer( bSizer431 )
		self.m_panel381.Layout()
		bSizer431.Fit( self.m_panel381 )
		bSizer16.Add( self.m_panel381, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.onConfigDiagInit )
		self.SelectChatFontButton.Bind( wx.EVT_BUTTON, self.OnSelectChatFontButton )
		self.SelectUserFontButton.Bind( wx.EVT_BUTTON, self.OnSelectUserListFontButton )
		self.SelectGameListFontButton.Bind( wx.EVT_BUTTON, self.OnGameListFontButton )
		self.SelectGameInfoFontButton.Bind( wx.EVT_BUTTON, self.OnGameInfoFontButton )
		self.hubcad_layout_button.Bind( wx.EVT_BUTTON, self.OnHubCadLayoutButton )
		self.config_default_button.Bind( wx.EVT_BUTTON, self.OnConfigDefaultButton )
		self.config_default_all_button.Bind( wx.EVT_BUTTON, self.OnConfigDefaultAllButton )
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.onConfigApply )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.onConfigCancel )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.onConfigOK )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onConfigDiagInit( self, event ):
		event.Skip()

	def OnSelectChatFontButton( self, event ):
		event.Skip()

	def OnSelectUserListFontButton( self, event ):
		event.Skip()

	def OnGameListFontButton( self, event ):
		event.Skip()

	def OnGameInfoFontButton( self, event ):
		event.Skip()

	def OnHubCadLayoutButton( self, event ):
		event.Skip()

	def OnConfigDefaultButton( self, event ):
		event.Skip()

	def OnConfigDefaultAllButton( self, event ):
		event.Skip()

	def onConfigApply( self, event ):
		event.Skip()

	def onConfigCancel( self, event ):
		event.Skip()

	def onConfigOK( self, event ):
		event.Skip()


