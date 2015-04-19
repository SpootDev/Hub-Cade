# import python mods
import sys,threading,gzip,os,copy,zipfile,zlib,time
from StringIO import StringIO
import multiprocessing
from threading import Thread
from Queue import Queue
import hashlib
SHA1 = hashlib.sha1()

# import compression mods
import pylzma
if str.upper(sys.platform[0:3])=='WIN' \
or str.upper(sys.platform[0:3])=='CYG':
    from py7zlib import Archive7z

import xml,json,glob
from xml.dom import minidom
from xml.parsers import expat
import xml.etree.ElementTree as ET
from xml.dom.minidom import getDOMImplementation

# import built in sqlite3 support
from sqlite3 import *

# import globals
import Client_GlobalData
import Client_GlobalData_Config

lock = threading.Lock()

# store files, zippped and hash globally
files = {}
zippedFiles = {}
hashFileMap = {}

class HashGenerate(Thread):
    def __init__ (self,file_name):
      Thread.__init__(self)
      self.file_name = file_name
      self.hash_result = None

    def get_generated_hash(self):
        return self.hash_result

    def run(self):
        if self.file_name[-3:]=='zip':
##            skip_next = False
##            if Client_GlobalData_Config.skip_mechanical == True:
##                sql_args = self.file_name.rsplit(".",1)[0],1
##                game_curs.execute("select count(*) from games where game_name = ? and is_mech = ?",sql_args)
##                if int(game_curs.fetchone()[0]) > 0:
##                    skip_next = True
##            if skip_next == False:
            #Need to unpack the zip and check all files inside it
            try:
                zip = zipfile.ZipFile(self.file_name,'r')  # issues if u do RB
                for zippedFile in zip.namelist():
                    CRC = zip.getinfo(zippedFile).CRC
                    fileHash = str(hex(CRC))
                    if fileHash[-1]=='L':
                        fileHash = fileHash[:-1]
                    fileHash = fileHash[2:]
                    while(len(fileHash)<8):
                        fileHash = "0"+fileHash
                    # calculate sha1 hash
##                        SHA1 = hashlib.sha1()  # "reset" the sha1 to blank
##                        SHA1.update(zip.read(zippedFile))
##                        sha1_hash_data = SHA1.hexdigest()
                    sha1_hash_data  = "fake"

                    #self.hash_result = self.file_name,fileHash,sha1_hash_data
                    lock.acquire()
                    hashFileMap[fileHash] = zippedFiles[ (fileHash,zippedFile) ] = self.file_name
                    lock.release()
            except:
                lock.acquire()
                Client_GlobalData.skipped_files.append(os.path.normpath(self.file_name) + "|Error reading zip")
                lock.release()
                #print 'ERROR READING',self.file_name
        elif self.file_name[-2:]=='7z':
            #Need to unpack the 7z and check all files inside it
            try:
                fp = open(self.file_name, 'rb')
                archive = Archive7z(fp)
                filenames = archive.getnames()
                for filename in filenames:
                    cf = archive.getmember(filename)
                    #print hex(cf.digest)[2:-1], cf.filename
                    fileHash = str(hex(cf.digest)[2:-1])
                    while(len(fileHash)<8):
                        fileHash = "0"+fileHash
                    # calculate sha1 hash
    ##                        SHA1 = hashlib.sha1()  # "reset" the sha1 to blank
    ##                        SHA1.update(cf.read())
    ##                        sha1_hash_data = SHA1.hexdigest()
                    sha1_hash_data  = "fake"

                    #self.hash_result = self.file_name,fileHash,sha1_hash_data
                    lock.acquire()
                    hashFileMap[fileHash] = zippedFiles[ (fileHash,filename) ] = self.file_name
                    lock.release()
            except:
                lock.acquire()
                Client_GlobalData.skipped_files.append(os.path.normpath(self.file_name) + "|Error reading 7z")
                lock.release()
                #print 'ERROR READING',self.file_name
        else:
            try:
                file_pointer = open(self.file_name,'rb')
                # calc crc32 hash
                CRC = zlib.crc32(file_pointer.read(1024*1024))
                while True:
                    data = file_pointer.read(1024*1024)
                    if len(data)==0:
                        break #Finished reading file
                    CRC = zlib.crc32(data,CRC)
                # calculate sha1 hash
    ##            file_pointer.seek(0, 0);
    ##            SHA1 = hashlib.sha1()  # "reset" the sha1 to blank
    ##            for chunk in iter(lambda: file_pointer.read(128*SHA1.block_size), ''):
    ##                 SHA1.update(chunk)
    ##            sha1_hash_data = SHA1.hexdigest()
                sha1_hash_data  = "fake"

                file_pointer.close()
                CRC = CRC & 0xffffffff
                fileHash = str(hex(CRC))
                if fileHash[-1]=='L':
                    fileHash = fileHash[:-1]
                fileHash = fileHash[2:]
                while(len(fileHash)<8):
                    fileHash = "0"+fileHash
                #self.hash_result = self.file_name,fileHash,sha1_hash_data
                lock.acquire()
                hashFileMap[fileHash] = files[ (fileHash,self.file_name) ] = self.file_name
                lock.release()
            except:
                lock.acquire()
                Client_GlobalData.skipped_files.append(os.path.normpath(self.file_name) + "|Error reading file")
                lock.release()

