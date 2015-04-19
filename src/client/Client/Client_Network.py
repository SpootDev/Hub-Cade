# import div for "proper" no floor division
from __future__ import division

# import wxWidgets files
import wx

# import python mods
import urllib2,socket,re,time,os,datetime,bz2,threading,struct
try:
    import cPickle as pickle
except:
    import pickle

# import twisted files that are required
import twisted.protocols.basic
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor,ssl
from twisted.protocols.basic import Int32StringReceiver

# import globals
import Client_GlobalData
import Client_GlobalData_Config

# import code
from Client_Ban_Dialog import BanDialog
import Client_Game
import Client_Database
from Client_DIP_Settings import *
from Client_ServerStats import ServerStatsDialog
from Client_Top10 import TopTenDialog

# download image file from specified url to save in specific directory
def download_image(url,directory):
    try:
        imageFile = urllib2.urlopen(url)
        localFile = open(directory, 'wb')
        localFile.write(imageFile.read())
        imageFile.close()
        localFile.close()
    except urllib2.URLError, e:
        #print 'you got an error with the code', e
        pass

# following code is the convert url's to links in chat
urls = '(?: %s)' % '|'.join("""http https telnet gopher file wais
ftp""".split())
ltrs = r'\w'
gunk = r'\/\#\~\:\.\?\+\=\&\%\@\!\-'
punc = r'\.\:\?\-'
any = "%(ltrs)s%(gunk)s%(punc)s" % { 'ltrs' : ltrs,
                                     'gunk' : gunk,
                                     'punc' : punc }

url = r"""
    \b                            # start at word boundary
        %(urls)s    :             # need resource and a colon
        [%(any)s]  +?             # followed by one or more
                                  #  of any valid character, but
                                  #  be conservative and take only
                                  #  what you need to....
    (?=                           # look-ahead non-consumptive assertion
            [%(punc)s]*           # either 0 or more punctuation
            (?:   [^%(any)s]      #  followed by a non-url char
                |                 #   or end of the string
                  $
            )
    )
    """ % {'urls' : urls,
           'any' : any,
           'punc' : punc }

url_re = re.compile(url, re.VERBOSE | re.MULTILINE)

def convertURLtoHREF(text):
    """Given a text string, returns all the urls we can find in it."""
    return re.sub(url_re,"<a href=\"\g<0>\" target=\"_blank\">\g<0></a>",text)

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def getAllBytes(con,byteCount):
    bytesLeft = byteCount
    buffer = ""
    while bytesLeft:
        data = con.recv(bytesLeft)
        bytesLeft -= len(data)
        buffer += data
    return buffer

