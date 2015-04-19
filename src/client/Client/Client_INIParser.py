# import python mods
import os

class INIParser(object):
    def __init__(self,iniFile):
        print "ini:",iniFile
        if os.path.isfile(iniFile)==False:
            raise Exception("Could not find ini file: "+iniFile)
        self.iniFile = iniFile
        self.iniData = open(self.iniFile,'r').read()
        for pos in xrange(0,len(self.iniData)):
            if ord(self.iniData[pos])>=128:
                self.iniData = self.iniData[:pos] + ' ' + self.iniData[pos+1:]

    def getRomPaths(self):
        self.iniEntries = self.iniData[self.iniData.find('rompath'):].partition('\n')[0].partition(' ')[2].strip()
        if len(self.iniEntries)==0:
            raise Exception("Could not find rompath in ini file")
        return self.iniEntries.split(';')

    def setRomPaths(self,newPaths):
        newPaths = newPaths
        self.iniEntries = self.iniData[self.iniData.find('rompath'):].partition('\n')[0].partition(' ')[2].strip()
        if len(self.iniEntries)==0:
            raise Exception("Could not find rompath in ini file")
        self.iniData = self.iniData.replace(self.iniEntries,newPaths)
        f = open(self.iniFile,'w')
        f.write(self.iniData)
        f.close()