import face_recognize
import threading
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

class Calibrate():
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background='Black')
		self.Frame.pack(fill=BOTH, expand= TRUE)
		self.auth_label=Label(self.Frame, font=('Helvetica', 30), fg='white', bg='black', text="User calibration")
		self.auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
		my_thread=threading.Thread(target=self.start_user_calib())
		my_thread.start()
		self.tk.mainloop()
	def start_user_calib(self):
		face_recognize.User_auth_GUI(self.Frame).pack()

Calibrate()
