# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec  2 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class GameLobbyTemplate
###########################################################################

class GameLobbyTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Game Lobby", pos = wx.DefaultPosition, size = wx.Size( 446,512 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.game_lobby_grid = wx.grid.Grid( self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.game_lobby_grid.CreateGrid( 0, 6 )
		self.game_lobby_grid.EnableEditing( True )
		self.game_lobby_grid.EnableGridLines( True )
		self.game_lobby_grid.EnableDragGridSize( False )
		self.game_lobby_grid.SetMargins( 0, 0 )

		# Columns
		self.game_lobby_grid.AutoSizeColumns()
		self.game_lobby_grid.EnableDragColMove( False )
		self.game_lobby_grid.EnableDragColSize( True )
		self.game_lobby_grid.SetColLabelSize( 30 )
		self.game_lobby_grid.SetColLabelValue( 0, u"Flag" )
		self.game_lobby_grid.SetColLabelValue( 1, u"Country" )
		self.game_lobby_grid.SetColLabelValue( 2, u"Player" )
		self.game_lobby_grid.SetColLabelValue( 3, u"Status" )
		self.game_lobby_grid.SetColLabelValue( 4, u"OS" )
		self.game_lobby_grid.SetColLabelValue( 5, u"Ping" )
		self.game_lobby_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.game_lobby_grid.EnableDragRowSize( True )
		self.game_lobby_grid.SetRowLabelSize( 0 )
		self.game_lobby_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.game_lobby_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer21.Add( self.game_lobby_grid, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel17.SetSizer( bSizer21 )
		self.m_panel17.Layout()
		bSizer21.Fit( self.m_panel17 )
		bSizer20.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.game_lobby_ready_toggle_button = wx.ToggleButton( self.m_panel18, wx.ID_ANY, u"Ready", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.game_lobby_ready_toggle_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.game_lobby_cancel_button = wx.Button( self.m_panel18, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.game_lobby_cancel_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.game_lobby_kick_button = wx.Button( self.m_panel18, wx.ID_ANY, u"Kick Selected User(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.game_lobby_kick_button, 1, wx.ALL, 5 )

		self.m_panel18.SetSizer( bSizer22 )
		self.m_panel18.Layout()
		bSizer22.Fit( self.m_panel18 )
		bSizer20.Add( self.m_panel18, 0, wx.EXPAND |wx.ALL, 5 )

		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.onGameLobbyDiagInit )
		self.game_lobby_ready_toggle_button.Bind( wx.EVT_TOGGLEBUTTON, self.onGameLobbyReadyButton )
		self.game_lobby_cancel_button.Bind( wx.EVT_BUTTON, self.onGameLobbyCancelButton )
		self.game_lobby_kick_button.Bind( wx.EVT_BUTTON, self.onGameLobbyKickUserButton )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onGameLobbyDiagInit( self, event ):
		event.Skip()

	def onGameLobbyReadyButton( self, event ):
		event.Skip()

	def onGameLobbyCancelButton( self, event ):
		event.Skip()

	def onGameLobbyKickUserButton( self, event ):
		event.Skip()


