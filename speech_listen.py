import speech_recognition as sr
import pyttsx3 as pyttsx
import os
import asyncio
import time
from wit import Wit
import requests
import json
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *



import io
import os
import sys
import subprocess
import wave
import aifc
import math
import audioop
import collections
import json
import base64
import threading
import platform
import stat
import hashlib
import hmac
import time
import uuid

try:  # attempt to use the Python 2 modules
    from urllib import urlencode
    #from urllib2 import Request, urlopen, URLError, HTTPError
except ImportError:  # use the Python 3 modules
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
class Speaking:
	def to_say(speaking_word):
		speech_engine = pyttsx.init()
		speech_engine.say(speaking_word)
		speech_engine.runAndWait()	
class Listening:
	def listening_function():
		r = sr.Recognizer()
		speach=""		
		print("TEST")
		API_KEY="UNYDMIHRNPDM53AKFKF4G3NSZNQIWXFZ"
		print("STARTING TO LISTEN: " + time.strftime("%H:%M:%S"))
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			#await audio
		try:
			print("LISTENING END: " + time.strftime("%H:%M:%S"))
			speach_audio=audio.get_wav_data()
			#speach=r.recognize_google(audio).lower()
			url = "https://api.wit.ai/speech?v=20170307"
			request = Request(url, data=speach_audio, headers={"Authorization": "Bearer {}".format(API_KEY), "Content-Type": "audio/wav"})
			try:
				response = urlopen(request, timeout=10)
			except HTTPError as e:
				raise print("recognition request failed: {}".format(e.reason))
			except URLError as e:
				raise print("recognition connection failed: {}".format(e.reason))
			print("RESPONSE ACCEPTED: " + time.strftime("%H:%M:%S"))
			response_text = response.read().decode("utf-8")
			result = json.loads(response_text)
			print(str(result) + time.strftime("%H:%M:%S"))
			entities=result["entities"]
			print(type(entities))
			print (entities.keys())
			#print(result["entities"]["mirror"]["confidence"])
			for s in entities:
				print(entities[s])
				if (s=="mirror"):	
					for p in entities[s]:
						if (p["confidence"]>0.9 and "hi " in result["_text"].lower()):
								speach="hi mirror"

			if(len(speach)==0):
				speach=result["_text"].lower()
		#l= Listening.listening_function()
		except sr.UnknownValueError:
			print("WIT Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from WIT Speech Recognition service;{0}".format(e))
		except Exception as e:
			print(e)
		'''BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		r = sr.Recognizer()
		speach=""		
		API_KEY="UNYDMIHRNPDM53AKFKF4G3NSZNQIWXFZ"
		print("STARTING TO LISTEN: " + time.strftime("%H:%M:%S"))
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			#await audio
		try:
			print("LISTENING END: " + time.strftime("%H:%M:%S"))
			speach=audio.get_wav_data()
			#speach=recognize_wit(r, audio, API_KEY).lower()
			url = "https://api.wit.ai/speech?v=20170307"
			request = Request(url, data=speach, headers={"Authorization": "Bearer {}".format(API_KEY), "Content-Type": "audio/wav"})
			try:
				response = urlopen(request, timeout=10)
			except HTTPError as e:
				raise RequestError("recognition request failed: {}".format(e.reason))
			except URLError as e:
				raise RequestError("recognition connection failed: {}".format(e.reason))
			print("RESPONSE ACCEPTED: " + time.strftime("%H:%M:%S"))
			response_text = response.read().decode("utf-8")
			result = json.loads(response_text)
			print(str(result) + time.strftime("%H:%M:%S"))
			#print("Google Speech Recognition thinks you said " + speach + '----------->' + time.strftime("%H:%M:%S"))
			
			#threading_q.put(l)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service;{0}".format(e))'''
		return speach
		#return razgovor
#Listening.listening_function()	
