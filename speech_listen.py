import speech_recognition as sr
import pyttsx3 as pyttsx
import time

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
			speach=r.recognize_google(audio).lower()
		#l= Listening.listening_function()
		except sr.UnknownValueError:
			print("WIT Speech Recognition could not understand audio")
		
		except sr.RequestError as e:
			print("Could not request results from WIT Speech Recognition service;{0}".format(e))
		
		except Exception as e:
			print(e)
		
		return speach
		#return razgovor
#Listening.listening_function()	
