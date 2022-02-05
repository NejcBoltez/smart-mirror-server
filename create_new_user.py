import subprocess
import os
import face_recognize
from speech_listen import Listening
from working_with_files import Work_with_files
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
from tkinter import ttk

class new_user_GUI(Frame):
	def main(self, tabcontrol):
		#self.tk=tk.Tk()
		#self.tk.geometry("1920x1000")
		
		#self.tk.attributes("-fullscreen", True)  
		#self.fullScreenState = False
		print("NEW USER TESTING")
		self.Frame=Frame(self, background="Black")
		self.Frame.pack(fill=BOTH, expand= TRUE)
		users_c=check_for_users(self)
		
		create_new_user_tab = ttk.Frame(tabcontrol)
		tabcontrol.add(self.Frame, text ="CREATING NEW USER")
		tabcontrol.select(len(tabcontrol.tabs())-1)
		if (users_c < 6):
			self.auth_label=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
			self.say_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.say_new_user_name.pack(fill=BOTH, expand= TRUE)
			self.get_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.get_new_user_name.pack(fill=BOTH, expand= TRUE)
			#my_thread=threading.Thread(target=self.check_for_user)
			#my_thread.start()
			self.update()
			new_user_create(self)
			#self.tk.mainloop()
		else:
			self.auth_label=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="User authontication")
			self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
			self.say_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.say_new_user_name.pack(fill=BOTH, expand= TRUE)
			self.get_new_user_name=Label(self.Frame, font=("Helvetica", 30), fg="white", bg="black", text="")
			self.get_new_user_name.pack(fill=BOTH, expand= TRUE)
			#my_thread=threading.Thread(target=self.check_for_user)
			#my_thread.start()
			#self.check_for_user()
			self.update()
			#self.tk.mainloop()
def check_for_users(self):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	users_dir=os.path.join(BASE_DIR, '../Users')
	path, dirs, files = next(os.walk(users_dir))
	count_users= len(dirs)
	return count_users
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
				#self.tk.destroy()
				break
	#pic_thread.start()
def new_user_calib(self,user):
	self.calibrate_user=face_recognize.User_calibration(self.Frame, user)
	self.calibrate_user.pack()


#new_user_name()
#new_user_GUI()
