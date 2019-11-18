import random
import time
import os
import datetime
import calendar
import subprocess
import webbrowser
#import wolframalpha
import wikipedia
import pyttsx3 as pyttsx
import speech_recognition as sr
import tkinter
import urllib.parse as urllib
import json
from tkinter import *
#import smartmirror
#import reminders
#import muzika
#import koledar
#from gtts import gTTS
new = 2
ukaz = [""]
izgovorjeno=[""]
speech_engine = pyttsx.init()

class AI():
    """docstring for ."""
    #def __init__(self, arg):
        #super(, self).__init__()

    #konstruktor
    def __init__(self):
        self.zac()

    def govor(self,besedilo):
        speech_engine.say(besedilo)
        speech_engine.runAndWait()
        #tts = gTTS(text=besedilo, lang='en')
        #tts.save("good.mp3")
        #os.system("good.mp3")
    def posluh(self):
        poslusa = 0
        while poslusa < 1:
            razgovor = ""
            go = sr.Recognizer()
            while True:
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = go.listen(source)
                    print(audio)
                    if go == "":
                        continue
                    else:
                        print('Hey')
                        break
            try:
                print("You said: " + go.recognize_google(audio))
                razgovor += go.recognize_google(audio)
                print (razgovor)
                razd = razgovor.split(" ")
            except:
                print("I didn't hear nothing.")
                continue
        return razgovor
    def start(self):
        poslusa = 0
        while poslusa < 1:
            razgovor = ""
            go = sr.Recognizer()
            while True:
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = go.listen(source)
                    if go == "":
                        continue
                    else:
                        break
            try:
                print("You said: " + go.recognize_google(audio))
                razgovor += go.recognize_google(audio)
                print (razgovor)
                razd = razgovor.split(" ")
                for t in razd:
                    if t == "computer":
                        #poja =+1
                        poslusa =+ 1
                        self.zac()
                    elif t == "morning":
                        mor= "Good morning sir."
                        self.govor(mor)
                        poslusa =+1
                        self.zac()
                    else:
                        continue
            except:
                continue
    #def glasba(self):
    #    muzika.okn()
    def datoteka(self):
        a = "How shuld I named the document"
        '''self.govor(a)
        ime = self.posluh()
        d = "What shuld I write in the document"
        self.govor(d)
        vno = self.posluh
        novdoc = gTTS(text=vno, lang='en')
        imedat = ime + ".txt"
        novdoc.save(imedat)'''
    def teden(self,mes):
        teden=("mon", "tue", "wed", "thu", "fri", "sat", "sun")
        mi = ""
        for wor in teden:
            if wor == mes:
                if mes == "mon":
                    mi+="monday"
                if mes == "tue":
                    mi+="tuesday"
                if mes == "wed":
                    mi+= "wednesday"
                if mes == "thu":
                    mi+= "thursday"
                if mes == "fri":
                    mi+= "friday"
                if mes == "sat":
                    mi+= "saturday"
                if mes == "sun":
                    mi+= "sunday"
        #print mi
        return mi
    def mesec(self,ted):
        me = ""
        mesec=("jan", "feb", "mar", "apr", "may", "jun", "jul", "avg", "sep", "oct", "nov", "dec")
        for bese in mesec:
            if bese == ted:
                if ted == "jan":
                    me+= "january"
                if ted == "feb":
                    me+= "february"
                if ted == "mar":
                    me+= "march"
                if ted == "apr":
                    me+= "april"
                if ted == "may":
                    me+= "may"
                if ted == "jun":
                    me+= "june"
                if ted == "jul":
                    me+= "july"
                if ted == "avg":
                    me+= "avgust"
                if ted == "sep":
                    me+= "september"
                if ted == "oct":
                    me+= "october"
                if ted == "nov":
                    me+= "november"
                if ted == "dec":
                    me+= "december"
        return me
    def deset(self,ste):
        des = ""
        if ste == "00":
            des+= "0"
        elif ste == "01":
            des+= "1"
        elif ste == "02":
            des+= "2"
        elif ste == "03":
            des+= "3"
        elif ste == "04":
            des+= "4"
        elif ste == "05":
            des+= "5"
        elif ste == "06":
            des+= "6"
        elif ste == "07":
            des+= "7"
        elif ste == "08":
            des+= "8"
        elif ste == "09":
            des+= "9"
        return des
    def wiki(self,elf):
        wi = elf.split(" ")
        for i in wi:
            print (i)
        return elf
    def quest(self):
        vprasanja= [' ']
        que = 0
        while True:
            vpras = ""
            h = 0
            if que == 0:
                vr = "What is your question?"
            else:
                vr = "Do you have any more questions?"
            self.govor(vr)
            que+=1
            vn = input("What is your question: ")
            if vn == "":
                vn = input("What is your question: ")
            else:
                self.govor(vn)
            data = "Accesing the data. Please wait."
            self.govor(data)
            vra = vn.split(" ")
            for y in vra:
                if y == "he" or y == "she" or y == "it":
                    if h == 0:
                        vpras += y + " "
                    else:
                        vp = self.wiki(vprasanja[len(vprasanja) - 1])
                        vpras += vp
                elif  y == "thank" or y == "thanks":
                    tha="You are welcome."
                    self.govor(tha)
                    self.start()
                elif y == "question":
                    h = 0
                else :
                    if y == vra[len(vra)-1]:
                        vpras += y + "."
                    else:
                        vpras += y + " "

            vprasanja.append(vpras)
            #try:
            #    app_id = "L82GJK-J6W72HEX54"
            #    client = wolframalpha.Client(app_id)
            #    res = client.query(vpras)
            #    answer = next(res.results).text
                #self.govor(answer)
            #    print answer
            #except:
            #wikipedia.set_lang("")
            odgovor = wikipedia.summary(vpras, sentences = 2)
            self.govor(odgovor)
            print (odgovor)
    def zac(self):
        GE = "Hello sir"
        self.govor(GE)
        #print GE
        #smartmirror.zacni()
        self.jarvis()
    def jarvis(self):
        while True:
            lis = ("Hello", "hello", "Wikipedia", "Google", "day", "hate", "of", "do not", "don't", "thanks", "map","maps", "search", "facebook", "new", "document", "folder", "alarm", "good", "how", "identify", "identified", "thank", "shutdown", "on", "lights", "living", "room", "my", "reminders", "reminder", "for", "music", "flip", "coin", "off", "shut", "up", "don't", "jokes", "email", "note", "problem", "bye", "time","calendar","morning","web","Alexa", "date", "YouTube", "question", "are", "smart", "stupid", "getting", "smarter", "name", "doing")

            resp2 = self.posluh()
            print (resp2)
            izgovorjeno.append(resp2)
            male = resp2.lower()
            vnos = resp2.split(" ")
            vneseno = [" "]
            besedilo = ""

            for word in vnos:
                for x in lis:
                    if word == x:
                        vneseno.append(x)
                        besedilo += x + " "
            print (vneseno)
            print (vnos)
            print (besedilo)
            ukaz.append(besedilo)
            print (ukaz)

            for z in range(0,len(vneseno)):
                esa = vneseno[z]
                if esa == "email":
                    b = random.choice(("email ok then", "ok. Whats your email adress", "what should I write in email"))
                    print (b)
                    self.govor(b)
                elif esa == "hello" or esa == "Hello":
                    he = "Hello to you too"
                    self.govor(he)
                elif esa == "do not":
                    z+=1
                elif esa == "don't":
                    z+=1
                elif esa == "Alexa":
                    h = random.choice(("Hello I am Alexa. I am waiting for your command", "Hy sir. What should I do for you"))
                    self.govor(h)
                elif esa == "date" or esa == "day":
                    a = time.asctime()
                    c = a.lower()
                    b = c.split(" ")
                    d = ""
                    m = ""
                    dane= b[2]
                    datum = [" "]
                    for bes in b:
                        #print bes
                        if bes == b[0]:
                            d+= self.teden(bes)
                        elif bes == b[1]:
                            m+= self.mesec(bes)
                        else:
                            continue
                    izpis = "Today it is "+d+", "+m+" "+dane
                    print (izpis)
                    self.govor(izpis)
                elif esa == "time":
                    t = time.asctime()
                    ti = t.split(" ")
                    tim = ti[3]
                    cur = tim.split(":")
                        #self.self.govor(tim)
                    q = ""
                    k = ""
                    h = ""
                    f = ""
                    s = 0
                    st = 0
                    for l in tim:
                        if l == ":":
                            st+= 1
                        elif st == 2:
                            break
                        elif st == 0:
                            h+= l
                        elif st == 1:
                            f+= l
                    if int(h) < 10:
                        q = self.deset(h)
                        h = q
                    elif int(f) < 10:
                        k = self.deset(f)
                        f = k
                    g= "Current time is "+h+" and "+f+" minutes"
                    '''print tim
                    print cur
                    print t
                    print g'''
                    self.govor(g)
                elif esa == "question":
                    self.quest()
                elif esa == "morning":
                    g = "Good morning, Nejc. Have a wonderful day."
                    self.govor(g)
                    print (g)
                elif esa == "YouTube":
                    speak = "Opening youtube"
                    self.govor(speak)
                    url = "https://www.youtube.com/"
                    webbrowser.open(url, new=new)
                elif esa == "facebook":
                    speak = "Opening facebook"
                    self.govor(speak)
                    url = "https://www.facebook.com/"
                    webbrowser.open(url, new=new)
                #elif esa == "calendar":
                #    koledar.cale()
                elif esa == "jokes":
                    c = random.choice(("I do not know any joke", "Knock Knock"))
                    print (c)
                    self.govor(c)
                elif esa == "problem":
                    t= random.choice(("I do not know how to help you", "What should I do about it."))
                    print (t)
                    self.govor(t)
                elif esa == "web":
                    print ("opening chrome!!")
                    webspeak = "Opening webbrowser"
                    self.govor(webspeak)
                    url = "https://www.google.com"
                    webbrowser.open(url, new=new)
                elif esa == "bye":
                    m = random.choice(("Goodbye", "See you later sir"))
                    print (m)
                    self.govor(m)
                    self.start()
                elif esa == "alarm":
                    ala = "On what time should I set an alarm."
                    self.govor(ala)
                    al = self.posluh()
                    alar = str(al)
                    print (alar)
                elif esa == "good":
                    dobr = "That is very nice to hear. Should I do anything else for you?"
                    self.govor(dobr)
                    break
                elif esa == "shutdown":
                    shut = "Shutting down ..."
                    self.govor(shut)
                    self.start()

            if besedilo == "are smart ":
                smartass = "Thank you sir."
                self.govor(smartass)
            elif besedilo == "flip coin ":
                coin = random.choice(("I got heads.", "I got tails."))
                self.govor(coin)
            elif besedilo == "are stupid ":
                stupido = "Well in that case you programmed me to be stupid."
                self.govor(stupido)
            elif besedilo == "are getting smarter ":
                sma = "I learn of my mistakes, sir."
                self.govor(sma)
            elif besedilo == "name ":
                name = "My name is Jayne"
                self.govor(name)
            elif besedilo == "search Google for ":
                t=0
                iskanje=""
                for k in vnos:
                    if k == "for":
                        t+=1
                        continue
                    if t == 1:
                        if k == vnos[len(vnos)-1]:
                            iskanje+= k
                        else:
                            iskanje+= k+" "
                print (iskanje)
                encoded = urllib.quote(iskanje)
                webbrowser.open("https://www.google.si/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q="+encoded)
            elif besedilo == "search Wikipedia for ":
                ig=0
                wiki=""
                for m in vnos:
                    if m == "for":
                        ig+=1
                        print (m)
                        continue
                    if ig == 1:
                        if m == vnos[len(vnos)-1]:
                            wiki+= m
                        else:
                            wiki+= m+" "
                print (wiki)
                encoded = urllib.quote(wiki)
                webbrowser.open("https://sl.wikipedia.org/wiki/"+encoded)
            elif besedilo == "hate ":
                sov= "I hate you to."
                self.govor(sov)
            elif besedilo == "how are ":
                pocutje = "I am very good. What about you?"
                self.govor(pocutje)
            elif besedilo == "identify ":
                description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
                self.govor(description)
            elif besedilo == "identified ":
                description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
                self.govor(description)
            elif besedilo == "are doing ":
                delo = "I am waiting for your command, sir."
                self.govor(delo)
            elif besedilo == "do something":
                de = "What should I do for you?"
                self.govor(de)
            elif besedilo == "music ":
                a = "playing music"
                self.govor(a)
                os.system("start C:/Users/nejcb/Desktop/seznam.xspf")
            elif besedilo == "new file ":
                self.datoteka()
            elif besedilo == "new document ":
                self.datoteka()
            elif besedilo == "off lights living room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.govor(predvajaj)
            elif besedilo == "on lights living room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.govor(predvajaj)
            elif besedilo == "off lights my room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.govor(predvajaj)
            elif besedilo == "on lights my room ":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.govor(predvajaj)
            elif besedilo == "":
                predvajaj = "I am not progrramed to do that yet but I will be soon."
                self.govor(predvajaj)
            elif besedilo == "map of " or besedilo == "maps of ":
                mesto = ""
                z=0
                zemla = "Openning google maps."
                self.govor(zemla)
                for i in vnos:
                    if i == "of":
                     z+=1
                     continue
                    if z == 1:
                        if i == vnos[len(vnos)-1]:
                            mesto+= i
                        else:
                            mesto+= i+" "
                city = urllib.quote(mesto)
                zemljevid= "https://www.google.de/maps/"
                webbrowser.open("https://www.google.de/maps/place/"+city)
            elif besedilo == "thank " or besedilo == "thanks ":
                izgovor="You are welcome"
                self.govor(izgovor)
                self.start()
AI()
