try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import time
import json
import requests
import urllib
import cv2
import numpy as np
from urllib3 import *
from PIL import Image, ImageTk
import dlib
import os
import face_recognition
import pyttsx3 as pyttsx
import speech_recognition as sr
import subprocess #as call
import posluh1 as listening
from multiprocessing import Queue
import multiprocessing



BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, 'Uporabniki')
user = ''
speech_engine = pyttsx.init()
class Ura(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.label1=Label(self, font=('Helvetica', 100), fg="white", bg="black")
		self.label1.pack(side=TOP,anchor=E)
		self.dan=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.dan.pack()
		self.pozdrav=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.pozdrav.pack()
		self.klik()
	def klik(self):
		ti=time.strftime('%H:%M:%S')
		dan=time.strftime('%A')
		self.label1.config(text=ti)
		self.dan.config(text=dan)
		
		# calls itself every 1000 milliseconds to update the time display as needed could use >200 ms, but display gets jerky
		self.label1.after(1000, self.klik)
class Vreme(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.LabelMain=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="Vreme:")
		self.LabelMain.pack()
		self.label1=Label(self, font=('Helvetica', 25), fg="white", bg="black")
		self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getVreme()
		self.label1.after(10000, self.getVreme)
	def getVreme(self):
		City = "Novo mesto"
		Country = "SI"
		APIK = "10fe78b8435d01d64ad7203ac4b87fe8"
		URL = "https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK
		r = requests.get(URL)
		preberi = r.json()
		temp="Temp: " + str(preberi['main']['temp'])
		humidity="Humidity: " + str(preberi['main']['humidity'])
		temp_min="Temp_min: " + str(preberi['main']['temp_min'])
		temp_max="Temp_max: " + str(preberi['main']['temp_max'])
		weather=temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max
		self.label1.config(text=weather)
class Novice(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.NewsFrame=Frame(self, background='Black')
		self.NewsFrame.pack(side=RIGHT)
		self.labelMain=Label(self.NewsFrame, font=('Helvetica', 30), fg='white', bg='black', text="Novice:")
		self.labelMain.pack()
		self.label1=Label(self.NewsFrame, font=('Helvetica', 9), fg="white", bg="black")
		self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getNovice()
		self.label1.after(100000, self.getNovice)
	def getNovice(self):
		NewsList=[]
		Novice=""
		News=""
		IzborNovic=""
		API = "fe1f07fb06114c9a94c9c8ced3f83f8d"
		URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+API
		News=requests.get(URLnews)
		Novice=News.json()
		NewsList=Novice['articles']
		for i in NewsList:
			Nov = str(i['title']).split("- ")
			#print(Nov)
			#if (Nov[1]=='24ur.com' or Nov[1]=='RTV Slovenija' or Nov[1]=='Računalniške Novice' or Nov[1]=='Siol.net'):
				#self.label1.config(text="")
			IzborNovic+=str(i['title']) + '\n'
		   # else:
			#    continue
		self.label1.config(text=IzborNovic)
class Asistant(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.PosluhFrame=Label(self, font=('Helvetica', 30), fg="white", bg="black", text=user)
		self.PosluhFrame.pack(side=RIGHT)
		#self.getPosluh()
		self.callListen=0
		if (self.callListen==0):
			self.PosluhFrame.after(500, self.getPosluh)
			self.callListen=self.callListen+1
	def getPosluh(self):
		#AI()
		#Listen=subprocess.Popen(["python3", "posluh1.py", self.parent])
		#subprocess.Popen(["python3", "posluh1.py"])
		print('test123')
		#q=Queue()
		#q.put([self])

		self.start_listening=multiprocessing.Process(target=listening.Listen, args=(self.PosluhFrame,))
		self.start_listening.start()
		#self.start_listening=Listen(self)
		#self.start_listening.pack()
		#listen_value=Listen.communicate()[0]
		#print(listen_value)
		#with subprocess.Popen(["python3", "posluh1.py"]) as Listen:#, "test"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
			#if (Listen.communicate())
		#    listen_value=Listen.communicate()[0]
		#    print(listen_value)

		
class Camera(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, background='Black')
		self.pack(side=LEFT, fill=BOTH, expand=YES)
		self.CamFrame=Frame(self, background='Black')
		self.CamFrame.pack(side=TOP,anchor=E)
		self.labelMain=Label(self.CamFrame, font=('Helvetica', 60), fg='white', bg='black', text="Please LOGIN")
		self.labelMain.pack(anchor='w')
		self.label1=Label(self.CamFrame, font=('Helvetica', 9), fg="white", bg="black")
		self.label1.pack(anchor='w')
		#self.get_home()
		self.getCamera()
	def getCamera(self):
		# .local is inside home directory
		try:
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		except:
			face_front=cv2.CascadeClassifier('../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Capture frame-by-frame
		global user
		#global login
		cap = cv2.VideoCapture(0)
		ret, frame = cap.read()
		tekst=''
		#detect face
		faces = face_front.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
		for (x, y, w, h) in faces:
			#tekst=str(x)+', '+str(y)+', '+str(w)+', '+str(h)
			
			#print (x)
			roi_color=frame[y:y+h, x:x+w]
			
			#image = face_recognition.load_image_file('./Images/stevejobs.png')
			image_encoding = face_recognition.face_encodings(frame)[0]
			for root, dirs, files in os.walk(image_dir):
				for d in dirs:
					#print(d)
					#print(image_dir+'/'+d)
					for root, dirs, files in os.walk(image_dir+'/'+d):
						print(files)
						for file in files:
							#print('File: '+file)
							unknown_image = face_recognition.load_image_file(image_dir+'/'+d+'/'+file)
							#print(unknown_image)
							unknown_encoding=face_recognition.face_encodings(unknown_image)
							#print(len(unknown_encoding))
							if (len(unknown_encoding)>0):
								unknown_encoding1=face_recognition.face_encodings(unknown_image)[0]

								results=face_recognition.compare_faces([image_encoding], unknown_encoding1)

								if results[0]:
									#print(file)
									tekst=d
									#print('tekst: '+tekst)
									#save the image
									path, dirs, files = next(os.walk(image_dir+'/'+d))
									file_count = len(files)
									print(d)
									#print(image_dir+'/'+d)
									#print(file_count)
									img_item2='./Uporabniki/'+d+'/'+d+'_'+str(file_count+1)+'.png'
									cv2.imwrite(img_item2, roi_color)
									break
								else:
									continue
							
			#cv2.imwrite(img_item2, roi_color)
			teskst123='Pozdravljen ' + tekst
			self.labelMain.config(text=teskst123)
			self.label1.config(text=tekst)
			self.labelMain.pack()
			#this.user=tekst
			#self.home_window()
			user=tekst
			#self.labelMain.after(700, self.home_window)
			#home=Okno()
#             root.destroy()
			#home.tk.mainloop()
			self.get_home()
			#self.labelMain.after(100, self.get_home())
			#self.labelMain.after(1000, AI())
			
		if len(faces)==0:
			self.label1.config(text='Prazno')
			self.label1.after(600, self.getCamera)

	def get_home(self):
		time.sleep(10)
		self.labelMain.config(text='')
		self.TopFrame = Frame(self, background='red')
		self.BottomFrame = Frame(self, background='yellow')
		self.TopLeftFrame=Frame(self.TopFrame, background='red')
		self.BottomLeftFrame=Frame(self.BottomFrame, background='yellow')
		self.TopRightFrame=Frame(self.TopFrame, background='red')
		self.BottomRightFrame=Frame(self.BottomFrame, background='yellow')
		
		self.TopFrame.pack(side=TOP, fill=BOTH, expand=YES)
		self.BottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
		self.TopLeftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
		self.BottomLeftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
		self.TopRightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)
		self.BottomRightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)

		self.ura=Ura(self)
		self.ura.pack(side=BOTTOM)
		self.vreme=Vreme(self.TopRightFrame)
		self.vreme.pack(side=RIGHT)
		self.news=Novice(self.BottomRightFrame)
		self.news.pack(side=RIGHT, fill=BOTH, expand=YES)
		self.label1234=Label(self.BottomFrame, text="Hello2", fg="white", bg="black")
		self.label1234.pack()
		self.cam=Label(self.BottomFrame, text="Hello234", fg="white", bg="black")
		self.cam.pack()
		self.asistant=Asistant(self)
		self.asistant.pack()
		
class Okno:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background='Purple')
		self.Frame.pack(fill=BOTH, expand=YES)
		
		self.recognize()
	def recognize(self):
		self.cam=Camera(self.Frame)
		self.cam.pack()
	
okno=Okno()
okno.tk.mainloop()