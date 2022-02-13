import os
from speech_listen import Listening
from speech_listen import Speaking
import threading
from working_with_files import Work_with_files
import Home_screen_test as SmartMirror
import create_new_user
from face_recognize import User_auth_GUI
from speech_listen import Listening
import asyncio
import requests
#from queue import Queue
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from tkinter import ttk
from multiprocessing import Process, Queue



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
		self.update()
		
		start_l=Process(target=self.get_listen, args=(main_q,))
		start_l.start()
		self.user_auth(tabControl, main_q)
	
	def get_listen(self, threading_q):
		l=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		try:
			while(True):
				if(count_users>0):
					l= Listening.listening_function()
					print(l)
					threading_q.put(l)
				else:
					continue
				
		except Exception as e:
			print(e)
	def user_auth(self, tabs, login_q):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		is_login=False
		try:
			timeout=5
			url = "http://www.google.com"
			request = requests.get(url, timeout=timeout)
			print("Connected to the Internet")
			while(True):
				#print("TESTING WHILE LOOP")
				if (count_users==2):
					create_new_user.new_user_GUI.main(self, tabs)
				else:
					if (login_q.empty()):
						path, dirs, files = next(os.walk(users_dir))
						count_users= len(dirs)
						#create_new_user.new_user_GUI.main(self,tabs)
						continue
					else:
						if(count_users>0 and len(tabs.tabs())==0 and "mirror" in login_q.get()):
							self.update()
							get_user=User_auth_GUI.main(self)
							if (get_user is not None and len(get_user)>0):
								SmartMirror.Home_screen.main(self, get_user,tabs, login_q)
		except (requests.ConnectionError, requests.Timeout) as exception:
			self.no_network_error=Label(self, font=("Helvetica", 40), fg="white", bg="black", text="PLEASE CONNECT TO NETWORK AND RESTART SMARTMIRROR")
			self.no_network_error.pack()
class Window_start():
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(bg='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#tk.attributes('-fullscreen', True)  
		#fullScreenState = False
		self.Frame=Frame(self.tk, bg='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.login=Login(self.Frame)
		self.login.pack()
		self.tk.mainloop()
window=Window_start()