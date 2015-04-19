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
## Class TopTenTemplate
###########################################################################

class TopTenTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hub!Cade Top 10", pos = wx.DefaultPosition, size = wx.Size( 755,453 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel48 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer53 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer40 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel48, wx.ID_ANY, u"Top 10 by Times Played" ), wx.VERTICAL )

		self.top10grid_times_played = wx.grid.Grid( self.m_panel48, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.top10grid_times_played.CreateGrid( 0, 3 )
		self.top10grid_times_played.EnableEditing( True )
		self.top10grid_times_played.EnableGridLines( True )
		self.top10grid_times_played.EnableDragGridSize( False )
		self.top10grid_times_played.SetMargins( 0, 0 )

		# Columns
		self.top10grid_times_played.SetColSize( 0, 80 )
		self.top10grid_times_played.SetColSize( 1, 80 )
		self.top10grid_times_played.SetColSize( 2, 100 )
		self.top10grid_times_played.AutoSizeColumns()
		self.top10grid_times_played.EnableDragColMove( False )
		self.top10grid_times_played.EnableDragColSize( True )
		self.top10grid_times_played.SetColLabelSize( 30 )
		self.top10grid_times_played.SetColLabelValue( 0, u"Game" )
		self.top10grid_times_played.SetColLabelValue( 1, u"Times Played" )
		self.top10grid_times_played.SetColLabelValue( 2, u"Total Playtime" )
		self.top10grid_times_played.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.top10grid_times_played.AutoSizeRows()
		self.top10grid_times_played.EnableDragRowSize( True )
		self.top10grid_times_played.SetRowLabelSize( 30 )
		self.top10grid_times_played.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.top10grid_times_played.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer40.Add( self.top10grid_times_played, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( sbSizer40, 1, wx.EXPAND, 5 )

		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel48, wx.ID_ANY, u"Top 10 by Total Playtime" ), wx.VERTICAL )

		self.top10grid_total_playtime = wx.grid.Grid( self.m_panel48, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.top10grid_total_playtime.CreateGrid( 0, 3 )
		self.top10grid_total_playtime.EnableEditing( True )
		self.top10grid_total_playtime.EnableGridLines( True )
		self.top10grid_total_playtime.EnableDragGridSize( False )
		self.top10grid_total_playtime.SetMargins( 0, 0 )

		# Columns
		self.top10grid_total_playtime.AutoSizeColumns()
		self.top10grid_total_playtime.EnableDragColMove( False )
		self.top10grid_total_playtime.EnableDragColSize( True )
		self.top10grid_total_playtime.SetColLabelSize( 30 )
		self.top10grid_total_playtime.SetColLabelValue( 0, u"Game" )
		self.top10grid_total_playtime.SetColLabelValue( 1, u"Times Played" )
		self.top10grid_total_playtime.SetColLabelValue( 2, u"Total Playtime" )
		self.top10grid_total_playtime.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.top10grid_total_playtime.AutoSizeRows()
		self.top10grid_total_playtime.EnableDragRowSize( True )
		self.top10grid_total_playtime.SetRowLabelSize( 30 )
		self.top10grid_total_playtime.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.top10grid_total_playtime.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer41.Add( self.top10grid_total_playtime, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( sbSizer41, 1, wx.EXPAND, 5 )


		self.m_panel48.SetSizer( bSizer53 )
		self.m_panel48.Layout()
		bSizer53.Fit( self.m_panel48 )
		bSizer52.Add( self.m_panel48, 1, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer8 = wx.StdDialogButtonSizer()
		self.m_sdbSizer8OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer8.AddButton( self.m_sdbSizer8OK )
		m_sdbSizer8.Realize();

		bSizer52.Add( m_sdbSizer8, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer52 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnTop10Init )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnTop10Init( self, event ):
		event.Skip()


