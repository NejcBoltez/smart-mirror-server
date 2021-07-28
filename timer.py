import time
import os
import threading
import sys
import pyttsx3 as pyttsx
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

speech_engine = pyttsx.init()

def govor(besedilo):
    print(besedilo)
    speech_engine.say(besedilo)
    speech_engine.runAndWait()

class Timer():
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self, remaining):
		self.tk=tk.Tk()
		self.tk.title("Timer")
		self.tk.geometry("1920x1080")
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.remaining=remaining*60
		
		#self.Frame=Frame(self, background='black')
		#self.Frame.pack(fill=BOTH, expand=YES)
		self.counts=Label(self.Frame,font=('Helvetica', 150), text="", bg="black", fg="white")
		self.counts.pack(pady=300)
		self.camera_stream=threading.Thread(target=self.start_timer)
		self.camera_stream.start()
		self.tk.mainloop()
	def start_timer(self):
		#while remaining:
		self.mins, self.secs = divmod(self.remaining, 60)
		self.timer = '{:02d}:{:02d}'.format(self.mins, self.secs)
		#print(timer, end="\r")
		print(self.timer)
		if (self.mins>0 or self.secs>0):
			self.counts.configure(text=self.timer)
			time.sleep(0.25)
			self.remaining=self.remaining-1
			self.counts.after(1000, self.start_timer())
		elif(self.mins==0 and self.secs==0):
			self.counts.configure(text=self.timer)
			govor('finished')
			time.sleep(2)
			self.tk.destroy()

arguments = list(sys.argv)
try:
	if(arguments[1].isnumeric()):
		Timer(int(arguments[1]))
	else:
		print("Provide numeric argument")
except Exception as e:
	print(e)
#t.tk.mainloop()
