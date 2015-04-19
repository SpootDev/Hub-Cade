# import globals
import Client_GlobalData

from Client_Template_Chat_View import *
from sqlite3 import *

class ChatViewDialog ( ChatViewTemplate ):
    # Virtual event handlers, overide them in your derived class
    def OnChatViewDialogInit( self, event ):
        Client_GlobalData.curs_chat.execute("select chat_user from chat_log group by chat_user order by chat_user")
        for sql_row in Client_GlobalData.curs_chat:
            self.chatview_checklistbox.Append(sql_row[0])
        event.Skip()

    def OnChatViewCalendarChange( self, event ):
        date_to_use = str(self.chatview_calendar.GetDate().Format("%Y-%m-%d"))
        sql_statement = "select chat_time,chat_user,chat_text from chat_log where chat_time >= \"" + date_to_use + " 00:00:00\" and chat_time <= \"" + date_to_use + " 23:59:59\""
        # find selected users (if any)
        first_rec= True
        for index in range(0,self.chatview_checklistbox.Count - 1):
            if self.chatview_checklistbox.IsChecked(index) == True:
                if first_rec == True:
                    sql_statement = sql_statement + " and chat_user in ("
                    first_rec = False
                sql_statement = sql_statement + "\"" + self.chatview_checklistbox.GetString(index) + "\","
        if first_rec == False:
            sql_statement = sql_statement[:-1] + ")"
        sql_statement = sql_statement + " order by chat_time"
        #print "date sql:",sql_statement
        Client_GlobalData.curs_chat.execute(sql_statement)
        self.chatview_grid.BeginBatch()
        # remove all rows if required
        if self.chatview_grid.GetNumberRows() > 0:
            self.chatview_grid.DeleteRows(0,self.chatview_grid.GetNumberRows())
        for sql_row in Client_GlobalData.curs_chat:
            self.chatview_grid.AppendRows(1)
            self.chatview_grid.SetCellValue((self.chatview_grid.GetNumberRows() - 1),0,sql_row[0])
            self.chatview_grid.SetCellValue((self.chatview_grid.GetNumberRows() - 1),1,sql_row[1])
            self.chatview_grid.SetCellValue((self.chatview_grid.GetNumberRows() - 1),2,sql_row[2])
        self.chatview_grid.AutoSizeColumns()
        self.chatview_grid.EndBatch()
        event.Skip()

    def OnChatViewAllButton( self, event ):
        for index in range(0,self.chatview_checklistbox.Count - 1):
            self.chatview_checklistbox.Check(index,True)
        event.Skip()

    def OnChatViewNoneButton( self, event ):
        for index in range(0,self.chatview_checklistbox.Count - 1):
            self.chatview_checklistbox.Check(index,False)
        event.Skip()