def ProcessChatString(chatString):
    chatString = chatString.replace("<","&lt;")
    chatString = chatString.replace(">","&gt;")
    chatString = chatString.replace("\n","<br />")
    chatString = chatString.replace("*", "&#42;")
    if Client_GlobalData_Config.display_emote_in_chat == True:
        if Client_GlobalData.webkit_enabled == False:
            chatString = chatString.replace("(ashamed)", "<img src=\"../images/emotes/Ashamed.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bangwall)", "<img src=\"../images/emotes/BangWall.gif\"  width=\"30\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(beer)", "<img src=\"../images/emotes/beerwez.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bgrin)", "<img src=\"../images/emotes/Biggin.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bslap)", "<img src=\"../images/emotes/bslap.gif\"  width=\"39\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(lol)", "<img src=\"../images/emotes/BigLaugh.gif\"  width=\"31\"  height=\"29\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(chair)", "<img src=\"../images/emotes/ChairHit.gif\"  width=\"45\"  height=\"40\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(clap)", "<img src=\"../images/emotes/Clap.gif\"  width=\"31\"  height=\"23\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(con)", "<img src=\"../images/emotes/Confused3.gif\"  width=\"22\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(cool)", "<img src=\"../images/emotes/cool_smiley.gif\"  width=\"35\"  height=\"30\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(first)", "<img src=\"../images/emotes/First.gif\"  width=\"36\"  height=\"27\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(alien)", "<img src=\"../images/emotes/GreenAlien.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(hammer)", "<img src=\"../images/emotes/Hammer3.gif\"  width=\"56\"  height=\"41\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(irr)", "<img src=\"../images/emotes/Irritated.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nono)", "<img src=\"../images/emotes/nono4.gif\"  width=\"31\"  height=\"30\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(rock)", "<img src=\"../images/emotes/Rock.gif\"  width=\"31\"  height=\"28\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(shade)", "<img src=\"../images/emotes/Shades.gif\"  width=\"23\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(sorry)", "<img src=\"../images/emotes/Sorry56fdg.gif\"  width=\"50\"  height=\"50\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(tongue)", "<img src=\"../images/emotes/Tongue2.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(uzi)", "<img src=\"../images/emotes/Uzi.gif\"  width=\"52\"  height=\"16\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(mad)", "<img src=\"../images/emotes/VeryAngry.gif\"  width=\"33\"  height=\"37\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(whistle)", "<img src=\"../images/emotes/Whistle.gif\"  width=\"27\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(cheers)", "<img src=\"../images/emotes/drinking08.gif\"  width=\"60\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(beta)", "<img src=\"../images/emotes/beta1.gif\"  width=\"46\"  height=\"51\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(troll)", "<img src=\"../images/emotes/feedtroll.gif\"  width=\"46\"  height=\"100\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(lame)", "<img src=\"../images/emotes/lame.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(pics)", "<img src=\"../images/emotes/pics.gif\"  width=\"52\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(jerry)", "<img src=\"../images/emotes/jerry.gif\"  width=\"74\"  height=\"51\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(drool)", "<img src=\"../images/emotes/drool.gif\"  width=\"15\"  height=\"30\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bat)", "<img src=\"../images/emotes/bat.gif\"  width=\"26\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(stupid)", "<img src=\"../images/emotes/stupid.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(hissy)", "<img src=\"../images/emotes/hissy.gif\"  width=\"45\"  height=\"31\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(404)", "<img src=\"../images/emotes/404.gif\"  width=\"105\"  height=\"65\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(blah)", "<img src=\"../images/emotes/blah2.gif\"  width=\"37\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bow)", "<img src=\"../images/emotes/bow2.gif\"  width=\"27\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(rofl)", "<img src=\"../images/emotes/laught16.gif\"  width=\"32\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(soap)", "<img src=\"../images/emotes/soapbox2.gif\"  width=\"43\"  height=\"58\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(zzz)", "<img src=\"../images/emotes/sleep1.gif\"  width=\"38\"  height=\"23\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(sick)", "<img src=\"../images/emotes/sick.gif\"  width=\"18\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(pirate)", "<img src=\"../images/emotes/pirate.gif\"  width=\"20\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(surrender)", "<img src=\"../images/emotes/surrender.gif\"  width=\"28\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nstar)", "<img src=\"../images/emotes/shuriken.gif\"  width=\"37\"  height=\"24\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(ok)", "<img src=\"../images/emotes/thumbup.gif\"  width=\"38\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(angel)", "<img src=\"../images/emotes/innocent.gif\"  width=\"18\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bday)", "<img src=\"../images/emotes/happybday.gif\"  width=\"81\"  height=\"26\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nuke)", "<img src=\"../images/emotes/nuke.gif\"  width=\"20\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(oops)", "<img src=\"../images/emotes/oops.gif\"  width=\"48\"  height=\"49\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(off)", "<img src=\"../images/emotes/offtopic.gif\"  width=\"47\"  height=\"51\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(wow)", "<img src=\"../images/emotes/w00t.gif\"  width=\"18\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(drink)", "<img src=\"../images/emotes/drink.gif\"  width=\"45\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(doh)", "<img src=\"../images/emotes/doh1.gif\"  width=\"44\"  height=\"38\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(yawn)", "<img src=\"../images/emotes/yawn.gif\"  width=\"18\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(help)", "<img src=\"../images/emotes/help.gif\"  width=\"35\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(eek)", "<img src=\"../images/emotes/eek.gif\"  width=\"26\"  height=\"24\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(ambulance)", "<img src=\"../images/emotes/ambulance.gif\"  width=\"26\"  height=\"21\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(peek)", "<img src=\"../images/emotes/peek.gif\"  width=\"32\"  height=\"43\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(blind)", "<img src=\"../images/emotes/blind.gif\"  width=\"24\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(crazy)", "<img src=\"../images/emotes/crazy.gif\"  width=\"23\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(blush)", "<img src=\"../images/emotes/blush.gif\"  width=\"15\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(circles)", "<img src=\"../images/emotes/circles.gif\"  width=\"28\"  height=\"17\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(borg)", "<img src=\"../images/emotes/assimilate.gif\"  width=\"100\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(yeah)", "<img src=\"../images/emotes/yeah.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(wtf)", "<img src=\"../images/emotes/wtf.gif\"  width=\"45\"  height=\"53\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(master)", "<img src=\"../images/emotes/master.gif\"  width=\"50\"  height=\"50\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(hi)", "<img src=\"../images/emotes/hi.gif\"  width=\"26\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(cold)", "<img src=\"../images/emotes/cold.gif\"  width=\"26\"  height=\"32\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(booboo)", "<img src=\"../images/emotes/booboo.gif\"  width=\"64\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(tmi)", "<img src=\"../images/emotes/tmi.gif\"  width=\"39\"  height=\"39\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(welcome)", "<img src=\"../images/emotes/welcome.gif\"  width=\"55\"  height=\"36\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(ballnchain)", "<img src=\"../images/emotes/ballnchain.gif\"  width=\"43\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bravo)", "<img src=\"../images/emotes/bravo.gif\"  width=\"48\"  height=\"33\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(phone)", "<img src=\"../images/emotes/phone.gif\"  width=\"22\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(rip)", "<img src=\"../images/emotes/rip.gif\"  width=\"43\"  height=\"34\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bye)", "<img src=\"../images/emotes/bye.gif\"  width=\"55\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(pray)", "<img src=\"../images/emotes/pray.gif\"  width=\"18\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(kids)", "<img src=\"../images/emotes/kids.gif\"  width=\"56\"  height=\"27\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nn)", "<img src=\"../images/emotes/nn.gif\"  width=\"66\"  height=\"40\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(shock)", "<img src=\"../images/emotes/shock.gif\"  width=\"19\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(gaming)", "<img src=\"../images/emotes/gaming.gif\"  width=\"67\"  height=\"37\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(party)", "<img src=\"../images/emotes/party.gif\"  width=\"45\"  height=\"33\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(smoke)", "<img src=\"../images/emotes/smoke.gif\"  width=\"21\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(sad)", "<img src=\"../images/emotes/sad.gif\"  width=\"90\"  height=\"90\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(horse)", "<img src=\"../images/emotes/deadhorse.gif\"  width=\"77\"  height=\"45\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(inoob)", "<img src=\"../images/emotes/inoob.gif\"  width=\"78\"  height=\"40\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(wski)", "<img src=\"../images/emotes/waterski.gif\"  width=\"300\"  height=\"28\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(woot)", "<img src=\"../images/emotes/woot.gif\"  width=\"80\"  height=\"28\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(flame)", "<img src=\"../images/emotes/flamewar.gif\"  width=\"45\"  height=\"53\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(lawn)", "<img src=\"../images/emotes/lawn.gif\"  width=\"48\"  height=\"33\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(owned)", "<img src=\"../images/emotes/owned.gif\"  width=\"56\"  height=\"44\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(punch)", "<img src=\"../images/emotes/inet_punch.gif\"  width=\"60\"  height=\"23\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(palm)", "<img src=\"../images/emotes/facepalm.gif\"  width=\"45\"  height=\"24\"  border=\"0\"  alt=\"graphic\" >")
        else:
            # this might only be needed in the windows version?
            image_local = Client_GlobalData.application_launch_directory.rsplit('/',1)[0]
            #print "two: ",image_local
            chatString = chatString.replace("(ashamed)", "<img src=\"" + image_local + "/images/emotes/Ashamed.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bangwall)", "<img src=\"" + image_local + "/images/emotes/BangWall.gif\"  width=\"30\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(beer)", "<img src=\"" + image_local + "/images/emotes/beerwez.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bgrin)", "<img src=\"" + image_local + "/images/emotes/Biggin.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bslap)", "<img src=\"" + image_local + "/images/emotes/bslap.gif\"  width=\"39\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(lol)", "<img src=\"" + image_local + "/images/emotes/BigLaugh.gif\"  width=\"31\"  height=\"29\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(chair)", "<img src=\"" + image_local + "/images/emotes/ChairHit.gif\"  width=\"45\"  height=\"40\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(clap)", "<img src=\"" + image_local + "/images/emotes/Clap.gif\"  width=\"31\"  height=\"23\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(con)", "<img src=\"" + image_local + "/images/emotes/Confused3.gif\"  width=\"22\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(cool)", "<img src=\"" + image_local + "/images/emotes/cool_smiley.gif\"  width=\"35\"  height=\"30\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(first)", "<img src=\"" + image_local + "/images/emotes/First.gif\"  width=\"36\"  height=\"27\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(alien)", "<img src=\"" + image_local + "/images/emotes/GreenAlien.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(hammer)", "<img src=\"" + image_local + "/images/emotes/Hammer3.gif\"  width=\"56\"  height=\"41\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(irr)", "<img src=\"" + image_local + "/images/emotes/Irritated.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nono)", "<img src=\"" + image_local + "/images/emotes/nono4.gif\"  width=\"31\"  height=\"30\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(rock)", "<img src=\"" + image_local + "/images/emotes/Rock.gif\"  width=\"31\"  height=\"28\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(shade)", "<img src=\"" + image_local + "/images/emotes/Shades.gif\"  width=\"23\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(sorry)", "<img src=\"" + image_local + "/images/emotes/Sorry56fdg.gif\"  width=\"50\"  height=\"50\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(tongue)", "<img src=\"" + image_local + "/images/emotes/Tongue2.gif\"  width=\"19\"  height=\"19\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(uzi)", "<img src=\"" + image_local + "/images/emotes/Uzi.gif\"  width=\"52\"  height=\"16\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(mad)", "<img src=\"" + image_local + "/images/emotes/VeryAngry.gif\"  width=\"33\"  height=\"37\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(whistle)", "<img src=\"" + image_local + "/images/emotes/Whistle.gif\"  width=\"27\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(cheers)", "<img src=\"" + image_local + "/images/emotes/drinking08.gif\"  width=\"60\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(beta)", "<img src=\"" + image_local + "/images/emotes/beta1.gif\"  width=\"46\"  height=\"51\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(troll)", "<img src=\"" + image_local + "/images/emotes/feedtroll.gif\"  width=\"46\"  height=\"100\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(lame)", "<img src=\"" + image_local + "/images/emotes/lame.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(pics)", "<img src=\"" + image_local + "/images/emotes/pics.gif\"  width=\"52\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(jerry)", "<img src=\"" + image_local + "/images/emotes/jerry.gif\"  width=\"74\"  height=\"51\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(drool)", "<img src=\"" + image_local + "/images/emotes/drool.gif\"  width=\"15\"  height=\"30\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bat)", "<img src=\"" + image_local + "/images/emotes/bat.gif\"  width=\"26\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(stupid)", "<img src=\"" + image_local + "/images/emotes/stupid.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(hissy)", "<img src=\"" + image_local + "/images/emotes/hissy.gif\"  width=\"45\"  height=\"31\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(404)", "<img src=\"" + image_local + "/images/emotes/404.gif\"  width=\"105\"  height=\"65\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(blah)", "<img src=\"" + image_local + "/images/emotes/blah2.gif\"  width=\"37\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bow)", "<img src=\"" + image_local + "/images/emotes/bow2.gif\"  width=\"27\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(rofl)", "<img src=\"" + image_local + "/images/emotes/laught16.gif\"  width=\"32\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(soap)", "<img src=\"" + image_local + "/images/emotes/soapbox2.gif\"  width=\"43\"  height=\"58\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(zzz)", "<img src=\"" + image_local + "/images/emotes/sleep1.gif\"  width=\"38\"  height=\"23\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(sick)", "<img src=\"" + image_local + "/images/emotes/sick.gif\"  width=\"18\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(pirate)", "<img src=\"" + image_local + "/images/emotes/pirate.gif\"  width=\"20\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(surrender)", "<img src=\"" + image_local + "/images/emotes/surrender.gif\"  width=\"28\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nstar)", "<img src=\"" + image_local + "/images/emotes/shuriken.gif\"  width=\"37\"  height=\"24\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(ok)", "<img src=\"" + image_local + "/images/emotes/thumbup.gif\"  width=\"38\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(angel)", "<img src=\"" + image_local + "/images/emotes/innocent.gif\"  width=\"18\"  height=\"22\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bday)", "<img src=\"" + image_local + "/images/emotes/happybday.gif\"  width=\"81\"  height=\"26\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nuke)", "<img src=\"" + image_local + "/images/emotes/nuke.gif\"  width=\"20\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(oops)", "<img src=\"" + image_local + "/images/emotes/oops.gif\"  width=\"48\"  height=\"49\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(off)", "<img src=\"" + image_local + "/images/emotes/offtopic.gif\"  width=\"47\"  height=\"51\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(wow)", "<img src=\"" + image_local + "/images/emotes/w00t.gif\"  width=\"18\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(drink)", "<img src=\"" + image_local + "/images/emotes/drink.gif\"  width=\"45\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(doh)", "<img src=\"" + image_local + "/images/emotes/doh1.gif\"  width=\"44\"  height=\"38\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(yawn)", "<img src=\"" + image_local + "/images/emotes/yawn.gif\"  width=\"18\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(help)", "<img src=\"" + image_local + "/images/emotes/help.gif\"  width=\"35\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(eek)", "<img src=\"" + image_local + "/images/emotes/eek.gif\"  width=\"26\"  height=\"24\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(ambulance)", "<img src=\"" + image_local + "/images/emotes/ambulance.gif\"  width=\"26\"  height=\"21\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(peek)", "<img src=\"" + image_local + "/images/emotes/peek.gif\"  width=\"32\"  height=\"43\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(blind)", "<img src=\"" + image_local + "/images/emotes/blind.gif\"  width=\"24\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(crazy)", "<img src=\"" + image_local + "/images/emotes/crazy.gif\"  width=\"23\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(blush)", "<img src=\"" + image_local + "/images/emotes/blush.gif\"  width=\"15\"  height=\"15\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(circles)", "<img src=\"" + image_local + "/images/emotes/circles.gif\"  width=\"28\"  height=\"17\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(borg)", "<img src=\"" + image_local + "/images/emotes/assimilate.gif\"  width=\"100\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(yeah)", "<img src=\"" + image_local + "/images/emotes/yeah.gif\"  width=\"41\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(wtf)", "<img src=\"" + image_local + "/images/emotes/wtf.gif\"  width=\"45\"  height=\"53\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(master)", "<img src=\"" + image_local + "/images/emotes/master.gif\"  width=\"50\"  height=\"50\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(hi)", "<img src=\"" + image_local + "/images/emotes/hi.gif\"  width=\"26\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(cold)", "<img src=\"" + image_local + "/images/emotes/cold.gif\"  width=\"26\"  height=\"32\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(booboo)", "<img src=\"" + image_local + "/images/emotes/booboo.gif\"  width=\"64\"  height=\"46\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(tmi)", "<img src=\"" + image_local + "/images/emotes/tmi.gif\"  width=\"39\"  height=\"39\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(welcome)", "<img src=\"" + image_local + "/images/emotes/welcome.gif\"  width=\"55\"  height=\"36\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(ballnchain)", "<img src=\"" + image_local + "/images/emotes/ballnchain.gif\"  width=\"43\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bravo)", "<img src=\"" + image_local + "/images/emotes/bravo.gif\"  width=\"48\"  height=\"33\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(phone)", "<img src=\"" + image_local + "/images/emotes/phone.gif\"  width=\"22\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(rip)", "<img src=\"" + image_local + "/images/emotes/rip.gif\"  width=\"43\"  height=\"34\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(bye)", "<img src=\"" + image_local + "/images/emotes/bye.gif\"  width=\"55\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(pray)", "<img src=\"" + image_local + "/images/emotes/pray.gif\"  width=\"18\"  height=\"18\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(kids)", "<img src=\"" + image_local + "/images/emotes/kids.gif\"  width=\"56\"  height=\"27\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(nn)", "<img src=\"" + image_local + "/images/emotes/nn.gif\"  width=\"66\"  height=\"40\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(shock)", "<img src=\"" + image_local + "/images/emotes/shock.gif\"  width=\"19\"  height=\"25\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(gaming)", "<img src=\"" + image_local + "/images/emotes/gaming.gif\"  width=\"67\"  height=\"37\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(party)", "<img src=\"" + image_local + "/images/emotes/party.gif\"  width=\"45\"  height=\"33\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(smoke)", "<img src=\"" + image_local + "/images/emotes/smoke.gif\"  width=\"21\"  height=\"20\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(sad)", "<img src=\"" + image_local + "/images/emotes/sad.gif\"  width=\"90\"  height=\"90\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(horse)", "<img src=\"" + image_local + "/images/emotes/deadhorse.gif\"  width=\"77\"  height=\"45\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(inoob)", "<img src=\"" + image_local + "/images/emotes/inoob.gif\"  width=\"78\"  height=\"40\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(wski)", "<img src=\"" + image_local + "/images/emotes/waterski.gif\"  width=\"300\"  height=\"28\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(woot)", "<img src=\"" + image_local + "/images/emotes/woot.gif\"  width=\"80\"  height=\"28\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(flame)", "<img src=\"" + image_local + "/images/emotes/flamewar.gif\"  width=\"45\"  height=\"53\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(lawn)", "<img src=\"" + image_local + "/images/emotes/lawn.gif\"  width=\"48\"  height=\"33\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(owned)", "<img src=\"" + image_local + "/images/emotes/owned.gif\"  width=\"56\"  height=\"44\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(punch)", "<img src=\"" + image_local + "/images/emotes/inet_punch.gif\"  width=\"60\"  height=\"23\"  border=\"0\"  alt=\"graphic\" >")
            chatString = chatString.replace("(palm)", "<img src=\"" + image_local + "/images/emotes/facepalm.gif\"  width=\"45\"  height=\"24\"  border=\"0\"  alt=\"graphic\" >")
    chatString = convertURLtoHREF(chatString)
    return chatString

