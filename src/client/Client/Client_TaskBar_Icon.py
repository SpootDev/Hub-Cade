from Client_TaskBarIconBase import *

# import globals
import Client_GlobalData

class MAMEHubTaskBarIcon(TaskBarIconBase):
    """
    Taskbar Icon Demo
    """
    def __init__(self, parent):
        TaskBarIconBase.__init__(self)

        self.parent = parent
        # Left click show the xp balloon
        self.Bind(wx.EVT_TASKBAR_LEFT_UP, self.showParent)
        # Right click quits the application
        self.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.showMenu)
        #self.updateIcon()

        # build the menu that we'll show when someone right-clicks
        self.menu = wx.Menu() # the menu object

        self.menu.Append(101, 'Show') # Resume
        wx.EVT_MENU(self, 101, self.showParent) # Bind a function to it

        self.menu.AppendSeparator() # Separator

        self.menu.Append(102, 'Exit') # Close
        wx.EVT_MENU(self, 102, self.onClose) # Bind a function to it

    def showParent(self,evt):
        print 'BRING BACK PARENT'
        mainFrame = Client_GlobalData.app.mainFrame
        if mainFrame.IsIconized():
            mainFrame.Iconize(False)
        if not mainFrame.IsShown():
            mainFrame.Show(True)
            mainFrame.Raise()
        #self.parent.Show(True)
        #self.parent.Iconize(False)
        #self.parent.Raise()
        #if self.IsIconInstalled():
            #self.RemoveIcon()

    def showMenu(self, event):
        self.PopupMenu(self.menu) # show the popup menu

    def onClose(self, evt):
        """
        Right click: Quit the app
        """
        Client_GlobalData.app.mainFrame.closeFrame()

    def onShowBalloonTip(self, evt):
        """
        Left click: show the balloon
        """
        self.ShowBalloonTip("TITLE", "MESSAGE")
        self.SetIcon(self.parent.icon)
        #evt.Skip()

    def updateIcon(self):
        """
        Updates icon (show/hide)
        """
        if self.IsIconInstalled():
            self.RemoveIcon()
        else:
            self.SetIcon(self.parent.icon)