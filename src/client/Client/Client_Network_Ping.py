# import python mods
import os,re,time,sys
from threading import Thread

class pingit(Thread):
   def __init__ (self,ip):
      Thread.__init__(self)
      self.ip = ip
      self.status = -1
   def run(self):
      pingaling = None
      if str.upper(sys.platform[0:3])=='WIN' \
      or str.upper(sys.platform[0:3])=='CYG':
        pingaling = os.popen("ping -n 2 "+self.ip,"r")
      else:
        pingaling = os.popen("ping -q -c2 "+self.ip,"r")
      while 1:
        line = pingaling.readline()
        print line
        if not line: break
        igot = re.findall(pingit.lifeline,line)
        if igot:
           self.status = int(igot[0])

pingit.lifeline = re.compile(r"(\d) received")
report = ("No response","Partial Response","Alive")

print time.ctime()

pinglist = []

for host in range(1,10):
   ip = "10.0.0."+str(host)
   current = pingit(ip)
   pinglist.append(current)
   current.start()

for pingle in pinglist:
   pingle.join()
   print "Status from ",pingle.ip,"is",report[pingle.status]

print time.ctime()