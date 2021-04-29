import speech_recognition as sr
import subprocess
import os
import signal
#import Virtual_asistent as asistant
#from wikipedia_window import wiki
#from youtube import *
import time
import multiprocessing
from multiprocessing import Queue
#from SmartMirror.py import okno
# obtain audio from the microphone
#from SmartMirror import *
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *


#class Start_Listening:
#while (True):
#def __init__(self):
listen=0
#print('OK')
    
#while listened<5:
r = sr.Recognizer()
while (True):
    with sr.Microphone() as source:
        print("Say something1234!")
        #q=Queue()
        #print(q.get())
        print(Frame)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        #audio = r.adjust_for_ambient_noise(source)
        print(audio)
        # recognize speech using Google Speech Recognition

    try:
        # for testing purposes, you're just using the default API key
        # to use another API key, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        razgovor=r.recognize_google(audio).lower()
        razgovor_search=""
        if('mirror' in razgovor):
            Open_yt_search=subprocess.Popen(["python3","SmartMirror.py"])
            break
    except:
	print(sys.exc_info()[0])
        continue
	
