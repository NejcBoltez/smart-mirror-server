try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import time
import requests
from urllib3 import *
import os
import pyttsx3 as pyttsx
import speech_recognition as sr
import threading
#import send_command
from send_command import Do_for_command
from face_recognize import Get_face
import signal
import subprocess
from speech_listen import Speaking
from working_with_files import Work_with_files
from PIL import ImageTk
import PIL.Image
from speech_listen import Listening
import sys
from queue import Queue
from tkinter import ttk
import SmartMirror
import asyncio



BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Users')
user = ''
speech_engine = pyttsx.init()

class Asistant(Frame):
	def __init__(self, parent, user, tabcontrol, main_q):
		self.listening_bool : str
		Frame.__init__(self, parent, bg='black')
		self.parent=parent
		self.tabcontrol=tabcontrol
		'''self.CommandHelpHeader=Label(self,font=('Helvetica', 40), fg="white", bg="black", text="HELLO "+user.upper())
		self.CommandHelpHeader.pack()
		self.CommandHelp=Label(self,font=('Helvetica', 12), fg="white", bg="black",text='First say "Hey Mirror" then you can try to say:')#Search youtube for\nShow me the forecast\nSearch wikipedia for\nStart the calibration')
		self.CommandHelp.pack()'''
		self.getPosluh(main_q)
	def getPosluh(self, q):
		my_thread=threading.Thread(target=self.Listening_test, args=(q,))
		my_thread.start()
			
	def Listening_test(self, thread_q):
		self.start_to_listen=True
		self.popup_id=''
		self.displayed=5
		self.previous_search=''
		self.l=''
		self.save_p_search=["next","back","previous","1","2","3","4","5","6","7","8","9","10","one","two","three","four","five","six","seven","eight","nine","ten","first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		try:
			while(True):
				#print('START LISTENING WHILE LOOP')
				self.l=Listening.listening_function()
				if ("mirror" in self.l.lower()):
					self.start_to_listen=True
					thread_q.put(True)
					Speaking.to_say('OK. I AM LISTENING.')
					start_popup=subprocess.Popen(["python3", "./show_popup.py"])
					self.popup_id=str(start_popup.pid)
					
				if (self.l.lower() != "" and self.l.lower() != "mirror" and self.start_to_listen==True):
					if('log out' in self.l.lower() or 'log off' in self.l.lower() or 'exit' in self.l.lower()):
						'''if (len(self.popup_id)>0):
							os.kill(int(self.popup_id), signal.SIGKILL)
						self.master.master.destroy()'''
						#sys.exit()
						self.parent.pack_forget()
						'''for t in threading.enumerate():
							if ("main" not in t.getName().lower()):
								print(t)
								t.
								#t.setDaemon = True
								t.cancel()'''
								#print(t.getName() + " : " + t.get_native_id())
					else:
						if ("next" in self.l.lower()):
							self.displayed=self.displayed+5
						asyncio.run(Do_for_command.main(self, self.l.lower(), user, str(self.displayed), self.tabcontrol))
						#self.send_command_thread=threading.Thread(target=Do_for_command.main(self, self.l.lower(), user, str(self.displayed), self.tabcontrol))
						#self.send_command_thread.start()
					self.start_to_listen=False
					if (len(self.popup_id)>0):
						os.kill(int(self.popup_id), signal.SIGKILL)
					if(self.l not in self.save_p_search):
						self.previous_search=self.l
					else:
						continue

		except Exception as e:
			print(e)
		
class Camera(Frame):
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self, parent, user):
		Frame.__init__(self, parent, background='Black')
		self.pack(fill=BOTH, expand=YES)
		self.tabControl = ttk.Notebook(self)
		self.tabControl.pack(expand = 1, fill ="both")
		self.user=user
		main_q=Queue()
		self.CamFrame=Frame(self, background='Black')
		self.CamFrame.pack(fill=BOTH, expand=YES)
		self.update()
		self.asistant=Asistant(self.CamFrame, self.user, self.tabControl, main_q)
		self.asistant.pack(side=TOP)
		#self.user_auth(self.tabControl, main_q)
	def user_auth(self, tabs, login_q):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		count_users= len(dirs)
		is_login=False
		try:
			while(True):
				#if (count_users==0):
				#	create_new_user.new_user_GUI.main(self, tabs)
				#else:
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
						time.sleep(10)
						self.auth_label.pack_forget()
						if (get_user is not None and len(get_user)>0):
							SmartMirror.Home_screen.get_home(self, get_user, tabs)
		except Exception as e:
			print(e)	
class Window:
	def __init__(self, user):
		#print("USER: "+ user)
		self.user=user
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.recognize()
		self.tk.mainloop()
	def recognize(self):
		self.cam=Camera(self.Frame, self.user)
		self.cam.pack()
		#print("TEST")
		#self.news=News(self.Frame)
		#self.news.pack(side=BOTTOM)
		#self.asistant=Asistant(self.Frame, self.user)
		#self.asistant.pack(side=TOP)
	
win=Window("nejc")
win.tk.mainloop()