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
## Class FriendBlockTemplate
###########################################################################

class FriendBlockTemplate ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Friend/Block List", pos = wx.DefaultPosition, size = wx.Size( 339,433 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel42 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer49 = wx.BoxSizer( wx.VERTICAL )

		friendblock_friend_listboxChoices = []
		self.friendblock_friend_listbox = wx.ListBox( self.m_panel42, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, friendblock_friend_listboxChoices, wx.LB_MULTIPLE )
		self.m_menu10 = wx.Menu()
		self.friendblock_remove_friend_menuItem = wx.MenuItem( self.m_menu10, wx.ID_ANY, u"Remove From Friend List", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu10.AppendItem( self.friendblock_remove_friend_menuItem )

		self.friendblock_friend_listbox.Bind( wx.EVT_RIGHT_DOWN, self.friendblock_friend_listboxOnContextMenu )

		bSizer49.Add( self.friendblock_friend_listbox, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel42.SetSizer( bSizer49 )
		self.m_panel42.Layout()
		bSizer49.Fit( self.m_panel42 )
		self.m_notebook5.AddPage( self.m_panel42, u"Friend(s)", True )
		self.m_panel43 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer50 = wx.BoxSizer( wx.VERTICAL )

		friendblock_block_listboxChoices = []
		self.friendblock_block_listbox = wx.ListBox( self.m_panel43, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, friendblock_block_listboxChoices, wx.LB_MULTIPLE )
		self.m_menu11 = wx.Menu()
		self.friendblock_remove_block_menuItem = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"Remove From Block List", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.AppendItem( self.friendblock_remove_block_menuItem )

		self.friendblock_block_listbox.Bind( wx.EVT_RIGHT_DOWN, self.friendblock_block_listboxOnContextMenu )

		bSizer50.Add( self.friendblock_block_listbox, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel43.SetSizer( bSizer50 )
		self.m_panel43.Layout()
		bSizer50.Fit( self.m_panel43 )
		self.m_notebook5.AddPage( self.m_panel43, u"Block(s)", False )

		bSizer48.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )

		self.SetSizer( bSizer48 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnFriendBlockInit )
		self.Bind( wx.EVT_MENU, self.OnFriendBlockRemoveFriendMenuItem, id = self.friendblock_remove_friend_menuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFriendBlockRemoveBlockMenuItem, id = self.friendblock_remove_block_menuItem.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnFriendBlockInit( self, event ):
		event.Skip()

	def OnFriendBlockRemoveFriendMenuItem( self, event ):
		event.Skip()

	def OnFriendBlockRemoveBlockMenuItem( self, event ):
		event.Skip()

	def friendblock_friend_listboxOnContextMenu( self, event ):
		self.friendblock_friend_listbox.PopupMenu( self.m_menu10, event.GetPosition() )

	def friendblock_block_listboxOnContextMenu( self, event ):
		self.friendblock_block_listbox.PopupMenu( self.m_menu11, event.GetPosition() )


