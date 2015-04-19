# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.combo
import os,sys
import Client_GlobalData
try:
    import wx.html2 as webview
except ImportError, e:
    import wx.html as webview
    Client_GlobalData.webkit_enabled = False
import wx.gizmos as gizmos
if str.upper(sys.platform[0:3])=='WIN' \
or str.upper(sys.platform[0:3])=='CYG':
    import wx.lib.iewin as iewin
else:
    from Client_Cairo_PDF import *

wx.ID_GAMELISTSIZER = 1000
wx.ID_PLAYERLISTSIZER = 1001
wx.ID_JOIN_GAME = 1002
wx.ID_HOST_GAME = 1003

###########################################################################
## Class MainFrameTemplate
###########################################################################

class MainFrameTemplate ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hub!Cade", pos = wx.DefaultPosition, size = wx.Size( 1056,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.sash_middle = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.sash_middle.Bind( wx.EVT_IDLE, self.sash_middleOnIdle )
		self.sash_middle.SetMinimumPaneSize( 50 )

		self.m_panel29 = wx.Panel( self.sash_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		self.sash_left = wx.SplitterWindow( self.m_panel29, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.sash_left.Bind( wx.EVT_IDLE, self.sash_leftOnIdle )
		self.sash_left.SetMinimumPaneSize( 50 )

		self.m_panel3 = wx.Panel( self.sash_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gameListSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_GAMELISTSIZER, u"Manage Game" ), wx.VERTICAL )

		self.manage_game_auinotebook = wx.aui.AuiNotebook( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_SCROLL_BUTTONS )
		self.m_panel2 = wx.Panel( self.manage_game_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer181 = wx.BoxSizer( wx.VERTICAL )

		self.publicGameGrid = wx.grid.Grid( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.publicGameGrid.CreateGrid( 0, 5 )
		self.publicGameGrid.EnableEditing( False )
		self.publicGameGrid.EnableGridLines( True )
		self.publicGameGrid.EnableDragGridSize( False )
		self.publicGameGrid.SetMargins( 0, 0 )

		# Columns
		self.publicGameGrid.AutoSizeColumns()
		self.publicGameGrid.EnableDragColMove( False )
		self.publicGameGrid.EnableDragColSize( True )
		self.publicGameGrid.SetColLabelSize( 30 )
		self.publicGameGrid.SetColLabelValue( 0, u"Host" )
		self.publicGameGrid.SetColLabelValue( 1, u"Game" )
		self.publicGameGrid.SetColLabelValue( 2, u"Players" )
		self.publicGameGrid.SetColLabelValue( 3, u"Time Started" )
		self.publicGameGrid.SetColLabelValue( 4, u"System" )
		self.publicGameGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.publicGameGrid.EnableDragRowSize( True )
		self.publicGameGrid.SetRowLabelSize( 0 )
		self.publicGameGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.publicGameGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.join_game_menu = wx.Menu()
		self.join_game_add_to_fav_menuItem = wx.MenuItem( self.join_game_menu, wx.ID_ANY, u"Add To Favorites", wx.EmptyString, wx.ITEM_NORMAL )
		self.join_game_menu.AppendItem( self.join_game_add_to_fav_menuItem )

		self.join_game_remove_from_fav_menuItem = wx.MenuItem( self.join_game_menu, wx.ID_ANY, u"Remove From Favorites", wx.EmptyString, wx.ITEM_NORMAL )
		self.join_game_menu.AppendItem( self.join_game_remove_from_fav_menuItem )

		self.join_game_menu.AppendSeparator()

		self.join_game_join_game_menuItem = wx.MenuItem( self.join_game_menu, wx.ID_ANY, u"Join Game", wx.EmptyString, wx.ITEM_NORMAL )
		self.join_game_menu.AppendItem( self.join_game_join_game_menuItem )

		self.publicGameGrid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.publicGameGridOnContextMenu)

		bSizer181.Add( self.publicGameGrid, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer181 )
		self.m_panel2.Layout()
		bSizer181.Fit( self.m_panel2 )

		self.manage_game_auinotebook.AddPage( self.m_panel2, u"Join Game" )

		self.m_panel1 = wx.Panel( self.manage_game_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer171 = wx.BoxSizer( wx.VERTICAL )

		# WARNING: wxPython code generation isn't supported for this widget yet.
		self.gameListTreeCtrl = gizmos.TreeListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_HIDE_ROOT|wx.TR_SINGLE );
		self.gameListTreeCtrl.AddColumn("Game Name")
		self.gameListTreeCtrl.AddColumn("Times Played")
		self.gameListTreeCtrl.AddColumn("Time Played")
		self.gameListTreeCtrl.AddColumn("Monitor")
		self.gameListTreeCtrl.AddColumn("Player(s)")
		self.gameListTreeCtrl.AddColumn("Game ID")
		self.gameListTreeCtrl.AddColumn("Category")
		self.gameListTreeCtrl.AddColumn("Time Played Seconds")
		self.gameListTreeCtrl.SetColumnWidth(0, 250)
		self.gameListTreeCtrl.SetColumnWidth(1, 100)
		self.gameListTreeCtrl.SetColumnWidth(2, 100)
		self.gameListTreeCtrl.SetColumnWidth(3, 100)
		self.gameListTreeCtrl.SetColumnWidth(4, 100)
		self.gameListTreeCtrl.SetColumnWidth(5, 100)
		self.gameListTreeCtrl.SetColumnWidth(6, 100)
		self.gameListTreeCtrl.SetColumnWidth(7, 100)

		bSizer171.Add( self.gameListTreeCtrl, 1, wx.EXPAND |wx.ALL, 5 )

		sbSizer46 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Game Search/Filter" ), wx.HORIZONTAL )

		self.gameSearchText = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer46.Add( self.gameSearchText, 2, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Monitor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		sbSizer46.Add( self.m_staticText20, 0, wx.ALL|wx.EXPAND, 5 )

		monitor_type_comboChoices = [ u"Both", u"Horizontal", u"Vertical" ]
		self.monitor_type_combo = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"Both", wx.DefaultPosition, wx.DefaultSize, monitor_type_comboChoices, wx.CB_READONLY )
		sbSizer46.Add( self.monitor_type_combo, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Players:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		sbSizer46.Add( self.m_staticText21, 0, wx.ALL|wx.EXPAND, 5 )

		self.filter_player_count_spinner = wx.SpinCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 1 )
		sbSizer46.Add( self.filter_player_count_spinner, 0, wx.ALL|wx.EXPAND, 5 )

		self.filtercategorylabel = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filtercategorylabel.Wrap( -1 )
		sbSizer46.Add( self.filtercategorylabel, 0, wx.ALL, 5 )

		filterjoincategorychoiceChoices = []
		self.filterjoincategorychoice = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, filterjoincategorychoiceChoices, 0 )
		self.filterjoincategorychoice.SetSelection( 0 )
		sbSizer46.Add( self.filterjoincategorychoice, 0, wx.ALL, 5 )

		self.filterresetButton = wx.Button( self.m_panel1, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer46.Add( self.filterresetButton, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer171.Add( sbSizer46, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer171 )
		self.m_panel1.Layout()
		bSizer171.Fit( self.m_panel1 )

		self.manage_game_auinotebook.AddPage( self.m_panel1, u"Host Game" )

		self.m_panel43 = wx.Panel( self.manage_game_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.favorites_grid = wx.grid.Grid( self.m_panel43, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.favorites_grid.CreateGrid( 0, 4 )
		self.favorites_grid.EnableEditing( False )
		self.favorites_grid.EnableGridLines( True )
		self.favorites_grid.EnableDragGridSize( False )
		self.favorites_grid.SetMargins( 0, 0 )

		# Columns
		self.favorites_grid.EnableDragColMove( False )
		self.favorites_grid.EnableDragColSize( True )
		self.favorites_grid.SetColLabelSize( 30 )
		self.favorites_grid.SetColLabelValue( 0, u"Game" )
		self.favorites_grid.SetColLabelValue( 1, u"Times Played" )
		self.favorites_grid.SetColLabelValue( 2, u"Time Played" )
		self.favorites_grid.SetColLabelValue( 3, u"System" )
		self.favorites_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.favorites_grid.EnableDragRowSize( True )
		self.favorites_grid.SetRowLabelSize( 0 )
		self.favorites_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.favorites_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.favorites_grid_menu = wx.Menu()
		self.fav_host_game_menuItem = wx.MenuItem( self.favorites_grid_menu, wx.ID_ANY, u"Host Game", wx.EmptyString, wx.ITEM_NORMAL )
		self.favorites_grid_menu.AppendItem( self.fav_host_game_menuItem )

		self.fav_remove_game_menuItem = wx.MenuItem( self.favorites_grid_menu, wx.ID_ANY, u"Remove From Favorites", wx.EmptyString, wx.ITEM_NORMAL )
		self.favorites_grid_menu.AppendItem( self.fav_remove_game_menuItem )

		self.favorites_grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.favorites_gridOnContextMenu)

		bSizer44.Add( self.favorites_grid, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel43.SetSizer( bSizer44 )
		self.m_panel43.Layout()
		bSizer44.Fit( self.m_panel43 )

		self.manage_game_auinotebook.AddPage( self.m_panel43, u"Favorites" )

		gameListSizer.Add( self.manage_game_auinotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel3.SetSizer( gameListSizer )
		self.m_panel3.Layout()
		gameListSizer.Fit( self.m_panel3 )
		self.m_panel4 = wx.Panel( self.sash_left, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Chat Window(s)" ), wx.VERTICAL )

		self.chat_aui_notebook = wx.aui.AuiNotebook( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_SCROLL_BUTTONS )
		self.m_panel53 = wx.Panel( self.chat_aui_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		if Client_GlobalData.webkit_enabled == False:
			self.chatLogHTML = webview.HtmlWindow( self.m_panel53, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, webview.HW_SCROLLBAR_AUTO )
		else:
			self.chatLogHTML = webview.WebView.New( self.m_panel53 )
		bSizer51.Add( self.chatLogHTML, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel53.SetSizer( bSizer51 )
		self.m_panel53.Layout()
		bSizer51.Fit( self.m_panel53 )

		self.chat_aui_notebook.AddPage( self.m_panel53, u"Global" )
		self.m_panel44 = wx.Panel( self.chat_aui_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer46 = wx.BoxSizer( wx.VERTICAL )


		if Client_GlobalData.webkit_enabled == False:
			self.privateLogHTML = webview.HtmlWindow( self.m_panel44, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, webview.HW_SCROLLBAR_AUTO )
		else:
			self.privateLogHTML = webview.WebView.New( self.m_panel44 )
		bSizer46.Add( self.privateLogHTML, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel44.SetSizer( bSizer46 )
		self.m_panel44.Layout()
		bSizer46.Fit( self.m_panel44 )

		self.chat_aui_notebook.AddPage( self.m_panel44, u"Private" )
		self.m_panel45 = wx.Panel( self.chat_aui_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer47 = wx.BoxSizer( wx.VERTICAL )


		if Client_GlobalData.webkit_enabled == False:
			self.adminLogHTML = webview.HtmlWindow( self.m_panel45, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, webview.HW_SCROLLBAR_AUTO )
		else:
			self.adminLogHTML = webview.WebView.New( self.m_panel45 )
		bSizer47.Add( self.adminLogHTML, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel45.SetSizer( bSizer47 )
		self.m_panel45.Layout()
		bSizer47.Fit( self.m_panel45 )

		self.chat_aui_notebook.AddPage( self.m_panel45, u"Admin" )

		sbSizer17.Add( self.chat_aui_notebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel4.SetSizer( sbSizer17 )
		self.m_panel4.Layout()
		sbSizer17.Fit( self.m_panel4 )
		self.sash_left.SplitHorizontally( self.m_panel3, self.m_panel4, 343 )
		bSizer37.Add( self.sash_left, 1, wx.EXPAND, 5 )


		self.m_panel29.SetSizer( bSizer37 )
		self.m_panel29.Layout()
		bSizer37.Fit( self.m_panel29 )
		self.m_panel28 = wx.Panel( self.sash_middle, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.sash_right = wx.SplitterWindow( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.sash_right.Bind( wx.EVT_IDLE, self.sash_rightOnIdle )
		self.sash_right.SetMinimumPaneSize( 50 )

		self.m_panel23 = wx.Panel( self.sash_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		bSizer19.SetMinSize( wx.Size( 400,-1 ) )
		self.game_info_images_auinotebook = wx.aui.AuiNotebook( self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_SCROLL_BUTTONS )
		self.gameinfo_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer28 = wx.StaticBoxSizer( wx.StaticBox( self.gameinfo_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		if Client_GlobalData.webkit_enabled == False:
			self.gameinfo_htmlwindow = webview.HtmlWindow( self.gameinfo_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, webview.HW_SCROLLBAR_AUTO )
		else:
			self.gameinfo_htmlwindow = webview.WebView.New( self.gameinfo_panel )
		sbSizer28.Add( self.gameinfo_htmlwindow, 1, wx.ALL|wx.EXPAND, 5 )

		self.gameinfo_panel.SetSizer( sbSizer28 )
		self.gameinfo_panel.Layout()
		sbSizer28.Fit( self.gameinfo_panel )

		self.game_info_images_auinotebook.AddPage( self.gameinfo_panel, u"Game Info" )
		self.title_snap_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer57 = wx.StaticBoxSizer( wx.StaticBox( self.title_snap_panel, wx.ID_ANY, u"Title" ), wx.VERTICAL )

		self.title_snap_title_bitmap = wx.StaticBitmap( self.title_snap_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer57.Add( self.title_snap_title_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer41.Add( sbSizer57, 1, wx.EXPAND, 5 )

		sbSizer59 = wx.StaticBoxSizer( wx.StaticBox( self.title_snap_panel, wx.ID_ANY, u"Snap" ), wx.VERTICAL )

		self.title_snap_snap_bitmap = wx.StaticBitmap( self.title_snap_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer59.Add( self.title_snap_snap_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer41.Add( sbSizer59, 1, wx.EXPAND, 5 )


		self.title_snap_panel.SetSizer( bSizer41 )
		self.title_snap_panel.Layout()
		bSizer41.Fit( self.title_snap_panel )
		self.game_info_images_auinotebook.AddPage( self.title_snap_panel, u"Title/Snap" )
		self.title_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer291 = wx.StaticBoxSizer( wx.StaticBox( self.title_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.title_bitmap = wx.StaticBitmap( self.title_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer291.Add( self.title_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		self.title_panel.SetSizer( sbSizer291 )
		self.title_panel.Layout()
		sbSizer291.Fit( self.title_panel )
		self.game_info_images_auinotebook.AddPage( self.title_panel, u"Title" )
		self.snap_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer301 = wx.StaticBoxSizer( wx.StaticBox( self.snap_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.snap_bitmap = wx.StaticBitmap( self.snap_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer301.Add( self.snap_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		self.snap_panel.SetSizer( sbSizer301 )
		self.snap_panel.Layout()
		sbSizer301.Fit( self.snap_panel )
		self.game_info_images_auinotebook.AddPage( self.snap_panel, u"Snap" )
		self.cart_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self.cart_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.cart_bitmap = wx.StaticBitmap( self.cart_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer31.Add( self.cart_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		self.cart_panel.SetSizer( sbSizer31 )
		self.cart_panel.Layout()
		sbSizer31.Fit( self.cart_panel )
		self.game_info_images_auinotebook.AddPage( self.cart_panel, u"Cabinet" )
		self.box_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer32 = wx.StaticBoxSizer( wx.StaticBox( self.box_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.box_bitmap = wx.StaticBitmap( self.box_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer32.Add( self.box_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		self.box_panel.SetSizer( sbSizer32 )
		self.box_panel.Layout()
		sbSizer32.Fit( self.box_panel )
		self.game_info_images_auinotebook.AddPage( self.box_panel, u"CPanel" )
		self.label_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer56 = wx.StaticBoxSizer( wx.StaticBox( self.label_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.label_bitmap = wx.StaticBitmap( self.label_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer56.Add( self.label_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		self.label_panel.SetSizer( sbSizer56 )
		self.label_panel.Layout()
		sbSizer56.Fit( self.label_panel )
		self.game_info_images_auinotebook.AddPage( self.label_panel, u"Marquee" )
		self.cart_top_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer58 = wx.StaticBoxSizer( wx.StaticBox( self.cart_top_panel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.cart_top_bitmap = wx.StaticBitmap( self.cart_top_panel, wx.ID_ANY, wx.Bitmap( u"../images/hubcade_default.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer58.Add( self.cart_top_bitmap, 1, wx.ALL|wx.EXPAND, 5 )


		self.cart_top_panel.SetSizer( sbSizer58 )
		self.cart_top_panel.Layout()
		sbSizer58.Fit( self.cart_top_panel )
		self.game_info_images_auinotebook.AddPage( self.cart_top_panel, u"PCB" )
		self.video_panel = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.video_playback_panel = wx.Panel( self.video_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer35.Add( self.video_playback_panel, 1, wx.EXPAND |wx.ALL, 5 )

		if str.upper(sys.platform[0:3])=='WIN' \
		or str.upper(sys.platform[0:3])=='CYG':
			try:
				self.vid_playback_control = wx.media.MediaCtrl(self.video_playback_panel, style=wx.SIMPLE_BORDER, szBackend=wx.media.MEDIABACKEND_WMP10)
			except:
				try:
					self.vid_playback_control = wx.media.MediaCtrl(self.video_playback_panel, style=wx.SIMPLE_BORDER, szBackend=wx.media.MEDIABACKEND_DIRECTSHOW)
				except:
					Client_GlobalData.os_video_playback = False
		elif str.upper(sys.platform[0:3])=='DAR':
			try:
				self.vid_playback_control = wx.media.MediaCtrl(self.video_playback_panel, style=wx.SIMPLE_BORDER, szBackend=wx.media.MEDIABACKEND_QUICKTIME)
			except:
				Client_GlobalData.os_video_playback = False
		else:
			try:
				self.vid_playback_control = wx.media.MediaCtrl(self.video_playback_panel, style=wx.SIMPLE_BORDER, szBackend=wx.media.MEDIABACKEND_GSTREAMER)
			except:
				Client_GlobalData.os_video_playback = False

		self.m_panel281 = wx.Panel( self.video_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer371 = wx.BoxSizer( wx.HORIZONTAL )

		self.video_playback_slider = wx.Slider( self.m_panel281, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer371.Add( self.video_playback_slider, 1, wx.ALL|wx.EXPAND, 5 )

		self.vid_play_button = wx.BitmapButton( self.m_panel281, wx.ID_ANY, wx.Bitmap( u"../images/button_black_play-128.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer371.Add( self.vid_play_button, 0, wx.ALL, 5 )

		self.vid_pause_button = wx.BitmapButton( self.m_panel281, wx.ID_ANY, wx.Bitmap( u"../images/button_black_pause-128.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer371.Add( self.vid_pause_button, 0, wx.ALL, 5 )

		self.vid_stop_button = wx.BitmapButton( self.m_panel281, wx.ID_ANY, wx.Bitmap( u"../images/button_black_stop-128.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer371.Add( self.vid_stop_button, 0, wx.ALL, 5 )

		self.vid_mute_toggle_button = wx.BitmapButton( self.m_panel281, wx.ID_ANY, wx.Bitmap( u"../images/speaker-128.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer371.Add( self.vid_mute_toggle_button, 0, wx.ALL, 5 )

		self.vid_volume_down = wx.BitmapButton( self.m_panel281, wx.ID_ANY, wx.Bitmap( u"../images/sub_black_down.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer371.Add( self.vid_volume_down, 0, wx.ALL, 5 )

		self.vid_vlume_up = wx.BitmapButton( self.m_panel281, wx.ID_ANY, wx.Bitmap( u"../images/sub_black_up.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer371.Add( self.vid_vlume_up, 0, wx.ALL, 5 )


		self.m_panel281.SetSizer( bSizer371 )
		self.m_panel281.Layout()
		bSizer371.Fit( self.m_panel281 )
		bSizer35.Add( self.m_panel281, 0, wx.EXPAND |wx.ALL, 5 )


		self.video_panel.SetSizer( bSizer35 )
		self.video_panel.Layout()
		bSizer35.Fit( self.video_panel )
		self.game_info_images_auinotebook.AddPage( self.video_panel, u"Video" )

		if str.upper(sys.platform[0:3])=='WIN' \
		or str.upper(sys.platform[0:3])=='CYG':
			self.ie = wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
			self.pdf_panel = iewin.IEHtmlWindow(self.ie, wx.ID_ANY, size=wx.Size(709, 689), style = wx.NO_FULL_REPAINT_ON_RESIZE)
		else:
			self.pdf_panel = PDFWindow(wx.Panel( self.game_info_images_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL ))

		bSizer50 = wx.BoxSizer( wx.VERTICAL )


		self.pdf_panel.SetSizer( bSizer50 )
		self.pdf_panel.Layout()
		bSizer50.Fit( self.pdf_panel )
		self.game_info_images_auinotebook.AddPage( self.pdf_panel, u"Manual" )

		bSizer19.Add( self.game_info_images_auinotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel23.SetSizer( bSizer19 )
		self.m_panel23.Layout()
		bSizer19.Fit( self.m_panel23 )
		self.m_panel25 = wx.Panel( self.sash_right, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		playerListSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel25, wx.ID_PLAYERLISTSIZER, u"0 Current User(s)" ), wx.VERTICAL )

		self.playerGridNew = wx.grid.Grid( self.m_panel25, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.playerGridNew.CreateGrid( 0, 6 )
		self.playerGridNew.EnableEditing( False )
		self.playerGridNew.EnableGridLines( True )
		self.playerGridNew.EnableDragGridSize( False )
		self.playerGridNew.SetMargins( 0, 0 )

		# Columns
		self.playerGridNew.AutoSizeColumns()
		self.playerGridNew.EnableDragColMove( False )
		self.playerGridNew.EnableDragColSize( True )
		self.playerGridNew.SetColLabelSize( 30 )
		self.playerGridNew.SetColLabelValue( 0, u"Flag" )
		self.playerGridNew.SetColLabelValue( 1, u"Country" )
		self.playerGridNew.SetColLabelValue( 2, u"Player" )
		self.playerGridNew.SetColLabelValue( 3, u"Status" )
		self.playerGridNew.SetColLabelValue( 4, u"OS" )
		self.playerGridNew.SetColLabelValue( 5, u"Data Transfer(s)" )
		self.playerGridNew.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.playerGridNew.EnableDragRowSize( True )
		self.playerGridNew.SetRowLabelSize( 0 )
		self.playerGridNew.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.playerGridNew.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.playerGridMenu = wx.Menu()
		self.joinGameItem = wx.MenuItem( self.playerGridMenu, wx.ID_ANY, u"Join Game", wx.EmptyString, wx.ITEM_NORMAL )
		self.playerGridMenu.AppendItem( self.joinGameItem )

		self.hostGameItem = wx.MenuItem( self.playerGridMenu, wx.ID_ANY, u"Host Game", wx.EmptyString, wx.ITEM_NORMAL )
		self.playerGridMenu.AppendItem( self.hostGameItem )

		self.playerGridMenu.AppendSeparator()

		self.addToFriendsMenuItem = wx.MenuItem( self.playerGridMenu, wx.ID_ANY, u"Add To Friends", wx.EmptyString, wx.ITEM_NORMAL )
		self.playerGridMenu.AppendItem( self.addToFriendsMenuItem )

		self.removeFromFriendsMenuItem = wx.MenuItem( self.playerGridMenu, wx.ID_ANY, u"Remove From Friends", wx.EmptyString, wx.ITEM_NORMAL )
		self.playerGridMenu.AppendItem( self.removeFromFriendsMenuItem )

		self.playerGridMenu.AppendSeparator()

		self.chatblockMenuItem = wx.MenuItem( self.playerGridMenu, wx.ID_ANY, u"Block Chat", wx.EmptyString, wx.ITEM_NORMAL )
		self.playerGridMenu.AppendItem( self.chatblockMenuItem )

		self.removechatblockMenuItem = wx.MenuItem( self.playerGridMenu, wx.ID_ANY, u"Remove Chat Block", wx.EmptyString, wx.ITEM_NORMAL )
		self.playerGridMenu.AppendItem( self.removechatblockMenuItem )

		self.playerGridMenu.AppendSeparator()

		self.playergrid_admin_submenu = wx.Menu()
		self.player_grid_admin_kick_user_menuItem = wx.MenuItem( self.playergrid_admin_submenu, wx.ID_ANY, u"&Kick User", wx.EmptyString, wx.ITEM_NORMAL )
		self.playergrid_admin_submenu.AppendItem( self.player_grid_admin_kick_user_menuItem )

		self.player_grid_admin_mute_user_menuItem = wx.MenuItem( self.playergrid_admin_submenu, wx.ID_ANY, u"&Mute User", wx.EmptyString, wx.ITEM_NORMAL )
		self.playergrid_admin_submenu.AppendItem( self.player_grid_admin_mute_user_menuItem )

		self.playergrid_admin_ban_submenu = wx.Menu()
		self.playergrid_admin_ban_tempban_menuItem = wx.MenuItem( self.playergrid_admin_ban_submenu, wx.ID_ANY, u"&Temp Ban (3 days)", wx.EmptyString, wx.ITEM_NORMAL )
		self.playergrid_admin_ban_submenu.AppendItem( self.playergrid_admin_ban_tempban_menuItem )

		self.playergrid_admin_ban_full_ban_menuItem = wx.MenuItem( self.playergrid_admin_ban_submenu, wx.ID_ANY, u"&Full Ban (user, ip, email)", wx.EmptyString, wx.ITEM_NORMAL )
		self.playergrid_admin_ban_submenu.AppendItem( self.playergrid_admin_ban_full_ban_menuItem )

		self.playergrid_admin_ban_user_email_menuItem = wx.MenuItem( self.playergrid_admin_ban_submenu, wx.ID_ANY, u"&Ban User/Email", wx.EmptyString, wx.ITEM_NORMAL )
		self.playergrid_admin_ban_submenu.AppendItem( self.playergrid_admin_ban_user_email_menuItem )

		self.playergrid_admin_submenu.AppendSubMenu( self.playergrid_admin_ban_submenu, u"&Ban User" )

		self.playerGridMenu.AppendSubMenu( self.playergrid_admin_submenu, u"&Admin" )

		self.playerGridNew.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.playerGridNewOnContextMenu )

		playerListSizer.Add( self.playerGridNew, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel25.SetSizer( playerListSizer )
		self.m_panel25.Layout()
		playerListSizer.Fit( self.m_panel25 )
		self.sash_right.SplitHorizontally( self.m_panel23, self.m_panel25, 343 )
		bSizer36.Add( self.sash_right, 1, wx.EXPAND, 5 )


		self.m_panel28.SetSizer( bSizer36 )
		self.m_panel28.Layout()
		bSizer36.Fit( self.m_panel28 )
		self.sash_middle.SplitVertically( self.m_panel29, self.m_panel28, 0 )
		bSizer20.Add( self.sash_middle, 1, wx.EXPAND, 5 )


		bSizer18.Add( bSizer20, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.chat_static_entry_text = wx.StaticText( self, wx.ID_ANY, u"Chat Entry:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chat_static_entry_text.Wrap( -1 )
		bSizer21.Add( self.chat_static_entry_text, 0, wx.ALL|wx.EXPAND, 5 )

		self.chatText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.WANTS_CHARS )
		bSizer21.Add( self.chatText, 1, wx.ALL, 5 )

		self.sendChatButton = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sendChatButton.SetDefault()
		bSizer21.Add( self.sendChatButton, 0, wx.ALL|wx.EXPAND, 5 )

		self.clear_chat_button = wx.Button( self, wx.ID_ANY, u"Clear Chat", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.clear_chat_button, 0, wx.ALL|wx.EXPAND, 5 )

		self.emote_bitmapcombo = wx.combo.BitmapComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, "", wx.CB_READONLY|wx.CB_SORT )
		bSizer21.Add( self.emote_bitmapcombo, 0, wx.ALL|wx.EXPAND, 5 )

		self.emote_button = wx.Button( self, wx.ID_ANY, u"Emotes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.emote_button.Hide()

		bSizer21.Add( self.emote_button, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer18.Add( bSizer21, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer18 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.postYoutubeButton = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"&Upload to Youtube\tAlt+U", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.postYoutubeButton )

		self.exportchatMenuItem = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"&Export Chat to File\tAlt+E", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.exportchatMenuItem )

		self.m_menu5.AppendSeparator()

		self.exitMenuItem = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"&Quit\tCtrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.AppendItem( self.exitMenuItem )

		self.m_menubar1.Append( self.m_menu5, u"&File" )

		self.editMenu = wx.Menu()
		self.editCopyMenuItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"&Copy Hightlighted Chat Text", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.AppendItem( self.editCopyMenuItem )

		self.editPasteMenuItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"&Paste clipboard to chat line", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.AppendItem( self.editPasteMenuItem )

		self.m_menubar1.Append( self.editMenu, u"&Edit" )

		self.commandsMenu = wx.Menu()
		self.hostCustomGameMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"&Host Custom Game\tAlt+H", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.hostCustomGameMenuItem )

		self.setDirectoriesMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"&Set Folders\tAlt+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.setDirectoriesMenuItem )

		self.auditGamesMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"&Audit Games - Rom Scan/Update\tAlt+A", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.auditGamesMenuItem )

		self.commandsMenu.AppendSeparator()

		self.configurationMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"Set GUI &Configuration\tAlt+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.configurationMenuItem )

		self.sliderresetMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"&Reset GUI Windows\tAlt+R", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.sliderresetMenuItem )

		self.commandsMenu.AppendSeparator()

		self.cademodeMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"Cabinet Mode", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.cademodeMenuItem )

		self.commandsMenu.AppendSeparator()

		self.viewlogMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"View Game &Log\tAlt+L", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.viewlogMenuItem )

		self.DEBUGMenuItem = wx.MenuItem( self.commandsMenu, wx.ID_ANY, u"&DEBUG Toggle\tAlt+D", wx.EmptyString, wx.ITEM_NORMAL )
		self.commandsMenu.AppendItem( self.DEBUGMenuItem )

		self.m_menubar1.Append( self.commandsMenu, u"&Options" )

		self.advancedMenu = wx.Menu()
		self.mameSettingsMenuItem = wx.MenuItem( self.advancedMenu, wx.ID_ANY, u"MAME Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.advancedMenu.AppendItem( self.mameSettingsMenuItem )

		self.messSettingsMenuItem = wx.MenuItem( self.advancedMenu, wx.ID_ANY, u"MESS Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.advancedMenu.AppendItem( self.messSettingsMenuItem )

		self.advancedMenu.AppendSeparator()

		self.hubcadeMenuItem = wx.MenuItem( self.advancedMenu, wx.ID_ANY, u"&Hub!Cade", wx.EmptyString, wx.ITEM_NORMAL )
		self.advancedMenu.AppendItem( self.hubcadeMenuItem )

		self.hubcadeEditorMenuItem = wx.MenuItem( self.advancedMenu, wx.ID_ANY, u"Hub!Cade &Editor", wx.EmptyString, wx.ITEM_NORMAL )
		self.advancedMenu.AppendItem( self.hubcadeEditorMenuItem )

		self.m_menubar1.Append( self.advancedMenu, u"&Advanced" )

		self.databaseMenu = wx.Menu()
		self.chatarchiveviewMenuItem = wx.MenuItem( self.databaseMenu, wx.ID_ANY, u"&Chat Archive View", wx.EmptyString, wx.ITEM_NORMAL )
		self.databaseMenu.AppendItem( self.chatarchiveviewMenuItem )

		self.friendsblockMenuItem = wx.MenuItem( self.databaseMenu, wx.ID_ANY, u"&Friends/Block Viewer", wx.EmptyString, wx.ITEM_NORMAL )
		self.databaseMenu.AppendItem( self.friendsblockMenuItem )

		self.m_menubar1.Append( self.databaseMenu, u"&Database" )

		self.statsMenu = wx.Menu()
		self.serverStatsMenuItem = wx.MenuItem( self.statsMenu, wx.ID_ANY, u"&Server Stats", wx.EmptyString, wx.ITEM_NORMAL )
		self.statsMenu.AppendItem( self.serverStatsMenuItem )

		self.clientStatsMenuItem = wx.MenuItem( self.statsMenu, wx.ID_ANY, u"&Client Statistics", wx.EmptyString, wx.ITEM_NORMAL )
		self.statsMenu.AppendItem( self.clientStatsMenuItem )

		self.statsMenu.AppendSeparator()

		self.top10StatsMenuItem = wx.MenuItem( self.statsMenu, wx.ID_ANY, u"Hub!Cade Arrange &Top 10", wx.EmptyString, wx.ITEM_NORMAL )
		self.statsMenu.AppendItem( self.top10StatsMenuItem )

		self.m_menubar1.Append( self.statsMenu, u"&Statistics" )

		self.utilsMenu = wx.Menu()
		self.imageconvertMenuItem = wx.MenuItem( self.utilsMenu, wx.ID_ANY, u"Convert &Image(s)", wx.EmptyString, wx.ITEM_NORMAL )
		self.utilsMenu.AppendItem( self.imageconvertMenuItem )

		self.utilsMenu.AppendSeparator()

		self.archiveconvertMenuItem = wx.MenuItem( self.utilsMenu, wx.ID_ANY, u"Convert &7z to ZIP", wx.EmptyString, wx.ITEM_NORMAL )
		self.utilsMenu.AppendItem( self.archiveconvertMenuItem )

		self.archiveconvertZip7zMenuItem = wx.MenuItem( self.utilsMenu, wx.ID_ANY, u"Convert &ZIP to 7z", wx.EmptyString, wx.ITEM_NORMAL )
		self.utilsMenu.AppendItem( self.archiveconvertZip7zMenuItem )

		self.utilsMenu.AppendSeparator()

		self.romzipconvertMenuItem = wx.MenuItem( self.utilsMenu, wx.ID_ANY, u"&ROM to Zip", wx.EmptyString, wx.ITEM_NORMAL )
		self.utilsMenu.AppendItem( self.romzipconvertMenuItem )

		self.rom7zconvertMenuItem = wx.MenuItem( self.utilsMenu, wx.ID_ANY, u"R&OM to 7z", wx.EmptyString, wx.ITEM_NORMAL )
		self.utilsMenu.AppendItem( self.rom7zconvertMenuItem )

		self.m_menubar1.Append( self.utilsMenu, u"&Utilities" )

		self.admin_menu = wx.Menu()
		self.admin_motd_MenuItem = wx.MenuItem( self.admin_menu, wx.ID_ANY, u"&MOTD Change", wx.EmptyString, wx.ITEM_NORMAL )
		self.admin_menu.AppendItem( self.admin_motd_MenuItem )

		self.admin_ban_List_MenuItem = wx.MenuItem( self.admin_menu, wx.ID_ANY, u"&Ban Inquiry", wx.EmptyString, wx.ITEM_NORMAL )
		self.admin_menu.AppendItem( self.admin_ban_List_MenuItem )

		self.m_menubar1.Append( self.admin_menu, u"Ad&min" )

		self.help = wx.Menu()
		self.aboutMenuItem = wx.MenuItem( self.help, wx.ID_ANY, u"&About\tF1", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.AppendItem( self.aboutMenuItem )

		self.help.AppendSeparator()

		self.main_hubcade_site_MenuItem = wx.MenuItem( self.help, wx.ID_ANY, u"Hub!Cade Arrange &Website", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.AppendItem( self.main_hubcade_site_MenuItem )

		self.forumMenuItem = wx.MenuItem( self.help, wx.ID_ANY, u"&Forum", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.AppendItem( self.forumMenuItem )

		self.help.AppendSeparator()

		self.bug_reportMenuItem = wx.MenuItem( self.help, wx.ID_ANY, u"Bug &Report", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.AppendItem( self.bug_reportMenuItem )

		self.m_menubar1.Append( self.help, u"&Help" )

		self.SetMenuBar( self.m_menubar1 )

		self.main_frame_status_bar = self.CreateStatusBar( 4, wx.ST_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.iconizeFrame )
		self.Bind( wx.EVT_ICONIZE, self.iconizeFrame )
		self.Bind( wx.EVT_SIZE, self.onMainFrameSize )
		self.sash_middle.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnImageChatResize )
		self.sash_left.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnChatResize )
		self.manage_game_auinotebook.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.game_notebook_tab_change )
		self.publicGameGrid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.joinGameInformation )
		self.publicGameGrid.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.joinGameFromGames )
		self.Bind( wx.EVT_MENU, self.OnJoinGameAddToFavMenuItem, id = self.join_game_add_to_fav_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnJoinGameRemoveFromFavMenuItem, id = self.join_game_remove_from_fav_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnJoinGameJoinGameMenuItem, id = self.join_game_join_game_menuItem.GetId() )
		self.gameListTreeCtrl.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.hostGameFromList )
		self.gameListTreeCtrl.Bind( wx.EVT_TREE_SEL_CHANGED, self.hostGameInformation )
		self.gameSearchText.Bind( wx.EVT_TEXT, self.filterGameTree )
		self.monitor_type_combo.Bind( wx.EVT_COMBOBOX, self.OnHostMonitorFilterComboChange )
		self.filter_player_count_spinner.Bind( wx.EVT_SPINCTRL, self.OnFilterPlayerSpinner )
		self.filterjoincategorychoice.Bind( wx.EVT_CHOICE, self.OnHostCategoryFilter )
		self.filterresetButton.Bind( wx.EVT_BUTTON, self.ongamefilterResetButton )
		self.favorites_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnFavoriteGameViewData )
		self.favorites_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnFavoriteGameHost )
		self.Bind( wx.EVT_MENU, self.OnFavoriteHostGameMenuItem, id = self.fav_host_game_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFavoriteRemFromFavMenuItem, id = self.fav_remove_game_menuItem.GetId() )
		self.chat_aui_notebook.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnChatPageChanged )
		self.chat_aui_notebook.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnChatPageClosed )
		if Client_GlobalData.webkit_enabled == False:
			self.chatLogHTML.Bind( webview.EVT_HTML_LINK_CLICKED, self.onURLclick )
		else:
			self.chatLogHTML.Bind( webview.EVT_WEB_VIEW_NEWWINDOW, self.onURLclick )
		self.sash_right.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnImageResize )
		self.game_info_images_auinotebook.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnGameInfoImagesPageChanged )
		self.game_info_images_auinotebook.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnGameInfoImagesPageClosed )
		self.video_playback_slider.Bind( wx.EVT_SCROLL, self.OnSeek )
		self.vid_play_button.Bind( wx.EVT_BUTTON, self.OnVidPlayButton )
		self.vid_pause_button.Bind( wx.EVT_BUTTON, self.OnVidPauseButton )
		self.vid_stop_button.Bind( wx.EVT_BUTTON, self.OnVidStopButton )
		self.vid_mute_toggle_button.Bind( wx.EVT_BUTTON, self.OnVidMuteToggleButton )
		self.vid_volume_down.Bind( wx.EVT_BUTTON, self.OnVidVolumeDownButton )
		self.vid_vlume_up.Bind( wx.EVT_BUTTON, self.OnVidVolumeUpButton )
		self.playerGridNew.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.joinGameFromUser )
		self.Bind( wx.EVT_MENU, self.joinGameFromUser, id = self.joinGameItem.GetId() )
		self.Bind( wx.EVT_MENU, self.hostGame, id = self.hostGameItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnaddToFriendsMenuItem, id = self.addToFriendsMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnremoveFromFriendsMenuItem, id = self.removeFromFriendsMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnChatBlockMenuItem, id = self.chatblockMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnremovechatblockMenuItem, id = self.removechatblockMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.onPlayerGridAdmin_KickUserMenuItem, id = self.player_grid_admin_kick_user_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnPlayerGridAdminMuteUsermenuItem, id = self.player_grid_admin_mute_user_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnPlayerGridAdminBanTemp, id = self.playergrid_admin_ban_tempban_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnPlayerGridAdminBanFull, id = self.playergrid_admin_ban_full_ban_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnPlayerGridAdminBanUserEmail, id = self.playergrid_admin_ban_user_email_menuItem.GetId() )
		self.chatText.Bind( wx.EVT_KEY_DOWN, self.sendChatOnEnter )
		self.sendChatButton.Bind( wx.EVT_BUTTON, self.sendChat )
		self.clear_chat_button.Bind( wx.EVT_BUTTON, self.OnClearChatButton )
		self.emote_bitmapcombo.Bind( wx.EVT_COMBOBOX, self.OnEmoteBitmapCombo )
		self.emote_button.Bind( wx.EVT_BUTTON, self.OnEmoteButton )
		self.Bind( wx.EVT_MENU, self.uploadToYoutube, id = self.postYoutubeButton.GetId() )
		self.Bind( wx.EVT_MENU, self.onExportChatMenuItem, id = self.exportchatMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.closeFrameEvent, id = self.exitMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnEditMenuItem_Copy, id = self.editCopyMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnEditMenuItem_Paste, id = self.editPasteMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.hostGame, id = self.hostCustomGameMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.setDirectories, id = self.setDirectoriesMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.auditGames, id = self.auditGamesMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.onConfigurationMenuItem, id = self.configurationMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnSliderResetMenuItem, id = self.sliderresetMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnCadeModeMenuItem, id = self.cademodeMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewMAMELog, id = self.viewlogMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.ToggleDebug, id = self.DEBUGMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.editMAMESettings, id = self.mameSettingsMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.editMESSSettings, id = self.messSettingsMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.onHubCadeMenuItem, id = self.hubcadeMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.onHubCadeEditorMenuItem, id = self.hubcadeEditorMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnChatArchiveViewMenuItem, id = self.chatarchiveviewMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFriendBlockMenuItem, id = self.friendsblockMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnServerStatsMenuItem, id = self.serverStatsMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnClientStatsMenu, id = self.clientStatsMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.Ontop10StatsMenuItem, id = self.top10StatsMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnImageConvertMenuItem, id = self.imageconvertMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnArchiveConvertMenuItem, id = self.archiveconvertMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnArchiveZip7zConvertMenuItem, id = self.archiveconvertZip7zMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnRomZipConvertMenuItem, id = self.romzipconvertMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnRom7zConvertMenuItem, id = self.rom7zconvertMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAdminMOTDMenuItem, id = self.admin_motd_MenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAdminBanInquiryMenuItem, id = self.admin_ban_List_MenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.onAboutMenuItem, id = self.aboutMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMainHubCadeSite, id = self.main_hubcade_site_MenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.openForumPage, id = self.forumMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnBugReportMenuItem, id = self.bug_reportMenuItem.GetId() )
		self.Bind(wx.media.EVT_MEDIA_LOADED, self.OnMediaLoad)
		self.Bind(wx.media.EVT_MEDIA_FINISHED, self.OnVideoFinished)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def iconizeFrame( self, event ):
		event.Skip()


	def onMainFrameSize( self, event ):
		event.Skip()

	def OnImageChatResize( self, event ):
		event.Skip()

	def OnChatResize( self, event ):
		event.Skip()

	def game_notebook_tab_change( self, event ):
		event.Skip()

	def joinGameInformation( self, event ):
		event.Skip()

	def joinGameFromGames( self, event ):
		event.Skip()

	def OnJoinGameAddToFavMenuItem( self, event ):
		event.Skip()

	def OnJoinGameRemoveFromFavMenuItem( self, event ):
		event.Skip()

	def OnJoinGameJoinGameMenuItem( self, event ):
		event.Skip()

	def hostGameFromList( self, event ):
		event.Skip()

	def hostGameInformation( self, event ):
		event.Skip()

	def filterGameTree( self, event ):
		event.Skip()

	def OnHostMonitorFilterComboChange( self, event ):
		event.Skip()

	def OnFilterPlayerSpinner( self, event ):
		event.Skip()

	def OnHostCategoryFilter( self, event ):
		event.Skip()

	def ongamefilterResetButton( self, event ):
		event.Skip()

	def OnFavoriteGameViewData( self, event ):
		event.Skip()

	def OnFavoriteGameHost( self, event ):
		event.Skip()

	def OnFavoriteHostGameMenuItem( self, event ):
		event.Skip()

	def OnFavoriteRemFromFavMenuItem( self, event ):
		event.Skip()

	def OnChatPageChanged( self, event ):
		event.Skip()

	def OnChatPageClosed( self, event ):
		event.Skip()

	def onURLclick( self, event ):
		event.Skip()

	def OnImageResize( self, event ):
		event.Skip()

	def OnGameInfoImagesPageChanged( self, event ):
		event.Skip()

	def OnGameInfoImagesPageClosed( self, event ):
		event.Skip()

	def OnSeek( self, event ):
		event.Skip()

	def OnVidPlayButton( self, event ):
		event.Skip()

	def OnVidPauseButton( self, event ):
		event.Skip()

	def OnVidStopButton( self, event ):
		event.Skip()

	def OnVidMuteToggleButton( self, event ):
		event.Skip()

	def OnVidVolumeDownButton( self, event ):
		event.Skip()

	def OnVidVolumeUpButton( self, event ):
		event.Skip()

	def joinGameFromUser( self, event ):
		event.Skip()


	def hostGame( self, event ):
		event.Skip()

	def OnaddToFriendsMenuItem( self, event ):
		event.Skip()

	def OnremoveFromFriendsMenuItem( self, event ):
		event.Skip()

	def OnChatBlockMenuItem( self, event ):
		event.Skip()

	def OnremovechatblockMenuItem( self, event ):
		event.Skip()

	def onPlayerGridAdmin_KickUserMenuItem( self, event ):
		event.Skip()

	def OnPlayerGridAdminMuteUsermenuItem( self, event ):
		event.Skip()

	def OnPlayerGridAdminBanTemp( self, event ):
		event.Skip()

	def OnPlayerGridAdminBanFull( self, event ):
		event.Skip()

	def OnPlayerGridAdminBanUserEmail( self, event ):
		event.Skip()

	def sendChatOnEnter( self, event ):
		event.Skip()

	def sendChat( self, event ):
		event.Skip()

	def OnClearChatButton( self, event ):
		event.Skip()

	def OnEmoteBitmapCombo( self, event ):
		event.Skip()

	def OnEmoteButton( self, event ):
		event.Skip()

	def uploadToYoutube( self, event ):
		event.Skip()

	def onExportChatMenuItem( self, event ):
		event.Skip()

	def closeFrameEvent( self, event ):
		event.Skip()

	def OnEditMenuItem_Copy( self, event ):
		event.Skip()

	def OnEditMenuItem_Paste( self, event ):
		event.Skip()


	def setDirectories( self, event ):
		event.Skip()

	def auditGames( self, event ):
		event.Skip()

	def onConfigurationMenuItem( self, event ):
		event.Skip()

	def OnSliderResetMenuItem( self, event ):
		event.Skip()

	def OnCadeModeMenuItem( self, event ):
		event.Skip()

	def OnViewMAMELog( self, event ):
		event.Skip()

	def ToggleDebug( self, event ):
		event.Skip()

	def editMAMESettings( self, event ):
		event.Skip()

	def editMESSSettings( self, event ):
		event.Skip()

	def onHubCadeMenuItem( self, event ):
		event.Skip()

	def onHubCadeEditorMenuItem( self, event ):
		event.Skip()

	def OnChatArchiveViewMenuItem( self, event ):
		event.Skip()

	def OnFriendBlockMenuItem( self, event ):
		event.Skip()

	def OnServerStatsMenuItem( self, event ):
		event.Skip()

	def OnClientStatsMenu( self, event ):
		event.Skip()

	def Ontop10StatsMenuItem( self, event ):
		event.Skip()

	def OnImageConvertMenuItem( self, event ):
		event.Skip()

	def OnArchiveConvertMenuItem( self, event ):
		event.Skip()

	def OnArchiveZip7zConvertMenuItem( self, event ):
		event.Skip()

	def OnRomZipConvertMenuItem( self, event ):
		event.Skip()

	def OnRom7zConvertMenuItem( self, event ):
		event.Skip()

	def OnAdminMOTDMenuItem( self, event ):
		event.Skip()

	def OnAdminBanInquiryMenuItem( self, event ):
		event.Skip()

	def onAboutMenuItem( self, event ):
		event.Skip()

	def OnMainHubCaseSite( self, event ):
		event.Skip()

	def openForumPage( self, event ):
		event.Skip()

	def OnBugReportMenuItem( self, event ):
		event.Skip()

	def sash_middleOnIdle( self, event ):
		self.sash_middle.SetSashPosition( 0 )
		self.sash_middle.Unbind( wx.EVT_IDLE )

	def sash_leftOnIdle( self, event ):
		self.sash_left.SetSashPosition( 343 )
		self.sash_left.Unbind( wx.EVT_IDLE )

	def publicGameGridOnContextMenu( self, event ):
		Client_GlobalData.grid_cell_row = event.GetRow()
		self.publicGameGrid.PopupMenu( self.join_game_menu, event.GetPosition() )

	def favorites_gridOnContextMenu( self, event ):
		Client_GlobalData.grid_cell_row = event.GetRow()
		self.favorites_grid.PopupMenu( self.favorites_grid_menu, event.GetPosition() )

	def sash_rightOnIdle( self, event ):
		self.sash_right.SetSashPosition( 343 )
		self.sash_right.Unbind( wx.EVT_IDLE )

	def playerGridNewOnContextMenu( self, event ):
		Client_GlobalData.grid_cell_row = event.GetRow()
		self.playerGridNew.PopupMenu( self.playerGridMenu, event.GetPosition() )
