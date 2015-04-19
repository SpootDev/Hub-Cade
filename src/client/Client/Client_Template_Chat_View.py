# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.calendar
import wx.grid

###########################################################################
## Class ChatViewTemplate
###########################################################################

class ChatViewTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Chat Archive Viewer", pos = wx.DefaultPosition, size = wx.Size( 767,662 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel40 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		self.chatview_calendar = wx.calendar.CalendarCtrl( self.m_panel40, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.calendar.CAL_SHOW_HOLIDAYS )
		bSizer46.Add( self.chatview_calendar, 0, wx.ALL, 5 )

		chatview_checklistboxChoices = []
		self.chatview_checklistbox = wx.CheckListBox( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chatview_checklistboxChoices, 0 )
		self.chatview_checklistbox.SetToolTipString( u"Select user(s) chat to view.  If none selected, all users are viewed." )

		bSizer46.Add( self.chatview_checklistbox, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel42 = wx.Panel( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer48 = wx.BoxSizer( wx.HORIZONTAL )

		self.chatview_all_button = wx.Button( self.m_panel42, wx.ID_ANY, u"All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chatview_all_button.SetToolTipString( u"Select all users" )

		bSizer48.Add( self.chatview_all_button, 0, wx.ALL, 5 )

		self.chatview_none_button = wx.Button( self.m_panel42, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chatview_none_button.SetToolTipString( u"Deselect all users." )

		bSizer48.Add( self.chatview_none_button, 0, wx.ALL, 5 )

		self.m_panel42.SetSizer( bSizer48 )
		self.m_panel42.Layout()
		bSizer48.Fit( self.m_panel42 )
		bSizer46.Add( self.m_panel42, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel40.SetSizer( bSizer46 )
		self.m_panel40.Layout()
		bSizer46.Fit( self.m_panel40 )
		bSizer45.Add( self.m_panel40, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel41 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		self.chatview_grid = wx.grid.Grid( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.chatview_grid.CreateGrid( 0, 3 )
		self.chatview_grid.EnableEditing( True )
		self.chatview_grid.EnableGridLines( True )
		self.chatview_grid.EnableDragGridSize( False )
		self.chatview_grid.SetMargins( 0, 0 )

		# Columns
		self.chatview_grid.AutoSizeColumns()
		self.chatview_grid.EnableDragColMove( False )
		self.chatview_grid.EnableDragColSize( True )
		self.chatview_grid.SetColLabelSize( 30 )
		self.chatview_grid.SetColLabelValue( 0, u"Time" )
		self.chatview_grid.SetColLabelValue( 1, u"User" )
		self.chatview_grid.SetColLabelValue( 2, u"Chat" )
		self.chatview_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Rows
		self.chatview_grid.EnableDragRowSize( True )
		self.chatview_grid.SetRowLabelSize( 80 )
		self.chatview_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

		# Label Appearance

		# Cell Defaults
		self.chatview_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer47.Add( self.chatview_grid, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel41.SetSizer( bSizer47 )
		self.m_panel41.Layout()
		bSizer47.Fit( self.m_panel41 )
		bSizer45.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )

		self.SetSizer( bSizer45 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnChatViewDialogInit )
		self.chatview_calendar.Bind( wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.OnChatViewCalendarChange )
		self.chatview_all_button.Bind( wx.EVT_BUTTON, self.OnChatViewAllButton )
		self.chatview_none_button.Bind( wx.EVT_BUTTON, self.OnChatViewNoneButton )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnChatViewDialogInit( self, event ):
		event.Skip()

	def OnChatViewCalendarChange( self, event ):
		event.Skip()

	def OnChatViewAllButton( self, event ):
		event.Skip()

	def OnChatViewNoneButton( self, event ):
		event.Skip()


