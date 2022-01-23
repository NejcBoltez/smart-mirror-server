import subprocess
import os
from speech_listen import Listening
import threading
from working_with_files import Work_with_files
import SmartMirror
from face_recognize import Get_face
from PIL import ImageTk
import PIL.Image
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *


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
		my_thread=threading.Thread(target=self.new_user_create())
		my_thread.start()
		self.tk.mainloop()
	def new_user_create(self):
		self.auth_label.config(text="Plase say your name without spaces")
		new_user=Listening.listening_function()
		if (new_user is not None or new_user != ""):
			while (True):
				self.say_new_user_name.config(text="Your new name would be '" + new_user + "'. IS THAT OK?")
				user_ok=Listening.listening_function()
				if ("yes" in user_ok.lower()):
					print("test")
					Work_with_files.create_dir_for_user(new_user)
					new_user_pic=subprocess.Popen(["python3","take_picture.py", new_user])
					self.tk.destroy()
					break
class Login(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, background='Black')
		self.auth_label=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="")
		self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
		start=threading.Thread(target=self.user_auth)
		start.start()
	def user_auth(self):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		print(path)
		print(dirs)
		print(files)
		count_users= len(dirs)
		
		try:
			if (count_users==2):
				new_user_GUI()
				path, dirs, files = next(os.walk(users_dir))
				print(path)
				print(dirs)
				print(files)
				count_users= len(dirs)

			if(count_users>2):
				while (True):
					test_user=Listening.listening_function()
					if (len(test_user)>0):
						self.auth_label.config(text="USER AUTHONTICATION")
						get_user=Get_face.User_auth()
						if (get_user is not None and len(get_user)>0):
							print(get_user)
							break
				#new_user_pic=subprocess.Popen(["python3","SmartMirror.py"])
				start_mirror=threading.Thread(target=SmartMirror.Window)
				start_mirror.start()
				self.tk.close()
		except Exception as e:
			print(e)
class Window_start:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		#self.tk.geometry("1920x1000")
		self.tk.attributes('-fullscreen', True)  
		self.fullScreenState = False
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.login=Login(self.Frame)
		self.login.pack()
		self.tk.mainloop()
		
win=Window_start()

