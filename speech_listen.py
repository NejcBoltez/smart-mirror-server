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
				print("Your name would be " + r.recognize_google(audio).replace(' ', '') + ".Is that OK?")
				user_test=r.recognize_google(audio).replace(' ', '')
				with sr.Microphone() as source:
					print("Plase say your name without spaces")
					#q=Queue()
					#print(q.get())
					print(Frame)
					r.adjust_for_ambient_noise(source)
					audio = r.listen(source)
					#audio = r.adjust_for_ambient_noise(source)
					print(audio)
				ok_name=r.recognize_google(audio).replace(' ', '')
				if('yes' in ok_name):
					print('Good name')
					user_name=user_test
					dir_path=str(image_dir)+'/'+str(user_name)
					os.mkdir(dir_path)
					os.chmod(dir_path, 0o777)
					#user_create=Get_face.User_creation(user_name)
					#create_new_user(user_name)
				else:
					continue
			except OSError as error:
				print('test')
				#print(str(sys.exc_info()[0]))
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