class HashScanner(object):
    def __init__(self):
        self.percentComplete = 0

    def calc_hash(self,audit_q, files):
        for file in files:
            thread = HashGenerate(file)
            thread.start()
            audit_q.put(thread, True)

    def get_hash_result(self,audit_q, total_files):
        onFile = 0
        lastPercent=0
        Client_GlobalData.audit_on_file = 0
        self.percentComplete = 0
        while Client_GlobalData.audit_on_file < total_files:
            thread = audit_q.get(True)
            thread.join()
            # update percentage
            onFile += 1
            if onFile*100/total_files != lastPercent:
                lastPercent = onFile*100/total_files
                print lastPercent,'% ',
                self.percentComplete = lastPercent
            Client_GlobalData.audit_on_file += 1

    def scan(self,paths):
        # open the db
        game_conn = connect('db/mame_xml.db')
        game_curs = game_conn.cursor()
        # find/count files to scan
        Client_GlobalData.skipped_files = []
        files_to_hash = []
        for path in paths:
            try:
                for file_name in os.listdir(path):
                    if os.path.isfile(os.path.join(path,file_name))==False:
                        continue
                    # skip file names with unicode in them
                    try:
                        file_name.decode('ascii')
                    except UnicodeDecodeError:
                        Client_GlobalData.skipped_files.append(os.path.normpath(path + "/" + file_name) + "|Unicode in name")
                        continue
                    # is file and no unicode add to files to hash
                    # not using join as it does the \\ in windows on the join between path and file
                    files_to_hash.append(os.path.normpath(path + "/" + file_name))
            except:
                pass
        # calculate crc32 and sha1 on all files selected
        files = {}
        zippedFiles = {}
        hashFileMap = {}
        Client_GlobalData.audit_files_to_audit = len(files_to_hash)
        # start the audit threads
        audit_q = Queue(multiprocessing.cpu_count() * 1)
        prod_thread = threading.Thread(target=self.calc_hash, args=(audit_q, files_to_hash))
        cons_thread = threading.Thread(target=self.get_hash_result, args=(audit_q, len(files_to_hash)))
        prod_thread.start()
        cons_thread.start()
        prod_thread.join()
        cons_thread.join()
        # verify all thread/ques are complete
        while not audit_q.empty():
            #print audit_q.get()
            time.sleep(0.05)
        # close the db
        game_curs.close()
        game_conn.close()

class ROMParser(object):
    def __init__(self,files,zippedFiles,hashFileMap,masterFile):
        self.gameName = ''
        self.gameDescription = ''
        self.gameFailed = True
        self.romFileMap = {}
        self.romExtraFilesMap = {}
        self.romDescriptionMap = {}
        self.nextDataIsDescription=False
        self.files = files
        self.zippedFiles = zippedFiles
        self.hashFileMap = hashFileMap
        parser = xml.parsers.expat.ParserCreate()
        parser.StartElementHandler = self.startElement
        parser.CharacterDataHandler = self.elementData
        parser.EndElementHandler = self.endElement
        parser.ParseFile(gzip.GzipFile(masterFile,'rb'))

    def startElement(self, name, attrs):
        if name=='game' or name=='machine':
            self.gameName = attrs['name']
            self.gameFailed = False
            self.goodRoms = 0
            self.badRoms = 0
        elif name=='description':
            self.nextDataIsDescription=True
            self.gameDescription = ''
        elif name=='rom':
            if self.gameFailed==False:
                if 'crc' in attrs:
                    self.goodRoms += 1
                    truehash = attrs['crc']
                    romname = attrs['name']
                    if (truehash,romname) in self.files:
                        self.romFileMap[self.gameName] = romname
                    elif (truehash,romname) in self.zippedFiles:
                        if self.zippedFiles[(truehash,romname)].find(self.gameName + ".") != -1:
                            self.romFileMap[self.gameName] = self.zippedFiles[(truehash,romname)]
                        else:
                            if self.gameName in self.romExtraFilesMap:
                                if self.hashFileMap[truehash] not in self.romExtraFilesMap[self.gameName]:
                                    self.romExtraFilesMap[self.gameName].append(self.hashFileMap[truehash])
                            else:
                                self.romExtraFilesMap[self.gameName] = [self.hashFileMap[truehash]]
                    elif truehash in self.hashFileMap:
                        pass
                    else:
                        self.gameFailed = True
                else:
                    self.badRoms += 1

    def elementData(self,data):
        if self.nextDataIsDescription:
            self.gameDescription += data

    def endElement(self, name):
        if name=='game' or name=='machine':
            #A game passes if it doesn't fail and either has no roms, or has at least one good rom
            if self.gameFailed == False and (self.goodRoms>0 or (self.goodRoms==0 and self.badRoms==0)):
                if self.gameName in self.romFileMap:
                    self.romDescriptionMap[self.gameName] = self.gameDescription
                else:
                    self.romFileMap[self.gameName] = ''
                    self.romDescriptionMap[self.gameName] = self.gameDescription
            else:
                if self.gameName in self.romFileMap:
                    del self.romFileMap[self.gameName]
                if self.gameName in self.romExtraFilesMap:
                    del self.romExtraFilesMap[self.gameName]
        elif name=='description':
            self.nextDataIsDescription=False

