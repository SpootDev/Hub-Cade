# import globals
import Client_GlobalData
import Client_Network

class DatabaseClient():
    def __init__(self):
        self.players = {}
        self.games = {}
        self.gameInstances = {}
        self.playerLFGs = {}

    def createPlayer(self,username,password,email):
        Client_GlobalData.networkProtocol.sendString("CREATE_PLAYER "+username+" "+password+" "+email)

    def getPlayerFromName(self,username):
        for player in self.players.itervalues():
            if player.username == username.encode("utf8"):
                return player
        return None

    def checkUsernamePassword(self,username,password):
        Client_GlobalData.networkProtocol.sendString("VALIDATE_PASSWORD "+username+" "+password+" "+str(Client_GlobalData.selfPort)+" "+str(Client_GlobalData.computer_os))

    def changePlayerStatus(self,newStatus,playingGameInstanceID):
        Client_GlobalData.networkProtocol.sendString("CHANGE_STATUS "+str(newStatus)+' '+str(playingGameInstanceID))

    def createGameInstance(self,db_game_id,hostID,maxPlayers,maxObservers):
        Client_GlobalData.networkProtocol.sendString("CREATE_GAME_INSTANCE "+db_game_id+" "+str(hostID)+" "+str(maxPlayers)+" "+str(maxObservers))

    def getGameInstanceWithHostID(self,hostID):
        for gameInstance in self.gameInstances.itervalues():
            if gameInstance.hostID == hostID:
                return gameInstance
        return None

    def getGameInstanceFromName(self,name):
        for gameInstance in self.gameInstances.itervalues():
            if gameInstance.gameName == name:
                return gameInstance
        return None

    def getGameInstanceFromHostName(self,name):
        for gameInstance in self.gameInstances.itervalues():
            #print "huh",name,gameInstance.host_name
            if Client_GlobalData.database.getNumPlayersForGameInstance(gameInstance.ID) and gameInstance.host_name == name:
                return gameInstance
        return None

    def removeGameInstance(self):
        # don't need to delete from dict as it's being deleted in the network code
        Client_GlobalData.networkProtocol.sendString("REMOVE_GAME_INSTANCE")

    def getNumPlayersForGameInstance(self,gameInstanceID):
        numplayers=0
        for player in self.players.itervalues():
            #print "wtf",player.playingGameInstanceID,gameInstanceID
            if player.playingGameInstanceID == gameInstanceID:
                numplayers += 1
        return numplayers

    def setLFG(self,newLFG):
        Client_GlobalData.networkProtocol.sendString("CHANGE_LFG "+newLFG)

    def getAutocompleteName(self,partialName):
        for player in self.players.itervalues():
            if player.status == Player.STATUS_OFFLINE: continue
            if len(player.username)>len(partialName) and player.username[0:len(partialName)].upper()==partialName.upper():
                return player.username
        return partialName

class FlatObject(object):
    def __cmp__(self,other):
        return self.__dict__.__cmp__(other.__dict__)

class GameInstance(FlatObject):
    def __init__(self,ID,db_game_id,hostID,maxPlayers,maxObservers,locked,time_started,host_name):
        self.ID,self.db_game_id,self.hostID,self.maxPlayers,self.maxObservers,self.locked,self.time_started,self.host_name = ID,db_game_id,hostID,maxPlayers,maxObservers,locked,time_started,host_name

class Game(FlatObject):
    def __init__(self,ID,filename,description):
        self.ID,self.filename,self.description = ID,filename,description

class Player(FlatObject):
    STATUS_LOBBY=1
    STATUS_PLAYING=2
    STATUS_OFFLINE=3

    def __init__(self):
        self.IPAddress = None
        self.port = 5805
        self.status = Player.STATUS_LOBBY
        self.playingGameInstanceID = -1
        self.LFG = ""
        self.friends = ""
        self.AFK = False
        self.OperatingSystem = 0
        self.Country = None
        self.Is_Admin = None

    def create(self,ID,username,password,email):
        self.ID,self.username,self.password,self.email = ID,username,password,email
