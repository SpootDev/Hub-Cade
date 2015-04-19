# import python mods
import os,sys,socket,platform
##import pickle
sys.path.append('../Common')

# import globals
import Client_GlobalData
import Client_GlobalData_Config

# import templates
from Client_Template_Program_Entry import *

# import code
from Client_Network import *
import Email_Verify

# import twisted files that are required
import twisted.protocols.basic
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import ssl, reactor
from twisted.protocols.basic import Int32StringReceiver

class ProgramEntryDialog ( ProgramEntryTemplate ):
    def initDialog( self, event ):
        self.connecting = False
        self.logging = False
        if os.path.isfile('dd.dat'):
            Client_GlobalData.app.entryDialog.rememberPasswordCheckBox.SetValue(True)
            f = bz2.BZ2File('dd.dat','r')
            userPass = f.read().split()
            Client_GlobalData.app.entryDialog.usernameText.SetValue(userPass[0])
            Client_GlobalData.app.entryDialog.passwordText.SetValue(userPass[1])
            Client_GlobalData.app.entryDialog.portNumberSpinner.SetValue(int(userPass[2]))
            f.close()
        event.Skip()

    def login( self, event ):
        if Client_GlobalData.Connected_Status == True:
            if self.logging: return
            self.logging = True
            if( \
            self.usernameText.GetLineText(0).find(' ')!=-1 or \
            self.passwordText.GetLineText(0).find(' ')!=-1 \
            ):
                mdial = wx.MessageDialog(None, 'Sorry, spaces are not allowed.', 'Spaces not allowed', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
            elif len(self.usernameText.GetLineText(0))==0 or len(self.passwordText.GetLineText(0))==0:
                mdial = wx.MessageDialog(None, 'Please fill out all fields.', 'Fill out all data', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
            else:
                Client_GlobalData.database.checkUsernamePassword(
                self.usernameText.GetLineText(0).encode("utf8"),
                self.passwordText.GetLineText(0).encode("utf8")
                )
            self.logging = False
        else:
            Client_GlobalData.playerName = self.usernameText.GetLineText(0).encode("utf8")
            Client_GlobalData.type_of_call = "login"
            self.connect(self)

    def emailPassword( self, event ):
        if Client_GlobalData.Connected_Status == True:
            if(self.usernameText.GetLineText(0).find(' ')!=-1):
                wx.MessageBox("Sorry, spaces are not allowed","Spaces not allowed")
            elif len(self.usernameText.GetLineText(0))==0:
                wx.MessageBox("Please fill out username","Fill out username")
            else:
                Client_GlobalData.networkProtocol.sendString("EMAIL_PASSWORD "+self.usernameText.GetLineText(0).encode("utf8"))
        else:
            Client_GlobalData.type_of_call = "email_password"
            self.connect(self)

    def registerAccount( self, event ):
        if Client_GlobalData.Connected_Status == True:
            if self.logging: return
            self.logging = True
            if( \
            self.usernameText.GetLineText(0).find(' ')!=-1 or \
            self.passwordText.GetLineText(0).find(' ')!=-1 or \
            self.emailText.GetLineText(0).find(' ')!=-1 \
##            self.emailRepeatText.GetLineText(0).find(' ')!=-1 \
            ):
                mdial = wx.MessageDialog(None, 'Sorry, spaces are not allowed.', 'Spaces not allowed', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
##            elif(self.emailText.GetLineText(0)!=self.emailRepeatText.GetLineText(0)):
##                mdial = wx.MessageDialog(None, 'Error, the two email fields must match.', 'Email Matching', wx.OK | wx.ICON_ERROR)
##                mdial.ShowModal()
##                mdial.Destroy()
            elif len(self.usernameText.GetLineText(0))==0 or len(self.passwordText.GetLineText(0))==0 or len(self.emailText.GetLineText(0))==0:
                mdial = wx.MessageDialog(None, 'Please fill out all fields.', 'Fill out all data', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
            elif Email_Verify.Check_Email(self.emailText.GetLineText(0)) == False:
                mdial = wx.MessageDialog(None, 'Invalid email address format.', 'Email Error', wx.OK | wx.ICON_EXCLAMATION)
                mdial.ShowModal()
                mdial.Destroy()
            else:
                Client_GlobalData.database.createPlayer(
                self.usernameText.GetLineText(0).encode("utf8"),
                self.passwordText.GetLineText(0).encode("utf8"),
                self.emailText.GetLineText(0).encode("utf8")
                )
            self.logging = False
        else:
            Client_GlobalData.type_of_call = "register"
            self.connect(self)

    def quit( self, event ):
        Client_GlobalData.app.mainFrame.closeFrame()
        self.Close(True)
        ##pickle.dump(Client_GlobalData.settings,open('settings.dat','wb'))
        sys.exit(0)

    def connect( self, event ):
        if self.connecting: return
        self.connecting = True
        #Client_GlobalData.serverName = self.serverName.GetLineText(0).encode('utf8')
        if platform.node() != "spoot8-PC" and platform.node() != "spootdev-virtual-machine":
            Client_GlobalData.serverName = u'www.spootsworld.com'
        else:
            Client_GlobalData.serverName = u'10.0.0.97'
        Client_GlobalData.selfPort = self.portNumberSpinner.GetValue()

        if Client_GlobalData_Config.use_miniupnpc == True and Client_GlobalData.u is not None:
            try:
                #Try to use upnp to map port
                Client_GlobalData.u.discoverdelay = 2000;
                print 'Discovering... delay=%ums' % Client_GlobalData.u.discoverdelay
                ndevices = Client_GlobalData.u.discover()
                print ndevices, 'device(s) detected'

                # select an igd
                self.mainFrame.u.selectigd()
                # display information about the IGD and the internet connection
                print 'local ip address :', Client_GlobalData.u.lanaddr
                externalipaddress = Client_GlobalData.u.externalipaddress()
                print 'external ip address :', externalipaddress
                print Client_GlobalData.u.statusinfo(), Client_GlobalData.u.connectiontype()

                port = Client_GlobalData.selfPort

                print 'trying to redirect %s port %u TCP => %s port %u TCP' % (externalipaddress, port, Client_GlobalData.u.lanaddr, port)

                b = Client_GlobalData.u.addportmapping(port, 'TCP', u.lanaddr, port,
                                    'HubCade', '')
                if b:
                    print 'Success.'
                else:
                    print 'Failed, hopefully the port is manually mapped.'

                b = Client_GlobalData.u.addportmapping(port, 'UDP', Client_GlobalData.u.lanaddr, port,
                                    'HubCade', '')
                if b:
                    print 'Success.'
                else:
                    print 'Failed, hopefully the port is manually mapped.'
            except:
                print 'miniupnpc port mapping failed.'

        print socket.getaddrinfo(Client_GlobalData.serverName,5804,0,0,socket.SOL_TCP)
        Client_GlobalData.masterServerIP = socket.getaddrinfo(Client_GlobalData.serverName,5804,0,0,socket.SOL_TCP)[0][4][0]

        while Client_GlobalData.masterServerIP == None:
            reactor.runUntilCurrent()
            reactor.doIteration(0)
        #reactor.connectTCP(Client_GlobalData.masterServerIP, 5804, Client_GlobalData.app.clientFactory)
        reactor.connectSSL(Client_GlobalData.masterServerIP, 5804, Client_GlobalData.app.clientFactory, ssl.ClientContextFactory( ))

        while Client_GlobalData.app.clientFactory.failed==False and ( \
        Client_GlobalData.app.clientFactory.protocol is None or \
        Client_GlobalData.app.clientFactory.protocol.connStatus==ClientProtocol.STARTED or \
        Client_GlobalData.app.clientFactory.protocol.connStatus==ClientProtocol.CHECKING_PORT
        ):
            reactor.runUntilCurrent()
            reactor.doIteration(0)

        if hasattr(Client_GlobalData.app.clientFactory.protocol, 'connStatus'):
            Client_GlobalData.Connected_Status = True
            if Client_GlobalData.type_of_call == "login":
                self.login(self)
            elif Client_GlobalData.type_of_call == "email_password":
                self.emailPassword(self)
            elif Client_GlobalData.type_of_call == "register":
                self.registerAccount(self)

            self.connecting = False
            self.Close(True)
        else:
            Client_GlobalData.Connected_Status = False
            mdial = wx.MessageDialog(None, 'The Hub!Cade server is not accepting connections at this time.', 'Cannot connect to server', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
