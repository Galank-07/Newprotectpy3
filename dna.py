# -*- coding: utf-8 -*-

from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import time,random,sys,json,codecs,threading,glob,re,os,subprocess
from datetime import datetime, timedelta
from humanfriendly import format_timespan, format_size, format_number, format_length
import requests
import datetime
import requests,urllib,json


#Khusus Login Qr
#ririn = LINE()
#ririn.log("Auth Token : " + str(ririn.authToken))
#ririn.log("Timeline Token : " + str(ririn.tl.channelAccessToken))

#Khusus Login Token
ririn = LINE('EsEacfkT0GULUY1GUGU5.qzjQVWZ0ZEOc9BUr4r9zrq.MPsltnq4KgeFuoJn35wrb3PozJ+JyJwWmPZfEAS2Buk=')
ririn.log("Auth Token : " + str(ririn.authToken))
ririn.log("Timeline Token : " + str(ririn.tl.channelAccessToken))

dna1 = LINE('EsmMahJSedRoWTAjlZGb.cY6+YCBCDcB6/j3HdvZCAW.JzHyvpp9UkAnxDofBajYZ4RqJWf5A2eWu3NcC1auZZs=')
dna1.log("Auth Token : " + str(dna1.authToken))
dna1.log("Timeline Token : " + str(dna1.tl.channelAccessToken))

dna2 = LINE('EswPaA5BOBJTsJYOn671.Sl2u8yHwWYZHMslzI9Bi8q.20nDyP69BtbKbjSH0g+Az8JIhjkvKDyF5cnu+TLbWJc=')
dna2.log("Auth Token : " + str(dna2.authToken))
dna2.log("Timeline Token : " + str(dna2.tl.channelAccessToken))

dna3 = LINE('EsEKNt02EJOcnTi6Xzx8.M53qiD/PJ1i6qsVfYwB7Ea.NaLIAwjUUJL6CgB0EDUFAPFuGYBt1Tfnu+Di90xex+w=')
dna3.log("Auth Token : " + str(dna3.authToken))
dna3.log("Timeline Token : " + str(dna3.tl.channelAccessToken))



startBot = time.time()
elapsed_time = format_timespan(time.time()-startBot)


