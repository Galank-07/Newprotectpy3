# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

ririn = LINE("EsdR19LLWC6MVxSf0Cb5.qzjQVWZ0ZEOc9BUr4r9zrq.eGdKw5YJkpX6J6O/Zc6mQzyZVcwiA3ZWbyPjV46VRlo=")
#ririn = LINE("TOKEN KAMU")
#ririn = LINE("Email","Password")
ririn.log("Auth Token : " + str(ririn.authToken))
channelToken = ririn.getChannelResult()
ririn.log("Channel Token : " + str(channelToken))

dna1 = LINE("EsTFbxUhbNEyMJc8a3Gb.cY6+YCBCDcB6/j3HdvZCAW.KlAbXbDvpnz+fWW+0V9GjqkVY1Do4K+JPbsXFPlDIHc=")
#dna1 = LINE("TOKEN KAMU")
#dna1 = LINE("Email","Password")
dna1.log("Auth Token : " + str(dna1.authToken))
channelToken = dna1.getChannelResult()
dna1.log("Channel Token : " + str(channelToken))

dna2 = LINE("EsuQOMu37XbfE6PWbUw1.Sl2u8yHwWYZHMslzI9Bi8q.uabGU7e4vGIFBf67xIvbUyR0Myxtvdshm9FVQzU8zg8=")
#dna2 = LINE("TOKEN KAMU")
#dna2 = LINE("Email","Password")
dna2.log("Auth Token : " + str(dna2.authToken))
channelToken = dna2.getChannelResult()
dna2.log("Channel Token : " + str(channelToken))

dna3 = LINE("Esdi76sv2b3VDT7ysWW8.M53qiD/PJ1i6qsVfYwB7Ea.6THnYxTGBDeb0HxSuZ0t/d7z9/dAh3ibODLJslVYt98=")
#dna3 = LINE("TOKEN KAMU")
#dna3 = LINE("Email","Password")
dna3.log("Auth Token : " + str(dna3.authToken))
channelToken = dna3.getChannelResult()
dna3.log("Channel Token : " + str(channelToken))

dna4 = LINE("Esy9TWqsCuyZ5sk2EWd3.LTjIccO9HW0I2OLJ9e3wmW.vsq04JKRbld65jL5zwzMKGFZobtWUqH5CCG1Sas43L0=")
#dna4 = LINE("TOKEN KAMU")
#dna4 = LINE("Email","Password")
dna4.log("Auth Token : " + str(dna4.authToken))
channelToken = dna4.getChannelResult()
dna4.log("Channel Token : " + str(channelToken))

dna5 = LINE("EskaExA78nvu16eTwlGa.i4cphH9h9VMs4DyAsZSSsG.trmAcPIaCXuwezkdtmgNMm3WLnJuDeS5fipJ88Q8qa8=")
#dna5 = LINE("TOKEN KAMU")
#dna5 = LINE("Email","Password")
dna5.log("Auth Token : " + str(dna5.authToken))
channelToken = dna5.getChannelResult()
dna5.log("Channel Token : " + str(channelToken))

dna6 = LINE("Es9xFXK0Z2RKlWZQhZOa.fW/HXK/P6ucyNSYHd42E2G.xjcNjhFe0Bovxxb0vIh9AORBkjU8wbNs1qcEYQ7jElE=")
#dna6 = LINE("TOKEN KAMU")
#dna6 = LINE("Email","Password")
dna6.log("Auth Token : " + str(dna6.authToken))
channelToken = dna6.getChannelResult()
dna6.log("Channel Token : " + str(channelToken))

dna7 = LINE("Es38qypTT7maznEoceo3.GQe1F0FLgkB3suGK5WtUCW.oTICiJ+WiNFFhzZ5H9NIVy16+2WxoDj9x2iVSZD2XY8=")
#dna7 = LINE("TOKEN KAMU")
#dna7 = LINE("Email","Password")
dna7.log("Auth Token : " + str(dna7.authToken))
channelToken = dna7.getChannelResult()
dna7.log("Channel Token : " + str(channelToken))

dna8 = LINE("EseBv9TlxzSKKX6OmcV3.fOtS1/ZYrVfyY2wr74a3uW.QONs/ScbnK5mRL8uVCtH5k7rEknJEaFAEQNXqODKtzw=")
#dna8 = LINE("TOKEN KAMU")
#dna8 = LINE("Email","Password")
dna8.log("Auth Token : " + str(dna8.authToken))
channelToken = dna8.getChannelResult()
dna8.log("Channel Token : " + str(channelToken))

dna9 = LINE("EsTDtoPf1879CvZVXlL1./PGYhVVe4uDle5Q6kp48qq.Pc58A6f/JLzyPy0muKWsel+QZOJkzN61HXEdmSOGbWk=")
#dna9 = LINE("TOKEN KAMU")
#dna9 = LINE("Email","Password")
dna9.log("Auth Token : " + str(dna9.authToken))
channelToken = dna9.getChannelResult()
dna9.log("Channel Token : " + str(channelToken))

KAC = [ririn,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]

ririnMID= ririn.profile.mid
dna1MID = dna1.profile.mid
dna2MID = dna2.profile.mid
dna3MID = dna3.profile.mid
dna4MID = dna4.profile.mid
dna5MID = dna5.profile.mid
dna6MID = dna6.profile.mid
dna7MID = dna7.profile.mid
dna8MID = dna8.profile.mid
dna9MID = dna9.profile.mid

Bots = [ririnMID,dna1MID,dna2MID,dna3MID,dna4MID,dna5MID,dna6MID,dna7MID,dna8MID,dna9MID]
creator = ["ueca4120a9d7b0e4a9e7f4f1b1b96a436"]
Owner = ["ueca4120a9d7b0e4a9e7f4f1b1b96a436"]
admin = ["ueca4120a9d7b0e4a9e7f4f1b1b96a436","u40d66b1f1c5ce30fdce9507a73247ef1","uc2d366327a79c98701b0b8bd9e08c0c9","ubcce0f23f428d75703fb33ee06c083b6","ubd3c3fa2c0128918d5b484caa42f9fee","u6fc2dc5f5f0d0fc6a4d2e92626afb742"]

ririnProfile = ririn.getProfile()
dna1Profile = dna1.getProfile()
dna2Profile = dna2.getProfile()
dna3Profile = dna3.getProfile()
dna4Profile = dna4.getProfile()
dna5Profile = dna5.getProfile()
dna6Profile = dna6.getProfile()
dna7Profile = dna7.getProfile()
dna8Profile = dna8.getProfile()
dna9Profile = dna9.getProfile()

lineSettings = ririn.getSettings()
dna1Settings = dna1.getSettings()
dna2Settings = dna2.getSettings()
dna3Settings = dna3.getSettings()
dna4Settings = dna4.getSettings()
dna5Settings = dna5.getSettings()
dna6Settings = dna6.getSettings()
dna7Settings = dna7.getSettings()
dna8Settings = dna8.getSettings()
dna9Settings = dna9.getSettings()

