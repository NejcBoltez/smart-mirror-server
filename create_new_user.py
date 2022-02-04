import speech_recognition as sr
import subprocess
import os
import numpy as np
import cv2
import face_recognize
from speech_listen import Listening
from working_with_files import Work_with_files
import threading
import take_picture
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *



listen=0
r = sr.Recognizer()
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, "../Users")

class new_user_GUI():
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.geometry("1920x1000")
		#self.tk.attributes("-fullscreen", True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background="Black")
		self.Frame.pack(fill=BOTH, expand= TRUE)
		self.auth_label=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="User authontication")
		self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
		self.say_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
		self.say_new_user_name.pack(fill=BOTH, expand= TRUE)
		self.get_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
		self.get_new_user_name.pack(fill=BOTH, expand= TRUE)
		my_thread=threading.Thread(target=self.check_for_user)
		my_thread.start()
		#self.check_for_user()
		self.tk.mainloop()
	def check_for_user(self):
		#user_check=""
		print("TEST")
		#while(True):
		user_check=face_recognize.Get_face.User_auth()
		print("USER: " + user_check)
			#break;
		self.new_user_create()
	def new_user_create(self):
		self.auth_label.config(text="Plase say your name without spaces")
		new_user=Listening.listening_function()
		if (new_user is not None or new_user != ""):
			while (True):
				self.say_new_user_name.config(text="Your new name would be "" + new_user + "". IS THAT OK?")
				user_ok=Listening.listening_function()
				if ("yes" in user_ok.lower()):
					print("test")
					Work_with_files.create_dir_for_user(new_user)
					new_user_pic=subprocess.Popen(["python3","take_picture.py", new_user])#self.take_pic=take_picture.take_pic("test")
					self.tk.destroy()
					break
		#pic_thread.start()
	def new_user_calib(self,user):
		self.calibrate_user=face_recognize.User_calibration(self.Frame, user)
		self.calibrate_user.pack()


#new_user_name()
new_user_GUI()
