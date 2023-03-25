import sys
sys.path.append('../controller')
sys.path.append('../repository')
import cv2
import sys
import time
from PIL import ImageTk
import PIL.Image
import threading
try:
	import tkinter as tk
	from tkinter import *
	from tkinter import ttk
except:
	import tk
	from tk import *
	from tk import ttk


from threading import Thread
seconds_left=11
arguments = list(sys.argv)
class take_pic:
	def __call__(args):
		try: 
			print("dummy call")
		except:
			print("")
	
	def __init__(self,user):
		self.user=user
		self.tk=tk.Tk()
		self.seconds_left=11
		self.tk.configure(background="white")
		#self.tk.title("Pozdravljeni")
		#self.tk.geometry("1920x1080")
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.counts=Label(self.Frame,font=("Helvetica", 40), text="", bg="black", fg="white")
		self.counts.pack()
		self.img = Label(self.Frame, width=700, height=700, bg="black")
		self.img.pack(padx=20, pady=20)
		self.cap = cv2.VideoCapture(-1)
		self.count_number=10
		self.count=-10
		self.camera_stream=threading.Thread(target=self.get_camera_stream)
		self.camera_stream.start()
		self.tk.mainloop()
	
	def get_camera_stream(self):
		self.rec, self.frame_image = self.cap.read()
		self.cv2image = cv2.cvtColor(self.frame_image, cv2.COLOR_BGR2RGBA)
		self.image = PIL.Image.fromarray(self.cv2image)
		render = ImageTk.PhotoImage(image=self.image)
		self.img.imgtk = render
		self.img.configure(image=render)
		self.count=self.count+10
		#print(self.count_number)
		if (self.count==100 and self.count_number>=0):
			self.counts.configure(text=self.count_number)
			self.count_number=self.count_number-1
			self.count=0
		if (str(self.count_number)=="-1"):
			self.counts.configure(text="0")
			self.save_picture()
		if(self.count_number>=0):
			self.img.after(6, self.get_camera_stream)
	
	def save_picture(self):
		try:
			self.rec, self.frame_image = self.cap.read()
			self.cv2image = cv2.cvtColor(self.frame_image, cv2.COLOR_BGR2RGBA)
			self.image = PIL.Image.fromarray(self.cv2image)
			render = ImageTk.PhotoImage(image=self.image)
			self.img.imgtk = render
			self.img.configure(image=render)
			self.tk.update()
			save_as="../Users/"+str(self.user)+"/"+self.user+".png"
			face_image=None
			haar_file = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
			face_front = cv2.CascadeClassifier(haar_file)
			record_cam = self.cap#cv2.VideoCapture(-1)
			image_gray=cv2.cvtColor(self.frame_image, cv2.COLOR_BGR2GRAY)
			faces = face_front.detectMultiScale(image_gray, 1.89, 5)
			for (x, y, w, h) in faces:
				face_image = image_gray[y:y + h, x:x + w]
				#print(face_image)
			if (face_image is not None):
				cv2.imwrite(save_as, face_image)
				time.sleep(2)
				self.cap.release()
				cv2.destroyAllWindows()
				self.tk.destroy()
			else:
				self.counts.configure(text="NO FACE DETECTED")
				self.save_picture()

		except Exception as e:
			print(e)
			self.counts.configure(text="NO FACE DETECTED")
			self.tk.update()
			self.save_picture()
try:
	take_pic(arguments[1])
except Exception as e:
	print(e)