class CartParser(object):
    def __init__(self,systemNames,hashFileMap):
        self.cartFileMaps = {}
        self.hashFileMap = hashFileMap
        filesToScan=0
        onFile = 0
        lastPercent=0
        for systemName in systemNames:
            self.cartFileMaps[systemName] = {}
            self.systemName = systemName
            parser = xml.parsers.expat.ParserCreate()
            parser.StartElementHandler = self.startElement
            parser.EndElementHandler = self.endElement
            hashFile = "hash/"+systemName+".hsi"
            if os.path.isfile(hashFile):
                print 'Reading ',hashFile
                parser.ParseFile(open(hashFile,'rb'))
            del self.systemName

    def startElement(self, name, attrs):
        if name=='hash':
            if 'crc32' in attrs:
                truehash = attrs['crc32']
                cartname = attrs['name']
                if truehash in self.hashFileMap:
                    self.cartFileMaps[self.systemName][cartname] = self.hashFileMap[truehash]

    def endElement(self, name):
        pass

class GameAuditer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.romFileMapMAME = {}
        self.romExtraFilesMapMAME = {}
        self.romDescriptionMapMAME = {}
        self.romFileMapMESS = {}
        self.romDescriptionMapMESS = {}
        self.cartFileMaps = {}
        self.baseDirectories = ''
        self.hashScanner = None

    def loadWithVersion(self,fileMask):
        filenames = glob.glob(fileMask)
        inputFile = None
        for filename in filenames:
            if fileMask[0:fileMask.index('*')]+'.dmp' in filename:
                inputFile = open(filename,"rb")
            else:
                os.remove(filename)
        return inputFile

    def load(self):
        if '-nolist' in sys.argv:
            return True
        inputFile = self.loadWithVersion("MAMEFiles*.dmp")
        if inputFile is None: return False
        self.romFileMapMAME = json.loads(inputFile.read())
        inputFile.close()
        inputFile = self.loadWithVersion("MAMEExtraFiles*.dmp")
        if inputFile is None: return False
        self.romExtraFilesMapMAME = json.loads(inputFile.read())
        inputFile.close()
        inputFile = self.loadWithVersion("MESSFiles*.dmp")
        if inputFile is None: return False
        self.romFileMapMESS = json.loads(inputFile.read())
        inputFile.close()
        inputFile = self.loadWithVersion("MAMEDescriptions*.dmp")
        if inputFile is None: return False
        self.romDescriptionMapMAME = json.loads(inputFile.read())
        inputFile.close()
        inputFile = self.loadWithVersion("MESSDescriptions*.dmp")
        if inputFile is None: return False
        self.romDescriptionMapMESS = json.loads(inputFile.read())
        inputFile.close()
        inputFile = self.loadWithVersion("CART*.dmp")
        if inputFile is None: return False
        self.cartFileMaps = json.loads(inputFile.read())
        inputFile.close()
        return True

    def run(self):
        self.audit()

    def audit(self):
        print 'Auditing directories:',self.baseDirectories
        self.romFileMapMAME = {}
        self.romExtraFilesMapMAME = {}
        self.romDescriptionMapMAME = {}
        self.romFileMapMESS = {}
        self.romDescriptionMapMESS = {}
        self.cartFileMaps = {}
        self.hashScanner = HashScanner()
        self.hashScanner.scan(self.baseDirectories)
        self.auditMAME()
        self.auditMESS()
        outputFile = open("MAMEFiles.dmp","wb")
        outputFile.write(json.dumps(self.romFileMapMAME,ensure_ascii=False))
        outputFile.close()
        outputFile = open("MAMEExtraFiles.dmp","wb")
        outputFile.write(json.dumps(self.romExtraFilesMapMAME,ensure_ascii=False))
        outputFile.close()
        outputFile = open("MESSFiles.dmp","wb")
        outputFile.write(json.dumps(self.romFileMapMESS,ensure_ascii=False))
        outputFile.close()
        outputFile = open("MAMEDescriptions.dmp","wb")
        outputFile.write(json.dumps(self.romDescriptionMapMAME,ensure_ascii=False))
        outputFile.close()
        outputFile = open("MESSDescriptions.dmp","wb")
        outputFile.write(json.dumps(self.romDescriptionMapMESS,ensure_ascii=False))
        outputFile.close()
        outputFile = open("CART.dmp","wb")
        outputFile.write(json.dumps(self.cartFileMaps,ensure_ascii=False))
        outputFile.close()

    def auditMAME(self):
        romParser = ROMParser(files,zippedFiles,hashFileMap,"hash/mameROMs.xml.gz")
        self.romFileMapMAME = romParser.romFileMap
        self.romExtraFilesMapMAME = romParser.romExtraFilesMap
        self.romDescriptionMapMAME = romParser.romDescriptionMap

    def auditMESS(self):
        romParser = ROMParser(files,zippedFiles,hashFileMap,"hash/messROMs.xml.gz")
        self.romFileMapMESS = romParser.romFileMap
        self.romDescriptionMapMESS = romParser.romDescriptionMap
        print 'SYSTEMS FOUND:',self.romFileMapMESS.keys()
        cartParser = CartParser(self.romFileMapMESS.keys(),hashFileMap)
        self.cartFileMaps = cartParser.cartFileMaps

    def getNames(self,subString):
        if len(subString)==0:
            #Fast method that doesn't need compare
            gameList = []
            gameList.extend(self.romDescriptionMapMAME.values())
            for systemCartMap in self.cartFileMaps.itervalues():
                gameList.extend(systemCartMap.keys())
            gameList.sort()
            return gameList
        subString = subString.lower()
        gameList = []
        for gameName in self.romDescriptionMapMAME.values():
            if subString in gameName.lower():
                gameList.append(gameName)
        for systemCartMap in self.cartFileMaps.itervalues():
            for gameName in systemCartMap.keys():
                if subString in gameName.lower():
                    gameList.append(gameName)
        gameList.sort()
        return gameList

    def getNamesDict(self,subString):
        if len(subString)==0:
            #Fast method that doesn't need compare
            gameList = {}
            gameList['Arcade'] = copy.deepcopy(self.romDescriptionMapMAME.values())
            gameList['Arcade'].sort()
            for systemName,systemCartMap in self.cartFileMaps.iteritems():
                if len(systemCartMap.keys())>0:
                    gameList[systemName] = copy.deepcopy(systemCartMap.keys())
                    gameList[systemName].sort()
            return gameList
        subString = subString.lower()
        gameList = {}
        for gameName in self.romDescriptionMapMAME.values():
            if subString in gameName.lower():
                if 'Arcade' not in gameList:
                    gameList['Arcade'] = []
                gameList['Arcade'].append(gameName)
        if 'Arcade' in gameList:
            gameList['Arcade'].sort()
        for systemName,systemCartMap in self.cartFileMaps.iteritems():
            for gameName in systemCartMap.keys():
                if subString in gameName.lower():
                    if systemName not in gameList:
                        gameList[systemName] = []
                    gameList[systemName].append(gameName)
            if systemName in gameList:
                gameList[systemName].sort()
        return gameList

    def getRomAndCartFileFromName(self,name):
        for systemName,systemCartMap in self.cartFileMaps.iteritems():
            for romname,file in systemCartMap.iteritems():
                if name == romname:
                    return systemName,file
                if name == romname.replace(' ','_'):
                    return systemName,file
        for romname,description in self.romDescriptionMapMAME.iteritems():
            if name == description:
                print name,description,self.romFileMapMAME[romname]
                return self.romFileMapMAME[romname],""
            if name == description.replace(' ','_'):
                print name,description,self.romFileMapMAME[romname]
                return self.romFileMapMAME[romname],""
        return '',''

    def getAllMAMEFilesFromName(self,name):
        for systemName,systemCartMap in self.cartFileMaps.iteritems():
            for romname,file in systemCartMap.iteritems():
                if name == romname or name == romname.replace(' ','_'):
                    biosfile = self.romFileMapMESS[systemName]
                    if len(biosfile)>0:
                        retval = [biosfile]
                    else:
                        retval = []
                    retval.append(file)
                    return retval
        for romname,description in self.romDescriptionMapMAME.iteritems():
            if name == description or name == description.replace(' ','_'):
                retval = [self.romFileMapMAME[romname]]
                if romname in self.romExtraFilesMapMAME:
                    retval.extend(self.romExtraFilesMapMAME[romname])
                return retval
        return []

if __name__ == '__main__':
    gameAuditer = GameAuditer()
    gameAuditer.baseDirectories = ['../roms']
    gameAuditer.audit()

