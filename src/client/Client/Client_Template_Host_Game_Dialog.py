# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class HostGameDialogTemplate
###########################################################################

class HostGameDialogTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Host New Game", pos = wx.DefaultPosition, size = wx.Size( 462,485 ), style = wx.CAPTION )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Room Name" ), wx.VERTICAL )

		self.roomName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		sbSizer221.Add( self.roomName, 0, wx.ALL, 5 )

		bSizer22.Add( sbSizer221, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		sbSizer25 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Game Name" ), wx.VERTICAL )

		gameListChoices = []
		self.gameList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, gameListChoices, wx.LB_ALWAYS_SB|wx.LB_SINGLE )
		sbSizer25.Add( self.gameList, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer22.Add( sbSizer25, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 20 )

		sbSizer19 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Details" ), wx.VERTICAL )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Visibility" ), wx.VERTICAL )

		self.publicCheckbox = wx.CheckBox( self, wx.ID_ANY, u"Public", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.publicCheckbox.SetValue(True)
		sbSizer20.Add( self.publicCheckbox, 0, wx.ALL, 5 )

		gbSizer1.Add( sbSizer20, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), 0, 5 )

		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Max Players" ), wx.VERTICAL )

		self.maxPlayerSlider = wx.Slider( self, wx.ID_ANY, 4, 1, 16, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer21.Add( self.maxPlayerSlider, 0, wx.ALL, 5 )

		gbSizer1.Add( sbSizer21, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), 0, 5 )

		sbSizer211 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Max Observers" ), wx.VERTICAL )

		self.maxObserverSlider = wx.Slider( self, wx.ID_ANY, 0, 0, 16, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		sbSizer211.Add( self.maxObserverSlider, 0, wx.ALL, 5 )

		gbSizer1.Add( sbSizer211, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		sbSizer19.Add( gbSizer1, 1, wx.EXPAND, 5 )

		bSizer22.Add( sbSizer19, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.launchButton = wx.Button( self, wx.ID_ANY, u"Launch", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.launchButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer13.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.cancelButton, 0, wx.ALL, 5 )

		bSizer22.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.initDialog )
		self.launchButton.Bind( wx.EVT_BUTTON, self.launch )
		self.cancelButton.Bind( wx.EVT_BUTTON, self.cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def initDialog( self, event ):
		event.Skip()

	def launch( self, event ):
		event.Skip()

	def cancel( self, event ):
		event.Skip()


