import speech_recognition as sr
import subprocess
import os
import signal
import Virtual_asistent as asistant
import time
import multiprocessing
from multiprocessing import Queue
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

class Listen(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent)
		self.Frame=(self)
		self.Frame.pack()
		time.sleep(5)
		r = sr.Recognizer()
		poslusa=0
		open_processes=[]
		show_news=5


		#class Start_Listening:
		#while (True):
		#def __init__(self):
		listen=0
		yt_search_query=""
		numbers_int=["1","2","3","4","5","6","7","8","9","10"]
		numbers_string=["one","two","three","four","five","six","seven","eight","nine","ten"]
		position=["first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		show_news=5
		while(True):
			razgovor=''
		#print('OK')
			
		#while listened<5:

			while razgovor=='':
				with sr.Microphone() as source:
					print("Say something12345678!")
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
					
					if ("mirror" in razgovor):
						print('LETS GO')
						listen=1
					elif (listen==1):
						print('WE HAVE IT')
						if (" for " in razgovor):
							razgovor_search=razgovor.split(" for ")[1]
						if (razgovor!="" and listen==1):
							if ("who" in razgovor or "was" in razgovor or "what" in razgovor):
								subprocess.Popen(["python3","wikipedia_window.py", razgovor])
							elif("forecast" in razgovor or "weather" in razgovor):
								if (razgovor_search==""):
									for p in open_processes:
										if ("Open_forecast" in p):
											Open_forecast.terminate()
									Open_forecast=subprocess.Popen(["python3","weather.py"])
									open_processes.append("Open_forecast:"+str(Open_forecast.pid))
									print(Open_forecast.pid)
								else:
									for p in open_processes:
										if ("Open_forecast" in p):
											Open_forecast.terminate()
									#Open_forecast.terminate()
									print(razgovor_search)
									Open_forecast=subprocess.Popen(["python3","weather.py",razgovor_search])
									open_processes.append("Open_forecast:"+str(Open_forecast.pid))
									print(Open_forecast.pid)
									
							elif ("youtube" in razgovor):
								#if ("open" in razgovor):
								#Openyt=multiprocessing.Process(target=youtube.yt())
								#Openyt.start()
								if ("search" in razgovor):
									Open_yt_search=subprocess.Popen(["python3","youtube.py", razgovor_search])
									open_processes.append("Open_yt_search")
									yt_search_query=razgovor_search
									#self.Frame.delete('1.0', END)
									#AskMirror=multiprocessing.Process(target=yt_search(self.Frame))
									#AskMirror.start()
								elif ("play" in razgovor):
									Open_yt=subprocess.Popen(["python3","youtube_stream.py", razgovor])
									open_processes.append("Open_yt")

							elif ("calibration" in razgovor):
								Open_calibrate=subprocess.Popen(["python3", "calibrate.py", "test"], stdin=subprocess.PIPE)
								open_processes.append("Open_calibrate")
							elif ("news" in razgovor):
								Open_news=subprocess.Popen(["python3", "news.py", str(show_news)])
								open_processes.append('Open_news')
							elif("picture" in razgovor):
								if ("take" in razgovor):
										take_pic=subprocess.Popen(["python3","tale_picture.py"])
										open_processes.append("take_pic")
							elif ("home" in razgovor):
								for i in open_processes:
									if("Open_news" in i):
										Open_news.terminate()
										open_processes.remove(i)
									elif("Open_yt_search" in i):
										Open_yt_search.terminate()
										open_processes.remove(i)
									elif("Open_yt" in i):
										Open_yt.terminate()
										open_processes.remove(i)							
									elif("Open_calibrate" in i):
										Open_calibrate.terminate()
										open_processes.remove(i)
									else:
										continue
							elif(razgovor in numbers_int or razgovor in numbers_string or razgovor in position):
								if (razgovor in numbers_int):
									ni = numbers_int.index(razgovor)
									print(yt_search_query)
									print(str(show_news-(5-int(ni))))
									if("Open_news" in open_processes[len(open_processes)-1]):
										Open_news=subprocess.Popen(["python3", "show_news.py", str(show_news-(5-int(ni)))])
									elif("Open_yt" in open_processes[len(open_processes)-1]):
										Open_yt=subprocess.Popen(["python3","youtube_stream.py", yt_search_query, str(ni)])
										
								elif (razgovor in numbers_string):
									ns = numbers_string.index(razgovor)
									print(str(show_news-(5-int(ns))))
									print(yt_search_query)
									if("Open_news" in open_processes[len(open_processes)-1]):
										Open_news=subprocess.Popen(["python3", "show_news.py", str(show_news-(5-int(ns)))])
									elif("Open_yt" in open_processes[len(open_processes)-1]):
										Open_yt=subprocess.Popen(["python3","youtube_stream.py", yt_search_query, str(ns)])
									
								elif (razgovor in position):
									po = position.index(razgovor)  	
									print(yt_search_query)
									print(str(show_news-(5-int(po))))
									if("Open_news" in open_processes[len(open_processes)-1]):
										Open_news=subprocess.Popen(["python3", "show_news.py", str(show_news-(5-int(po)))])
									elif("Open_yt" in open_processes[len(open_processes)-1]):
										Open_yt=subprocess.Popen(["python3","youtube_stream.py", yt_search_query, str(po)])
									
							elif ("close" in razgovor):
								if("Open_news" in open_processes[len(open_processes)-1]):
									Open_news.terminate()
									open_processes.remove([len(open_processes)-1])
								elif("Open_yt_search" in open_processes[len(open_processes)-1]):
									Open_yt_search.terminate()
									#open_processes.remove([len(open_processes)-1])
									open_processes.remove("Open_yt_search")
								elif("Open_yt" in open_processes[len(open_processes)-1]):
									Open_yt.terminate()
									open_processes.remove("Open_yt")    								
								elif("Open_calibrate" in open_processes[len(open_processes)-1]):
									Open_calibrate.terminate()
									open_processes.remove([len(open_processes)-1])
								elif("take_pic" in open_processes[len(open_processes)-1]):
										take_pic.terminate()
										open_processes.remove([len(open_processes)-1])
										
								else:
									continue
							elif ("next" in razgovor):
								if("Open_news" in open_processes[len(open_processes)-1]):
									Open_news.terminate()
									Open_news=subprocess.Popen(["python3", "news.py", show_news+5])
									show_news=show_news+5			
							else:
								AskMirror=multiprocessing.Process(target=asistant.jarvis(razgovor))
								AskMirror.start()
								#AskMirror.join()
								#subprocess.Popen(["python3","Virtual_asistent.py", razgovor])
							listen=0
				except sr.UnknownValueError:
					print("Google Speech Recognition could not understand audio")
					#listened+=1
				except sr.RequestError as e:
					print("Could not request results from Google Speech Recognition service;{0}".format(e))
					#listened+=1
				#print(razgovor)