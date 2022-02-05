import multiprocessing
import subprocess
import os
from speech_listen import Listening
from speech_listen import Speaking
import threading
from working_with_files import Work_with_files
import SmartMirror
import calibrate
import create_new_user
from face_recognize import Get_face
from speech_listen import Listening
import asyncio
from multiprocessing import Value
from multiprocessing import cpu_count
from send_command import Do_for_command
import concurrent.futures 
from queue import Queue
import show_popup
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from tkinter import ttk



class Login(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.pack(fill=BOTH, expand=YES)
		main_q=Queue()
		self.tabControl = ttk.Notebook(self, height=100)
		self.tabControl.pack(expand = 1, fill ="both")
		
		self.update()
		start_l=threading.Thread(target=self.get_listen, args=(main_q,))#(name='Listen 1', target=Listening)
		#start_l.setDaemon(True)
		start_l.start()
		#x=Listening()
		self.user_auth(self.tabControl, main_q)
		#self.user_auth()
	
	def get_listen(self, threading_q):
		displayed=5
		l=""
		print("TEST")
		is_login=False
		start_to_listen=False
		not_recognize=0
		user=""
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		try:
			while(True):
				if(count_users>0):
					l= Listening.listening_function()
					if ("mirror" in l.lower()):
						if (is_login==False):
							is_login=True
							threading_q.put(True)
						elif (is_login==True):
							start_to_listen=True
							Speaking.to_say("OK. I AM LISTENING.")
							#start_popup=subprocess.Popen(["python3", "./show_popup.py"])
							show_popup.Popup_window()
					if (l.lower() != "" and l.lower() != "mirror" and start_to_listen==True):
						if("log out" in l.lower() or "log off" in l.lower() or "exit" in l.lower()):
							is_login=False

						else:
							if ("next" in l.lower()):
								displayed=displayed+5

							task1=asyncio.run(Do_for_command.main(self, l.lower(), user, str(displayed), self.tabControl))
						
						start_to_listen=False
						self.update()

					elif (l.lower == "" and start_to_listen==True):
						not_recognize=not_recognize + 1

					else:
						continue
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
			while(True):
				if (count_users==0):
					create_new_user.new_user_GUI.main(self, tabs)
				else:
					if (login_q.empty()):
						path, dirs, files = next(os.walk(users_dir))
						count_users= len(dirs)
						#create_new_user.new_user_GUI.main(self,tabs)
						continue
					else:
						print("IS_LOGIN: "+str(login_q.get()))
						if(count_users>0):						
							self.auth_label=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="TEST")
							self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
							self.update()
							get_user=Get_face.User_auth()
							self.auth_label.pack_forget()
							if (get_user is not None and len(get_user)>0):
								SmartMirror.Home_screen.get_home(self, get_user, tabs)
		except Exception as e:
			print(e)
class Window_start:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(bg='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, bg='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.login=Login(self.Frame)
		self.login.pack()
		self.tk.mainloop()
window=Window_start()


'''
tk=tk.Tk()
tk.configure(background='black')
tk.title("Pozdravljeni")
tk.geometry("1920x1000")
#self.tk.attributes('-fullscreen', True)  
#self.fullScreenState = False
Frame=Frame(tk, background='black')
Frame.pack(fill=BOTH, expand=YES)
tabControl = ttk.Notebook(Frame)
tabControl.pack(expand = 1, fill ="both")
auth_label=Label(Frame, font=('Helvetica', 30), fg='white', bg='black', text="TEST")
auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
tk.update()
start_l=threading.Thread(target=get_listen())#(name='Listen 1', target=Listening)
#start_l.setDaemon(True)
start_l.start()
#x=Listening()
user_auth(tk, tabControl)
#start_login=threading.Thread(target=user_auth(tk, tabControl, test_q))
#start_login.start()
tk.mainloop()'''
