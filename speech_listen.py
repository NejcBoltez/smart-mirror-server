import speech_recognition as sr
import pyttsx3 as pyttsx
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import asyncio
import os
import subprocess
import signal
import time
from multiprocessing import Process
#from send_command import Do_for_command
r = sr.Recognizer()

class Speaking:
	def to_say(speaking_word):
		speech_engine = pyttsx.init()
		speech_engine.say(speaking_word)
		speech_engine.runAndWait()	
class Listening:
	def listening_function():
		r = sr.Recognizer()
		razgovor=""		
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			#await audio
		try:
			print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
			razgovor=r.recognize_google(audio).lower()
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service;{0}".format(e))
		return razgovor	