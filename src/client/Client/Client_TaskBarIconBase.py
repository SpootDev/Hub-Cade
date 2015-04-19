"""
A Taskbar Icon with xp balloon tooltip support
"""

import os
import wx

import Client_GlobalData

if os.name == 'nt':
    import win32gui

class TaskBarIconBase(wx.TaskBarIcon):
    """
    Base Taskbar Icon Class
    Note: self.icon must be defined in the taskbar icon parent.
    """
    def __init__(self):
        wx.TaskBarIcon.__init__(self)

    def ShowBalloonTip(self, title, msg):
        """
        Show Balloon tooltip
         @param title The title of the balloon
         @param msg   The tooltip message
        """
        if os.name == 'nt':
            try:
                self.SetBalloonTip(Client_GlobalData.app.mainFrame.icon.GetHandle(), title, msg)
            except Exception, e:
                print e

    def SetBalloonTip(self, hicon, title, msg):
        """
        Don't call this method, call ShowBalloonTip instead
        """
        lpdata = (self.GetIconHandle(),
                  99,
                  win32gui.NIF_MESSAGE | win32gui.NIF_ICON | win32gui.NIF_INFO,
                  0,
                  hicon,
                  '', msg, 0, title, win32gui.NIIF_INFO)
        #win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, lpdata)

    def GetIconHandle(self):
        """
        Find the icon window.
        this is ugly but for now there is no way
        to find this window directly from wx
        """
        if not hasattr(self, "_chwnd"):
            try:
                for handle in wx.GetTopLevelWindows():
                    handle = handle.GetHandle()
                    if len(win32gui.GetWindowText(handle)) == 0 and \
                       win32gui.GetWindowRect(handle) == (0,0,400,250):
                        self._chwnd = handle
                        break
                if not hasattr(self, "_chwnd"):
                    print 'no icon window'
                    raise Exception
            except:
                raise Exception, "Icon window not found"
        return self._chwnd
