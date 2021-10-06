import speech_recognition as sr
import subprocess
import os
import numpy as np
import cv2
import face_recognize
from speech_listen import Listening
import threading
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *



listen=0
r = sr.Recognizer()
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Users')

class new_user_GUI():
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.geometry("1920x1080")
		self.Frame=Frame(self.tk, background='Black')
		self.Frame.pack(fill=BOTH, expand= TRUE)
		self.auth_label=Label(self.Frame, font=('Helvetica', 30), fg='white', bg='black', text="User authontication")
		self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
		self.say_new_user_name=Label(self.Frame, font=('Helvetica', 30), fg='white', bg='black', text="")
		self.say_new_user_name.pack(fill=BOTH, expand= TRUE)
		self.get_new_user_name=Label(self.Frame, font=('Helvetica', 30), fg='white', bg='black', text="")
		self.get_new_user_name.pack(fill=BOTH, expand= TRUE)
		my_thread=threading.Thread(target=self.check_for_user)
		my_thread.start()
		self.tk.mainloop()
	def check_for_user(self):
		user_check=''
		#while(True):
			#user_check=face_recognize.User_auth_GUI()
		face_recognize.User_auth_GUI(self.Frame).pack()
		#self.user_auth.pack()
		#user_check='nejc'
		#print(self.user_auth.winfo_exists)
		#print(self.user_name)
		'''if(user_check is not None):
			#self.auth_label.config(text="Hello " + user_check)'''
		#self.new_user_name(user_check)
			#break'''

	def new_user_name(self,user):
		self.calibrate_user=face_recognize.User_calibration(self.Frame, user)
		self.calibrate_user.pack()


#new_user_name()
new_user_GUI()
