import subprocess
import os
from speech_listen import Listening
import threading
from working_with_files import Work_with_files
import SmartMirror
from face_recognize import Get_face
import time
'''from PIL import ImageTk
import PIL.Image'''
import asyncio
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
		Frame.__init__(self, parent, background='red')
		self.pack(fill=BOTH, expand=YES)
		self.auth_label=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="TEST")
		self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
		#start=threading.Thread(target=self.user_auth)
		#start.start()
		loop = asyncio.get_event_loop()
		loop.run_until_complete(self.user_auth())
	async def user_auth(self):
		asyncio.sleep(1)
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		users_dir=os.path.join(BASE_DIR, '../Users')
		path, dirs, files = next(os.walk(users_dir))
		print(path)
		print(dirs)
		print(files)
		count_users= len(dirs)
		try:
			if (count_users==0):
				new_user_GUI()
				path, dirs, files = next(os.walk(users_dir))
				print(path)
				print(dirs)
				print(files)
				count_users= len(dirs)

			if(count_users>0):
				'''while (True):
					test_user=Listening.listening_function()
					if (len(test_user)>0):
						self.auth_label.config(text="USER AUTHONTICATION")'''
				get_user=Get_face.User_auth()
				'''		if (get_user is not None and len(get_user)>0):
							print(get_user)
							break'''
				#new_user_pic=subprocess.Popen(["python3","SmartMirror.py"])
				#start_mirror=subprocess.Popen(["python3","SmartMirror.py"])
				#label.pack_forget()
				
				login_home=asyncio.create_task(SmartMirror.Camera.get_home(self, get_user))
				await login_home
				#start_mirror=threading.Thread(target=SmartMirror.Camera(self, get_user))
				#start_mirror.start()
				#start_mirror.join()
				print("TEST")
				#while (True):
				#	print("TEST")
			#		time.sleep(1)
				#self.tk.close()
		except Exception as e:
			print(e)

class Window_start:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background='purple')
		self.Frame.pack(fill=BOTH, expand=YES)
		#self.auth_label=Label(self.Frame, font=('Helvetica', 30), fg='white', bg='black', text="TEST")
		#self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
		self.login=Login(self.Frame)
		#await user_auth(self.auth_label)
		#task1 = asyncio.create_task(user_auth(self.auth_label))
		self.login.pack()
		self.tk.mainloop()


#Open_forecast=subprocess.Popen(["python3","get_json_data.py"])
win=Window_start()
async def main():
	tk=tk.Tk()
	tk.configure(background='black')
	tk.title("Pozdravljeni")
	tk.geometry("1920x1000")
	#self.tk.attributes('-fullscreen', True)  
	#self.fullScreenState = False
	Frame=Frame(tk, background='purple')
	Frame.pack(fill=BOTH, expand=YES)
	auth_label=Label(Frame, font=('Helvetica', 30), fg='white', bg='black', text="TEST")
	auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
	#self.login=Login(self.Frame)
	#await user_auth(self.auth_label)
	task1 = asyncio.create_task(user_auth(auth_label))
	#asyncio.run(user_auth(auth_label))
	#await task1
	#self.login.pack()
	tk.mainloop()
#asyncio.run(main())

async def foo (text):
	print(text)
	await asyncio.sleep(1)

#asyncio.run(main())

