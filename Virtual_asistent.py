try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
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
#import pyaudio
#from pygsr import Pygsr
#import smartmirror
#import reminders
#import muzika
#import koledar
#from gtts import gTTS
new = 2
ukaz = [""]
izgovorjeno=[""]
speech_engine = pyttsx.init()
'''form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 1 # device index found by p.get_device_info_by_index(ii)'''

#class AI():
    #def __init__():
    #    GE = "Hello sir"
    #    govor(GE)
        #jarvis("test")

def govor(besedilo):
    speech_engine.say(besedilo)
    speech_engine.runAndWait()
def posluh():
    r = sr.Recognizer()
    razgovor=''
    poslusa=0
    while razgovor=='':
        with sr.Microphone() as source:
            print("Say something1234!")
            audio = r.listen(source)
            #print(audio)
            # recognize speech using Google Speech Recognition
            '''if audio=="":
                continue
            else:
                break'''
        try:
            # for testing purposes, you're just using the default API key
            # to use another API key, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
            razgovor=r.recognize_google(audio)
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service;{0}".format(e))
    return razgovor
    '''speech = Pygsr()
    # duration in seconds
    speech.record(0)
    # select the language
    phrase, complete_response = speech.speech_to_text('en_US')
    print(phrase)
    print(complete_response)'''
    '''audio = pyaudio.PyAudio() # create pyaudio instantiation
    go = sr.Recognizer()
    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(go.recognize_google(stream))
        
    print (frames)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()'''
    '''
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
            print("You said: " + go.recognize(audio))
            razgovor += go.recognize(audio)
            print (razgovor)
            razd = razgovor.split(" ")
        except:
            print("I didn't hear nothing.")
            continue
    return razgovor'''
def start():
    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)
    print (frames)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()
#def glasba():
#    muzika.okn()
def datoteka():
    a = "How shuld I named the document"
    '''govor(a)
    ime = posluh()
    d = "What shuld I write in the document"
    govor(d)
    vno = posluh
    novdoc = gTTS(text=vno, lang='en')
    imedat = ime + ".txt"
    novdoc.save(imedat)'''
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
def wiki(elf):
    wi = elf.split(" ")
    for i in wi:
        print (i)
    return elf