oepoll = OEPoll(ririn)
oepoll1 = OEPoll(dna1)
oepoll2 = OEPoll(dna2)
oepoll3 = OEPoll(dna3)
oepoll4 = OEPoll(dna4)
oepoll5 = OEPoll(dna5)
oepoll6 = OEPoll(dna6)
oepoll7 = OEPoll(dna7)
oepoll8 = OEPoll(dna8)
oepoll9 = OEPoll(dna9)

responsename = ririn.getProfile().displayName
responsename2 = dna1.getProfile().displayName
responsename3 = dna2.getProfile().displayName
responsename4 = dna3.getProfile().displayName
responsename5 = dna4.getProfile().displayName
responsename6 = dna5.getProfile().displayName
responsename7 = dna6.getProfile().displayName
responsename8 = dna7.getProfile().displayName
responsename9 = dna8.getProfile().displayName
responsename10 = dna9.getProfile().displayName
#==============================================================================#




with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = ririnProfile.displayName
myProfile["statusMessage"] = ririnProfile.statusMessage
myProfile["pictureStatus"] = ririnProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

#if settings["restartPoint"] != None:
#    ririn.sendMessage(settings["restartPoint"], "Bot kembali aktif")
#    settings["restartBot"] = None

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    ririn.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLogtxt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        ririn.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╔════════════════════╗" + "\n" + \
                  "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                  "╚════════════════════╝" + "\n" + \
                  "╔════════════════════╗" + "\n" + \
                  "                  ◄]·✪·Help·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Help" + "\n" + \
                  "╠❂➣ Translate" + "\n" + \
                  "╠❂➣ Texttospeech" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "             ◄]·✪·Protection·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Protect 「On/Off」" + "\n" + \
                  "╠❂➣ QrProtect 「On/Off」" + "\n" + \
                  "╠❂➣ InviteProtect 「On/Off」" + "\n" + \
                  "╠❂➣ CancelProtect 「On/Off」" + "\n" + \
                  "╠❂➣ SetPro 「On/Off」" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                ◄]·✪·Status·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Restart" + "\n" + \
                  "╠❂➣ Runtime" + "\n" + \
                  "╠❂➣ Speed" + "\n" + \
                  "╠❂➣ Status" + "\n" + \
                  "╠❂➣ About" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "              ◄]·✪·Settings·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ AutoAdd「On/Off」" + "\n" + \
                  "╠❂➣ AutoJoin「On/Off」" + "\n" + \
                  "╠❂➣ AutoLeave「On/Off」" + "\n" + \
                  "╠❂➣ AutoRead「On/Off」" + "\n" + \
                  "╠❂➣ CheckSticker「On/Off」" + "\n" + \
                  "╠❂➣ DetectMention「On/Off」" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                  ◄]·✪·Self·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Me" + "\n" + \
                  "╠❂➣ MyMid" + "\n" + \
                  "╠❂➣ MyName" + "\n" + \
                  "╠❂➣ MyBio" + "\n" + \
                  "╠❂➣ MyPicture" + "\n" + \
                  "╠❂➣ MyVideoProfile" + "\n" + \
                  "╠❂➣ MyCover" + "\n" + \
                  "╠❂➣ StealContact「@」" + "\n" + \
                  "╠❂➣ StealMid「@」" + "\n" + \
                  "╠❂➣ StealName「@」" + "\n" + \
                  "╠❂➣ StealBio「@」" + "\n" + \
                  "╠❂➣ StealPicture「@」" + "\n" + \
                  "╠❂➣ StealVideoProfile「@」" + "\n" + \
                  "╠❂➣ StealCover「@」" + "\n" + \
                  "╠❂➣ CloneProfile「@」" + "\n" + \
                  "╠❂➣ RestoreProfile" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                 ◄]·✪·Group·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ GroupCreator" + "\n" + \
                  "╠❂➣ GroupId" + "\n" + \
                  "╠❂➣ GroupName" + "\n" + \
                  "╠❂➣ GroupPicture" + "\n" + \
                  "╠❂➣ GroupTicket" + "\n" + \
                  "╠❂➣ GroupTicket「On/Off」" + "\n" + \
                  "╠❂➣ GroupList" + "\n" + \
                  "╠❂➣ GroupMemberList" + "\n" + \
                  "╠❂➣ GroupInfo" + "\n" + \
                  "╠❂➣ Kill「Mention」" + "\n" + \
                  "╠❂➣ KickAllMember" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                ◄]·✪·Special·✪·►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Mimic「On/Off」" + "\n" + \
                  "╠❂➣ MimicList" + "\n" + \
                  "╠❂➣ MimicAdd「Mention」" + "\n" + \
                  "╠❂➣ MimicDel「Mention」" + "\n" + \
                  "╠❂➣ Tagall" + "\n" + \
                  "╠❂➣ Read「Oɴ/Off/Reset」" + "\n" + \
                  "╠❂➣ Lurking" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "               ◄]·✪·Media·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ Kalender" + "\n" + \
                  "╠❂➣ CheckDate「Date」" + "\n" + \
                  "╠❂➣ InstagramInfo「UserName」" + "\n" + \
                  "╠❂➣ InstagramPost「UserName」" + "\n" + \
                  "╠❂➣ SearchYoutube「Search」" + "\n" + \
                  "╠❂➣ SearchMusic「Search」" + "\n" + \
                  "╠❂➣ SearchLyric「Search」" + "\n" + \
                  "╠❂➣ SearchImage「Search」" + "\n" + \
                  "╠❂➣ ScreenshootWebsite「Url」" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "                  ◄]·✪·Bot·✪·[►" + "\n" + \
                  "╠════════════════════╝" + "\n" + \
                  "╠❂➣ AdminAdd" + "\n" + \
                  "╠❂➣ AdminDel" + "\n" + \
                  "╠❂➣ AdminList" + "\n" + \
                  "╠❂➣ OwnerAdd" + "\n" + \
                  "╠❂➣ OwnerDel" + "\n" + \
                  "╠❂➣ OwnerList" + "\n" + \
                  "╠❂➣ BanContact" + "\n" + \
                  "╠❂➣ UnbanContact" + "\n" + \
                  "╠❂➣ BanList" + "\n" + \
                  "╠❂➣ ClearBan" + "\n" + \
                  "╠❂➣ Respon" + "\n" + \
                  "╠❂➣ Absen" + "\n" + \
                  "╠❂➣ Come dna" + "\n" + \
                  "╠❂➣ Bye dna" + "\n" + \
                  "╠════════════════════╗" + "\n" + \
                  "              Credits by : ©D̶e̶e̶ ✯" + "\n" + \
                  "╚════════════════════╝" + "\n" + \
                  "╔════════════════════╗" + "\n" + \
                  "                    ✰ ᴅɴᴀ ʙᴏᴛ ✰" + "\n" + \
                  "╚════════════════════╝"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╔══〘 T E X T   T O   S P E E C H 〙" + "\n" + \
                         "╠❂➣ af : Afrikaans" + "\n" + \
                         "╠❂➣ sq : Albanian" + "\n" + \
                         "╠❂➣ ar : Arabic" + "\n" + \
                         "╠❂➣ hy : Armenian" + "\n" + \
                         "╠❂➣ bn : Bengali" + "\n" + \
                         "╠❂➣ ca : Catalan" + "\n" + \
                         "╠❂➣ zh : Chinese" + "\n" + \
                         "╠❂➣ zh-cn : Chinese (Mandarin/Cina)" + "\n" + \
                         "╠❂➣ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠❂➣ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠❂➣ hr : Croatian" + "\n" + \
                         "╠❂➣ cs : Czech" + "\n" + \
                         "╠❂➣ da : Danish" + "\n" + \
                         "╠❂➣ nl : Dutch" + "\n" + \
                         "╠❂➣ en : English" + "\n" + \
                         "╠❂➣ en-au : English (Australia)" + "\n" + \
                         "╠❂➣ en-uk : English (United Kingdom)" + "\n" + \
                         "╠❂➣ en-us : English (United States)" + "\n" + \
                         "╠❂➣ eo : Esperanto" + "\n" + \
                         "╠❂➣ fi : Finnish" + "\n" + \
                         "╠❂➣ fr : French" + "\n" + \
                         "╠❂➣ de : German" + "\n" + \
                         "╠❂➣ el : Greek" + "\n" + \
                         "╠❂➣ hi : Hindi" + "\n" + \
                         "╠❂➣ hu : Hungarian" + "\n" + \
                         "╠❂➣ is : Icelandic" + "\n" + \
                         "╠❂➣ id : Indonesian" + "\n" + \
                         "╠❂➣ it : Italian" + "\n" + \
                         "╠❂➣ ja : Japanese" + "\n" + \
                         "╠❂➣ km : Khmer (Cambodian)" + "\n" + \
                         "╠❂➣ ko : Korean" + "\n" + \
                         "╠❂➣ la : Latin" + "\n" + \
                         "╠❂➣ lv : Latvian" + "\n" + \
                         "╠❂➣ mk : Macedonian" + "\n" + \
                         "╠❂➣ no : Norwegian" + "\n" + \
                         "╠❂➣ pl : Polish" + "\n" + \
                         "╠❂➣ pt : Portuguese" + "\n" + \
                         "╠❂➣ ro : Romanian" + "\n" + \
                         "╠❂➣ ru : Russian" + "\n" + \
                         "╠❂➣ sr : Serbian" + "\n" + \
                         "╠❂➣ si : Sinhala" + "\n" + \
                         "╠❂➣ sk : Slovak" + "\n" + \
                         "╠❂➣ es : Spanish" + "\n" + \
                         "╠❂➣ es-es : Spanish (Spain)" + "\n" + \
                         "╠❂➣ es-us : Spanish (United States)" + "\n" + \
                         "╠❂➣ sw : Swahili" + "\n" + \
                         "╠❂➣ sv : Swedish" + "\n" + \
                         "╠❂➣ ta : Tamil" + "\n" + \
                         "╠❂➣ th : Thai" + "\n" + \
                         "╠❂➣ tr : Turkish" + "\n" + \
                         "╠❂➣ uk : Ukrainian" + "\n" + \
                         "╠❂➣ vi : Vietnamese" + "\n" + \
                         "╠❂➣ cy : Welsh" + "\n" + \
                         "╚══〘 Jangan Typo 〙"  "\n" + "\n\n" + \
                          "Contoh : say-en Ririn Cantik"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔══〘 T R A N S L A T E 〙" + "\n" + \
                       "╠❂➣ af : afrikaans" + "\n" + \
                       "╠❂➣ sq : albanian" + "\n" + \
                       "╠❂➣ am : amharic" + "\n" + \
                       "╠❂➣ ar : arabic" + "\n" + \
                       "╠❂➣ hy : armenian" + "\n" + \
                       "╠❂➣ az : azerbaijani" + "\n" + \
                       "╠❂➣ eu : basque" + "\n" + \
                       "╠❂➣ be : belarusian" + "\n" + \
                       "╠❂➣ bn : bengali" + "\n" + \
                       "╠❂➣ bs : bosnian" + "\n" + \
                       "╠❂➣ bg : bulgarian" + "\n" + \
                       "╠❂➣ ca : catalan" + "\n" + \
                       "╠❂➣ ceb : cebuano" + "\n" + \
                       "╠❂➣ ny : chichewa" + "\n" + \
                       "╠❂➣ zh-cn : chinese (simplified)" + "\n" + \
                       "╠❂➣ zh-tw : chinese (traditional)" + "\n" + \
                       "╠❂➣ co : corsican" + "\n" + \
                       "╠❂➣ hr : croatian" + "\n" + \
                       "╠❂➣ cs : czech" + "\n" + \
                       "╠❂➣ da : danish" + "\n" + \
                       "╠❂➣ nl : dutch" + "\n" + \
                       "╠❂➣ en : english" + "\n" + \
                       "╠❂➣ eo : esperanto" + "\n" + \
                       "╠❂➣ et : estonian" + "\n" + \
                       "╠❂➣ tl : filipino" + "\n" + \
                       "╠❂➣ fi : finnish" + "\n" + \
                       "╠❂➣ fr : french" + "\n" + \
                       "╠❂➣ fy : frisian" + "\n" + \
                       "╠❂➣ gl : galician" + "\n" + \
                       "╠❂➣ ka : georgian" + "\n" + \
                       "╠❂➣ de : german" + "\n" + \
                       "╠❂➣ el : greek" + "\n" + \
                       "╠❂➣ gu : gujarati" + "\n" + \
                       "╠❂➣ ht : haitian creole" + "\n" + \
                       "╠❂➣ ha : hausa" + "\n" + \
                       "╠❂➣ haw : hawaiian" + "\n" + \
                       "╠❂➣ iw : hebrew" + "\n" + \
                       "╠❂➣ hi : hindi" + "\n" + \
                       "╠❂➣ hmn : hmong" + "\n" + \
                       "╠❂➣ hu : hungarian" + "\n" + \
                       "╠❂➣ is : icelandic" + "\n" + \
                       "╠❂➣ ig : igbo" + "\n" + \
                       "╠❂➣ id : indonesian" + "\n" + \
                       "╠❂➣ ga : irish" + "\n" + \
                       "╠❂➣ it : italian" + "\n" + \
                       "╠❂➣ ja : japanese" + "\n" + \
                       "╠❂➣ jw : javanese" + "\n" + \
                       "╠❂➣ kn : kannada" + "\n" + \
                       "╠❂➣ kk : kazakh" + "\n" + \
                       "╠❂➣ km : khmer" + "\n" + \
                       "╠❂➣ ko : korean" + "\n" + \
                       "╠❂➣ ku : kurdish (kurmanji)" + "\n" + \
                       "╠❂➣ ky : kyrgyz" + "\n" + \
                       "╠❂➣ lo : lao" + "\n" + \
                       "╠❂➣ la : latin" + "\n" + \
                       "╠❂➣ lv : latvian" + "\n" + \
                       "╠❂➣ lt : lithuanian" + "\n" + \
                       "╠❂➣ lb : luxembourgish" + "\n" + \
                       "╠❂➣ mk : macedonian" + "\n" + \
                       "╠❂➣ mg : malagasy" + "\n" + \
                       "╠❂➣ ms : malay" + "\n" + \
                       "╠❂➣ ml : malayalam" + "\n" + \
                       "╠❂➣ mt : maltese" + "\n" + \
                       "╠❂➣ mi : maori" + "\n" + \
                       "╠❂➣ mr : marathi" + "\n" + \
                       "╠❂➣ mn : mongolian" + "\n" + \
                       "╠❂➣ my : myanmar (burmese)" + "\n" + \
                       "╠❂➣ ne : nepali" + "\n" + \
                       "╠❂➣ no : norwegian" + "\n" + \
                       "╠❂➣ ps : pashto" + "\n" + \
                       "╠❂➣ fa : persian" + "\n" + \
                       "╠❂➣ pl : polish" + "\n" + \
                       "╠❂➣ pt : portuguese" + "\n" + \
                       "╠❂➣ pa : punjabi" + "\n" + \
                       "╠❂➣ ro : romanian" + "\n" + \
                       "╠❂➣ ru : russian" + "\n" + \
                       "╠❂➣ sm : samoan" + "\n" + \
                       "╠❂➣ gd : scots gaelic" + "\n" + \
                       "╠❂➣ sr : serbian" + "\n" + \
                       "╠❂➣ st : sesotho" + "\n" + \
                       "╠❂➣ sn : shona" + "\n" + \
                       "╠❂➣ sd : sindhi" + "\n" + \
                       "╠❂➣ si : sinhala" + "\n" + \
                       "╠❂➣ sk : slovak" + "\n" + \
                       "╠❂➣ sl : slovenian" + "\n" + \
                       "╠❂➣ so : somali" + "\n" + \
                       "╠❂➣ es : spanish" + "\n" + \
                       "╠❂➣ su : sundanese" + "\n" + \
                       "╠❂➣ sw : swahili" + "\n" + \
                       "╠❂➣ sv : swedish" + "\n" + \
                       "╠❂➣ tg : tajik" + "\n" + \
                       "╠❂➣ ta : tamil" + "\n" + \
                       "╠❂➣ te : telugu" + "\n" + \
                       "╠❂➣ th : thai" + "\n" + \
                       "╠❂➣ tr : turkish" + "\n" + \
                       "╠❂➣ uk : ukrainian" + "\n" + \
                       "╠❂➣ ur : urdu" + "\n" + \
                       "╠❂➣ uz : uzbek" + "\n" + \
                       "╠❂➣ vi : vietnamese" + "\n" + \
                       "╠❂➣ cy : welsh" + "\n" + \
                       "╠❂➣ xh : xhosa" + "\n" + \
                       "╠❂➣ yi : yiddish" + "\n" + \
                       "╠❂➣ yo : yoruba" + "\n" + \
                       "╠❂➣ zu : zulu" + "\n" + \
                       "╠❂➣ fil : Filipino" + "\n" + \
                       "╠❂➣ he : Hebrew" + "\n" + \
                       "╚══〘 Jangan Typo 〙" + "\n" + "\n\n" + \
                         "Contoh : tr-en Ririn Cantik"
    return helpTranslate
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
            
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                ririn.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(ririn.getContact(op.param1).displayName)))
                
