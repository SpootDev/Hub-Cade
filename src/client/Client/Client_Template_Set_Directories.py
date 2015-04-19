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
## Class SetDirectoriesDialogTemplate
###########################################################################

class SetDirectoriesDialogTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Set Folders", pos = wx.DefaultPosition, size = wx.Size( 526,446 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		sbSizer22 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Current Folders List" ), wx.VERTICAL )

		directoryListboxChoices = []
		self.directoryListbox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, directoryListboxChoices, wx.LB_MULTIPLE )
		sbSizer22.Add( self.directoryListbox, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( sbSizer22, 1, wx.EXPAND, 5 )

		self.deleteDirectoryButton = wx.Button( self, wx.ID_ANY, u"Remove Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.deleteDirectoryButton, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		sbSizer24 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Add New Folder(s)" ), wx.HORIZONTAL )

		self.setfolder_text_control = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.setfolder_text_control, 1, wx.ALL, 5 )

		self.setfolder_button = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.setfolder_button, 0, wx.ALL, 5 )

		self.multidir_select_button = wx.Button( self, wx.ID_ANY, u"Multi Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.multidir_select_button, 0, wx.ALL, 5 )

		self.addNewDirectoryButton = wx.Button( self, wx.ID_ANY, u"Add to List", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.addNewDirectoryButton, 0, wx.ALL, 5 )

		self.autoaddDirectoryButton = wx.Button( self, wx.ID_ANY, u"Auto Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer24.Add( self.autoaddDirectoryButton, 0, wx.ALL, 5 )


		bSizer13.Add( sbSizer24, 0, wx.EXPAND, 5 )

		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();

		bSizer13.Add( m_sdbSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.closeDialog )
		self.Bind( wx.EVT_INIT_DIALOG, self.initDialog )
		self.directoryListbox.Bind( wx.EVT_LISTBOX_DCLICK, self.removeSelectedDirectory )
		self.deleteDirectoryButton.Bind( wx.EVT_BUTTON, self.removeSelectedDirectory )
		self.setfolder_button.Bind( wx.EVT_BUTTON, self.OnSetFolder_Button )
		self.multidir_select_button.Bind( wx.EVT_BUTTON, self.OnMultiDirButton )
		self.addNewDirectoryButton.Bind( wx.EVT_BUTTON, self.addNewDirectory )
		self.autoaddDirectoryButton.Bind( wx.EVT_BUTTON, self.OnAutoAddDirButton )
		self.m_sdbSizer3Cancel.Bind( wx.EVT_BUTTON, self.OnSetFolderCancelButton )
		self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.closeDialog )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def closeDialog( self, event ):
		event.Skip()

	def initDialog( self, event ):
		event.Skip()

	def removeSelectedDirectory( self, event ):
		event.Skip()


	def OnSetFolder_Button( self, event ):
		event.Skip()

	def OnMultiDirButton( self, event ):
		event.Skip()

	def addNewDirectory( self, event ):
		event.Skip()

	def OnAutoAddDirButton( self, event ):
		event.Skip()

	def OnSetFolderCancelButton( self, event ):
		event.Skip()



