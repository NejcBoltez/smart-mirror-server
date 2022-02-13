import speech_recognition as sr
import pyttsx3 as pyttsx
import os
import asyncio
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

class Speaking:
	def to_say(speaking_word):
		speech_engine = pyttsx.init()
		speech_engine.say(speaking_word)
		speech_engine.runAndWait()	
class Listening:
	def listening_function():
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		r = sr.Recognizer()
		speach=""		
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			#await audio
		try:
			print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
			speach=r.recognize_google(audio).lower()
			
			#threading_q.put(l)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service;{0}".format(e))
		return speach
		#return razgovor	