#==============================================================================#
        if op.type == 13:
            if ririnMID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ririn.acceptGroupInvitation(op.param1)
                else:
                  ririn.rejectGroupInvitation(op.param1)
                
            if dna1MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna1.acceptGroupInvitation(op.param1)
                else:
                  dna1.rejectGroupInvitation(op.param1)
                
            if dna2MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna2.acceptGroupInvitation(op.param1)
                else:
                  dna2.rejectGroupInvitation(op.param1)
                
            if dna3MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna3.acceptGroupInvitation(op.param1)
                else:
                  dna3.rejectGroupInvitation(op.param1)
                
            if dna4MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna4.acceptGroupInvitation(op.param1)
                else:
                  dna4.rejectGroupInvitation(op.param1)
                    
            if dna5MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna5.acceptGroupInvitation(op.param1)
                else:
                  dna5.rejectGroupInvitation(op.param1)
                  
            if dna6MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna6.acceptGroupInvitation(op.param1)
                else:
                  dna6.rejectGroupInvitation(op.param1)
                  
            if dna7MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna7.acceptGroupInvitation(op.param1)
                else:
                  dna7.rejectGroupInvitation(op.param1)
                  
            if dna8MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna8.acceptGroupInvitation(op.param1)
                else:
                  dna8.rejectGroupInvitation(op.param1)
                  
            if dna9MID in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  dna9.acceptGroupInvitation(op.param1)
                else:
                  dna9.rejectGroupInvitation(op.param1)
                
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            group = ririn.getGroup(op.param1)
            contact = ririn.getContact(op.param2)
            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   User Join : {}".format(str(contact.displayName))
            print (arg)
            
        if op.type == 17:
            if op.param2 in admin:
              if op.param2 not in Bots:    
                return
            ginfo = ririn.getGroup(op.param1)
            contact = ririn.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            c = Message(to=op.param1, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ririn.sendMessage(c)
            ririn.sendText(op.param1,"Hallo " + ririn.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            ririn.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }                
            ririn.sendMessage(d)             
            print ("MEMBER JOIN TO GROUP")

        if op.type == 19:
            print ("[ 19 ] NOTIFIED KICKOUT FROM GROUP")
            group = ririn.getGroup(op.param1)
            contact = ririn.getContact(op.param2)
            victim = ririn.getContact(op.param3)
            arg = "   Group Name : {}".format(str(group.name))
            arg += "\n   Executor : {}".format(str(contact.displayName))
            arg += "\n   Victim : {}".format(str(victim.displayName))
            print (arg)                
                
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                ririn.leaveRoom(op.param1)
#-------------------------------------------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        ririn.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        ririn.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        ririn.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        ririn.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        ririn.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        ririn.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        ririn.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        ririn.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 26:
            print ("[ 26 ] SEND MESSAGE COMMAND")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != ririn.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                elif text.lower() == 'help':
                    helpMessage = helpmessage()
                    ririn.sendMessage(to, str(helpMessage))
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    ririn.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    ririn.sendMessage(to, str(helpTranslate))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    ririn.sendMessage(to, "Please Wait...")
                    elapsed_time = time.time() - start
                    ririn.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                  if msg._from in Owner:    
                    ririn.sendMessage(to, "Please Wait...")
                    time.sleep(5)
                    ririn.sendMessage(to, "Restart Sukses")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    ririn.sendMessage(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ueca4120a9d7b0e4a9e7f4f1b1b96a436"
                        creator = ririn.getContact(owner)
                        contact = ririn.getContact(ririnMID)
                        grouplist = ririn.getGroupIdsJoined()
                        contactlist = ririn.getAllContactIds()
                        blockedlist = ririn.getBlockedContactIds()
                        ret_ = "╔══[ About Self ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ Dilarang Remake :P ]"
                        ririn.sendContact(to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                        ririn.sendMessage(to, str(ret_))
                    except Exception as e:
                        ririn.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["protect"] == True: ret_ += "\n╠ Protect ✅"
                        else: ret_ += "\n╠ Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠ Qr Protect ✅"
                        else: ret_ += "\n╠ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ Invite Protect ✅"
                        else: ret_ += "\n╠ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n╠ Cancel Protect ✅"
                        else: ret_ += "\n╠ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        ret_ += "\n╚══[ Status ]"
                        ririn.sendMessage(to, str(ret_))
                    except Exception as e:
                        ririn.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
                    else:
                        ririn.sendMessage(msg.to,"Owner Permission Required")
                    
                elif msg.text.lower().startswith("ownerdel "):
                    if msg._from in Owner:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
                    else:
                        ririn.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ownerlist':
                    try:
                        arr = []
                        owner = "ueca4120a9d7b0e4a9e7f4f1b1b96a436"
                        creator = ririn.getContact(owner)
                        ret_ = "╔════════════════\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰"
                        ret_ += "\n╠══✪〘Owner  List〙✪═══"
                        ret_ += "\n╠✪ Ownerlist : {}".format(creator.displayName)
                        ret_ += "\n╠════════════════"
                        ret_ += "\n╠✪〘 line.me/ti/p/ppgIZ0JLDW 〙"
                        ret_ += "\n╚════════════════"
                        ririn.sendContact(to, "ueca4120a9d7b0e4a9e7f4f1b1b96a436")
                        ririn.sendMessage(msg.to,"Loading...")
                        ririn.sendMessage(to, str(ret_))
                    except Exception as e:
                        ririn.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("adminadd "):
                    if msg._from in Owner:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendMessage(msg.to,"Admin ☢-Bot-☢\nAdd\nExecuted")
                                break
                            except:
                                ririn.sendMessage(msg.to,"Added Target Fail !")
                                break
                    else:
                        ririn.sendMessage(msg.to,"Owner Permission Required")
                    
                elif msg.text.lower().startswith("admindel "):
                    if msg._from in Owner:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                ririn.sendMessage(msg.to,"Admin ☢-Bot-☢\nRemove\nExecuted")
                                break
                            except:
                                ririn.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                    else:
                        ririn.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                    if msg._from in Owner:
                        if admin == []:
                            ririn.sendMessage(msg.to,"The Adminlist is empty")
                        else:
                            ririn.sendMessage(msg.to,"Loading...")
                            mc = "╔════════════════\n╠✪➣  ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╠══✪〘Owner  List〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +ririn.getContact(mi_d).displayName + "\n"
                            ririn.sendMessage(msg.to,mc + "╠════════════════\n╠✪〘 line.me/ti/p/ppgIZ0JLDW 〙\n╚════════════════")
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                    if msg._from in Owner:
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Already On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Set To On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Set To On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Already On")
                                
                elif text.lower() == 'protect off':
                    if msg._from in Owner:
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Already Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Set To Off")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Set To Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Already Off")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                    if msg._from in Owner:
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Qr Already On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Qr Set To On")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Qr Set To On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Qr Already On")
                                
                elif text.lower() == 'qrprotect off':
                    if msg._from in Owner:
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Qr Already Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Qr Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Invite Already On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Invite Set To On")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Invite Set To On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Invite Already On")
                                
                elif text.lower() == 'inviteprotect off':
                    if msg._from in Owner:
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Invite Already Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                                
                elif text.lower() == 'cancelprotect off':
                    if msg._from in Owner:
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                            else:
                                ririn.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'setpro on':
                    if msg._from in Owner:
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        ririn.sendMessage(msg.to,"➲ All Protect Set To On")
                    else:
                        ririn.sendMessage(msg.to,"Just for Owner")
                        		            
                elif text.lower() == 'setpro off':
                    if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        ririn.sendMessage(msg.to,"➲ All Protect Set To Off")
                    else:
                        ririn.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    ririn.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    ririn.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                  if msg._from in Owner:    
                    settings["autoJoin"] = True
                    ririn.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    ririn.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                  if msg._from in Owner:
                    settings["autoLeave"] = True
                    ririn.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
                  if msg._from in Owner:
                    settings["autoLeave"] = False
                    ririn.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    ririn.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    ririn.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    ririn.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    ririn.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    ririn.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    ririn.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'autojoinlink on':
                    settings["autoJoinTicket"] = True
                    ririn.sendMessage(to, "Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'autojoinlink off':
                    settings["autoJoinTicket"] = False
                    ririn.sendMessage(to, "Berhasil menonaktifkan Auto Join Link")                    
#==============================================================================#
                elif text.lower() == "respon":
                    ririn.sendMessage(msg.to,responsename)
                    dna1.sendMessage(msg.to,responsename2)
                    dna2.sendMessage(msg.to,responsename3)
                    dna3.sendMessage(msg.to,responsename4)
                    dna4.sendMessage(msg.to,responsename5)
                    dna5.sendMessage(msg.to,responsename6)
                    dna6.sendMessage(msg.to,responsename7)
                    dna7.sendMessage(msg.to,responsename8)
                    dna8.sendMessage(msg.to,responsename9)
                    dna9.sendMessage(msg.to,responsename10)
                    
                elif msg.text.lower() == 'absen':
                    if msg._from in Owner:
                        ririn.sendContact(to, ririnMID)
                        dna1.sendContact(to, dna1MID)
                        dna2.sendContact(to, dna2MID)
                        dna3.sendContact(to, dna3MID)
                        dna4.sendContact(to, dna4MID)
                        dna5.sendContact(to, dna5MID)
                        dna6.sendContact(to, dna6MID)
                        dna7.sendContact(to, dna7MID)
                        dna8.sendContact(to, dna8MID)
                        dna9.sendContact(to, dna9MID)
                        
                elif text.lower() in ["bye dna"]:
                  if msg._from in Owner:    
                    dna1.leaveGroup(msg.to)
                    dna2.leaveGroup(msg.to)
                    dna3.leaveGroup(msg.to)
                    dna4.leaveGroup(msg.to)   
                    dna5.leaveGroup(msg.to)
                    dna6.leaveGroup(msg.to)
                    dna7.leaveGroup(msg.to)
                    dna8.leaveGroup(msg.to)
                    dna9.leaveGroup(msg.to)
               
                elif text.lower() in ["come dna"]:
                  if msg._from in Owner:    
                    G = ririn.getGroup(msg.to)
                    ginfo = ririn.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    ririn.updateGroup(G)
                    invsend = 0
                    Ticket = ririn.reissueGroupTicket(msg.to)
                    dna1.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    dna9.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = ririn.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    ririn.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    ririn.updateGroup(G)
                
                elif text.lower() == 'me':
                    sendMessageWithMention(to, ririnMID)
                    ririn.sendContact(to, ririnMID)
                elif text.lower() == 'mymid':
                    ririn.sendMessage(msg.to,"[MID]\n" +  ririnMID)
                elif text.lower() == 'myname':
                    me = ririn.getContact(ririnMID)
                    ririn.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = ririn.getContact(ririnMID)
                    ririn.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = ririn.getContact(ririnMID)
                    ririn.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = ririn.getContact(ririnMID)
                    ririn.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = ririn.getContact(ririnMID)
                    cover = ririn.getProfileCoverURL(ririnMID)    
                    ririn.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = ririn.getContact(ls)
                            mi_d = contact.mid
                            ririn.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        ririn.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = ririn.getContact(ls)
                            ririn.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = ririn.getContact(ls)
                            ririn.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.ririn.naver.jp/" + ririn.getContact(ls).pictureStatus
                            ririn.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.ririn.naver.jp/" + ririn.getContact(ls).pictureStatus + "/vp"
                            ririn.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = ririn.getProfileCoverURL(ls)
                                ririn.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                  if msg._from in Owner:    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            ririn.cloneContactProfile(contact)
                            ririn.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            ririn.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                  if msg._from in Owner:    
                    try:
                        ririnProfile.displayName = str(myProfile["displayName"])
                        ririnProfile.statusMessage = str(myProfile["statusMessage"])
                        ririnProfile.pictureStatus = str(myProfile["pictureStatus"])
                        ririn.updateProfileAttribute(8, ririnProfile.pictureStatus)
                        ririn.updateProfile(ririnProfile)
                        ririn.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        ririn.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            ririn.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            ririn.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            ririn.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            ririn.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        ririn.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+ririn.getContact(mi_d).displayName
                        ririn.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            ririn.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            ririn.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = ririn.getGroup(to)
                    GS = group.creator.mid
                    ririn.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = ririn.getGroup(to)
                    ririn.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = ririn.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ririn.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = ririn.getGroup(to)
                    ririn.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = ririn.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = ririn.reissueGroupTicket(to)
                            ririn.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            ririn.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'groupticket on':
                    if msg.toType == 2:
                        group = ririn.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ririn.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            ririn.updateGroup(group)
                            ririn.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'groupticket off':
                    if msg.toType == 2:
                        group = ririn.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            ririn.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            ririn.updateGroup(group)
                            ririn.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = ririn.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    ririn.sendMessage(to, str(ret_))
                    ririn.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = ririn.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        ririn.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = ririn.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ririn.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        ririn.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                    if msg._from in Owner:
                        settings["blacklist"] = {}
                        ririn.sendMessage(msg.to,"Blacklist Dibersihkan")
                        
                elif text.lower() == 'bancontact':
                    if msg._from in Owner:
                        settings["wblacklist"] = True
                        ririn.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                    if msg._from in Owner:
                        settings["dblacklist"] = True
                        ririn.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                    if msg._from in Owner:
                        if settings["blacklist"] == {}:
                            ririn.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            ririn.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="══════════List Blacklist═════════"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, ririn.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist :  %i" % len(settings["blacklist"])
                            ririn.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("kill "):
                    if msg._from in Owner:
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(KAC).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(KAC).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'dna clear':
                    if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("dna clear","")
                            gs = ririn.getGroup(msg.to)
                            gs = dna1.getGroup(msg.to)
                            gs = dna2.getGroup(msg.to)
                            gs = dna3.getGroup(msg.to)
                            gs = dna4.getGroup(msg.to)
                            gs = dna5.getGroup(msg.to)
                            gs = dna6.getGroup(msg.to)
                            gs = dna7.getGroup(msg.to)
                            gs = dna8.getGroup(msg.to)
                            gs = dna9.getGroup(msg.to)
    #                       ririn.sendMessage(msg.to,"「 Bye All 」")
    #                       ririn.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ririn.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,dna1,dna2,dna3,dna4,dna5,dna6,dna7,dna8,dna9]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    ririn.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'tagall':
                    group = ririn.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        ririn.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        ririn.sendMessage(to, "Total {} Mention".format(str(len(nama))))          
                elif text.lower() == 'read on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                ririn.sendMessage(msg.to,"Read already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            ririn.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'read off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        ririn.sendMessage(msg.to,"Read already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        ririn.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'read reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        ririn.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        ririn.sendMessage(msg.to, "Read belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            ririn.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = ririn.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            ririn.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        ririn.sendMessage(receiver,"Read has not been set.")
                        
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    ririn.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    ririn.sendMessage(msg.to, A)
#==============================================================================#   
                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    ririn.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        ririn.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    ririn.sendMessage(to, str(ret_))
                elif "instagraminfo" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            ririn.sendImageWithURL(to, str(path))
                            ririn.sendMessage(to, str(ret_))
                        except:
                            ririn.sendMessage(to, "Pengguna tidak ditemukan")
                elif "instagrampost" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
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
                                    ririn.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    ririn.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                elif "searchimage" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            ririn.sendImageWithURL(to, str(path))
                elif "searchyoutube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        ririn.sendMessage(to, str(ret_))
                        
                elif "searchmusic " in msg.text.lower():
                            try:                    
                                search = text.replace("searchmusic ","")
                                r = requests.get("https://farzain.xyz/api/joox.php?id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                ririn.sendImageWithURL(to, str(data["gambar"]))
                                ririn.sendMessage(to, str(hasil))
                                ririn.sendMessage(to, "Downloading...")
                                ririn.sendMessage(to, "「 Result MP3 」")
                                ririn.sendAudioWithURL(to, str(audio["mp3"]))
                                ririn.sendMessage(to, "「 Result M4A 」")
                                ririn.sendVideoWithURL(to, str(audio["m4a"]))
                                ririn.sendMessage(to, "Success Download...")
                            except Exception as error:
                            	ririn.sendMessage(to, "「 Result Error 」\n" + str(error))
                            
                elif "searchlyric" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                ririn.sendMessage(to, str(ret_))
                        except:
                            ririn.sendMessage(to, "Lirik tidak ditemukan")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    ririn.sendMessage(to, str(ret_))
                            
#===============================================================================[NEW]                    
                    
            
            elif msg.text.lower().startswith("checkpraytime "):    
                sep = text.split(" ")
                location = text.replace(sep[0] + " ","")
                with requests.session() as web:
                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                    r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                    data = r.text
                    data = json.loads(data)
                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                        ret_ = "╔══[ Prayer Schedule ]"
                        ret_ += "\n╠ Lokasi : " + data[0]
                        ret_ += "\n╠ " + data[1]
                        ret_ += "\n╠ " + data[2]
                        ret_ += "\n╠ " + data[3]
                        ret_ += "\n╠ " + data[4]
                        ret_ += "\n╠ " + data[5]
                        ret_ += "\n╚══[ Complete ]"
                    else:
                        ret_ = "[ Prayer Schedule ] Error : Lokasi tidak ditemukan" 
                        ririn.sendMessage(to, str(ret_))
                        
            elif msg.text.lower().startswith("checkweather "):       
                sep = text.split(" ")
                location = text.replace(sep[0] + " ","")
                with requests.session() as web:
                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                    r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                    data = r.text
                    data = json.loads(data)
                    if "result" not in data:
                        ret_ = "╔══[ Weather Status ]"
                        ret_ += "\n╠ Lokasi : " + data[0].replace("Temperatur di kota ","")
                        ret_ += "\n╠ Suhu : " + data[1].replace("Suhu : ","")
                        ret_ += "\n╠ Kelembaban : " + data[2].replace("Kelembaban : ","")
                        ret_ += "\n╠ Tekanan Udara : " + data[3].replace("Tekanan udara : ","")
                        ret_ += "\n╠ Kecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                        ret_ += "\n╚══[ Complete ]"
                    else:
                        ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                        ririn.sendMessage(to, str(ret_))
                        
            elif msg.text.lower().startswith("checklocation "):   
                sep = text.split(" ")
                location = text.replace(sep[0] + " ","")
                with requests.session() as web:
                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                    r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                    data = r.text
                    data = json.loads(data)
                    if data[0] != "" and data[1] != "" and data[2] != "":
                        link = "https://www.google.co.id/maps/@{},{},(15z".format(str(data[1]), str(data[2]))
                        ret_ = "╔══[ Details Location ]"
                        ret_ += "\n╠ Lokasi : " + data[0]
                        ret_ += "\n╠ Google Maps : " + link
                        ret_ += "\n╚══[ Complete ]"
                    else:
                        ret_ = "[ Details Location ] Error : Lokasi tidak ditemukan"
                        ririn.sendMessage(to,str(ret_))
                # Check if only image
                
            elif text.lower() == 'cpp':
                settings["changePicture"] = True
                ririn.sendMessage(to, "Silahkan kirim gambarnya")
                
            elif text.lower() == 'cgp':
                if msg.toType == 2:
                    if to not in settings["changeGroupPicture"]:
                        settings["changeGroupPicture"].append(to)
                        ririn.sendMessage(to, "Silahkan kirim gambarnya")
                
            elif msg.contentType == 1:
                if settings["changePicture"] == True:
                    path = ririn.downloadObjectMsg(msg_id)
                    settings["changePicture"] = False
                    ririn.updateProfilePicture(path)
                    ririn.sendMessage(to, "Berhasil mengubah foto profile")
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = ririn.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        ririn.updateGroupPicture(to, path)
                        ririn.sendMessage(to, "Berhasil mengubah foto group")   
                            
            elif text.lower() == 'rejectall':
                ginvited = ririn.ginvited
                if ginvited != [] and ginvited != None:
                    for gid in ginvited:
                        ririn.rejectGroupInvitation(gid)
                        ririn.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                else:
                    ririn.sendMessage(to, "Tidak ada undangan yang tertunda")
            
            elif text.lower() == 'invgroupcall':    
                if msg.toType == 2:
                    group = ririn.getGroup(to)
                    members = [mem.mid for mem in group.members]
                    call.acquireGroupCallRoute(to)
                    call.inviteIntoGroupCall(to, contactIds=members)
                    ririn.sendMessage(to, "Berhasil mengundang kedalam telponan group")
                    
            elif text.lower() == 'removeallchat':
                ririn.removeAllMessages(op.param2)
                ririn.sendMessage(to, "Berhasil hapus semua chat")

            elif text.lower() == 'time':
                ririn.sendMessage(to, "Vangke cek sendiri di tanggal jangan manja")
                

            elif msg.text.lower().startswith("gbc "):   
                sep = text.split(" ")
                txt = text.replace(sep[0] + " ","")
                groups = ririn.groups
                for group in groups:
                    ririn.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                    ririn.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                    
            elif msg.text.lower().startswith("bc "):   
                sep = text.split(" ")
                txt = text.replace(sep[0] + " ","")
                friends = ririn.friends
                for friend in friends:
                    ririn.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                    ririn.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
            elif msg.text.lower().startswith("allbroadcast "):   
                sep = text.split(" ")
                txt = text.replace(sep[0] + " ","")
                friends = ririn.friends
                groups = ririn.groups
                for group in groups:
                    ririn.sendMessage(group, "[ Broadcast ]\n{}".format(str(txt)))
                    ririn.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                for friend in friends:
                    ririn.sendMessage(friend, "[ Broadcast ]\n{}".format(str(txt)))
                    ririn.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(friends))))                             
                                    
