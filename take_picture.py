import numpy as np
import cv2
import sys
import time
from PIL import ImageTk
import PIL.Image
import multiprocessing
import threading
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *


from threading import Thread
seconds_left=11
class take_pic(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, background='Black')
		self.Frame=Frame(self, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.counts=Label(self.Frame, text="TEXT,", bg="white")
		self.counts.pack()
		#self.img = Label(self.Frame, width=700, height=700, bg="green")
		#self.img.pack(padx=20, pady=20)
		#self.cap = cv2.VideoCapture(0)
		#self.get_camera_stream()
		self.my_thread=threading.Thread(target=self.count_seconds(10))
		self.my_thread.start()
		#self.count_seconds(10)
		#self.count_seconds(10)
	def get_camera_stream(self):
		
		self.rec, self.frame_image = self.cap.read()
		self.cv2image = cv2.cvtColor(self.frame_image, cv2.COLOR_BGR2RGBA)
		self.image = PIL.Image.fromarray(self.cv2image)
		render = ImageTk.PhotoImage(image=self.image)

		self.img.imgtk = render
		self.img.configure(image=render)
		self.img.after(10, self.get_camera_stream)
		self.save_picture()
	def count_seconds(self, remaining):
		#self.counts.configure(text="%d" % remaining)
		'''if (remaining == 0):
			self.get_camera_stream()'''
		#else:
		#self.counts.after(1000, self.count_seconds(remaining - 1))
		while remaining:
			mins, secs = divmod(remaining, 60)
			timer = '{:02d}:{:02d}'.format(mins, secs)
			print(timer, end="\r")
			time.sleep(1)
			remaining -= 1
		#for i in range(10):
		#    self.counts.config(text=str(i))
		#    time.sleep(1)
	   # seconds_left=seconds_left-1
	   # if (seconds_left==0):
	   #     self.save_picture()
	   # return seconds_left
	def save_picture(self):
		save_as="../Users/nejc/nejc(1).jpg"
		cv2.imwrite(save_as, self.frame_image)
		#if()
		#time.sleep(15)
		#self.cap.release()
		#cv2.destroyAllWindows()
class Window:
	def __init__(self):
		seconds_left=11
		self.tk=tk.Tk()
		self.seconds_left=11
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1000x600")
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		#self.tk.mainloop()
		
		self.get_camera=take_pic(self.Frame)
		self.get_camera.pack()
		#self.counts.after(1000, self.count_seconds)
		#self.count_seconds(10)
		#self.img.after(1000, self.save_picture)

	
		#for
	
		

window=Window()
window.tk.mainloop()
