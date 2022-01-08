import speech_recognition as sr
import os
import pyttsx3 as pyttsx
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
r = sr.Recognizer()

class Speaking:
	def to_say(speaking_word):
		speech_engine = pyttsx.init()
		speech_engine.say(speaking_word)
		speech_engine.runAndWait()	
class Listening:
	def new_user_name():
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, '../Users')
		user_name=''
		while user_name=='':
			with sr.Microphone() as source:
				print("Plase say your name without spaces")
				print(Frame)
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				print(audio)

			try:
				print("Your name would be " + r.recognize_google(audio).replace(' ', '') + ".Is that OK?")
				user_test=r.recognize_google(audio).replace(' ', '')
				with sr.Microphone() as source:
					print("Plase say your name without spaces")
					r.adjust_for_ambient_noise(source)
					audio = r.listen(source)
					print(audio)
				user_name=r.recognize_google(audio).replace(' ', '')
				print("USER_NAME: "+user_name)
			except OSError as error:
				print(error)
				continue
		return user_name
		
	def listening_function():
		r = sr.Recognizer()
		razgovor=''		
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		try:
			print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
			razgovor=r.recognize_google(audio).lower()
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service;{0}".format(e))
		return razgovor