#===============================================================================[ririnMID - dna1MID]
        if op.type == 19:
            print ("[ 19 ] KICKOUT RIRIN MESSAGE")
            try:
                if op.param3 in ririnMID:
                    if op.param2 in dna1MID:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                    else:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        dna1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna2MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna2MID:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                    else:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        dna2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna3MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna3MID:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                    else:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        dna3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna4MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna4MID:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                    else:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        dna4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna5MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna5MID:
                        G = dna5.getGroup(op.param1)
#                        ginfo = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna5.updateGroup(G)
                        invsend = 0
                        Ticket = dna5.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna5.updateGroup(G)
                    else:
                        G = dna5.getGroup(op.param1)
#                        ginfo = dna5.getGroup(op.param1)
                        dna5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna5.updateGroup(G)
                        invsend = 0
                        Ticket = dna5.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna5.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna6MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna6MID:
                        G = dna6.getGroup(op.param1)
#                        ginfo = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna6.updateGroup(G)
                        invsend = 0
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna6.updateGroup(G)
                    else:
                        G = dna6.getGroup(op.param1)
#                        ginfo = dna6.getGroup(op.param1)
                        dna6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna6.updateGroup(G)
                        invsend = 0
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna6.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna7MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna7MID:
                        G = dna7.getGroup(op.param1)
