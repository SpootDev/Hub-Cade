# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 10 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class BanDialogTemplate
###########################################################################

class BanDialogTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ban List", pos = wx.DefaultPosition, size = wx.Size( 677,640 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bandialog_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.ban_dialog_top_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		ban_dialog_top_panel_sizer = wx.BoxSizer( wx.VERTICAL )

		self.ban_dialog_ban_grid = wx.grid.Grid( self.ban_dialog_top_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.ban_dialog_ban_grid.CreateGrid( 0, 6 )
		self.ban_dialog_ban_grid.EnableEditing( True )
		self.ban_dialog_ban_grid.EnableGridLines( True )
		self.ban_dialog_ban_grid.EnableDragGridSize( False )
		self.ban_dialog_ban_grid.SetMargins( 0, 0 )

		# Columns
		self.ban_dialog_ban_grid.AutoSizeColumns()
		self.ban_dialog_ban_grid.EnableDragColMove( False )
		self.ban_dialog_ban_grid.EnableDragColSize( True )
		self.ban_dialog_ban_grid.SetColLabelSize( 30 )
		self.ban_dialog_ban_grid.SetColLabelValue( 0, u"User" )
		self.ban_dialog_ban_grid.SetColLabelValue( 1, u"Ban Time" )
		self.ban_dialog_ban_grid.SetColLabelValue( 2, u"Days" )
		self.ban_dialog_ban_grid.SetColLabelValue( 3, u"Time Left" )
		self.ban_dialog_ban_grid.SetColLabelValue( 4, u"IP Addr" )
		self.ban_dialog_ban_grid.SetColLabelValue( 5, u"Email Address" )
		self.ban_dialog_ban_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.ban_dialog_ban_grid.EnableDragRowSize( True )
		self.ban_dialog_ban_grid.SetRowLabelSize( 80 )
		self.ban_dialog_ban_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.ban_dialog_ban_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		ban_dialog_top_panel_sizer.Add( self.ban_dialog_ban_grid, 1, wx.ALL|wx.EXPAND, 5 )


		self.ban_dialog_top_panel.SetSizer( ban_dialog_top_panel_sizer )
		self.ban_dialog_top_panel.Layout()
		ban_dialog_top_panel_sizer.Fit( self.ban_dialog_top_panel )
		bandialog_main_sizer.Add( self.ban_dialog_top_panel, 1, wx.EXPAND |wx.ALL, 5 )

		self.ban_dialog_bottom_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		ban_dialog_bottom_panel_sizer = wx.BoxSizer( wx.HORIZONTAL )

		self.ban_dialog_remove_ban_button = wx.Button( self.ban_dialog_bottom_panel, wx.ID_ANY, u"Remove Ban", wx.DefaultPosition, wx.DefaultSize, 0 )
		ban_dialog_bottom_panel_sizer.Add( self.ban_dialog_remove_ban_button, 1, wx.ALL|wx.EXPAND, 5 )

		self.ban_dialog_upgrade_ban_button = wx.Button( self.ban_dialog_bottom_panel, wx.ID_ANY, u"Upgrade Ban", wx.DefaultPosition, wx.DefaultSize, 0 )
		ban_dialog_bottom_panel_sizer.Add( self.ban_dialog_upgrade_ban_button, 1, wx.ALL, 5 )


		self.ban_dialog_bottom_panel.SetSizer( ban_dialog_bottom_panel_sizer )
		self.ban_dialog_bottom_panel.Layout()
		ban_dialog_bottom_panel_sizer.Fit( self.ban_dialog_bottom_panel )
		bandialog_main_sizer.Add( self.ban_dialog_bottom_panel, 0, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bandialog_main_sizer )
		self.Layout()

		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.initBanDialog )
		self.ban_dialog_remove_ban_button.Bind( wx.EVT_BUTTON, self.OnBanDialog_Remove_Ban_Button )
		self.ban_dialog_upgrade_ban_button.Bind( wx.EVT_BUTTON, self.OnBanDialog_Upgrade_Ban_Button )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def initBanDialog( self, event ):
		event.Skip()

	def OnBanDialog_Remove_Ban_Button( self, event ):
		event.Skip()

	def OnBanDialog_Upgrade_Ban_Button( self, event ):
		event.Skip()


