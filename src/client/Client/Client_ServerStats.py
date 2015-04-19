# import localization
import locale
locale.setlocale(locale.LC_ALL, '')

# import mods
import time

# import globals
import Client_GlobalData

from Client_Template_ServerStats import *

class ServerStatsDialog ( ServerStatsTemplate ):

    def OnServerStatsInitDialog( self, event ):
        ndx = 0
        new_row = True
        self.ServerStatsGrid.Freeze()
        for field_data in Client_GlobalData.generic_string.split(","):
            if new_row == True:
                self.ServerStatsGrid.AppendRows(1)
                self.ServerStatsGrid.SetCellValue(ndx, 0, field_data.decode("utf8"))  # stat
                new_row = False
            else:
                if self.ServerStatsGrid.GetCellValue(ndx,0) == "Server Uptime" or self.ServerStatsGrid.GetCellValue(ndx,0) == "Total Time Played":
                    if self.ServerStatsGrid.GetCellValue(ndx,0) == "Server Uptime":
                        seconds_running = float(time.mktime(time.gmtime()) - float(field_data.decode("utf8")))
                    elif self.ServerStatsGrid.GetCellValue(ndx,0) == "Total Time Played":
                        seconds_running = float(field_data.decode("utf8"))
                    if seconds_running < 31104000: # year
                        if seconds_running < 2592000: # month
                            if seconds_running < 86400: # day
                                self.ServerStatsGrid.SetCellValue(ndx, 1, time.strftime('%H:%M:%S', time.gmtime(seconds_running)))
                            else:
                                self.ServerStatsGrid.SetCellValue(ndx, 1, time.strftime('%d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                        else:
                            self.ServerStatsGrid.SetCellValue(ndx, 1, time.strftime('%m Month(s) %d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                    else:
                        self.ServerStatsGrid.SetCellValue(ndx, 1, time.strftime('%y Year(s) %m Month(s) %d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                else:
                    self.ServerStatsGrid.SetCellValue(ndx, 1, locale.format("%.0f", float(field_data.decode("utf8")), 1))  # value
                ndx += 1
                new_row = True
        self.ServerStatsGrid.AutoSizeColumns(True)
        self.ServerStatsGrid.AutoSizeRows(True)
        self.ServerStatsGrid.Thaw()
        event.Skip()