#                        ginfo = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna7.updateGroup(G)
                        invsend = 0
                        Ticket = dna7.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna7.updateGroup(G)
                    else:
                        G = dna7.getGroup(op.param1)
#                        ginfo = dna7.getGroup(op.param1)
                        dna7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna7.updateGroup(G)
                        invsend = 0
                        Ticket = dna7.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna7.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna8MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna8MID:
                        G = dna8.getGroup(op.param1)
#                        ginfo = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna8.updateGroup(G)
                        invsend = 0
                        Ticket = dna8.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna8.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna8.updateGroup(G)
                    else:
                        G = dna8.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        dna8.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna8.updateGroup(G)
                        invsend = 0
                        Ticket = dna8.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna8.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna8.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ririnMID - dna9MID]
                elif op.param3 in ririnMID:
                    if op.param2 in dna9MID:
                        G = dna9.getGroup(op.param1)
#                        ginfo = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna9.updateGroup(G)
                        invsend = 0
                        Ticket = dna9.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna9.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna9.updateGroup(G)
                    else:
                        G = dna9.getGroup(op.param1)
#                        ginfo = dna9.getGroup(op.param1)
                        dna9.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna9.updateGroup(G)
                        invsend = 0
                        Ticket = dna9.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna9.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna9.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[dna1MID ririnMID]
                if op.param3 in dna1MID:
                    if op.param2 in ririnMID:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                    else:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna2MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna2MID:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                    else:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        dna2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna3MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna3MID:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                    else:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        dna3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna4MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna4MID:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                    else:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        dna4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna5MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna5MID:
                        G = dna5.getGroup(op.param1)
