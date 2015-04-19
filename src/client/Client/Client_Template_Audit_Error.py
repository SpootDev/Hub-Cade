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
## Class AuditErrorTemplate
###########################################################################

class AuditErrorTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rom(s) skipped in audit", pos = wx.DefaultPosition, size = wx.Size( 564,425 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.audit_skipped_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.audit_skipped_grid.CreateGrid( 0, 2 )
		self.audit_skipped_grid.EnableEditing( True )
		self.audit_skipped_grid.EnableGridLines( True )
		self.audit_skipped_grid.EnableDragGridSize( False )
		self.audit_skipped_grid.SetMargins( 0, 0 )

		# Columns
		self.audit_skipped_grid.SetColSize( 0, 162 )
		self.audit_skipped_grid.SetColSize( 1, 189 )
		self.audit_skipped_grid.EnableDragColMove( False )
		self.audit_skipped_grid.EnableDragColSize( True )
		self.audit_skipped_grid.SetColLabelSize( 30 )
		self.audit_skipped_grid.SetColLabelValue( 0, u"Rom" )
		self.audit_skipped_grid.SetColLabelValue( 1, u"Reason Skipped" )
		self.audit_skipped_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.audit_skipped_grid.EnableDragRowSize( True )
		self.audit_skipped_grid.SetRowLabelSize( 0 )
		self.audit_skipped_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.audit_skipped_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer51.Add( self.audit_skipped_grid, 1, wx.ALL|wx.EXPAND, 5 )

		m_sdbSizer6 = wx.StdDialogButtonSizer()
		self.m_sdbSizer6OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer6.AddButton( self.m_sdbSizer6OK )
		m_sdbSizer6.Realize();

		bSizer51.Add( m_sdbSizer6, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer51 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnAuditErrorInit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnAuditErrorInit( self, event ):
		event.Skip()


