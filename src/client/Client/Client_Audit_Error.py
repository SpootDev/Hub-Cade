# import globals
import Client_GlobalData

# import templates
from Client_Template_Audit_Error import *

class AuditErrorDialog ( AuditErrorTemplate ):

    def OnAuditErrorInit( self, event ):
        self.audit_skipped_grid.Freeze()
        for x in xrange(0,len(Client_GlobalData.skipped_files)):
            self.audit_skipped_grid.AppendRows(1)
            self.audit_skipped_grid.SetCellValue(x, 0, Client_GlobalData.skipped_files[x].rsplit("|",1)[0])  # rom
            self.audit_skipped_grid.SetCellValue(x, 1, Client_GlobalData.skipped_files[x].rsplit("|",1)[1])  # reason
        self.audit_skipped_grid.AutoSizeColumns(True)
        self.audit_skipped_grid.AutoSizeRows(True)
        self.audit_skipped_grid.Thaw()