#                        ginfo = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna5.updateGroup(G)
                        invsend = 0
                        Ticket = dna5.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna5.updateGroup(G)
                    else:
                        G = dna5.getGroup(op.param1)
#                        ginfo = dna5.getGroup(op.param1)
                        dna5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna5.updateGroup(G)
                        invsend = 0
                        Ticket = dna5.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna5.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna6MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna6MID:
                        G = dna6.getGroup(op.param1)
#                        ginfo = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna6.updateGroup(G)
                        invsend = 0
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna6.updateGroup(G)
                    else:
                        G = dna6.getGroup(op.param1)
#                        ginfo = dna6.getGroup(op.param1)
                        dna6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna6.updateGroup(G)
                        invsend = 0
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna6.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna7MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna7MID:
                        G = dna7.getGroup(op.param1)
#                        ginfo = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna7.updateGroup(G)
                        invsend = 0
                        Ticket = dna7.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna7.updateGroup(G)
                    else:
                        G = dna7.getGroup(op.param1)
#                        ginfo = dna7.getGroup(op.param1)
                        dna7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna7.updateGroup(G)
                        invsend = 0
                        Ticket = dna7.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna7.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna8MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna8MID:
                        G = dna8.getGroup(op.param1)
#                        ginfo = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna8.updateGroup(G)
                        invsend = 0
                        Ticket = dna8.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna8.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna8.updateGroup(G)
                    else:
                        G = dna8.getGroup(op.param1)
