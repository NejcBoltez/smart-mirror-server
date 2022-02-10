import os
from speech_listen import Listening
import threading
import Home_screen_test as SmartMirror
import create_new_user
from face_recognize import Get_face
from speech_listen import Listening
from queue import Queue
#import show_popup
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
		pack(fill=BOTH, expand=YES)
		main_q=Queue()
		noteStyle = ttk.Style()
		noteStyle.theme_use('default')
		noteStyle.configure("TNotebook", background="#000000", borderwidth=0)
		noteStyle.configure("TNotebook.Tab", background="#F9F3F2", borderwidth=0)
		noteStyle.map("TNotebook", background=[("selected", "#000000")])
		tabControl = ttk.Notebook(self, height=10)
		tabControl.pack(fill=BOTH, expand=YES)
		update()
		start_l=threading.Thread(target=get_listen, args=(main_q,))
		start_l.start()
		user_auth(tabControl, main_q)
	
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
			while(True):
				#print("TESTING WHILE LOOP")
				if (count_users==0):
					create_new_user.new_user_GUI.main(self, tabs)
				else:
					if (login_q.empty()):
						path, dirs, files = next(os.walk(users_dir))
						count_users= len(dirs)
						#create_new_user.new_user_GUI.main(self,tabs)
						continue
					else:
						if(count_users>0 and len(tabs.tabs())==0 and "mirror" in login_q.get()):						
							auth_label=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="TEST")
							auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
							update()
							get_user=Get_face.User_auth()
							auth_label.pack_forget()
							if (get_user is not None and len(get_user)>0):
								#threading.Thread(target=
								
								#Home=
								SmartMirror.Home_screen.main(self, get_user,tabs, login_q)
								#Home.pack(fill=BOTH, expand=YES)
							#HOME.pack()
		except Exception as e:
			print(e)
class Window_start:
	def __init__(self):
		tk=tk.Tk()
		tk.configure(bg='black')
		tk.title("Pozdravljeni")
		tk.geometry("1920x1000")
		#tk.attributes('-fullscreen', True)  
		#fullScreenState = False
		Frame=Frame(tk, bg='black')
		Frame.pack(fill=BOTH, expand=YES)
		login=Login(Frame)
		login.pack()
		tk.mainloop()
window=Window_start()