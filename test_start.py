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
		listening_bool : str
		Frame.__init__(self, parent, bg='black')
		parent=parent
		tabcontrol=tabcontrol
		'''CommandHelpHeader=Label(self,font=('Helvetica', 40), fg="white", bg="black", text="HELLO "+user.upper())
		CommandHelpHeader.pack()
		CommandHelp=Label(self,font=('Helvetica', 12), fg="white", bg="black",text='First say "Hey Mirror" then you can try to say:')#Search youtube for\nShow me the forecast\nSearch wikipedia for\nStart the calibration')
		CommandHelp.pack()'''
		getPosluh(main_q)
	def getPosluh(self, q):
		my_thread=threading.Thread(target=Listening_test, args=(q,))
		my_thread.start()
			
	def Listening_test(self, thread_q):
		start_to_listen=True
		popup_id=''
		displayed=5
		previous_search=''
		l=''
		save_p_search=["next","back","previous","1","2","3","4","5","6","7","8","9","10","one","two","three","four","five","six","seven","eight","nine","ten","first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		try:
			while(True):
				#print('START LISTENING WHILE LOOP')
				l=Listening.listening_function()
				if ("mirror" in l.lower()):
					start_to_listen=True
					thread_q.put(True)
					Speaking.to_say('OK. I AM LISTENING.')
					start_popup=subprocess.Popen(["python3", "./show_popup.py"])
					popup_id=str(start_popup.pid)
					
				if (l.lower() != "" and l.lower() != "mirror" and start_to_listen==True):
					if('log out' in l.lower() or 'log off' in l.lower() or 'exit' in l.lower()):
						'''if (len(popup_id)>0):
							os.kill(int(popup_id), signal.SIGKILL)
						master.master.destroy()'''
						#sys.exit()
						parent.pack_forget()
						'''for t in threading.enumerate():
							if ("main" not in t.getName().lower()):
								print(t)
								t.
								#t.setDaemon = True
								t.cancel()'''
								#print(t.getName() + " : " + t.get_native_id())
					else:
						if ("next" in l.lower()):
							displayed=displayed+5
						asyncio.run(Do_for_command.main(self, l.lower(), user, str(displayed), tabcontrol))
						#send_command_thread=threading.Thread(target=Do_for_command.main(self, l.lower(), user, str(displayed), tabcontrol))
						#send_command_thread.start()
					start_to_listen=False
					if (len(popup_id)>0):
						os.kill(int(popup_id), signal.SIGKILL)
					if(l not in save_p_search):
						previous_search=l
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
		pack(fill=BOTH, expand=YES)
		tabControl = ttk.Notebook(self)
		tabControl.pack(expand = 1, fill ="both")
		user=user
		main_q=Queue()
		CamFrame=Frame(self, background='Black')
		CamFrame.pack(fill=BOTH, expand=YES)
		update()
		asistant=Asistant(CamFrame, user, tabControl, main_q)
		asistant.pack(side=TOP)
		#user_auth(tabControl, main_q)
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
						auth_label=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="TEST")
						auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
						update()
						get_user=Get_face.User_auth()
						time.sleep(10)
						auth_label.pack_forget()
						if (get_user is not None and len(get_user)>0):
							SmartMirror.Home_screen.get_home(self, get_user, tabs)
		except Exception as e:
			print(e)	
class Window:
	def __init__(self, user):
		#print("USER: "+ user)
		user=user
		tk=tk.Tk()
		tk.configure(background='black')
		tk.title("Pozdravljeni")
		tk.geometry("1920x1000")
		#tk.attributes('-fullscreen', True)  
		#fullScreenState = False
		Frame=Frame(tk, background='black')
		Frame.pack(fill=BOTH, expand=YES)
		recognize()
		tk.mainloop()
	def recognize(self):
		cam=Camera(Frame, user)
		cam.pack()
		#print("TEST")
		#news=News(Frame)
		#news.pack(side=BOTTOM)
		#asistant=Asistant(Frame, user)
		#asistant.pack(side=TOP)
	
win=Window("nejc")
win.tk.mainloop()