import face_recognize
import threading
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from tkinter import ttk

class Calibrate():
	def main (self, tabControl):
		#tk=tk.Tk()
		#tk.geometry("1920x1000")
		#tk.attributes("-fullscreen", True)  
		#fullScreenState = False
		Frame=Frame(self, background="Black")
		Frame.pack(fill=BOTH, expand= TRUE)
		
		calibrate_tab = ttk.Frame(tabControl)
		tabControl.add(Frame, text ="CALIBRATE")
		tabControl.select(len(tabControl.tabs())-1)
		auth_label=Label(Frame, font=("Helvetica", 30), fg="white", bg="black", text="User calibration")
		auth_label.pack(side=TOP,fill=BOTH, expand= TRUE)
		#my_thread=threading.Thread(target=start_user_calib())
		#my_thread.start()
		update()
		face_recognize.User_auth_GUI(Frame).pack()
		#tk.mainloop()
	def start_user_calib(self):
		face_recognize.User_auth_GUI(Frame).pack()

#Calibrate()
