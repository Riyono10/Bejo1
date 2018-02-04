# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia, goslate
import html5lib
import timeit
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

import six

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse

cl = LINETCR.LINE()
cl.login(token="EpK8VOX3hHBFkhAdRT2a.q0ZUhecQjWOb4P2GDwpVUG.LAvxW3Kbr4h4TRYkW48PXa1tb20Hq+VXgbFQ3Caw4Ag=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="Epx8YjpnxtVL4ykPQZHe.MtQKnjOeeJ4QLUxcT/0+3G.KiaIV4N/kQbDcWoKDPcurbMIyl8kPL0FZ2Qiwhp4Eik=")
ki.loginResult()

#kk = LINETCR.LINE()
#kk.login(token="")
#kk.loginResult()

#kc = LINETCR.LINE()
#kc.login(token="")
#kc.loginResult()

#kl = LINETCR.LINE()
#kl.login(token="")
#kl.loginResult()

print "==================[Login Success]==================="
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●
║●▬ஜ۩★COMMAND★۩ஜ▬●
║[★]● Help1 [SOSMED]
║[★]● Help2 [SETTING]
║[★]● Help3 [GROUP]
║[★]● Help4 [SELFBOT]
║[★]● Help5 [PROTECT]
║[★]● Mystatus
║[★]● Prostatus
║[★]● Help1-Help5
║[★]● Promo
║  http://line.me/ti/p/H2VZm0LFeR
●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●"""

helppro ="""●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●
║●▬ஜ۩★PROTECT★۩ஜ▬●
║[★]●〘Protect on/off〙
║[★]●〘Qr on/off〙
║[★]●〘Invite on/off〙
║[★]●〘Cancel on/off〙
║[★]●〘Status set all on/off〙
║[★]●〘Mode protect on/off〙
║  http://line.me/ti/p/H2VZm0LFeR
●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●"""

helpself ="""●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●
║●▬ஜ۩★SELFBOT★۩ஜ▬●
║[★]●〘Me〙
║[★]●〘Bot contact〙
║[★]●〘Kicker contact〙
║[★]●〘Myname: 〙
║[★]●〘Mybio: 〙
║[★]●〘Myname〙
║[★]●〘Mybio〙
║[★]●〘Mypict〙
║[★]●〘Mycover〙
║[★]●〘Clone @[Tag]〙
║[★]●〘Backup〙
║[★]●〘Getgrup image〙
║[★]●〘Getmid @[Tag]〙
║[★]●〘Getprofile @[Tag]〙
║[★]●〘Getcontact @[Tag]〙
║[★]●〘Getinfo @[Tag]〙
║[★]●〘Getname @[Tag]〙
║[★]●〘Getbio @[Tag]〙
║[★]●〘Getpict @[Tag]〙
║[★]●〘Getvid @[Tag]〙
║[★]●〘Getcover @[Tag]〙
║[★]●〘Picturl @[Tag]〙
║[★]●〘Coverurl @[Tag]〙
║[★]●〘Time〙
║[★]●〘Checkdate〙
║[★]●〘Kalender〙
║[★]●〘Tagall〙
║[★]●〘Sider [on/off]〙
║[★]●〘Cek〙
║[★]●〘Sider〙
║[★]●〘Gift〙
║[★]●〘Kicker gift〙
║[★]●〘Gift1-Gift10 [Tag] 〙
║[★]●〘Mybio: 〙
║[★]●〘Myname〙
║[★]●〘Mimic on/off〙
║[★]●〘Micadd @[Tag]〙
║[★]●〘Micdel @[Tag]〙
║  http://line.me/ti/p/H2VZm0LFeR
●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●"""

helpset ="""●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●
║●▬ஜ۩★SETTING★۩ஜ▬●
║[★]●〘Status〙
║[★]●〘ProStatus〙
║[★]●〘Contact on/off〙
║[★]●〘Auto join on/off〙
║[★]●〘Auto leave on/off〙
║[★]●〘Auto add on/off〙
║[★]●〘Protect on/off〙
║[★]●〘Qr on/off〙
║[★]●〘Like on/off〙
║[★]●〘Jam on/off〙
║[★]●〘Invite on/off〙
║[★]●〘Cancel on/off〙
║[★]●〘Share on/off〙
║[★]●〘Respon on/off[Group]〙
║[★]●〘Respon pc on/off[PC]〙
║[★]●〘Greet join on/off〙
║[★]●〘Greet leave on/off〙
║[★]●〘Read on/off〙
║[★]●〘Simisimi on/off〙
║[★]●〘Like me〙
║[★]●〘Like friend〙
║  http://line.me/ti/p/H2VZm0LFeR
●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●"""

helpgrup ="""●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●
║●▬ஜ۩★GROUP★۩ஜ▬●
║[★]●〘Bye aku pamit dulu〙
║[★]●〘Come/In〙
║[★]●〘Bye/Out〙
║[★]●〘Kicker in〙
║[★]●〘Kicker bye〙
║[★]●〘Invite〙
║[★]●〘1invite-3invite〙
║[★]●〘Stay〙
║[★]●〘Kicker stay〙
║[★]●〘Url〙
║[★]●〘Cancel〙
║[★]●〘Gcreator〙
║[★]●〘Kick @[Tag]〙
║[★]●〘Ulti @[Tag]〙
║[★]●〘Cancel〙
║[★]●〘Gname: 〙
║[★]●〘Infogrup〙
║[★]●〘Gruplist〙
║[★]●〘LG/LG1/LG2〙
║[★]●〘Friendlist〙
║[★]●〘Gbroadcast: [Text]〙
║[★]●〘Cbroadcast: [Text]〙
║[★]●〘GbroadcastImage: 〙
║[★]●〘CbroadcastImage: [Text]〙
║[★]●〘Blocklist〙
║[★]●〘Ban @[Tag]〙
║[★]●〘Unban @[Tag]〙
║[★]●〘Clearban〙
║[★]●〘Banlist〙
║[★]●〘Contactban〙
║[★]●〘Midban〙
║  http://line.me/ti/p/H2VZm0LFeR
●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●"""

helpmed ="""●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●
║●▬ஜ۩★SOSMED★۩ஜ▬●
║[★]●〘kalender〙
║[★]●〘/id [Text]〙
║[★]●〘/en [Text]〙
║[★]●〘/jp [Text]〙
║[★]●〘/ko [Text]〙
║[★]●〘say-id 〙
║[★]●〘say-en 〙
║[★]●〘say-jp 〙
║[★]●〘say-ko 〙
║[★]●〘/cekig 〙
║[★]●〘/postig 〙
║[★]●〘Checkdate 〙
║[★]●〘wikipedia 〙
║[★]●〘Music 〙
║[★]●〘Lirik 〙
║[★]●〘Video 〙
║[★]●〘/image 〙
║[★]●〘/youtube 〙
║  http://line.me/ti/p/H2VZm0LFeR
●▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●"""

helprom ="""●▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●
║●▬ஜ۩★PROMOTION★۩ஜ▬●
║[★]● Rental SelfBot & ProtectBot
║[★]● SB + 5Assist + 3Kicker(Luar)
║[★]● SB + 5Assist + 2Kicker(Luar)
║[★]● SB + 5Assist + 1Kicker(Luar)
║[★]● SB + 3Assist + 1Kicker(Luar)
║[★]● SB + 5Assist 
║[★]● SB + 3Assist 
║[★]● SB Tanpa Assist
║[★]● ProtectBot 3-20 Bot Assist
║[★]● Pasang Siri V10 & V11
║        [👇 Minat Silahan hub👇]
║[★]● http://line.me/ti/p/H2VZm0LFeR
║[★]● http://line.me/ti/p/rGlnNi8lsn
║▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
║   [★R4D15T1&R4NGERS T34M★] 
║▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
●▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬●"""

mid = cl.getProfile().mid
Amid = ki.getProfile().mid
#Bmid = kk.getProfile().mid
#Cmid = kc.getProfile().mid
#mid1 = kl.getProfile().mid
Bots=[mid,Amid]
Creator = ["u0f4cbccff2b03754d07d8db8707023f6"]
administrator = [mid]
admin = [mid]
wait = {
    "likeOn":True,
    "alwayRead":False,
    "detectMention":True,    
    "detectMentionPc":True,
    "kickMention":False,
    "steal":True,
    'gift':{},
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks For Add Me 🙏🙏😊😊",
    "lang":"JP",
    "comment":"Haii Kakak",
    "commentOn":True,
    "Sambutan":True,
    "SambutanLv":True,
    "commentBlack":{},
    "winvite" :False,
    "winvite2" :False,
    "wblack":False,
    "dblack":False,
    "clock":False,
    "alwaysRead":False,
    "Sider":{},
    "cNames":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage                        
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup2 = ki.getProfile()
backup2.displayName = contact.displayName
backup2.statusMessage = contact.statusMessage                        
backup2.pictureStatus = contact.pictureStatus

#contact = kk.getProfile()
#backup3 = kk.getProfile()
#backup3.displayName = contact.displayName
#backup3.statusMessage = contact.statusMessage                        
#backup3.pictureStatus = contact.pictureStatus

#contact = kc.getProfile()
#backup3 = kc.getProfile()
#backup3.displayName = contact.displayName
#backup3.statusMessage = contact.statusMessage                        
#backup3.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs) 
    
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
         
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')

        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMentionPc"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                     balas = [" Aku masih Sibuk Jangan Tag dulu ya\nKalo Penting P M aja ya ☞   ",cName + " Dont Tag Me please!! Im Busy ☞ ",cName + " Ngapain Ngetag Kak?\nKalo perlu penting P c aja ya ☞ ",cName + " Nggak Usah Tag-Tag mulu!!\nKalo Penting Langsung P C Aja Kak ☞ ",cName + " Kenapa Tag Aku kak?\nKalo penting PC Aja Ya ☞ "]
                     ret_ = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     tts = gTTS(text=ret_, lang='id')
                     tts.save('tts.mp3')
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.from_,ret_ + cName)
                                  cl.sendAudio(msg.from_,'tts.mp3')
                                  cl.sendImageWithURL(msg.from_,image)
                                  break            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                     balas = [" Aku masih Sibuk Jangan Tag dulu ya\nKalo Penting p c aja ya ☞   ",cName + " Dont Tag Me!! Im Busy ☞ ",cName + " Ngapain Ngetag Kak?\nKalo perlu penting P c aja ya ☞ ",cName + " Nggak Usah Tag-Tag mulu!!\nKalo Penting Langsung P C Aja Kak ☞ ",cName + " Kenapa Tag Aku kak?\nKalo penting P C Aja Ya ☞ "]
                     ret_ = "" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     tts = gTTS(text=ret_, lang='id')
                     tts.save('tts.mp3')
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_ + cName)
                                  cl.sendAudio(msg.to,'tts.mp3')
                                  cl.sendImageWithURL(msg.to,image)
                                  break

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [" Dont Tag Me!! Im Busy ☞ ",cName + " Ngapain Ngetag?klo perlu penting Pc aja ☞ ",cName + " Nggak Usah Tag-Tag mulu!!Kalo Penting Langsung PC Aja Guys ☞ ",cName + " Kenapa Tag saya?Klo penting PC Aja Bro ☞ "]
                     ret_ = "[Kick Respon] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
              if wait["winvite"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = cl.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      cl.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      cl.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        cl.inviteIntoGroup(msg.to,[target])
                        cl.sendText(msg.to,"Already Invited Done✔ Bro: \n➡" + _name)
                        wait["winvite"] = False
                        break
                      except:
                        try:
                          cl.findAndAddContactsByMid(invite)
                          cl.inviteIntoGroup(op.param1,[invite])
                          wait["winvite"] = False
                        except:
                          try:
                            cl.findAndAddContactsByMid(invite)
                            cl.inviteIntoGroup(op.param1,[invite])
                            wait["winvite"] = False
                            cl.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              cl.findAndAddContactsByMid(invite)
                              cl.inviteIntoGroup(op.param1,[invite])
                              wait["winvite"] = False
                              cl.sendText(msg.to,"Done ✔ Bro \n➡" + _name)
                              break
                            except:
                              cl.sendText(msg.to,"Negative, Error detected")
                              wait["winvite"] = False
                              break
              elif wait["winvite1"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ki.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ki.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ki.sendText(msg.to,"Remove User From Blacklist Done✔" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ki.findAndAddContactsByMid(target)
                        ki.inviteIntoGroup(msg.to,[target])
                        ki.sendText(msg.to,"Already Invited Done✔: \n➡" + _name)
                        wait["winvite1"] = False
                        break
                      except:
                        try:
                          ki.findAndAddContactsByMid(invite)
                          ki.inviteIntoGroup(op.param1,[invite])
                          wait["winvite1"] = False
                        except:
                          try:
                            ki.findAndAddContactsByMid(invite)
                            ki.inviteIntoGroup(op.param1,[invite])
                            wait["winvite1"] = False
                            ki.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ki.findAndAddContactsByMid(invite)
                              ki.inviteIntoGroup(op.param1,[invite])
                              wait["winvite1"] = False
                              ki.sendText(msg.to,"Done ✔  \n➡" + _name)
                              break
                            except:
                              ki.sendText(msg.to,"Negative, Error detected")
                              wait["winvite1"] = False
                              break
              elif wait["winvite2"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kk.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kk.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kk.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kk.sendText(msg.to,"Remove User From Blacklist Done✔" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kk.findAndAddContactsByMid(target)
                        kk.inviteIntoGroup(msg.to,[target])
                        kk.sendText(msg.to,"Already Invited Done✔Bro : \n➡" + _name)
                        wait["winvite2"] = False
                        break
                      except:
                        try:
                          kk.findAndAddContactsByMid(invite)
                          kk.inviteIntoGroup(op.param1,[invite])
                          wait["winvite2"] = False
                        except:
                          try:
                            kk.findAndAddContactsByMid(invite)
                            kk.inviteIntoGroup(op.param1,[invite])
                            wait["winvite2"] = False
                            kk.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kk.findAndAddContactsByMid(invite)
                              kk.inviteIntoGroup(op.param1,[invite])
                              wait["winvite2"] = False
                              kk.sendText(msg.to,"Done ✔  Bro \n➡" + _name)
                              break
                            except:
                              kk.sendText(msg.to,"Negative, Error detected")
                              wait["winvite2"] = False
                              break
                              
              elif wait["winvite3"] == True:
                #if msg.from_ in owner:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kk.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kk.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kk.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kk.sendText(msg.to,"Remove User From Blacklist Done✔" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kk.findAndAddContactsByMid(target)
                        kk.inviteIntoGroup(msg.to,[target])
                        kk.sendText(msg.to,"Already Invited Done✔Bro : \n➡" + _name)
                        wait["winvite3"] = False
                        break
                      except:
                        try:
                          kk.findAndAddContactsByMid(invite)
                          kk.inviteIntoGroup(op.param1,[invite])
                          wait["winvite3"] = False
                        except:
                          try:
                            kk.findAndAddContactsByMid(invite)
                            kk.inviteIntoGroup(op.param1,[invite])
                            wait["winvite3"] = False
                            kk.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kk.findAndAddContactsByMid(invite)
                              kk.inviteIntoGroup(op.param1,[invite])
                              wait["winvite3"] = False
                              kk.sendText(msg.to,"Done ✔  Bro \n➡" + _name)
                              break
                            except:
                              kk.sendText(msg.to,"Negative, Error detected")
                              wait["winvite3"] = False
                              break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass
                                
            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break
                                
            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Bots:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"HELLO KAK ☞ " + cl.getContact(op.param2).displayName +" ☜"+ "\n[🙋 WELCOME TO GROUP 🙋]\n☞ " + str(ginfo.name) + " ☜" +"\n[👑 OWNER CREATOR GROUP 👑]\n☞ "+ginfo.creator.displayName+" ☜"+"\n▶Budayakan Baca Note Ya kak\n▶Dilarang Nikung😁😁😁\n▶No Baber😜😜😜\n▶Salam Cipok😘😘😘")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
        if op.type == 15:
          if wait["SambutanLv"] == True:
            if op.param2 in Bots:
                return
            cl.sendText(op.param1,"[Good Bye 🙋🙋Kak]☞ " + cl.getContact(op.param2).displayName +  "\nSee You Next Time Kak. . . 😘😘😘 ")
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                                else:
                                    cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass 
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpmsg)
                else:
                    cl.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'help5':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helppro)
                else:
                    cl.sendText(msg.to,helppro)
            elif msg.text.lower() == 'help4':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpself)
                else:
                    cl.sendText(msg.to,helpself)
            elif msg.text.lower() == 'help3':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpgrup)
                else:
                    cl.sendText(msg.to,helpgrup)
            elif msg.text.lower() == 'help2':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpset)
                else:
                    cl.sendText(msg.to,helpset)
            elif msg.text.lower() == 'help1':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpmed)
                else:
                    cl.sendText(msg.to,helpmed)
            elif msg.text.lower() == 'promo':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helprom)
                else:
                    cl.sendText(msg.to,helprom)
            elif msg.text.lower() == 'sp':
                cl.sendText(msg.to, "「Speed My SelfBot」")
                start = time.time()
                time.sleep(0.002)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "☞「 Speed SelfBot 」\n☞ Type: Speed\n☞ Speed : %sseconds" % (elapsed_time))
            elif msg.text.lower() == 'speed':
                cl.sendText(msg.to, "「Speed My SelfBot」")
                start = time.time()
                time.sleep(0.002)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "☞「 Speed SelfBot 」\n☞ Type: Speed\n☞ Speed : %sseconds" % (elapsed_time))
            elif msg.text.lower() == 'chrash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u0f4cbccff2b03754d07d8db8707023f6',"}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'bot contact':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentType = 13
            elif msg.text.lower() == 'kicker contact':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid1}
                kl.sendMessage(msg)
                msg.contentType = 13
            elif msg.text.lower() == 'creator contact':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Creator}
                cl.sendMessage(msg)
                msg.contentType = 13
#========================== B O T ``C O M M A N D =============================#
#==============================================================================#
            elif msg.text.lower() == 'status set all on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto join already set to ON [✔]")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto join Already set to ON [✔]")
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Already  room set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already On [✔]")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Already room set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already On [✔]")
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Joined Already On [✔]")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Joined Already On [✔]")
                if wait["SambutanLv"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Leave Already On [✔]")
                else:
                    wait["SambutanLv"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Leave Already On [✔]")
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Already set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Share already set to On [✔]")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Already set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Share already On [✔]")
                if wait["steal"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Steal Already set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Steal Already On [✔]")
                else:
                    wait["steal"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Steal Share contact set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Steal Share contact already On [✔]")
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Add Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Add already ON [✔]")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Add Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto  Add Already set to ON [✔]")
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Like already Set to ON [✔]")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Like Already set to ON [✔]")
                if wait["alwayRead"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Read Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Read Already ON [✔]")
                else:
                    wait["alwayRead"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Read Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto  Read Already set to ON [✔]")
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Respon Already Set to ON [✔]")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto ResponAlready set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Respon Already set to ON [✔]")
                if wait["detectMentionPc"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Respon Already Set to ON [✔]")
                else:
                    wait["detectMentionPc"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon PC Already set to ON [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Respon  PC Already set to ON [✔]")
            elif msg.text.lower() == 'status set all off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Contact Already set to Off [✖]")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Contact Already set to Off [✖]")
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto join already set to Off [✖]")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto join Already set to Off [✖]")
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Already  room set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already On Off [✖]")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Already room set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already Off [✖]")
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet joined Already Off [✖]")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet joined Already Off [✖]")
                if wait["SambutanLv"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Leave Already Off [✖]")
                else:
                    wait["SambutanLv"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Leave Already Off [✖]")
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Share already set to Off [✖]")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Share already Off [✖]")
                if wait["steal"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Steal Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Steal Already Off [✖]")
                else:
                    wait["steal"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Steal Share contact set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Steal Share contact already Off [✖]")
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Add Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Add already Off [✖]")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Add Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto  Add Already set to Off [✖]")
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Like already Set to Off [✖]")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Like Already set to Off [✖]")
                if wait["alwayRead"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Read Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Read Already Off [✖]")
                else:
                    wait["alwayRead"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Read Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto  Read Already set to Off [✖]")
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Respon Already Set to Off [✖]")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto ResponAlready set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Respon Already set to Off [✖]")
                if wait["detectMentionPc"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Respon Already Set to Off [✖]")
                else:
                    wait["detectMentionPc"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Respon PC Already set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Respon  PC Already set to Off [✖]")
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Contact Already set to On [✔]")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Contact already Off [✖]")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Contact already Off [✖]")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection already On [✔]")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection already On [✔]")
            elif msg.text.lower() == 'qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Qr already On [✔]")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Qr already On [✔]")
            elif msg.text.lower() == 'invite on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Invite already On [✔]")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Invite already On [✔]")
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already On [✔]")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already On [✔]")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto join already On [✔]")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto join already On [✔]")
            elif msg.text.lower() == 'mode protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection already On [✔]")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection already On [✔]")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Qr already On [✔]")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Qr already On [✔]")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Invite already On [✔]")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Protection Invite already On [✔]")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already On [✔]")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already On [✔]")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Autojoin already Off [✖]")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto join already Off [✖]")
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Protection already Off [✖]")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Protection already Off [✖]")
            elif msg.text.lower() == 'qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Protection Qr already Off [✖]")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Protection Qr already Off [✖]")
            elif msg.text.lower() == 'invite off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Protection Invite already Off [✖]")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Protection Invite already Off [✖]")
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already Off [✖]")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already Off [✖]")
            elif "Grup cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Grup cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar")
                    else:
                        cl.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'auto leave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already On [✔]")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already On [✔]")
            elif msg.text.lower() == 'auto leave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already Off [✖]")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already Off [✖]")
            elif msg.text.lower() == 'share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Share already On [✔]")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Share already On [✔]")
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Share already Off [✖]")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Share already Off [✖]")
            elif msg.text in ["Greet join on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet joinned already On [✔]")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet joinned already On [✔]")
            elif msg.text in ["Greet join off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet joinned already Off [✖]")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet joinned already Off [✖]")
            elif msg.text in ["Greet leave on"]:
                if wait["SambutanLv"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Leave already On [✔]")
                else:
                    wait["SambutanLv"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Leave already On [✔]")
            elif msg.text in ["Greet leave off"]:
                if wait["SambutanLv"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet Leave already Off [✖]")
                else:
                    wait["SambutanLv"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Greet joinned already Off [✖]")
            elif msg.text.lower() == 'steal on':
                if wait["steal"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Share already On [✔]")
                else:
                    wait["steal"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Share already On [✔]")
            elif msg.text.lower() == 'steal off':
                if wait["steal"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Steal set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Steal already Off [✖]")
                else:
                    wait["steal"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Steal set to off [✖]")
                    else:
                        cl.sendText(msg.to,"Steal already off [✖]")
            elif "Sider on" in msg.text:
#	      if msg.from_ in Creator:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Cek Sider On [✔]")
                
            elif "Sider off" in msg.text:
#	      if msg.from_ in Creator:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off [✖]")
                else:
                    cl.sendText(msg.to, "Heh Belom Di Set")
            elif msg.text.lower() == 'status':
                md = "╔═══════════════\n║★ STATUS  SELFBOT ★\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                if wait["contact"] == True: md+="║[★]Contact [On] ✔\n"
                else: md+="║[★]Contact [Off] ✖\n"
                if wait["autoJoin"] == True: md+="║[★]Auto Join [On] ✔\n"
                else: md +="║[★]Auto Join [Off] ✖\n"
                if wait["autoCancel"]["on"] == True:md+="􀠁􀆩􏿿║Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "║[★]Group cancel [Off] ✖\n"
                if wait["leaveRoom"] == True: md+="║[★]Auto leave [On] ✔\n"
                else: md+="║[★]Auto leave [Off]✖\n"
                if wait["Sambutan"] == True: md+="║[★]Greet join [On] ✔\n"
                else: md+="║[★]Greet join [Off] ✖\n"
                if wait["SambutanLv"] == True: md+="║[★]Greet Leave [On]✔\n"
                else: md+="║[★]Greet Leave [Off] ✖\n"
                if wait["timeline"] == True: md+="║[★]Share [On] ✔\n"
                else:md+="║[★]Share [Off] ✖\n"
                if wait["steal"] == True: md+="║[★]Steal [On] ✔\n"
                else:md+="║[★]Steal [Off] ✖\n"
                if wait["autoAdd"] == True: md+="║[★]Auto add [On] ✔\n"
                else:md+="║[★]Auto add [Off] ✖\n"
                if wait["likeOn"] == True: md+="║[★]Auto like [On] ✔\n"
                else:md+="║[★]Auto like [Off]\n"
                if wait["alwayRead"] == True: md+="║[★]Read [On] ✔\n"
                else:md+="║[★]Read [Off] ✖\n"
                if wait["detectMention"] == True: md+="║[★]Auto Respon [On] ✔\n"
                else:md+="║[★]Auto Respon [Off] ✖\n"
                if wait["detectMentionPc"] == True: md+="║[★]Auto Respon PC [On] ✔\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║★ R4D15T1 T34M ★\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                else:md+="║[★]Auto Respon PC [Off] ✖\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║★ R4D15T1 T34M ★\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                cl.sendText(msg.to,md)
            elif msg.text.lower() == 'prostatus':
                md = "╔═══════════════\n║★STATUS PROTECT★\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                if wait["protect"] == True: md+="║[★]Protect [On] ✔\n"
                else:md+="║[★]Protect [Off] ✖\n"
                if wait["linkprotect"] == True: md+="║[★]Link Qr Protect [On] ✔\n"
                else:md+="║[★]Link Qr Protect [Off] ✖\n"
                if wait["inviteprotect"] == True: md+="║[★]Invite Protect [On] ✔\n"
                else:md+="║[★]Invite Protect [Off] ✖\n"
                if wait["cancelprotect"] == True: md+="║[★]Cancel Protect [On] ✔\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║★ R4D15T1 T34M ★\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                else:md+="║[★]Cancel Protect [Off] ✖\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n║★ R4D15T1 T34M ★\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n╚═══════════════"
                cl.sendText(msg.to,md) 
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u0f4cbccff2b03754d07d8db8707023f6"}
                cl.sendMessage(msg)
                cl.sendMessage(msg.to,"👆👆He is my Creator👆👆👆")
            elif msg.text.lower() == 'auto add on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto add already On [✔]")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to On [✔]")
                    else:
                        cl.sendText(msg.to,"Auto add already On [✔]")
            elif msg.text.lower() == 'auto add off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto add already Off [✖]")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to Off [✖]")
                    else:
                        cl.sendText(msg.to,"Auto add already Off [✖]")
            elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                cl.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Comment on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di")
                    else:
                        cl.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Actived")
                    else:
                        cl.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text.lower() == 'mode protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to Off✔")
                    else:
                        cl.sendText(msg.to,"Protection already Off✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to Off✔")
                    else:
                        cl.sendText(msg.to,"Protection already Off✔")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to Off✔")
                    else:
                        cl.sendText(msg.to,"Protection Qr already Off✔")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to Off✔")
                    else:
                        cl.sendText(msg.to,"Protection Qr already Off✔")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to Off✔")
                    else:
                        cl.sendText(msg.to,"Protection Invite already Off✔")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to Off✔")
                    else:
                        cl.sendText(msg.to,"Protection Invite already Off✔")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to Off✔")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already Off✔")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to Off✔")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already Off✔")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"The following is a blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Jam")
#==============================================================================#
#==============================================================================#
            elif msg.text in ["Invite"]:
              if msg.from_ in owner:
                wait["winvite"] = True
                cl.sendText(msg.to,"Share contact your friends Bro")
                
            elif msg.text in ["1invite"]:
              if msg.from_ in owner:
                wait["winvite1"] = True
                ki.sendText(msg.to,"Share contact your friends Bro")
                
            elif msg.text in ["2invite"]:
              if msg.from_ in owner:
                wait["winvite2"] = True
                kk.sendText(msg.to,"Share contact your friends Bro")
                
            elif msg.text in ["3invite"]:
              if msg.from_ in owner:
                wait["winvite2"] = True
                kk.sendText(msg.to,"Share contact your friends Bro")
            
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["like on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to ON [✔]")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to ON [✔]")
                        
            elif msg.text in ["Like off","like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to Off [✔]")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like Already set to Off [✔]")
                        
            elif msg.text in ["My simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["My simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["Read on","read on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"Auto Sider ON [✔] ")
                
            elif msg.text in ["Read off","read off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"Auto Sider Off [✔]")
                
            elif msg.text in ["Respon on","respon on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Auto Respon ON [✔]")
                
            elif msg.text in ["Respon off","respon off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Auto Respon Off [✔]")
                
            elif msg.text in ["Respon pc on","Respon pc on"]:
                wait["detectMentionPc"] = True
                cl.sendText(msg.to,"Auto Respon to PC ON [✔]")
                
            elif msg.text in ["Respon pc off","respon pc off"]:
                wait["detectMentionPc"] = False
                cl.sendText(msg.to,"Auto Respon to PC Off [✔]")
            
            elif msg.text in ["Tag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"[AUTO RESPOND] Auto Kick yang tag ON")
                
            elif msg.text in ["Tag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"[AUTO RESPOND] Auto Kick yang tag OFF")
#==============================================================================#
            elif "らたかn" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("らたかn","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendMessage(msg.to,"Grup Dibersihkan")
            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif ("Ulti " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            
            elif 'invite ' in msg.text.lower():
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
            
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak ada undangan")
                        else:
                            cl.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'url on':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'url off':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","Gurl"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif "Gcreator" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'invite:gcreator':
                if msg.toType == 2:
                       ginfo = cl.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           cl.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           cl.inviteIntoGroup(msg.to,[gcmid])
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(X)
            
            elif msg.text.lower() == 'infogrup':        
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
                
            elif msg.text.lower() == 'grup id1':
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ki.getGroup(i).name,i)
                ki.sendText(msg.to,h)
                
            elif msg.text.lower() == 'grup id2':
                gid = kk.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (kk.getGroup(i).name,i)
                kk.sendText(msg.to,h)
            
            elif msg.text.lower() == 'grup id2':
                gid = kc.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (kk.getGroup(i).name,i)
                kc.sendText(msg.to,h)
#==============================================================================#
            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="☀☀☀☀☀☀☀LIST FRIEND☀☀☀☀☀☀☀"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀LIST FRIEND☀☀☀☀☀☀☀\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="☀☀☀☀☀☀☀LIST MEMBER☀☀☀☀☀☀☀"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀LIST MEMBER☀☀☀☀☀☀☀\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Grupmember: " in msg.text:
                saya = msg.text.replace('Grupmember: ','')
                gid = cl.getGroupIdsJoined()
                num=1
                msgs="☀☀☀☀☀☀☀LIST MEMBER☀☀☀☀☀☀☀"
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    me = gna.members(i)
                    msgs+="\n[%i] %s" % (num, me.displayName)
                    num=(num+1)
                    msgs+="\n☀☀☀☀☀☀☀LIST MEMBER☀☀☀☀☀☀☀\nTotal Members : %i" % len(me)
                    if h == saya:
                        cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="☀☀☀☀☀☀☀LIST FRIEND MID☀☀☀☀☀☀☀"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀LIST FRIEND MID☀☀☀☀☀☀☀\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="☀☀☀☀☀☀☀LIST BLOCKED☀☀☀☀☀☀☀"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀LIST BLOCKED☀☀☀☀☀☀☀\nTOTAL BLOCKED : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["LG"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="☀☀☀☀☀☀☀LIST GROUP ID☀☀☀☀☀☀☀"
                for ids in kontak:
                    msgs+="\n║[★] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀LIST GROUP ID☀☀☀☀☀☀☀\n\nTOTAL GROUP : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["LG1"]:   
                gruplist = ki.getGroupIdsJoined()
                kontak = ki.getGroups(gruplist)
                num=1
                msgs="☀☀☀☀☀☀☀LIST GROUP ID☀☀☀☀☀☀☀"
                for ids in kontak:
                    msgs+="\n║[★] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀LIST GROUP ID☀☀☀☀☀☀☀\n\nTOTAL GROUP : %i" % len(kontak)
                ki.sendText(msg.to, msgs)
                
            elif msg.text in ["LG2"]:   
                gruplist = kk.getGroupIdsJoined()
                kontak = kk.getGroups(gruplist)
                num=1
                msgs="☀☀☀☀☀☀☀[LIST GROUP ID]☀☀☀☀☀☀☀"
                for ids in kontak:
                    msgs+="\n║[★] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀[LIST GROUP ID]☀☀☀☀☀☀☀\n\nTOTAL GROUP : %i" % len(kontak)
                kk.sendText(msg.to, msgs)
                
            elif msg.text in ["LG2"]:   
                gruplist = kc.getGroupIdsJoined()
                kontak = kc.getGroups(gruplist)
                num=1
                msgs="☀☀☀☀☀☀☀[LIST GROUP ID]☀☀☀☀☀☀☀"
                for ids in kontak:
                    msgs+="\n║[★] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n☀☀☀☀☀☀☀[LIST GROUP ID]☀☀☀☀☀☀☀\n\nTOTAL GROUP : %i" % len(kontak)
                kc.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID GROUP : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (cl.getGroup(i).name +"║[★]["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"☀☀☀☀☀☀☀[LIST GROUP]☀☀☀☀☀☀☀\n"+ h +"\nTOTAL GROUP =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'gcancel':
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
                         
            elif "Auto add" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.findAndAddContactsByMids(mi_d)
                cl.sendText(msg.to,"Success Add all")
#==============================================================================#
            elif "tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
                 
            elif msg.text in ["Come","In"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)                  
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Kicker come","Kicker in"]:
                  X = cl.getGroup(msg.to)                    
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0 
                  Ti = cl.reissueGroupTicket(msg.to)
                  kl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kl.updateGroup(G)
                  Ticket = kl.reissueGroupTicket(msg.to)
                 
            elif msg.text in ["Bye aku pamit dulu"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					cl.leaveGroup(msg.to)
                except:
                     pass
                  
            elif msg.text in ["Bye","Out"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					ki.leaveGroup(msg.to)
					kk.leaveGroup(msg.to)
					kc.leaveGroup(msg.to)
					cl.sendText(msg.to,"Bye bye🙋🙋🙋Assist...")
                except:
                     pass
                     
            elif msg.text in ["Kicker bye","kicker out"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
					kl.leaveGroup(msg.to)
					cl.sendText(msg.to,"Bye bye🙋🙋🙋Kicker...")
                except:
                     pass

            elif "cek" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Cek Sider already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "sider off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Cek Sider already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "sider" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Sider:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
            elif "Gbroadcast: " in msg.text:
                bc = msg.text.replace("Bc ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendText(i,"☀☀☀☀☀[BROADCAST]☀☀☀☀☀\n\n"+bc+"\n\n#BROADCAST!!")
                    
            elif "Cbroadcast: " in msg.text:
                bc = msg.text.replace("Cbroadcast: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendText(i, bc)
            
            elif "GbroadcastImage: " in msg.text:
                bc = msg.text.replace("GbroadcastImage: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendImageWithURL(i, bc)
                    
            elif "CbroadcastImage: " in msg.text:
                bc = msg.text.replace("CbroadcastImage: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendImageWithURL(i, bc)
            
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
            
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                        
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            
            #elif msg.text.lower() in dangerMessage:
            #    if msg.toType == 2:
            #        try:
            #            cl.kickoutFromGroup(msg.to,[msg.from_])
            #        except:
            #            cl.kickoutFromGroup(msg.to,[msg.from_])
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["pap"])
#==============================================================================#
            elif '/image ' in msg.text:
                googl = msg.text.replace('/image ',"")

                url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl

                raw_html =  (download_page(url))

                items = []

                items = items + (_images_get_all_items(raw_html))

                path = random.choice(items)

                try:

                    start = timeit.timeit()

                    cl.sendImageWithURL(msg.to,path)

                    cl.sendText(msg.to, "Google Image \nType: Search Image\nWaktu dicari: %s" % (start) +"\nTotal Image Links = "+str(len(items)))

                    print "[Notif] Search Image Google Sucess"

                except Exception as e:

                    cl.sendText(msg.to, str(e))
            elif msg.text.lower() == 'mymid':
                cl.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Changed " + string + "")
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Changed " + string)
            elif msg.text in ["Myname"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"☀☀☀[DisplayName]☀☀☀\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"☀☀☀[StatusMessage]☀☀☀\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
            elif "Clone @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Clone @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Backup","backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
#==============================================================================#
            elif "/fancytext: " in msg.text.lower():
                txt = msg.text.replace("/fancytext: ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)
                 #-------------------------------------------------
            elif "/translate" in msg.text:
            	cl.sendText(msg.to,"contoh :\n- id to english : /en aku\n- english to id : /id you\n- id to japan : /jp halo\n- japan to id : /jpid kimochi\n- id to korea : /kor pagi\n- id to malaysia : /malay enak\n- id to arab : /arab jalan\n- id to jawa : /jawa kamu")
            elif "/id " in msg.text:
                isi = msg.text.replace("/id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "/en " in msg.text:
                isi = msg.text.replace("/en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "/jp " in msg.text:
                isi = msg.text.replace("/jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "/jpid " in msg.text:
                isi = msg.text.replace("/jpid ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "/kor " in msg.text:
                isi = msg.text.replace("/kor ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "/malay " in msg.text:
                isi = msg.text.replace("/malay ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ms')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "/arab " in msg.text:
                isi = msg.text.replace("/arab ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "/jawa " in msg.text:
                isi = msg.text.replace("/jawa ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='jw')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
#---------------------------------------------------------------
            elif "/removechat" in msg.text.lower():
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#---------------------------------------------------------
                
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
            
            elif '/video ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('/video ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            
            elif "/youtube " in msg.text:
              #if msg.from_ in admin:
                query = msg.text.replace("/Youtube: ","")
                cl.sendText(msg.to, "Searching...")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'https://www.youtube.com/results'
                    params = {'search_query':query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    loop = 1
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            if loop == 0:
                                cl.sendText(msg.to, a['title']+'\nhttps://www.youtube.com'+a['href'])
                                break
                            else:
                                loop = loop - 1
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "/cekig " in msg.text:
                    try:
                        instagram = msg.text.replace("/cekig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                        cl.sendImageWithURL(msg.to, profileIG)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
                        
            elif "/postig" in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                        
            elif msg.text.lower() == 'time':
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bulan = blan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text.lower() == 'kalender':
	    	    wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	            cl.sendText(msg.to, "KALENDER\n\n" + (wait2['setTime'][msg.to]))
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif msg.text.lower() == 'reboot':
                    print "[Command]Restart"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        cl.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
                
            elif msg.text.lower() == 'runtime':
                cl.sendText(msg.to,"「Please wait..」\nType  :Loading...\nStatus : Loading...")
                eltime = time.time() - mulai
                van = "Type : Bot Sedang Berjalan \nStatus : Aktif \nMySelbot sudah berjalan selama"+waktu(eltime)
                cl.sendText(msg.to,van)                    
#==============================================================================#
#==============================================================================#
            elif msg.text.lower() == 'stay':
              if msg.from_ in admin:
                profile = ki.getProfile()
                text = profile.displayName + "すでに保護している86(Already On Protect Group)"
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + "すでに保護している86(Already On Protect Group)"
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + "すでに保護している86(Already On Protect Group)"
                kc.sendText(msg.to, text)
            elif msg.text.lower() == 'kicker stay':
              if msg.from_ in admin:
                profile = kl.getProfile()
                text = profile.displayName + "すでに保護している86(Kicker Already Protect In Out side The Group)"
                kl.sendText(msg.to, text)
                kl.leaveGroup(msg.to)
		cl.sendText(msg.to,"[Bye bye🙋🙋🙋Kicker...]")
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
                
            elif ("Kicker gift " in msg.text):
              #if msg.from_ in owner:
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"] [0] ["M"]
                for x in key["MENTIONEES"]:
                  targets.append(x["M"])
                for target in targets:
                   try:
                       kl.sendText(msg.to,_name + " Check Your Gift By Me😘")
                       msg.contentType = 9
                       msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                            'STKVER': '1',
                                            'MSGTPL': '2',
                                            'STKPKGID': '9167'}
                       msg.to = target
                       msg.text = None
                       kl.sendMessage(msg)
                       gs = kl.getGroup(msg.to)
                       gs.preventJoinByTicket = True
                       kl.updateGroup(gs)
                       kl.leaveGroup(op.param1)
                       print (msg.to,[g.mid])
                   except:
                       kl.sendText(msg.to,"Done✔Please Check Message Gift For U\nBye Bye....😘😘😘😘")
                       gs = kl.getGroup(msg.to)
                       gs.preventJoinByTicket = True
                       kl.updateGroup(gs)
                       gs.preventJoinByTicket(gs)
                       kl.updateGroup(gs)
                       kl.leaveGroup(op.param1)
                   else:
                       cl.sendText(msg.to,"Error")

            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                cl.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                cl.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                cl.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    cl.sendText(msg.to,_name + " Not In Blacklist")
                                    
            elif msg.text in ["Clear"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text.lower() == 'ban:on':
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'unban:on':
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            #cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass       
#==============================================#
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        #cl.kickoutFromGroup(op.param1,[op.param2])
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    except:
                        try:
                            #cl.kickoutFromGroup(op.param1,[op.param2])
                            G = cl.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                        
                        
                        #ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False

                elif op.param3 in op.param3:
                    if op.param1 in protection:
                        OWN = "ub4ec190dc4450579d841fba7968311b4"
                    if op.param2 in OWN:
                        kicker1 = [cl,ki,kk,ks,kr,kl,km,kn,ko]
                        G = random.choice(kicker1).getGroup(op.param1)
                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)
                    else:
                        G = random.choice(kicker1).getGroup(op.param1)

                        #random.choice(kicker1).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        random.choice(kicker1).updateGroup(G)
                        Ticket = random.choice(kicker1).reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        random.choice(kicker1).updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        #cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass

        if op.type == 19:
            try:
                if op.param3 in Amid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        #cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        #ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        #ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        
                elif op.param3 in Amid:
                    if op.param2 in Bmid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        #kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in Cmid:
                    if op.param2 in Bimid:
                        G = kk.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)

                        
                        #kk.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        kk.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)


                elif op.param3 in Bmid:
                    if op.param2 in Cmid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        #ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in Cmid:
                        G = ks.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = ks.getGroup(op.param1)

                        
                        #ks.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ks.updateGroup(G)
                        Ticket = ks.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)

                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif op.param3 in Cmid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        #cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ks.updateGroup(G)
                        wait["blacklist"][op.param2] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)            
            except:
                pass
        if op.type == 32:
            if not op.param2 in Bots and admin:
                if wait["protect"] == True: 
                    try:
                        klist=[ki,kk]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        #kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    #cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    #cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            ki.cancelGroupInvitation(op.param1,[op.param3])
                            cl.sendText(op.param1,"Are U KICKER ☞ " + cl.getContact(op.param2).displayName +" ☜"+"\nWho do you want to invite???👊👊👊😡😡😡\nSorry your invited to cancel\nPlease Contact Admin Or Owner Group😡😡😡")
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    ki.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    ginfo = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    #cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(op.param1)
                    kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    #kl.kickoutFromGroup(op.param1,[op.param2])
                    X = kl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kl.updateGroup(X)
                    kl.leaveGroup(op.param1)
                    ki.sendText(op.param1,"Are U KICKER ☞ " + cl.getContact(op.param2).displayName +" ☜"+ "\nPlease Dont Playing Link QR Group Bro 😡😡😡👊👊👊")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param2}
                    kk.sendMessage(c)

        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    ginfo = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    #cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(op.param1)
                    kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    #kl.kickoutFromGroup(op.param1,[op.param2])
                    X = kl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kl.updateGroup(X)
                    kl.leaveGroup(op.param1)
                    ki.sendText(op.param1,"Are U KICKER ☞ " + cl.getContact(op.param2).displayName +" ☜"+ "\nPlease Dont Playing Link QR Group Bro 😡😡😡👊👊👊")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param2}
                    kk.sendMessage(c)

#==============================================================================#
#------------------------------------------------------------------------------#
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like"


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