#                        ginfo = dna8.getGroup(op.param1)
                        dna8.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna8.updateGroup(G)
                        invsend = 0
                        Ticket = dna8.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna8.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna8.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna1MID dna9MID]
                elif op.param3 in dna1MID:
                    if op.param2 in dna9MID:
                        G = dna9.getGroup(op.param1)
#                        ginfo = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna9.updateGroup(G)
                        invsend = 0
                        Ticket = dna9.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna9.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna9.updateGroup(G)
                    else:
                        G = dna9.getGroup(op.param1)
#                        ginfo = dna9.getGroup(op.param1)
                        dna9.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna9.updateGroup(G)
                        invsend = 0
                        Ticket = dna9.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna9.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna9.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[dna2MID ririnMID]
                if op.param3 in dna2MID:
                    if op.param2 in ririnMID:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                    else:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna1MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna1MID:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                    else:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        dna1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna3MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna3MID:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                    else:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        dna3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitatram1,Ticket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna4MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna4MID:
                        G = dna4.getGroup(op.param1)
#            op.param2 in dna4MID:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                    else:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        dna4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna5MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna5MID:
                        G = dna5.getGroup(op.param1)
#                        ginfo = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna5.updateGroup(G)
                        invsend = 0
                        Ticket = dna5.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna5.updateGroup(G)
                    else:
                        G = dna5.getGroup(op.param1)