class FileSenderThread(threading.Thread):
    def __init__(self,targetIP,targetPort,fileNames,fileLocations):
        self.host = targetIP
        self.port = targetPort
        self.fileNames = fileNames
        self.fileLocations = fileLocations
        threading.Thread.__init__(self)

    def run(self):
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.settimeout(60.0)
            clientSocket.connect((self.host, self.port))
            for fileIndex in xrange(0,len(self.fileNames)):
                data = open(self.fileLocations[fileIndex],'rb').read()
                print self.fileNames[fileIndex],type(self.fileNames[fileIndex])
                clientSocket.sendall("FILE"+struct.pack("<i256s",len(data),str(self.fileNames[fileIndex])))
                for x in xrange(0,(len(data)+1023)/1024):
                    clientSocket.sendall(data[x*1024:(x+1)*1024])
                    time.sleep(0.05)
            clientSocket.sendall('FEND')
            clientSocket.close()
        except socket.error,msg:
            mdial = wx.MessageDialog(None, str(msg), 'Sending files failed.', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
            #print "Sending files failed."
            #print msg

class FileReceiverThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.fileDone = 0
        self.fileSize = 1

    def run(self):
        try:
            localHostname = ''
            localPort = Client_GlobalData.selfPort
            print 'Listening for response on port',Client_GlobalData.selfPort
            localSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            localSocket.settimeout(60.0)
            localSocket.bind((localHostname,localPort))
            localSocket.listen(1)

            con,addr = localSocket.accept()
            print 'Connection address:',addr
            con.settimeout(60.0)

            while True:
                data = getAllBytes(con,4)
                if not data:
                    break
                if data=='FEND':
                    break
                elif data=='FILE':
                    data = getAllBytes(con,260)
                    fileSize,fileName = struct.unpack("<i256s",data)
                    self.fileSize = fileSize
                    fileName = fileName.replace('\0','')
                    print fileSize,fileName
                    fileName = str(fileName)
                    print 'fileName',fileName
                    f = open('../roms/'+fileName,'wb')
                    fileLeft = fileSize
                    self.fileDone = 0
                    while fileLeft:
                        data = con.recv(min(fileLeft,1024))
                        fileLeft = max(0,fileLeft-len(data))
                        self.fileDone = self.fileSize - fileLeft
                        print 'percent done',self.fileDone*100/self.fileSize
                        f.write(data)
                    print 'file finished'
                    f.close()
                else:
                    raise Exception('ERROR GETTING FILES (NO FILE OR FEND)')
                    break
            print 'Finished getting all files!'
            del localSocket
            Client_GlobalData.needAudit=True
        except socket.error as msg:
            #print msg
            Client_GlobalData.messageBoxQueue.append( (str(msg),"ROM Transfer Failed.") )

class MyClientFactory(ClientFactory):
    def __init__(self):
        self.protocol=None
        self.failed = False

    def startedConnecting(self, connector):
        print 'Started to connect to',connector.getDestination()

    def buildProtocol(self, addr):
        print 'Connected to ',str(addr)

        self.protocol = ClientProtocol()
        return self.protocol

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason
        self.failed = True
        if self.protocol:
            if self.protocol.connStatus == ClientProtocol.CHECKING_PORT:
                self.protocol.connStatus = ClientProtocol.PORT_CLOSED
            else:
                self.protocol.connStatus = ClientProtocol.CLOSED

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
        self.failed = True
        if self.protocol:
            if self.protocol.connStatus == ClientProtcol.CHECKING_PORT:
                self.protocol.connStatus = ClientProtocol.PORT_CLOSED
            else:
                self.protocol.connStatus = ClientProtocol.CLOSED

class ClientProtocol(Int32StringReceiver):
    STARTED=0
    CHECKING_PORT=1
    CONNECTED=2
    NOTSTARTED=3
    PORTCLOSED=4
    CLOSED=5

    def __init__(self):
        self.connStatus = ClientProtocol.STARTED
        self.lastPongTime = time.time()
        self.lastPingTime = time.time()

    def connectionMade(self):
        self.connStatus = ClientProtocol.CHECKING_PORT
        #self.sendString("INIT "+str(Client_GlobalData.selfPort))
        reactor.runUntilCurrent()
        reactor.doIteration(0)
##        try:
##            localHostname = ''
##            localPort = Client_GlobalData.selfPort
##            print 'Listening for response on port',Client_GlobalData.selfPort
##            localSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##            localSocket.settimeout(15.0)
##            localSocket.bind((localHostname,localPort))
##            localSocket.listen(1)
##            con,addr = localSocket.accept()
##            print 'Connection address:',addr
        self.connStatus = ClientProtocol.CONNECTED
##        except socket.error,msg:
##            print 'Local port is not correctly mapped'
##            print msg
##            self.connStatus = ClientProtocol.PORTCLOSED
##            mdial = wx.MessageDialog(None, 'You do not have your port forwarded correctly!  You will not be able to host games until you set up port forwarding.', 'Port Warning', wx.OK | wx.ICON_EXCLAMATION)
##            mdial.ShowModal()
##            mdial.Destroy()
##            Client_GlobalData.hasPortForwarded = False
##        #Someone connected to us, so our port forwarding must be ok
##        #Kill this socket and let's get going!
##        localSocket.close()
##        del localSocket
        Client_GlobalData.networkProtocol = self

    def pingServer(self):
        self.sendString("PING")
        self.lastPingTime = time.time()

    def stringReceived(self, data):
        print 'GOT Data:',data
        messageWords = data.split(' ')
        print messageWords

        if messageWords[0]=="FILE_REQUEST_GRANTED":
            while Client_GlobalData.fileReceiverThread is not None \
                and Client_GlobalData.fileReceiverThread.is_alive():
                    pass
            Client_GlobalData.fileReceiverThread = FileReceiverThread()
            Client_GlobalData.fileReceiverThread.start()
            return
        elif messageWords[0]=="FILE_REQUEST":
            if Client_GlobalData_Config.allow_client_downloads == True:
                clientIP = messageWords[1]
                clientPort = int(messageWords[2])
                hostedFileNames = copy.deepcopy(Client_GlobalData.hostedFiles)
                for fileIndex in xrange(0,len(hostedFileNames)):
                    hostedFileNames[fileIndex] = os.path.basename(hostedFileNames[fileIndex])
                Client_GlobalData.fileSenderThreads.append(FileSenderThread(clientIP,clientPort,hostedFileNames,Client_GlobalData.hostedFiles))
                Client_GlobalData.fileSenderThreads[-1].start()
            return

        # receive request to send dips
        if messageWords[0]=="REQUEST_DIPS":
            SendDIPSettings()
            return
        # receive dips from host
        elif messageWords[0]=="RECEIVE_DIPS":
            ReceiveDIPSettings(data[len("RECEIVE_DIPS "):])
            return

        if messageWords[0]=="CHAT_MESSAGE" or messageWords[0]=="PRIV_CHAT" or messageWords[0]=="ADMIN_CHAT" \
        and Client_GlobalData.player is not None \
        and Client_GlobalData.player.username.upper() in data.upper().replace("<"+Client_GlobalData.player.username.upper()+">",""):
            Client_GlobalData.app.mainFrame.RequestUserAttention()

        if messageWords[0]=="PONG":
            self.lastPongTime = time.time()
        elif messageWords[0]=="FILE_REQUEST_DENIED":
            mdial = wx.MessageDialog(None, 'This host does not allow ROM downloads.', 'Cannot Download', wx.OK | wx.ICON_EXCLAMATION)
            mdial.ShowModal()
            mdial.Destroy()
        elif messageWords[0]=="NOT_ADMIN":
            mdial = wx.MessageDialog(None, 'You are not flagged to allow admin commands.', 'Not Admin', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
        elif messageWords[0]=="ADD_UPDATE_PLAYER":
            playerID = int(messageWords[1])
            if playerID not in Client_GlobalData.database.players:
                Client_GlobalData.database.players[playerID] = Client_Game.Player()
            Client_GlobalData.database.players[playerID].ID = playerID
            Client_GlobalData.database.players[playerID].username = messageWords[2]
            #Client_GlobalData.database.players[playerID].email = messageWords[3]
            Client_GlobalData.database.players[playerID].IPAddress = messageWords[3]
            Client_GlobalData.database.players[playerID].port = int(messageWords[4])
            Client_GlobalData.database.players[playerID].status = int(messageWords[5])
            Client_GlobalData.database.players[playerID].playingGameInstanceID = int(messageWords[6])
            Client_GlobalData.database.players[playerID].LFG = messageWords[7]
            #Client_GlobalData.database.players[playerID].friends = messageWords[9]
            Client_GlobalData.database.players[playerID].AFK = int(messageWords[8])
            Client_GlobalData.database.players[playerID].OperatingSystem = messageWords[9]
            Client_GlobalData.database.players[playerID].Country = messageWords[10]
            Client_GlobalData.database.players[playerID].Is_Admin = messageWords[11]
            Client_GlobalData.gui_update_user_grid = True
            Client_GlobalData.gui_update_hosted_game_grid = True  # so the other thing display for count
        elif messageWords[0]=="ADD_UPDATE_GAME_INSTANCE":
            gameInstanceID = int(messageWords[1])
            if gameInstanceID not in Client_GlobalData.database.gameInstances:
##                Client_GlobalData.app.mainFrame.notifyIfInactive("Game Started", messageWords[2])
                if Client_GlobalData.player and Client_GlobalData.player.AFK==False and Client_GlobalData_Config.mute_chat_sounds == False:
                    if Client_GlobalData.app.gameStartedSound.IsOk():
                        Client_GlobalData.app.gameStartedSound.Play()
                    else:
                        print 'Cannot find game started sound!'
            Client_GlobalData.database.gameInstances[gameInstanceID] = \
            Client_Game.GameInstance( \
            gameInstanceID, \
            int(messageWords[2]),
            int(messageWords[3]),
            int(messageWords[4]),
            int(messageWords[5]),
            int(messageWords[6]),
            float(messageWords[7]),
            messageWords[8]
            )
            Client_GlobalData.gui_update_hosted_game_grid = True
            Client_GlobalData.gui_update_user_grid = True  # do this so the game count works
        elif messageWords[0]=="REMOVE_GAME_INSTANCE":
            gameInstanceID = int(messageWords[1])
            if gameInstanceID in Client_GlobalData.database.gameInstances:
                del Client_GlobalData.database.gameInstances[gameInstanceID]
                Client_GlobalData.gui_update_hosted_game_grid = True
        elif messageWords[0]=="PLAYER_CREATED":
            Client_GlobalData.player = Client_GlobalData.database.players[int(messageWords[1])]
            if Client_GlobalData.app.entryDialog.rememberPasswordCheckBox.IsChecked():
                f = bz2.BZ2File('dd.dat','w')
                f.write(Client_GlobalData.app.entryDialog.usernameText.GetLineText(0))
                f.write(' ')
                f.write(Client_GlobalData.app.entryDialog.passwordText.GetLineText(0))
                f.close()
            else:
                if os.path.isfile('dd.dat'):
                    os.remove('dd.dat')
            Client_GlobalData.app.entryDialog.Close()
        elif messageWords[0]=="PASSWORD_VALIDATED":
            Client_GlobalData.player = Client_GlobalData.database.players[int(messageWords[1])]
            Client_GlobalData.playerID = int(messageWords[1])
            print "wtf2:",int(messageWords[1]),messageWords[1]
            if messageWords[2] != "1":
                # not admin so turn off options
                Client_GlobalData.app.mainFrame.chat_aui_notebook.DeletePage(2)
                menu_id = None
                # update main menu options
                Client_GlobalData.app.mainFrame.m_menubar1.Remove(7)
                # update play grid options
                for pos in range(Client_GlobalData.app.mainFrame.playerGridMenu.GetMenuItemCount()):
                    item = Client_GlobalData.app.mainFrame.playerGridMenu.FindItemByPosition(pos)
                    if "Admin" == item.GetLabel():
                        menu_id = item.GetId()
                        Client_GlobalData.app.mainFrame.playerGridMenu.Remove(menu_id)
                        break
                items = Client_GlobalData.app.mainFrame.playerGridMenu.GetMenuItems()
                count = 0
                for item in items:
                    if item.IsSeparator():
                        count += 1
                        if count == 3:
                            Client_GlobalData.app.mainFrame.playerGridMenu.RemoveItem(item)
                            break;
            if Client_GlobalData.app.entryDialog.rememberPasswordCheckBox.IsChecked():
                f = bz2.BZ2File('dd.dat','w')
                f.write(Client_GlobalData.app.entryDialog.usernameText.GetLineText(0))
                f.write(' ')
                f.write(Client_GlobalData.app.entryDialog.passwordText.GetLineText(0))
                f.close()
            else:
                if os.path.isfile('dd.dat'):
                    os.remove('dd.dat')
            Client_GlobalData.app.entryDialog.Hide()
            Client_GlobalData.app.entryDialog.Close()
            Client_GlobalData.app.entryDialog.Destroy()
        elif messageWords[0]=="USERNAME_INVALID":
            wx.MessageBox("Your username was not found.","Unknown user.")
        elif messageWords[0]=="EMAIL_SENT":
            wx.MessageBox("Your password has been emailed to the email address provided when you registered. If you do not see the email, check your spam folder.","Email sent.")
        elif messageWords[0]=="EMAIL_INVALID":
            wx.MessageBox("An email could not be sent to the email provided for this user. Please contact Digitalghost for assisstance","Bad Email.")
        elif messageWords[0]=="PASSWORD_INVALID":
            mdial = wx.MessageDialog(None, 'Your password is incorrect, please try again.', 'Wrong password', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
##        elif messageWords[0]=="CLIENT_INVALID":
##            wx.MessageBox("A new version of MAMEHub has been released!  You must uninstall this version and install the new version.  **NOTE** When you uninstall mamehub, it will COMPLETELY DELETE ALL FILES IN THE MAMEHUB FOLDER!!!!!!!!  If you have any roms/cfgs/videos/screenshots/etc. in your mamehub folder, move it somewhere safe BEFORE YOU UNINSTALL!!!!!  Visit http://10ghost.net/MAMEHubDownloads/ to get the new version of MAMEHub","Old client")
        elif messageWords[0]=="PRIV_CHAT":
            # see if chat block
            user_name = chatString.split(">",1)[0].replace("<","")
            sql_args = user_name.split(" ")[1],
            Client_GlobalData.curs_player.execute("select count(*) from player_info where player_name = ? and player_block_chat = 1",sql_args)
            if int(Client_GlobalData.curs_player.fetchone()[0]) > 0:
                pass
            else:
                timeString = datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S")
                chatString = "["+timeString+"] " + data[len("PRIV_CHAT "):] + "\n"
                if Client_GlobalData_Config.chat_save_to_db == True:
                    user_name = chatString.split(">",1)[0].replace("<","")
                    sql_chat_string = chatString.decode("utf8").replace("\"","'")
                    sql_chat_string = sql_chat_string.split(">")[1].lstrip()
                    sql_args = sql_chat_string,time.strftime("%Y-%m-%d %H:%M:%S"),user_name.split(" ")[1]
                    Client_Database.SQL_MameHub_Arrange_Chat(u"insert into chat_log (id,chat_text,chat_time,chat_user) values (NULL,?,?,?)",sql_args)
                chatString = ProcessChatString(chatString)
##                scrollPosition = Client_GlobalData.app.mainFrame.privateLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.privateLogHTML.GetScrollPixelsPerUnit()[1]
##                scrollBottomPosition = (Client_GlobalData.app.mainFrame.privateLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.privateLogHTML.GetScrollPixelsPerUnit()[1])+Client_GlobalData.app.mainFrame.privateLogHTML.GetClientSize()[1]
##                Client_GlobalData.app.mainFrame.privateLogHTML.SetPage("<html>" + Client_GlobalData.privHTML + "</html>")
##                Client_GlobalData.app.mainFrame.privateLogHTML.Scroll(-1, scrollBottomPosition/Client_GlobalData.app.mainFrame.privateLogHTML.GetScrollPixelsPerUnit()[1])
                Client_GlobalData.app.mainFrame.privateLogHTML.Freeze()
                if Client_GlobalData.webkit_enabled == False:
                    Client_GlobalData.app.mainFrame.privateLogHTML.AppendToPage("<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>")
                else:
                    Client_GlobalData.privHTML = Client_GlobalData.privHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>"
                    Client_GlobalData.app.mainFrame.privateLogHTML.SetPage("<html>" + Client_GlobalData.privHTML + "</html>","")
                Client_GlobalData.app.mainFrame.privateLogHTML.Thaw()
                # play chime if option is set and name is typed
                if Client_GlobalData_Config.chime_on_chat_name == True and chatString[0] != "*":
                    try:
                        if chatString.split(">",1)[1].count(Client_GlobalData.player.username) > 0:
                            if Client_GlobalData.player.AFK == False and Client_GlobalData_Config.mute_chat_sounds == False:
                                if Client_GlobalData.app.chimeSound.IsOk():
                                    Client_GlobalData.app.chimeSound.Play()
                                else:
                                    print 'Cannot find chimeSound!'
                    except:
                        pass
        elif messageWords[0]=="ADMIN_CHAT":
            timeString = datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S")
            chatString = "["+timeString+"] " + data[len("ADMIN_CHAT "):] + "\n"
            if Client_GlobalData_Config.chat_save_to_db == True:
                user_name = chatString.split(">",1)[0].replace("<","")
                sql_chat_string = chatString.decode("utf8").replace("\"","'")
                sql_chat_string = sql_chat_string.split(">")[1].lstrip()
                sql_args = sql_chat_string,time.strftime("%Y-%m-%d %H:%M:%S"),user_name.split(" ")[1]
                Client_Database.SQL_MameHub_Arrange_Chat(u"insert into chat_log (id,chat_text,chat_time,chat_user) values (NULL,?,?,?)",sql_args)
            chatString = ProcessChatString(chatString)
##            scrollPosition = Client_GlobalData.app.mainFrame.adminLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.adminLogHTML.GetScrollPixelsPerUnit()[1]
##            scrollBottomPosition = (Client_GlobalData.app.mainFrame.adminLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.adminLogHTML.GetScrollPixelsPerUnit()[1])+Client_GlobalData.app.mainFrame.adminLogHTML.GetClientSize()[1]
##            Client_GlobalData.app.mainFrame.adminLogHTML.SetPage("<html>" + Client_GlobalData.adminHTML + "</html>")
##            Client_GlobalData.app.mainFrame.adminLogHTML.Scroll(-1, scrollBottomPosition/Client_GlobalData.app.mainFrame.adminLogHTML.GetScrollPixelsPerUnit()[1])
            Client_GlobalData.app.mainFrame.adminLogHTML.Freeze()
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.adminLogHTML.AppendToPage("<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>")
            else:
                Client_GlobalData.adminHTML = Client_GlobalData.adminHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>"
                Client_GlobalData.app.mainFrame.adminLogHTML.SetPage("<html>" + Client_GlobalData.adminHTML + "</html>","")
            Client_GlobalData.app.mainFrame.adminLogHTML.Thaw()
            # play chime if option is set and name is typed
            if Client_GlobalData_Config.chime_on_chat_name == True and chatString[0] != "*":
                try:
                    if chatString.split(">",1)[1].count(Client_GlobalData.player.username) > 0:
                        if Client_GlobalData.player.AFK == False and Client_GlobalData_Config.mute_chat_sounds == False:
                            if Client_GlobalData.app.chimeSound.IsOk():
                                Client_GlobalData.app.chimeSound.Play()
                            else:
                                print 'Cannot find chimeSound!'
                except:
                    pass
        elif messageWords[0]=="MOTD":
            chatString = data[len("MOTD "):] + "\n"
            Client_GlobalData.motd_value = chatString
            chatString = ProcessChatString(chatString)
            Client_GlobalData.app.mainFrame.chatLogHTML.Freeze()
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.chatLogHTML.AppendToPage("<BR><BR>" +chatString + "<BR><BR>")
            else:
                Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + chatString.decode("utf8")
                Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>","")
            Client_GlobalData.app.mainFrame.chatLogHTML.Thaw()
        elif messageWords[0]=="RES_TOP10":
            Client_GlobalData.generic_string = data[len("RES_TOP10 "):]
            dialog = TopTenDialog(Client_GlobalData.app.mainFrame)
            dialog.Show()
        elif messageWords[0]=="RES_SRV_STATS":
            Client_GlobalData.generic_string = data[len("RES_SRV_STATS "):]
            dialog = ServerStatsDialog(Client_GlobalData.app.mainFrame)
            dialog.Show()
        elif messageWords[0]=="CHAT_MESSAGE":
            #print "data:",data[len("CHAT_MESSAGE "):]
            if data[len("CHAT_MESSAGE ")]=='<':
                timeString = datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S")
                chatString = "["+timeString+"] " + data[len("CHAT_MESSAGE "):] + "\n"
            else:
                chatString = data[len("CHAT_MESSAGE "):] + "\n"
##            Client_GlobalData.app.mainFrame.notifyIfInactive("Chat Message", chatString)
            # see if chat block
            user_name = chatString.split(">",1)[0].replace("<","")
            block_chat = False
            if len(chatString) > 11 and chatString[11] == "<":
                sql_args = user_name.split(" ")[1],
                Client_GlobalData.curs_player.execute("select count(*) from player_info where player_name = ? and player_block_chat = 1",sql_args)
                if int(Client_GlobalData.curs_player.fetchone()[0]) > 0:
                    block_chat = True
            else:
                if chatString[0] == "*":
                    chatString = chatString[:-1] + " at "+datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S") + "\n"
                if Client_GlobalData.player.AFK == False and Client_GlobalData_Config.mute_chat_sounds == False:
                    if chatString[0] == "*":
                        login_logoff = chatString.find(" left")
                        sql_args = user_name.split(" ")[1],
                        Client_GlobalData.curs_player.execute("select count(*) from player_info where player_name = ? and player_friend = 1",sql_args)
                        if int(Client_GlobalData.curs_player.fetchone()[0]) > 0:
                            print "chat thing: ",login_logoff
                            if login_logoff < 1:
                                # login
                                try:
                                    if Client_GlobalData.app.friendEntrySound.IsOk():
                                        Client_GlobalData.app.friendEntrySound.Play()
                                    else:
                                        print 'Cannot find friendEntrySound!'
                                except:
                                    pass
                            # logoff
                            else:
                                try:
                                    if Client_GlobalData.app.friendExitSound.IsOk():
                                        Client_GlobalData.app.friendExitSound.Play()
                                    else:
                                        print 'Cannot find friendExitSound!'
                                except:
                                    pass
            if block_chat == False:
                if Client_GlobalData_Config.chat_save_to_db == True:
                    # only want to save user chat
                    if len(chatString) > 11 and chatString[11] == "<":
                        sql_chat_string = chatString.decode("utf8").replace("\"","'")
                        sql_chat_string = sql_chat_string.split(">")[1].lstrip()
                        sql_args = sql_chat_string,time.strftime("%Y-%m-%d %H:%M:%S"),user_name.split(" ")[1]
                        Client_Database.SQL_MameHub_Arrange_Chat(u"insert into chat_log (id,chat_text,chat_time,chat_user) values (NULL,?,?,?)",sql_args)
                # play chime if option is set and name is typed
                if Client_GlobalData_Config.chime_on_chat_name == True and chatString[0] != "*":
                    try:
                        if chatString.split(">",1)[1].count(Client_GlobalData.player.username) > 0:
                            if Client_GlobalData.player.AFK == False and Client_GlobalData_Config.mute_chat_sounds == False:
                                if Client_GlobalData.app.chimeSound.IsOk():
                                    Client_GlobalData.app.chimeSound.Play()
                                else:
                                    print 'Cannot find chimeSound!'
                    except:
                        pass
                chatString = ProcessChatString(chatString)
                '''
                #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<span style=\"font-family: "+Client_GlobalData_Config.chat_font.lower()+"; font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt; color: rgb" + Client_GlobalData_Config.chat_font_color + ";\">" + chatString.decode("utf8") + "</span>"
                #print "chat",Client_GlobalData.chatHTML
                #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt; color: rgb" + Client_GlobalData_Config.chat_font_color + "; font-family:"+Client_GlobalData_Config.chat_font+";\">" + chatString.decode("utf8") + "</span>"
                #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\">" + chatString.decode("utf8") + "</font>"
                scrollPosition = Client_GlobalData.app.mainFrame.chatLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1]
                scrollBottomPosition = (Client_GlobalData.app.mainFrame.chatLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])+Client_GlobalData.app.mainFrame.chatLogHTML.GetClientSize()[1]
##                scroll_bottom = False
##                #print scrollBottomPosition, Client_GlobalData.app.mainFrame.chatLogHTML.GetVirtualSize()[1]
##                if scrollBottomPosition+30 >= Client_GlobalData.app.mainFrame.chatLogHTML.GetVirtualSize()[1]:
##                    scroll_bottom = True
                Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>")
##                #print scroll_bottom
##                if scroll_bottom == True:
##                    Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(-1, scrollBottomPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
##                else:
##                    Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(0, scrollPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
                Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(-1, scrollBottomPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
                '''
                Client_GlobalData.app.mainFrame.chatLogHTML.Freeze()
                if Client_GlobalData.webkit_enabled == False:
                    Client_GlobalData.app.mainFrame.chatLogHTML.AppendToPage("<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>")
                else:
                    Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>"
                    Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>","")
                Client_GlobalData.app.mainFrame.chatLogHTML.Thaw()

        # lfg is a challege from chat
        elif messageWords[0]=="LFG":
            if Client_GlobalData.player and Client_GlobalData.player.AFK==False and Client_GlobalData_Config.mute_chat_sounds == False:
                if Client_GlobalData.app.challengeSound.IsOk():
                    Client_GlobalData.app.challengeSound.Play()
                else:
                    print 'Cannot find challengeSound!'
            timeString = datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S")
            chatString = "["+timeString+"] " + data[len("LFG "):]
            #Client_GlobalData.app.mainFrame.chatLog.AppendText(chatString.decode("utf8"))
            chatString = chatString.replace("<","&lt;")
            chatString = chatString.replace(">","&gt;")
            chatString = chatString.replace("*", "&#42;")
            '''
            Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>"
            #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<br /><font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\">" + chatString.decode("utf8") + "</font><br />"
            #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\">" + chatString.decode("utf8") + "<br /></font>"
            #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"px\; color: rgb+" + Client_GlobalData_Config.chat_font_color + "; font-family:"+Client_GlobalData_Config.chat_font+";\">" + chatString.decode("utf8") + "</span>"
            #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<span style=\"font-family: "+Client_GlobalData_Config.chat_font+"; font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt; color: rgb" + Client_GlobalData_Config.chat_font_color + ";\">" + chatString.decode("utf8") + "</span>"
            #Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt; color: rgb" + Client_GlobalData_Config.chat_font_color + "; font-family:"+Client_GlobalData_Config.chat_font+";\">" + chatString.decode("utf8") + "</span>"
            scrollPosition = Client_GlobalData.app.mainFrame.chatLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1]
            scrollBottomPosition = (Client_GlobalData.app.mainFrame.chatLogHTML.GetViewStart()[1]*Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])+Client_GlobalData.app.mainFrame.chatLogHTML.GetClientSize()[1]
##            scroll_bottom = False
##            #print scrollBottomPosition, Client_GlobalData.app.mainFrame.chatLogHTML.GetVirtualSize()[1]
##            if scrollBottomPosition+30 >= Client_GlobalData.app.mainFrame.chatLogHTML.GetVirtualSize()[1]:
##                scroll_bottom = True
            Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>")
##            #print scroll_bottom
##            if scroll_bottom == True:
##                Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(-1, scrollBottomPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
##            else:
##                Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(0, scrollPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
            Client_GlobalData.app.mainFrame.chatLogHTML.Scroll(-1, scrollBottomPosition/Client_GlobalData.app.mainFrame.chatLogHTML.GetScrollPixelsPerUnit()[1])
            '''
            Client_GlobalData.app.mainFrame.chatLogHTML.Freeze()
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.chatLogHTML.AppendToPage("<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>")
            else:
                Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>"
                Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>","")
            Client_GlobalData.app.mainFrame.chatLogHTML.Thaw()
        # test
        elif messageWords[0]=="GAME_PLAY" or messageWords[0]=="GAME_CHALLENGE":
            if messageWords[0]=="GAME_PLAY":  # user wants to play x game
                timeString = datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S")
                if Client_GlobalData.player and Client_GlobalData.player.AFK==False and Client_GlobalData_Config.mute_chat_sounds == False:
                    if Client_GlobalData.app.playSound.IsOk():
                        Client_GlobalData.app.playSound.Play()
                    else:
                        print 'Cannot find playSound!'
                chatString = "["+timeString+"] " + data[len("GAME_PLAY "):].split(" ")[0] + " wants to play " + SQL_Retrieve_Game_Name(data[len("GAME_PLAY "):].split(" ",1)[1])
            else: # user wants to challenge x game
                if Client_GlobalData.player and Client_GlobalData.player.AFK==False and Client_GlobalData_Config.mute_chat_sounds == False:
                    if Client_GlobalData.app.challengeSound.IsOk():
                        Client_GlobalData.app.challengeSound.Play()
                    else:
                        print 'Cannot find challengeSound!'
                chatString = "["+timeString+"] " + data[len("GAME_CHALLENGE "):].split(" ")[0] + " challenges everyone to " + SQL_Retrieve_Game_Name(data[len("GAME_CHALLENGE "):].split(" ",1)[1])
            chatString = chatString.replace("<","&lt;")
            chatString = chatString.replace(">","&gt;")
            chatString = chatString.replace("*", "&#42;")
            Client_GlobalData.app.mainFrame.chatLogHTML.Freeze()
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.chatLogHTML.AppendToPage("<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>")
            else:
                Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>"
                Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>","")
            Client_GlobalData.app.mainFrame.chatLogHTML.Thaw()
        # admin bans/kicks/etc
        elif messageWords[0]=="ADMIN_USER_KICK" or messageWords[0]=="ADMIN_USER_BAN_TEMP" or messageWords[0]=="ADMIN_USER_BAN_FULL":
            if messageWords[0]=="ADMIN_USER_KICK":
                dialog_message = "You've been kicked by an admin."
            elif messageWords[0]=="ADMIN_USER_BAN_TEMP":
                dialog_message = "You've been temp banned."
            else:
                dialog_message = "You've been permabanned."
            mdial = wx.MessageDialog(None, dialog_message, 'Server Disconnect.', wx.OK | wx.ICON_ERROR)
            mdial.ShowModal()
            mdial.Destroy()
            Client_GlobalData.app.mainFrame.Close(True)
            Client_GlobalData.app.mainFrame.exit(0)
        # inq on ban list
        elif messageWords[0]=="REQ_BAN_LIST":
            Client_GlobalData.generic_string = data.split(' ',1)[1]
            if len(Client_GlobalData.generic_string) > 0:
                dialog = BanDialog(Client_GlobalData.app.mainFrame)
                dialog.Show()
            else:
                mdial = wx.MessageDialog(None, 'There are no bans to display.', 'No Information.', wx.OK | wx.ICON_ERROR)
                mdial.ShowModal()
                mdial.Destroy()
        # admin events to show in chat
        elif messageWords[0] == "ADMIN_EVENT":
            timeString = datetime.datetime.time(datetime.datetime.now()).strftime("%H:%M:%S")
            chatString = "["+timeString+"] " + data[len("ADMIN_EVENT "):].replace("_"," ") + "<BR>"
            Client_GlobalData.app.mainFrame.chatLogHTML.Freeze()
            if Client_GlobalData.webkit_enabled == False:
                Client_GlobalData.app.mainFrame.chatLogHTML.AppendToPage("<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>")
            else:
                Client_GlobalData.chatHTML = Client_GlobalData.chatHTML + "<font size=\"" + str(Client_GlobalData_Config.chat_font_size) + "\" color=\"rgb" + Client_GlobalData_Config.chat_font_color + "\" face=\"" + Client_GlobalData_Config.chat_font + "\"><span style=\"font-size:"+str(Client_GlobalData_Config.chat_font_size)+"pt;\">" + chatString.decode("utf8") + "</span></font>"
                Client_GlobalData.app.mainFrame.chatLogHTML.SetPage("<html>" + Client_GlobalData.chatHTML + "</html>","")
            Client_GlobalData.app.mainFrame.chatLogHTML.Thaw()
        else:
            print 'Unknown Data:',data