helpMessage ="""
╔════════════════════╗
                    ✰ ᴅɴᴀ ʙᴏᴛ ✰
╚════════════════════╝
╔════════════════════╗
                ◄]·✪·Public·✪·[►
╠════════════════════╝
╠❂➣ Id
╠❂➣ Mid
╠════════════════════╗
                 ◄]·✪·Group·✪·[►
╠════════════════════╝
╠❂➣ Tutup qr
╠❂➣ Buka qr
╠❂➣ Invite 「mid」
╠❂➣ Ginfo
╠❂➣ Cancel
╠❂➣ White 「mention」
╠❂➣ Restart
╠❂➣ Guest 「On/Off」
╠❂➣ Qr 「On/Off」
╠❂➣ Lurking
╠❂➣ Kill
╠❂➣ Group bc 「text」
╠❂➣ Contact bc 「text」
╠❂➣ List group
╠❂➣ Speed
╠❂➣ Runtime
╠════════════════════╗
                ◄]·✪·Owner·✪·[►
╠════════════════════╝
╠❂➣ Bunuh 「mention」
╠❂➣ Kick 「mid」
╠❂➣ Bye dna
╠❂➣ Come dna
╠❂➣ Bye all
╠❂➣ Kill ban
╠❂➣ Ban 「mention」
╠❂➣ Unban 「mention」
╠❂➣ Banlist
╠❂➣ Clearban
╠❂➣ Tes
╠❂➣ Clear
╠════════════════════╗
                Credits by : D̶e̶e̶ ✯
╚════════════════════╝
╔════════════════════╗
                   ✰ ᴅɴᴀ ʙᴏᴛ  ✰
╚════════════════════╝
"""
oepoll = OEPoll(ririn)
KAC=[ririn,dna1,dna2,dna3]
mid = ririn.getProfile().mid
Amid = dna1.getProfile().mid
Bmid = dna2.getProfile().mid
Cmid = dna3.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["ueca4120a9d7b0e4a9e7f4f1b1b96a436"] 
owner=["ueca4120a9d7b0e4a9e7f4f1b1b96a436"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add me \n Creator line.me/ti/p/~mamanggd",
    "lang":"JP",
    "comment":"Thanks for add me \n Creator line.me/ti/p/~mamanggd",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "ririnock":True,
    "cName":"􀜁􀇔􏿿D͆̒̄ͧ́ͨ̀͠҉͈͓̳̞̬͓͈̖̲̰͚ ̡͉̜͓͓͉̖̺̌ͤ̅̈́̉͌ͅͅͅW̵̧̺̗̝ͥͧ̐ͨ͆͆ͯ͆͂̓ͣ̃ͣ͒ͬͬ̎ͮ͢ ̴̶̶̧̳̖̤͕͖͈̞͖͎͉̔̃̔͑ͧ̌̂ͫͬ̄͒̋̈́ͭ͐̽̆͘Ĩ̶̏͑ͤͯͦ̊̓̒́ͬͥ̽̀ͮ͑̓ͬ́҉̢̖̻̮͇̭͍",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":True,
    "acck":False,
    "spamer":{},
    "CloseQR":True,
    "Protectguest":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = ririn.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        ririn.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                ririn.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    ririn.sendText(op.param1,str(wait["message"]))

	#--------Open Qr Kick Start--------------#
        if op.type == 11:
            if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = ririn.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ririn.kickoutFromGroup(op.param1,[op.param2])
                   ririn.updateGroup(G)
	#--------Open Qr Kick Finish--------------#
	#--------Open Qr Auto Close---------------#
        if op.type == 11:
            if not op.param2 in Bots:
                if wait["CloseQR"] == True:
                  try:
                      kpist=[ririn]
                      puck=random.choice(kpist)
                      G = puck.getGroup(op.param1)
                      G.preventJoinByTicket = True
                      puck.updateGroup(G)
                  except Exception as e:
                      print(e)
	#--------Open Qr Auto Close---------------#
        if op.type == 13:
            if mid in op.param2:
                if wait["autoJoin"] == True:
                    if op.param2 in Bots:
                       G = ririn.getGroup(op.param1)
                       ririn.acceptGroupInvitation(op.param1)
	#--------Invite User Kick Start-----------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
	#------Invite User Kick Finish------------#
	#------Join Kicked start------------------#
        if op.type == 17:
            if wait["acck"] == True:
                if op.param2 not in admin:
                    try:
                        contact = ririn.getContact(op.param2)
                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except Exception as e:
                        print(e)
        #-------Join Kicked Finish----------------# 
	#-------Blacklist Join Kick Start---------#
        if op.type == 17:
           if op.param2 in wait["blacklist"]:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Kick Auto BL------------------------#
        if op.type == 19:
           if op.param2 not in admin:
              if op.param2 not in Bots:
                 if op.param2 not in wait["whitelist"]:
                    wait["blacklist"][op.param2] = True
                    print("kicker kicked")
                 else:
                    pass
        #--------------------Kick Auto Bl-------#
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = ririn.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ririn.updateGroup(X)
                        Ti = ririn.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ririn.updateGroup(X)
                        Ti = ririn.reissueGroupTicket(op.param1)

        if op.type == 13:
            print(op.param1)
            print(op.param2)
            print(op.param3)
            if mid in op.param3:
                G = ririn.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ririn.rejectGroupInvitation(op.param1)
                        else:
                            ririn.acceptGroupInvitation(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ririn.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ririn.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
           if op.param2 not in Bots:
               try:
                   ririn.kickoutFromGroup(op.param1,[op.param2])
               except:
                   try:
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                       random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                   except:
                       print ("bot Aktif")

        if op.type == 19:
           if op.param3 in admin:
               try:
                   ririn.kickoutFromGroup(op.param1,[op.param2])
                   ririn.inviteIntoGroup(op.param1,admin)
               except:
                   try:
                       random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                       random.choice(KAC).inviteIntoGroup(op.param1,admin)
                   except:
                       print ("bot bekerja")

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        ririn.inviteIntoGroup(op.param1,[op.param3])
                        ririn.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,Bots)
                        except:
                            print ("ririnient Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    ririn.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ririn.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ririn.updateGroup(X)
                    Ti = ririn.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
                        except:
                            print ("ririnientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ririn.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ririn.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("ririnientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ririn.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("ririnientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ririn.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ririn.updateGroup(X)
                    Ti = ririn.reissueGroupTicket(op.param1)
                    ririn.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = ririn.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ririn.rejectGroupInvitation(op.param1)
                        else:
                            ririn.acceptGroupInvitation(op.param1)
                    else:
                        ririn.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ririn.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ririn.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ririn.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
	#------Cancel User Kick start------#
        if op.type == 32:
            if op.param2 not in Bots:
               ririn.kickoutFromGroup(op.param1,[op.param2])
	#-------------------------------------#
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg._from
                if msg._from == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ririn.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = ririn.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            ririn.updateGroup(X)
                        except:
                            ririn.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ririn.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ririn.like(url[25:58], url[66:], likeType=1001)
#============================================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ririn.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ririn.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        ririn.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ririn.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ririn.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ririn.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        ririn.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    ririn.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ririn.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ririn.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ririn.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = ririn.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ririn.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ririn.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    ririn.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Keyword","help","Help"]:
               if msg._from in admin:
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,helpMessage)
                else:
                    ririn.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
               if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    ririn.updateGroup(X)
                else:
                    ririn.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bunuh " in msg.text):
               if msg._from in admin:
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  targets = []
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    try:
                        ririn.kickoutFromGroup(msg.to,[target])
                    except:
                      ririn.sendText(msg.to,"Semoga Tenang Di Luar Sana")
                      pass
            elif "Kick " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick ","")
                ririn.kickoutFromGroup(msg.to,[midd])
            elif "Kick2 " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick2 ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Kick3 " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick3 ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Kick4 " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Kick4 ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
               if msg._from in admin:
                midd = msg.text.replace("Invite ","")
                ririn.findAndAddContactsByMid(midd)
                ririn.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["List grup","List group","list grup","list group"]:
               if msg._from in admin:
                  ki.sendText(msg.to,"「Group」\n\nWaiting for : Group List")
                  gid = ririn.getGroupIdsJoined()
                  h = ""
                  for i in gid:
                      h += "║○%s\n" % (ririn.getGroup(i).name+"\n║Members: "+str(len(ririn.getGroup(i).members)))
                  ririn.sendText(msg.to,"╔═════¤|{ List Grup }|¤═════\n" + h + "╠═══════[  Total  ]════════\n║" + str(len(gid)) + "\n╚════════════════════")
            elif msg.text in ["Restart"]:
               if msg._from in admin:
                  ririn.sendText(msg.to, "Bot Have Been Restart")
                  restart_program()
                  print ("Restart")
            elif msg.text in ["cancel","Cancel"]:
               if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ririn.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"No one is inviting")
                        else:
                            ririn.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print ririn.getGroup(msg.to)
                ##ririn.sendMessage(msg)
            elif msg.text in ["Ourl","ourl"]:
               if msg._from in admin:
               	if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Done")
                    else:
                        ririn.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        ririn.sendText(msg.to,"Sudah Tertutup")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
              else:
                  ririn.sendText(msg.to,"Perintah Ditolak.")
                  ririn.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
            elif msg.text == "Ginfo":
               if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ririnose"
                        else:
                            u = "open"
                        ririn.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ririn.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                ririn.sendText(msg.to,msg.to)
            elif msg.text in ["Mid ku","mid ku","My mid","Mid saya"]:
                ririn.sendText(msg.to,msg._from)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                ririn.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ririn.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Cn " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = ririn.getProfile()
                    profile.displayName = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"Update Names " + string)
            elif "Mybio " in msg.text:
               if msg._from in admin:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 100000000000000:
                    profile = ririn.getProfile()
                    profile.statusMessage = string
                    ririn.updateProfile(profile)
                    ririn.sendText(msg.to,"()Update Bio→" + string + "←")
            elif msg.text in ["Pc On","pc on"]:
               if msg._from in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect Cancel On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"protect cancel On")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Pc Off","pc off"]:
               if msg._from in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect Cancel Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                         ririn.sendText(msg.to,"protect cancel  Off")
                    else:
                         ririn.sendText(msg.to,"done")
            elif msg.text in ["Guest On","guest on"]:
               if msg._from in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Guest Stranger On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Guest Stranger On")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
               if msg._from in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Guest Stranger Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                         ririn.sendText(msg.to,"Guest Stranger Off")
                    else:
                         ririn.sendText(msg.to,"done")
            elif msg.text in ["CloseQR On","ririnoseqr on"]:
               if msg._from in admin:
                if wait["CloseQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR ON")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["CloseQR Off","ririnoseqr off"]:
               if msg._from in admin:
                if wait["CloseQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["CloseQR"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Closed QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Acc on","acc on","A on","a on"]:
               if msg._from in admin:
                if wait["acck"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Udah aktif kak")
                    else:
                        ririn.sendText(msg.to,"Done")
                else:
                    wait["acck"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Anti Join Mode on")
                    else:
                        ririn.sendText(msg.to,"Done")
            elif msg.text in ["Acc off","acc off","A off","a off"]:
               if msg._from in admin:
                if wait["acck"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Sudah off kak")
                    else:
                        ririn.sendText(msg.to,"Done")
                else:
                    wait["acck"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Anti Join Mode off")
                    else:
                        ririn.sendText(msg.to,"Done")
            elif msg.text in ["Qr On","qr on"]:
               if msg._from in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR On")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR ON")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Qr Off","qr off"]:
               if msg._from in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Protect QR Off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
               if msg._from in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
               if msg._from in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
               if msg._from in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
               if msg._from in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
               if msg._from in admin:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            ririn.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            ririn.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            ririn.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Value is wrong")
                    else:
                        ririn.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
               if msg._from in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
               if msg._from in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
               if msg._from in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
               if msg._from in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
               if msg._from in admin:
                md = ""
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect QR	    : on\n"
                else: md+=" Protect QR	 : off\n"
                if wait["CloseQR"] == True: md+=" Closed QR : on\n"
                else: md+=" CloseQR   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                ririn.sendText(msg.to,md)
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
               if msg._from in admin:
                gid = ririn.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ririn.getGroup(i).name,i)
                ririn.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
               if msg._from in admin:
                gid = ririn.getGroupIdsInvited()
                for i in gid:
                    ririn.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ririn.sendText(msg.to,"All invitations have been refused")
                else:
                    ririn.sendText(msg.to,"Semua grup sudah dibatalkan")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
               if msg._from in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already on")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
               if msg._from in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"already off")
                    else:
                        ririn.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"done")
                    else:
                        ririn.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Buka qr","Open qr"]:
              if msg._from in admin:
                if msg.toType == 2:
                    X = ririn.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    ririn.updateGroup(X)
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        ririn.sendText(msg.to,"Sudah Terbuka")
                else:
                    if wait["lang"] == "JP":
                        ririn.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ririn.sendText(msg.to,"Not for use less than group")
              else:
                  ririn.sendText(msg.to,"Perintah Ditolak.")
                  ririn.sendText(msg.to,"Hanya Admin Yang bisa Gunain Perintah ini.")
	#-----------------------------------------------------------------#

            elif msg.text in ["Lurking","lurking"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        ririn.sendText(msg.to, "========HAI KANG NYIMAK========%s\n\nKamu tercyduk muehehehe👻👻👻👻\n[%s]" %(wait2['readMember'][msg.to],setTime[msg.to]))
                        print("ReadPoint Set...")
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        ririn.sendText(msg.to, "Kami telah memperbarui poin baca secara otomatis.")
                    else:
#                        ririn.sendText(msg.to, "Kami telah memperbarui poin baca secara otomatis.")
                        print("ReadPoint Set...")
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        ririn.sendText(msg.to, "Kami telah memperbarui poin baca secara otomatis.")
#-----------------------------------------------

#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["All join"]: #Panggil Semua Bot
              if msg._from in admin:
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventedJoinByTicket = False
                ririn.updateGroup(G)
                invsend = 0
                Ticket = ririn.reissueGroupTicket(msg.to)
                ririn.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.1)
                G = ririn.getGroup(msg.to)
                ginfo = ririn.getGroup(msg.to)
                G.preventedJoinByTicket = True
                ririn.updateGroup(G)
