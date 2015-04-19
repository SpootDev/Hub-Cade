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
## Class YoutubeUploaderTemplate
###########################################################################

class YoutubeUploaderTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Youtube Uploader", pos = wx.DefaultPosition, size = wx.Size( 723,480 ), style = wx.CAPTION|wx.STAY_ON_TOP|wx.SYSTEM_MENU )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		sbSizer30 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Youtube Account Information" ), wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer31 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Email Address" ), wx.VERTICAL )

		self.emailText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sbSizer31.Add( self.emailText, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer20.Add( sbSizer31, 1, 0, 5 )

		sbSizer32 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Youtube Password (NOT YOUR Hub!Cade PASSWORD)" ), wx.VERTICAL )

		self.passwordText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer32.Add( self.passwordText, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer20.Add( sbSizer32, 1, 0, 5 )

		sbSizer30.Add( bSizer20, 1, wx.EXPAND, 5 )

		bSizer19.Add( sbSizer30, 0, wx.EXPAND, 5 )

		sbSizer33 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Select a Video" ), wx.VERTICAL )

		videoChoiceChoices = []
		self.videoChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, videoChoiceChoices, 0 )
		self.videoChoice.SetSelection( 0 )
		self.videoChoice.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Courier New" ) )

		sbSizer33.Add( self.videoChoice, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer19.Add( sbSizer33, 0, wx.EXPAND, 5 )

		sbSizer34 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Video Information" ), wx.VERTICAL )

		sbSizer35 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Title" ), wx.HORIZONTAL )

		self.titleText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer35.Add( self.titleText, 1, wx.ALL|wx.EXPAND, 5 )

		self.addTitleCheckbox = wx.CheckBox( self, wx.ID_ANY, u"Add \"- Hub!Cade\" to title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addTitleCheckbox.SetValue(True)
		sbSizer35.Add( self.addTitleCheckbox, 0, wx.ALL, 5 )

		sbSizer34.Add( sbSizer35, 0, wx.EXPAND, 5 )

		sbSizer351 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Keywords (separate with commas)" ), wx.HORIZONTAL )

		self.keywordsText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer351.Add( self.keywordsText, 1, wx.ALL|wx.EXPAND, 5 )

		self.addKeywordsCheckbox = wx.CheckBox( self, wx.ID_ANY, u"Add Hub!Cade Keywords", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addKeywordsCheckbox.SetValue(True)
		sbSizer351.Add( self.addKeywordsCheckbox, 0, wx.ALL, 5 )

		sbSizer34.Add( sbSizer351, 0, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer36 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Description" ), wx.VERTICAL )

		self.descriptionText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizer36.Add( self.descriptionText, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer22.Add( sbSizer36, 1, wx.EXPAND, 5 )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Settings" ), wx.VERTICAL )

		self.privateCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Make Video Private", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer40.Add( self.privateCheckBox, 0, wx.ALL, 5 )

		bSizer22.Add( sbSizer40, 0, wx.EXPAND, 5 )

		sbSizer34.Add( bSizer22, 1, wx.EXPAND, 5 )

		bSizer19.Add( sbSizer34, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.uploadButton = wx.Button( self, wx.ID_ANY, u"&Upload", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.uploadButton.SetDefault()
		bSizer21.Add( self.uploadButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.exitButton = wx.Button( self, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.exitButton, 0, wx.ALL, 5 )

		bSizer19.Add( bSizer21, 0, wx.ALL|wx.EXPAND, 5 )

		self.SetSizer( bSizer19 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.uploadButton.Bind( wx.EVT_BUTTON, self.upload )
		self.exitButton.Bind( wx.EVT_BUTTON, self.exit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def upload( self, event ):
		event.Skip()

	def exit( self, event ):
		event.Skip()


