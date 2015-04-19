# import python mods
import os

# import globals
import Client_GlobalData

# send requested dip settings
def SendDIPSettings():
    file_name = "../cfg/" + blahgamefilenamethingie
    if os.path.exists(file_name):
        dips_data = None
        file_pointer = open(file_name, 'r')
        for file_line in file_pointer:
            if file_line.find("type=\"DIPSWITCH\"") > 0:
                dips_data += file_line
            elif file_line.find("</input>") > 0:
                break
        if len(dips_data) == 0:
            dips_data = "DEFAULT"
        Client_GlobalData.networkProtocol.sendString("RECEIVE_DIPS " + dips_data)
    else:
        Client_GlobalData.networkProtocol.sendString("RECEIVE_DIPS DEFAULT")

# receive requested dip settings
def ReceiveDIPSettings(dip_data):
    if dip_data == "DEFAULT":
        # drop out if not updated from default
        pass
    else:
        if os.path.exists("../cfg/" + blahgamefilenamethingie):
            pass
        else:
            pass