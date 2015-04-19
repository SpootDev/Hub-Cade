# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class ClientStatsTemplate
###########################################################################

class ClientStatsTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MameHub Arrange Client Statistics", pos = wx.DefaultPosition, size = wx.Size( 570,554 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		self.ClientStatsGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.ClientStatsGrid.CreateGrid( 0, 2 )
		self.ClientStatsGrid.EnableEditing( False )
		self.ClientStatsGrid.EnableGridLines( True )
		self.ClientStatsGrid.EnableDragGridSize( False )
		self.ClientStatsGrid.SetMargins( 0, 0 )

		# Columns
		self.ClientStatsGrid.AutoSizeColumns()
		self.ClientStatsGrid.EnableDragColMove( False )
		self.ClientStatsGrid.EnableDragColSize( True )
		self.ClientStatsGrid.SetColLabelSize( 30 )
		self.ClientStatsGrid.SetColLabelValue( 0, u"Statistic" )
		self.ClientStatsGrid.SetColLabelValue( 1, u"Value" )
		self.ClientStatsGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.ClientStatsGrid.EnableDragRowSize( True )
		self.ClientStatsGrid.SetRowLabelSize( 0 )
		self.ClientStatsGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.ClientStatsGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer49.Add( self.ClientStatsGrid, 1, wx.ALL|wx.EXPAND, 5 )

		self.ClientStatsGameGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.ClientStatsGameGrid.CreateGrid( 0, 4 )
		self.ClientStatsGameGrid.EnableEditing( False )
		self.ClientStatsGameGrid.EnableGridLines( True )
		self.ClientStatsGameGrid.EnableDragGridSize( False )
		self.ClientStatsGameGrid.SetMargins( 0, 0 )

		# Columns
		self.ClientStatsGameGrid.AutoSizeColumns()
		self.ClientStatsGameGrid.EnableDragColMove( False )
		self.ClientStatsGameGrid.EnableDragColSize( True )
		self.ClientStatsGameGrid.SetColLabelSize( 30 )
		self.ClientStatsGameGrid.SetColLabelValue( 0, u"System" )
		self.ClientStatsGameGrid.SetColLabelValue( 1, u"Game" )
		self.ClientStatsGameGrid.SetColLabelValue( 2, u"Times Played" )
		self.ClientStatsGameGrid.SetColLabelValue( 3, u"Time Played" )
		self.ClientStatsGameGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.ClientStatsGameGrid.EnableDragRowSize( True )
		self.ClientStatsGameGrid.SetRowLabelSize( 0 )
		self.ClientStatsGameGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.ClientStatsGameGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer49.Add( self.ClientStatsGameGrid, 2, wx.ALL|wx.EXPAND, 5 )

		m_sdbSizer5 = wx.StdDialogButtonSizer()
		self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
		m_sdbSizer5.Realize();
		bSizer49.Add( m_sdbSizer5, 0, wx.EXPAND, 5 )

		self.SetSizer( bSizer49 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnClientStatsDialogInit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClientStatsDialogInit( self, event ):
		event.Skip()


