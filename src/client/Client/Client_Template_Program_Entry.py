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
## Class ProgramEntryTemplate
###########################################################################

class ProgramEntryTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome to Hub!Cade", pos = wx.DefaultPosition, size = wx.Size( 512,447 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel54 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer231 = wx.BoxSizer( wx.VERTICAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel54, wx.ID_ANY, u"User Login Information" ), wx.HORIZONTAL )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel54, wx.ID_ANY, u"Username" ), wx.VERTICAL )

		self.usernameText = wx.TextCtrl( self.m_panel54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.usernameText.SetMaxLength( 16 )
		sbSizer4.Add( self.usernameText, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer46.Add( sbSizer4, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel54, wx.ID_ANY, u"Password" ), wx.VERTICAL )

		self.passwordText = wx.TextCtrl( self.m_panel54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer5.Add( self.passwordText, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer46.Add( sbSizer5, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer46, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.loginButton = wx.Button( self.m_panel54, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.loginButton.SetDefault()
		bSizer15.Add( self.loginButton, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.rememberPasswordCheckBox = wx.CheckBox( self.m_panel54, wx.ID_ANY, u"Remember Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.rememberPasswordCheckBox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.emailPasswordButton = wx.Button( self.m_panel54, wx.ID_ANY, u"Email Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.emailPasswordButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		sbSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer231.Add( sbSizer2, 0, wx.ALL|wx.EXPAND, 20 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel54, wx.ID_ANY, u"New Users Enter Email to Register" ), wx.HORIZONTAL )

		self.emailText = wx.TextCtrl( self.m_panel54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.emailText, 1, wx.ALL|wx.EXPAND, 5 )

		self.program_entry_register_button = wx.Button( self.m_panel54, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.program_entry_register_button, 0, wx.ALL, 5 )


		bSizer231.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 25 )

		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel54, wx.ID_ANY, u"Fowarded Port Number" ), wx.VERTICAL )

		self.portNumberSpinner = wx.SpinCtrl( self.m_panel54, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1025, 65535, 5805 )
		sbSizer61.Add( self.portNumberSpinner, 0, wx.ALL, 5 )


		bSizer231.Add( sbSizer61, 1, wx.ALIGN_CENTER, 5 )


		self.m_panel54.SetSizer( bSizer231 )
		self.m_panel54.Layout()
		bSizer231.Fit( self.m_panel54 )
		bSizer23.Add( self.m_panel54, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel36 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_button28 = wx.Button( self.m_panel36, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_button28, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel36.SetSizer( bSizer42 )
		self.m_panel36.Layout()
		bSizer42.Fit( self.m_panel36 )
		bSizer23.Add( self.m_panel36, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.initDialog )
		self.loginButton.Bind( wx.EVT_BUTTON, self.login )
		self.emailPasswordButton.Bind( wx.EVT_BUTTON, self.emailPassword )
		self.program_entry_register_button.Bind( wx.EVT_BUTTON, self.registerAccount )
		self.m_button28.Bind( wx.EVT_BUTTON, self.quit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def initDialog( self, event ):
		event.Skip()

	def login( self, event ):
		event.Skip()

	def emailPassword( self, event ):
		event.Skip()

	def registerAccount( self, event ):
		event.Skip()

	def quit( self, event ):
		event.Skip()


