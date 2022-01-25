try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
import random
import time
from tkinter import *
new = 2
ukaz = [""]
izgovorjeno=[""]

def teden(mes):
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
def mesec(ted):
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
def deset(ste):
    des = ""
    if int(ste)<10:
        des="0"+ste
    '''if ste == "00":
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
        des+= "9"'''
    return des
def zac():
    GE = "Hello sir"
    govor(GE)
    jarvis()
    #jarvis()
def jarvis(listening):
#def __init__( listening):
    #while True:
    lis = ("test", "Hello", "hello", "Jane", "Wikipedia", "Google", "day", "hate", "of", "do not", "don't", "thanks", "map","maps", "search", "facebook", "new", "document", "folder", "alarm", "good", "how", "identify", "identified", "thank", "shutdown", "on", "lights", "living", "room", "my", "reminders", "reminder", "for", "music", "flip", "coin", "off", "shut", "up", "don't", "jokes", "email", "note", "problem", "bye", "time","calendar","morning","web","Alexa", "date", "YouTube", "question", "are", "smart", "stupid", "getting", "smarter", "name", "doing", "calibrate", "calibration","start", "stop", "close", "end" )

    resp2 = listening#posluh()
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
    '''print (vneseno)
    print (vnos)'''
    print (besedilo)
    ukaz.append(besedilo)
    #label1
    #print (ukaz)

    for z in range(0,len(vneseno)):
        esa = vneseno[z]
        if "hello" in esa or "Hello" in esa:
            he = "Hello to you too"
            govor(he)
        elif "do not" in esa:
            z+=1
        elif "don't" in esa:
            z+=1
        elif "Jayne"  in esa or "Jane" in esa:
            h = random.choice(("Hello I am Jayne. I am waiting for your command", "Hy sir. What should I do for you"))
            govor(h)
        elif "date" in esa or "day" in esa:
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
                    d+= teden(bes)
                elif bes == b[1]:
                    m+= mesec(bes)
                else:
                    continue
            izpis = "Today it is "+d+", "+m+" "+dane
            print (izpis)
            govor(izpis)
        elif "time" in esa:
            t = time.asctime()
            ti = t.split(" ")
            tim = ti[3]
            cur = tim.split(":")
                #govor(tim)
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
                q = deset(h)
                h = q
            elif int(f) < 10:
                k = deset(f)
                f = k
            g= "Current time is "+h+" and "+f+" minutes"
            '''print tim
            print cur
            print t
            print g'''
            govor(g)
        elif "morning" in esa:
            g = "Good morning, Nejc. Have a wonderful day."
            govor(g)
            print (g)
        elif "jokes" in esa:
            c = random.choice(("I do not know any joke", "Knock Knock"))
            print (c)
            govor(c)
        elif "good" in esa:
            dobr = "That is very nice to hear. Should I do anything else for you?"
            govor(dobr)
            break

    if "are smart" in besedilo:
        smartass = "Thank you sir."
        govor(smartass)
    elif "flip coin" in besedilo:
        coin = random.choice(("I got heads.", "I got tails."))
        govor(coin)
    elif "are stupid" in besedilo:
        stupido = "Well in that case you programmed me to be stupid."
        govor(stupido)
    elif "are getting smarter" in besedilo:
        sma = "I learn of my mistakes, sir."
        govor(sma)
    elif "name" in besedilo:
        name = "My name is Jayne"
        govor(name)
    elif "hate" in besedilo:
        sov= "I hate you to."
        govor(sov)
    elif "how are" in besedilo:
        pocutje = "I am very good. What about you?"
        govor(pocutje)
    elif "identify" in besedilo:
        description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
        govor(description)
    elif "identified" in besedilo:
        description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
        govor(description)
    elif "are doing" in besedilo:
        delo = "I am waiting for your command, sir."
        govor(delo)
    elif "do something" in besedilo:
        de = "What should I do for you?"
        govor(de)    
    elif "thank " or "thanks ":
        izgovor="You are welcome"
        govor(izgovor)
