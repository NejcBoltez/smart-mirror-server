import numpy as np
import cv2
import sys
import time
from PIL import ImageTk
import PIL.Image
#import multiprocessing
import threading
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *


from threading import Thread
seconds_left=11
arguments = list(sys.argv)
class take_pic:
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self,user):
		#seconds_left=11
		self.user=user
		self.tk=tk.Tk()
		self.seconds_left=11
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1080")
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		
		#self.Frame=Frame(self, background='black')
		#self.Frame.pack(fill=BOTH, expand=YES)
		self.counts=Label(self.Frame,font=('Helvetica', 40), text="", bg="black", fg="white")
		self.counts.pack()
		self.img = Label(self.Frame, width=700, height=700, bg="black")
		self.img.pack(padx=20, pady=20)
		self.cap = cv2.VideoCapture(0)
		self.count_number=10
		self.count=-10
		self.camera_stream=threading.Thread(target=self.get_camera_stream)
		self.camera_stream.start()
		self.tk.mainloop()
		
		#time.sleep(10)
		#self.my_thread=threading.Thread(target=self.count_seconds(10))
		#self.my_thread.start()
		#self.count_seconds(10)
		#self.count_seconds(10)
	def get_camera_stream(self):
		print("test123")
		self.rec, self.frame_image = self.cap.read()
		self.cv2image = cv2.cvtColor(self.frame_image, cv2.COLOR_BGR2RGBA)
		self.image = PIL.Image.fromarray(self.cv2image)
		render = ImageTk.PhotoImage(image=self.image)

		self.img.imgtk = render
		self.img.configure(image=render)
		self.count=self.count+10
		print(self.count_number)
		
		#self.my_thread=threading.Thread(target=self.count_seconds(10))
		#self.my_thread.start()

		if (self.count==100 and self.count_number>=0):
			self.counts.configure(text=self.count_number)
			self.count_number=self.count_number-1
			#if (self.count_number>0):
			self.count=0
			print (self.count_number)
		if (str(self.count_number)=='-1'):
			self.counts.configure(text='0')
			self.save_picture()
				#print("SAVING_PICTURES")
				#save_as="../taken_pictures/"+str(self.user)+"/"+self.user+".jpg"
				#cv2.imwrite(save_as, self.frame_image)
				#if()
				#time.sleep(5)
				#print("PIC SAVED")
					#
				#self.tk.destroy()
					#self.camera_stream.join()
		if(self.count_number>=0):
			print("test")
			self.img.after(10, self.get_camera_stream)
		#self.save_picture()
	def count_seconds(self, remaining):
		#self.counts.configure(text="%d" % remaining)
		'''if (remaining == 0):
			self.get_camera_stream()'''
		#else:
		#self.counts.after(1000, self.count_seconds(remaining - 1))
		while remaining:
			print('TEST')
			mins, secs = divmod(remaining, 60)
			timer = '{:02d}:{:02d}'.format(mins, secs)
			#print(timer, end="\r")
			self.counts.configure(text=timer)
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
		try:
			print("SAVING_PICTURES")
			save_as="../taken_pictures/"+str(self.user)+"/"+self.user+".jpg"
			cv2.imwrite(save_as, self.frame_image)
			#if()
			time.sleep(2)
			print("PIC SAVED")
			self.cap.release()
			cv2.destroyAllWindows()
			self.tk.destroy()
		except Exception as e:
			print(e)
try:
	take_pic(arguments[1])
except Exception as e:
	print(e)
