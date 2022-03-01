import os
#from speech_listen import Listening
#from speech_listen import Speaking
import threading
from working_with_files import Work_with_files
from SmartMirror import Home_screen
import create_new_user
from face_recognize import User_auth_GUI
from speech_listen import Listening
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
		noteStyle = ttk.Style()
		noteStyle.theme_use('default')
		noteStyle.configure("TNotebook", background="#000000", borderwidth=0)
		noteStyle.configure("TNotebook.Tab", background="#F9F3F2", borderwidth=0)
		noteStyle.map("TNotebook", background=[("selected", "#000000")])
		tabControl = ttk.Notebook(self, height=10)
		tabControl.pack(fill=BOTH, expand=YES)
		self.what_i_say=Label(self, font=("Helvetica", 40), fg="white", bg="black", text="TESTING")
		self.what_i_say.pack(side=TOP, fill=BOTH)
		self.listening_word=""
		self.to_wait=0
		self.update()
		
		start_l=threading.Thread(target=self.get_listen)
		start_l.start()
		self.user_auth(tabControl)

	def get_listen(self):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		try:
			while(True):
				if(count_users>0):
					time.sleep(self.to_wait)
					speach=Listening.listening_function()
					print(speach)
					self.listening_word=speach.replace('.','')
				else:
					continue
				
		except Exception as e:
			print(e)

	def user_auth(self, tabs):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		try:
			timeout=5
			url = "http://www.google.com"
			request = requests.get(url, timeout=timeout)
			print("Connected to the Internet")
			self.what_i_say.config(text=self.listening_word)
			while(True):
				if (count_users==0):
					create_new_user.new_user_GUI.main(self, tabs)
				else:
					if (len(self.listening_word)==0):
						path, dirs, files = next(os.walk(users_dir))
						count_users= len(dirs)
						continue
					else:
						if(count_users>0 and len(tabs.tabs())==0 and "hi mirror" in self.listening_word):
							self.update()
							get_user=User_auth_GUI.main(self)
							if (get_user is not None and len(get_user)>0):
								Home_screen.main(self, get_user,tabs)
		except (requests.ConnectionError, requests.Timeout) as exception:
			self.no_network_error=Label(self, font=("Helvetica", 40), fg="white", bg="black", text="PLEASE CONNECT TO NETWORK AND RESTART SMARTMIRROR")
			self.no_network_error.pack(side=TOP, fill=BOTH)
class Window_start():
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(bg='black')
		self.tk.attributes('-fullscreen', True)  
		fullScreenState = False
		self.Frame=Frame(self.tk, bg='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.login=Login(self.Frame)
		self.login.pack()
		self.tk.mainloop()
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)
start_popup=subprocess.Popen(["./do_not_go_to_sleep.sh"])
get_json_data=subprocess.Popen(["python3", BASE_DIR+os.path.sep+"get_json_data.py"])
window=Window_start()
