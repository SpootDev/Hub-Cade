# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MOTDTemplate
###########################################################################

class MOTDTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MOTD Update", pos = wx.DefaultPosition, size = wx.Size( 611,432 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer51.Add( self.m_textCtrl12, 1, wx.ALL|wx.EXPAND, 5 )

		m_sdbSizer7 = wx.StdDialogButtonSizer()
		self.m_sdbSizer7OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer7.AddButton( self.m_sdbSizer7OK )
		self.m_sdbSizer7Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer7.AddButton( self.m_sdbSizer7Cancel )
		m_sdbSizer7.Realize();

		bSizer51.Add( m_sdbSizer7, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer51 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnMOTDDialogInit )
		self.m_sdbSizer7OK.Bind( wx.EVT_BUTTON, self.OnMOTDSaveText )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnMOTDDialogInit( self, event ):
		event.Skip()

	def OnMOTDSaveText( self, event ):
		event.Skip()