#----------------Bot Out All Group Start------------------------------#
            elif msg.text in ["Bot Out"]:
               if msg._from in admin:
                if msg.toType == 2:
                   gid = ririn.getGroupIdsJoined()
                   for i in gid:
                     ririn.leaveGroup(msg.to)
                   if wait["lang"] == "JP":
                     ririn.sendText(msg.to,"Sayonara")
                   else:
                     ririn.sendText(msg.to,"He deririnined all invitations")
#--------------------------Bot Out All Group Start----------------------------#
            elif msg.text in ["Bye all"]:
               if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        ririn.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Dwi Bye"]:
               if msg._from in admin:
                if msg.toType == 2:
                    ginfo = ririn.getGroup(msg.to)
                    try:
                        ririn.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------Leave Group Bot---------------------------------------#
            elif msg.text in ["Kill"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ririn.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ririn]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#--------------------------Group Bc Start-------------------------------------#
            elif "Group bc " in msg.text:
               if msg._from in admin:
                  bctxt = msg.text.replace("Group bc ", "")
                  a = ririn.getGroupIdsJoined()
                  for manusia in a:
                    ririn.sendText(manusia, (bctxt))
#--------------------------Group Bc Finish------------------------------------#
            elif "Salken Ya" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("ok")
                    _name = msg.text.replace("Salken Ya","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ririn.sendText(msg.to,"⚠DENG DENG DENG DENG !⚠")
                    ririn.sendText(msg.to,"JANGAN PANIK SEMUA PINTU KELUAR ADA DI POJOK KANAN🔫")
                    ririn.sendText(msg.to,"CEPET TANGKIS GOBLOK JANGAN DILIATIN NTAR GRUP LU RATA GOBLOK")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"Tidak Ditemukan.")
                    else:
                        for target in targets:
                          if not target in admin and Bots:
                            try:
                                klist=[ririn]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ririn.sendText(msg.to,"Grup Bersih")
            elif "Nk " in msg.text:
                  if msg._from in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ririn.getGroup(msg.to)
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
                                    klist=[ririn]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Bye")
            elif "Blacklist @ " in msg.text:
               if msg._from in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            ririn.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ririn.sendText(msg.to,"Succes Cv")
                                except:
                                    ririn.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Ban]ok")
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ririn.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"Target Tidak Djtemukan")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"Target Siap")
                            except:
                                ririn.sendText(msg.to,"Berhasil")
            elif "Unban @" in msg.text:
               if msg._from in admin:
                if msg.toType == 2:
                    print("[Unban]ok")
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ririn.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ririn.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendText(msg.to,"Succes Cv")
                            except:
                                ririn.sendText(msg.to,"Succes Cv")
