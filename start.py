import os
#from speech_listen import Listening
#from speech_listen import Speaking
import threading
from working_with_files import Work_with_files
import Home_screen_test as SmartMirror
import create_new_user
from face_recognize import User_auth_GUI
#from speech_listen import Listening
import asyncio
import requests
import subprocess
#from queue import Queue
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import json
import time
import os
import requests
from tkinter import ttk
from multiprocessing import Process, Queue
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import speech_recognition as sr



class Login(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.pack(fill=BOTH, expand=YES)
		main_q=Queue()
		noteStyle = ttk.Style()
		noteStyle.theme_use('default')
		noteStyle.configure("TNotebook", background="#000000", borderwidth=0)
		noteStyle.configure("TNotebook.Tab", background="#F9F3F2", borderwidth=0)
		noteStyle.map("TNotebook", background=[("selected", "#000000")])
		tabControl = ttk.Notebook(self, height=10)
		tabControl.pack(fill=BOTH, expand=YES)
		self.listening_word=""
		self.to_wait=0
		self.update()
		
		start_l=threading.Thread(target=self.get_listen, args=(main_q,))
		start_l.start()
		self.user_auth(tabControl, main_q)

	def get_listen(self, threading_q):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		try:
			while(True):
				if(count_users>0):
					time.sleep(self.to_wait)
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
						#speach=recognize_wit(r, audio, API_KEY).lower()
						url = "https://api.wit.ai/speech?v=20170307"
						request = Request(url, data=speach_audio, headers={"Authorization": "Bearer {}".format(API_KEY), "Content-Type": "audio/wav"})
						try:
							response = urlopen(request, timeout=10)
						except Exception as e:
							print(e)
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
					print(speach)
					threading_q.put(speach)
					self.listening_word=speach.replace('.','')
				else:
					continue
				
		except Exception as e:
			print(e)

	def user_auth(self, tabs, login_q):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		try:
			timeout=5
			url = "http://www.google.com"
			request = requests.get(url, timeout=timeout)
			print("Connected to the Internet")
			while(True):
				#print("TESTING WHILE LOOP")
				if (count_users==0):
					create_new_user.new_user_GUI.main(self, tabs)
				else:
					if (login_q.empty()):
						path, dirs, files = next(os.walk(users_dir))
						count_users= len(dirs)
						continue
					else:
						if(count_users>0 and len(tabs.tabs())==0 and "mirror" in login_q.get()):
							self.update()
							get_user=User_auth_GUI.main(self)
							if (get_user is not None and len(get_user)>0):
								SmartMirror.Home_screen.main(self, get_user,tabs, login_q)
		except (requests.ConnectionError, requests.Timeout) as exception:
			self.no_network_error=Label(self, font=("Helvetica", 40), fg="white", bg="black", text="PLEASE CONNECT TO NETWORK AND RESTART SMARTMIRROR")
			self.no_network_error.pack(side=TOP, fill=BOTH)
class Window_start():
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(bg='black')
		#self.tk.title("Pozdravljeni")
		#self.tk.geometry("1920x1000")
		self.tk.attributes('-fullscreen', True)  
		fullScreenState = False
		self.Frame=Frame(self.tk, bg='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.login=Login(self.Frame)
		self.login.pack()
		self.tk.mainloop()
start_popup=subprocess.Popen(["./do_not_go_to_sleep.sh"])
start_popup=subprocess.Popen(["python3", "get_json_data.py"])
window=Window_start()