def quest():
    vprasanja= [' ']
    que = 0
    while True:
        vpras = ""
        h = 0
        if que == 0:
            vr = "What is your question?"
        else:
            vr = "Do you have any more questions?"
        govor(vr)
        que+=1
        vn = input("What is your question: ")
        if vn == "":
            vn = input("What is your question: ")
        else:
            govor(vn)
        data = "Accesing the data. Please wait."
        govor(data)
        que+=1
        vra = vn.split(" ")
        for y in vra:
            if y == "he" or y == "she" or y == "it":
                if h == 0:
                    vpras += y + " "
                else:
                    vp = wiki(vprasanja[len(vprasanja) - 1])
                    vpras += vp
            elif  y == "thank" or y == "thanks":
                tha="You are welcome."
                govor(tha)
                start()
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
            #govor(answer)
        #    print answer
        #except:
        #wikipedia.set_lang("")
        odgovor = wikipedia.summary(vpras, sentences = 2)
        root=tk.Tk()
        #root.tk.geometry("800x600")
        FrameWiki=Label(root, text=odgovor)
        FrameWiki.pack
        root.mainloop()
        govor(odgovor)
        print (odgovor)
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
        if esa == "email":
            b = random.choice(("email ok then", "ok. Whats your email adress", "what should I write in email"))
            print (b)
            govor(b)
        elif esa == "hello" or esa == "Hello":
            he = "Hello to you too"
            govor(he)
        elif esa == "do not":
            z+=1
        elif esa == "don't":
            z+=1
        elif esa == "Jayne" or esa == "Jane":
            h = random.choice(("Hello I am Jayne. I am waiting for your command", "Hy sir. What should I do for you"))
            govor(h)
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
                    d+= teden(bes)
                elif bes == b[1]:
                    m+= mesec(bes)
                else:
                    continue
            izpis = "Today it is "+d+", "+m+" "+dane
            print (izpis)
            govor(izpis)
        elif esa == "time":
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
        elif esa == "question":
            quest()
        elif esa == "morning":
            g = "Good morning, Nejc. Have a wonderful day."
            govor(g)
            print (g)
        elif esa == "YouTube":
            speak = "Opening youtube"
            govor(speak)
            YoutubeWindow=subprocess.Popen(["python3", "youtube.py", "test"], stdin=subprocess.PIPE)
            #url = "https://www.youtube.com/"
            #webbrowser.open(url, new=new)
        elif esa == "facebook":
            speak = "Opening facebook"
            govor(speak)
            url = "https://www.facebook.com/"
            webbrowser.open(url, new=new)
        #elif esa == "calendar":
        #    koledar.cale()
        elif esa == "jokes":
            c = random.choice(("I do not know any joke", "Knock Knock"))
            print (c)
            govor(c)
        elif esa == "problem":
            t= random.choice(("I do not know how to help you", "What should I do about it."))
            print (t)
            govor(t)
        elif esa == "web":
            print ("opening chrome!!")
            webspeak = "Opening webbrowser"
            govor(webspeak)
            url = "https://www.google.com"
            webbrowser.open(url, new=new)
        elif esa == "bye":
            m = random.choice(("Goodbye", "See you later sir"))
            print (m)
            govor(m)
            start()
        elif esa == "alarm":
            ala = "On what time should I set an alarm."
            govor(ala)
            al = posluh()
            alar = str(al)
            print (alar)
        elif esa == "good":
            dobr = "That is very nice to hear. Should I do anything else for you?"
            govor(dobr)
            break
        elif esa == "shutdown":
            shut = "Shutting down ..."
            govor(shut)
            start()
        elif esa == "calibrate" or esa == "calibration":
            if "stop" not in besedilo:
                calibrateWindow=subprocess.Popen(["python3", "calibrate.py", "test"], stdin=subprocess.PIPE)
            else:
                try:
                    calibrateWindow.stdin.write(str.encode('q'))
                except(exec):
                    Calibnotopen="Calibration is not open"
                    govor(Calibnotopen)
                    print(exec)

    if besedilo == "are smart ":
        smartass = "Thank you sir."
        govor(smartass)
    elif besedilo == "flip coin ":
        coin = random.choice(("I got heads.", "I got tails."))
        govor(coin)
    elif besedilo == "are stupid ":
        stupido = "Well in that case you programmed me to be stupid."
        govor(stupido)
    elif besedilo == "are getting smarter ":
        sma = "I learn of my mistakes, sir."
        govor(sma)
    elif besedilo == "name ":
        name = "My name is Jayne"
        govor(name)
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
    # elif (besedilo == "start calibration" or besedilo == "calibrate") and besedilo != "stop":
    #elif besedilo == "start calibration":
        #calib_start=subprocess.Popen(["python3", "cv.py"])
    #    govor("Starting to calibrate")
    #elif besedilo == "stop calibration":
    #    try:   
    #        calib_start.kill()
    #    except:
    #        govor('Calibration is not running')
    elif besedilo == "hate ":
        sov= "I hate you to."
        govor(sov)
    elif besedilo == "how are ":
        pocutje = "I am very good. What about you?"
        govor(pocutje)
    elif besedilo == "identify ":
        description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
        govor(description)
    elif besedilo == "identified ":
        description = "I am an virtual asistent made by Nejc Boltez. I can do many of things. I can tell you time date. I also can open youtube and google for you. But most important thing I can do is that I can answer your question"
        govor(description)
    elif besedilo == "are doing ":
        delo = "I am waiting for your command, sir."
        govor(delo)
    elif besedilo == "do something":
        de = "What should I do for you?"
        govor(de)
    elif besedilo == "music ":
        a = "playing music"
        govor(a)
        os.system("start C:/Users/nejcb/Desktop/seznam.xspf")
    elif besedilo == "new file ":
        datoteka()
    elif besedilo == "new document ":
        datoteka()
    elif besedilo == "off lights living room ":
        predvajaj = "I am not progrramed to do that yet but I will be soon."
        govor(predvajaj)
    elif besedilo == "on lights living room ":
        predvajaj = "I am not progrramed to do that yet but I will be soon."
        govor(predvajaj)
    elif besedilo == "off lights my room ":
        predvajaj = "I am not progrramed to do that yet but I will be soon."
        govor(predvajaj)
    elif besedilo == "on lights my room ":
        predvajaj = "I am not progrramed to do that yet but I will be soon."
        govor(predvajaj)
    elif besedilo == "":
        predvajaj = "I am not programed to do that yet but I will be soon."
        govor(predvajaj)
    #elif besedilo == "test":
    #    continue
    elif besedilo == "map of " or besedilo == "maps of " or besedilo == "Map of " or besedilo == "Maps of ":
        mesto = ""
        z=0
        zemla = "Openning google maps."
        govor(zemla)
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
        govor(izgovor)
        start()

'''if str(sys.argv[1]) != "":
    index=str(sys.argv[1])
    jarvis(index)
else:
    print("please put some arg")'''