#----------------------------------------------------------------------------#
            elif msg.text in ["Tes"]:
               if msg._from in admin:
                ririn.sendText(msg.to,"Hazza Here 􀜁􀇔Mask􏿿")
#-----------------------------------------------------------------------------
            elif msg.text in ["Sp","sp"]:
                ririn.sendText(msg.to, "Process Waiting...")
                sp = int(round(time.time() *1000))
                ririn.sendText(msg.to,"my speed : %sms" % (sp - op.createdTime))
#---------------------------------------------------------------------
            elif msg.text in ["Speed","speed"]:
                start = time.time()
                ririn.sendText(msg.to, "Proccess...")
                elapsed_time = time.time() - start
                ririn.sendText(msg.to, "Kecepatan mengirim pesan: %sms" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Runtime"]:
               if msg._from in admin:
                runtime = time.time()-startBot
                elapsed_time = format_timespan(time.time()-startBot)
                ririn.sendText(msg.to,"Running in %s" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
               if msg._from in admin:
                wait["wblacklist"] = True
                ririn.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Unban"]:
               if msg._from in admin:
                wait["dblacklist"] = True
                ririn.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Banlist"]:
               if msg._from in admin:
                if wait["blacklist"] == {}:
                    ririn.sendText(msg.to,"nothing")
                else:
                    ririn.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ririn.getContact(mi_d).displayName + "\n"
                    ririn.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    ririn.sendText(msg.to,cocoa + "")
            elif msg.text in ["Clear ban"]:
                if msg._from in admin:
                    wait["blacklist"] = {}
                    ririn.sendText(msg.to,"Done")
            elif msg.text in ["Kill ban"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ririn.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ririn.kickoutFromGroup(msg.to,[jj])
                    ririn.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
               if msg._from in admin:
                if msg.toType == 2:
                    group = ririn.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ririn.cancelGroupInvitation(msg.to,[_mid])
                    ririn.sendText(msg.to,"I pretended to cancel and canceled.")
#----------------Fungsi Cek Sider-------------------#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = ririn.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n - " + Name
                        wait2['ROM'][op.param1][op.param2] = " - " + Name
                else:
                    ki.sendText
            except:
                pass
#----------------Fungsi Cek Sider-------------------#
        if op.type == 59:
            print(op)


    except Exception as error:
        print(error)


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["ririnock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = ririn.getProfile()
                profile.displayName = wait["cName"]
                ririn.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
