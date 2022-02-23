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

__author__ = "Anthony Zhang (Uberi)"
__version__ = "3.8.1"
__license__ = "BSD"

try:  # attempt to use the Python 2 modules
    from urllib import urlencode
    #from urllib2 import Request, urlopen, URLError, HTTPError
except ImportError:  # use the Python 3 modules
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError


class WaitTimeoutError(Exception): pass


class RequestError(Exception): pass


class UnknownValueError(Exception): pass






API_KEY="UNYDMIHRNPDM53AKFKF4G3NSZNQIWXFZ"
class Speaking:
	def to_say(speaking_word):
		speech_engine = pyttsx.init()
		speech_engine.say(speaking_word)
		speech_engine.runAndWait()	
def recognize_wit(self, audio_data, key, show_all=False):
	"""
	Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Wit.ai API.
	The Wit.ai API key is specified by ``key``. Unfortunately, these are not available without `signing up for an account <https://wit.ai/>`__ and creating an app. You will need to add at least one intent to the app before you can see the API key, though the actual intent settings don't matter.
	To get the API key for a Wit.ai app, go to the app's overview page, go to the section titled "Make an API request", and look for something along the lines of ``Authorization: Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX``; ``XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`` is the API key. Wit.ai API keys are 32-character uppercase alphanumeric strings.
	The recognition language is configured in the Wit.ai app settings.
	Returns the most likely transcription if ``show_all`` is false (the default). Otherwise, returns the `raw API response <https://wit.ai/docs/http/20141022#get-intent-via-text-link>`__ as a JSON dictionary.
	Raises a ``speech_recognition.UnknownValueError`` exception if the speech is unintelligible. Raises a ``speech_recognition.RequestError`` exception if the speech recognition operation failed, if the key isn't valid, or if there is no internet connection.
	"""
	#assert isinstance(audio_data, self.AudioData), "Data must be audio data"
	#assert isinstance(key, str), "``key`` must be a string"

	wav_data = audio_data.get_wav_data(
		convert_rate=None if audio_data.sample_rate >= 8000 else 8000,  # audio samples must be at least 8 kHz
		convert_width=2  # audio samples should be 16-bit
	)
	print("CONVERTED TO WAV: " + time.strftime("%H:%M:%S"))
	url = "https://api.wit.ai/speech?v=20170307"
	request = Request(url, data=wav_data, headers={"Authorization": "Bearer {}".format(key), "Content-Type": "audio/wav"})
	try:
		response = urlopen(request, timeout=self.operation_timeout)
	except HTTPError as e:
		raise RequestError("recognition request failed: {}".format(e.reason))
	except URLError as e:
		raise RequestError("recognition connection failed: {}".format(e.reason))
	print("RESPONSE ACCEPTED: " + time.strftime("%H:%M:%S"))
	response_text = response.read().decode("utf-8")
	result = json.loads(response_text)
	print(str(result) + time.strftime("%H:%M:%S"))

	# return results
	if show_all: return result
	if "_text" not in result or result["_text"] is None: raise UnknownValueError()
	return result["_text"]
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
			entities=result["entities"]
			print(type(entities))
			print (entities.keys())
			#print(result["entities"]["mirror"]["confidence"])
			for s in entities:
				print(entities[s])
				if (s=="mirror"):	
					for p in entities[s]:
						if (p["confidence"]>0.9 and "hi " in result["_text"].lower()):
								speach="mirror"

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
