# import localization
import locale
locale.setlocale(locale.LC_ALL, '')

# import mods
import time

# import globals
import Client_GlobalData

#import template
from Client_Template_Top10 import *

# import code
import Client_Database

class TopTenDialog ( TopTenTemplate ):

    def OnTop10Init( self, event ):
        # times played top 10
        field_num = 0
        self.top10grid_times_played.Freeze()
        split_data = Client_GlobalData.generic_string.split("|")[0:30]
        for field_data in split_data:
            field_num += 1
            if field_num == 1:
                self.top10grid_times_played.AppendRows(1)
                self.top10grid_times_played.SetCellValue((self.top10grid_times_played.GetNumberRows() - 1), 0, Client_Database.SQL_Retrieve_Game_Name(field_data.decode("utf8")))  # stat
            elif field_num == 2:
                self.top10grid_times_played.SetCellValue((self.top10grid_times_played.GetNumberRows() - 1), 1, locale.format("%.0f", float(field_data.decode("utf8")), 1))  # value
            elif field_num == 3:
                seconds_running = float(field_data.decode("utf8"))
                if seconds_running < 31104000: # year
                    if seconds_running < 2592000: # month
                        if seconds_running < 86400: # day
                            self.top10grid_times_played.SetCellValue((self.top10grid_times_played.GetNumberRows() - 1), 2, time.strftime('%H:%M:%S', time.gmtime(seconds_running)))
                        else:
                            self.top10grid_times_played.SetCellValue((self.top10grid_times_played.GetNumberRows() - 1), 2, time.strftime('%d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                    else:
                        self.top10grid_times_played.SetCellValue((self.top10grid_times_played.GetNumberRows() - 1), 2, time.strftime('%m Month(s) %d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                else:
                    self.top10grid_times_played.SetCellValue((self.top10grid_times_played.GetNumberRows() - 1), 2, time.strftime('%y Year(s) %m Month(s) %d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                field_num = 0
        self.top10grid_times_played.AutoSizeColumns(True)
        self.top10grid_times_played.AutoSizeRows(True)
        self.top10grid_times_played.Thaw()
        # time played time top 10
        field_num = 0
        self.top10grid_total_playtime.Freeze()
        split_data = Client_GlobalData.generic_string.split("|")[30:60]
        for field_data in split_data:
            field_num += 1
            if field_num == 1:
                self.top10grid_total_playtime.AppendRows(1)
                self.top10grid_total_playtime.SetCellValue((self.top10grid_total_playtime.GetNumberRows() - 1), 0, Client_Database.SQL_Retrieve_Game_Name(field_data.decode("utf8")))  # stat
            elif field_num == 2:
                self.top10grid_total_playtime.SetCellValue((self.top10grid_total_playtime.GetNumberRows() - 1), 1, locale.format("%.0f", float(field_data.decode("utf8")), 1))  # value
            elif field_num == 3:
                seconds_running = float(field_data.decode("utf8"))
                if seconds_running < 31104000: # year
                    if seconds_running < 2592000: # month
                        if seconds_running < 86400: # day
                            self.top10grid_total_playtime.SetCellValue((self.top10grid_total_playtime.GetNumberRows() - 1), 2, time.strftime('%H:%M:%S', time.gmtime(seconds_running)))
                        else:
                            self.top10grid_total_playtime.SetCellValue((self.top10grid_total_playtime.GetNumberRows() - 1), 2, time.strftime('%d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                    else:
                        self.top10grid_total_playtime.SetCellValue((self.top10grid_total_playtime.GetNumberRows() - 1), 2, time.strftime('%m Month(s) %d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                else:
                    self.top10grid_total_playtime.SetCellValue((self.top10grid_total_playtime.GetNumberRows() - 1), 2, time.strftime('%y Year(s) %m Month(s) %d Day(s) %H:%M:%S', time.gmtime(seconds_running)))
                field_num = 0
        self.top10grid_total_playtime.AutoSizeColumns(True)
        self.top10grid_total_playtime.AutoSizeRows(True)
        self.top10grid_total_playtime.Thaw()
        event.Skip()
