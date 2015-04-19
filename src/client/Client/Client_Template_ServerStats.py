# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class ServerStatsTemplate
###########################################################################

class ServerStatsTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MameHub Arrange Server Statistics", pos = wx.DefaultPosition, size = wx.Size( 377,420 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.ServerStatsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.ServerStatsGrid.CreateGrid( 0, 2 )
		self.ServerStatsGrid.EnableEditing( False )
		self.ServerStatsGrid.EnableGridLines( True )
		self.ServerStatsGrid.EnableDragGridSize( False )
		self.ServerStatsGrid.SetMargins( 0, 0 )

		# Columns
		self.ServerStatsGrid.AutoSizeColumns()
		self.ServerStatsGrid.EnableDragColMove( False )
		self.ServerStatsGrid.EnableDragColSize( True )
		self.ServerStatsGrid.SetColLabelSize( 30 )
		self.ServerStatsGrid.SetColLabelValue( 0, u"Statistic" )
		self.ServerStatsGrid.SetColLabelValue( 1, u"Value" )
		self.ServerStatsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.ServerStatsGrid.EnableDragRowSize( True )
		self.ServerStatsGrid.SetRowLabelSize( 0 )
		self.ServerStatsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.ServerStatsGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer48.Add( self.ServerStatsGrid, 1, wx.ALL|wx.EXPAND, 5 )

		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		m_sdbSizer4.Realize();

		bSizer48.Add( m_sdbSizer4, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer48 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnServerStatsInitDialog )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnServerStatsInitDialog( self, event ):
		event.Skip()