#                        ginfo = dna5.getGroup(op.param1)
                        dna5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna5.updateGroup(G)
                        invsend = 0
                        Ticket = dna5.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna5.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna6MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna6MID:
                        G = dna6.getGroup(op.param1)
#                        ginfo = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna6.updateGroup(G)
                        invsend = 0
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna6.updateGroup(G)
                    else:
                        G = dna6.getGroup(op.param1)
#                        ginfo = dna6.getGroup(op.param1)
                        dna6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna6.updateGroup(G)
                        invsend = 0
                        Ticket = dna6.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna6.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna7MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna7MID:
                        G = dna7.getGroup(op.param1)
#                        ginfo = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna7.updateGroup(G)
                        invsend = 0
                        Ticket = dna7.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna7.updateGroup(G)
                    else:
                        G = dna7.getGroup(op.param1)
#                        ginfo = dna8.getGroup(op.param1)
                        dna7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna7.updateGroup(G)
                        invsend = 0
                        Ticket = dna7.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna7.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna8MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna8MID:
                        G = dna8.getGroup(op.param1)
#                        ginfo = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna8.updateGroup(G)
                        invsend = 0
                        Ticket = dna8.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna8.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna8.updateGroup(G)
                    else:
                        G = dna8.getGroup(op.param1)
#                        ginfo = dna8.getGroup(op.param1)
                        dna8.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna8.updateGroup(G)
                        invsend = 0
                        Ticket = dna8.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna8.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna8.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna8.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna2MID dna9MID]
                elif op.param3 in dna2MID:
                    if op.param2 in dna9MID:
                        G = dna9.getGroup(op.param1)
#                        ginfo = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna9.updateGroup(G)
                        invsend = 0
                        Ticket = dna9.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna9.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna9.updateGroup(G)
                    else:
                        G = dna9.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        dna9.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna9.updateGroup(G)
                        invsend = 0
                        Ticket = dna9.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna9.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna9.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna9.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[dna3MID ririnMID]
                if op.param3 in dna3MID:
                    if op.param2 in ririnMID:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                    else:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna3MID dna1MID]
                elif op.param3 in dna3MID:
                    if op.param2 in dna1MID:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                    else:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        dna1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna3MID dna2MID]
                elif op.param3 in dna3MID:
                    if op.param2 in dna2MID:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                    else:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        dna2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna3MID dna4MID]
                elif op.param3 in dna3MID:
                    if op.param2 in dna4MID:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                    else:
                        G = dna4.getGroup(op.param1)
#                        ginfo = dna4.getGroup(op.param1)
                        dna4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna4.updateGroup(G)
                        invsend = 0
                        Ticket = dna4.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[dna4MID ririnMID]
                if op.param3 in dna4MID:
                    if op.param2 in ririnMID:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                    else:
                        G = ririn.getGroup(op.param1)
#                        ginfo = ririn.getGroup(op.param1)
                        ririn.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ririn.updateGroup(G)
                        invsend = 0
                        Ticket = ririn.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ririn.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ririn.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ririn.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna4MID dna1MID]
                elif op.param3 in dna4MID:
                    if op.param2 in dna1MID:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                    else:
                        G = dna1.getGroup(op.param1)
#                        ginfo = dna1.getGroup(op.param1)
                        dna1.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna1.updateGroup(G)
                        invsend = 0
                        Ticket = dna1.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna1.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna1.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna4MID dna2MID]
                elif op.param3 in dna4MID:
                    if op.param2 in dna2MID:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                    else:
                        G = dna2.getGroup(op.param1)
#                        ginfo = dna2.getGroup(op.param1)
                        dna2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna2.updateGroup(G)
                        invsend = 0
                        Ticket = dna2.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[dna4MID dna3MID]
                elif op.param3 in dna4MID:
                    if op.param2 in dna3MID:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                    else:
                        G = dna3.getGroup(op.param1)
#                        ginfo = dna3.getGroup(op.param1)
                        dna3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        dna3.updateGroup(G)
                        invsend = 0
                        Ticket = dna3.reissueGroupTicket(op.param1)
                        ririn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        dna9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = dna3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        dna3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        dna3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).sendText(op.param1, "Mau Ngundang Siapa Ka?\nKk Bukan Admin\nJadi Aku Cancel😛")
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = dna1.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    dna1.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    ririn.sendMessage(op.param1,"Qr under protect")
            else:
                ririn.sendMessage(op.param1,"")
#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            if op.param1 in read["readPoint"]:
                _name = ririn.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
        backupData()
    except Exception as error:
        logError(error)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = ririn.findGroupByTicket(ticket_id)
                        ririn.acceptGroupInvitationByTicket(group.id,ticket_id)
                        ririn.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name)) 
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != ririn.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    ririn.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        ririn.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in ririnMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if ririnMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = ririn.getContact(sender)
                                    ririn.sendMessage(to, "sundala nu")
                                    sendMessageWithMention(to, contact.mid)
                                break
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        ririn.acceptGroupInvitation(op.param1)
        dna1.acceptGroupInvitation(op.param1)
        dna2.acceptGroupInvitation(op.param1)
        dna3.acceptGroupInvitation(op.param1)
        dna4.acceptGroupInvitation(op.param1)
        dna5.acceptGroupInvitation(op.param1)
        dna6.acceptGroupInvitation(op.param1)
        dna7.acceptGroupInvitation(op.param1)
        dna8.acceptGroupInvitation(op.param1)
        dna9.acceptGroupInvitation(op.param1)
    except Exception as e:
        ririn.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        ririn.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
