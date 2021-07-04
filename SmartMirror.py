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
#import posluh1 as listening
from multiprocessing import Queue
import multiprocessing
import speech_recognition as sr
import threading
import send_command
from send_command import Do_for_command




BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Users')
user = ''
speech_engine = pyttsx.init()
#q=Queue()
#q.cancel_join_thread()
#global listening_bool
global Queue_listening
#listening_bool='False'
Queue_listening=Queue()
def get_api_keys():
	api_keys_dir=os.path.join(BASE_DIR, '../api_keys.json')
	with open(api_keys_dir, 'r') as f:
		d=json.load(f)
	#print(len(d))
	#print(d['weather_api'])
	return d
class Asistant(Frame):
	def __init__(self, parent, *args, **kwargs):
		self.listening_bool : str
		Frame.__init__(self, parent, bg='black')
		#self.PosluhFrame=Label(self, font=('Helvetica', 40), fg="white", bg="yellow", text=user)
		#self.PosluhFrame.pack(side=RIGHT)
		self.CommandHelpHeader=Label(self,font=('Helvetica', 40), fg="white", bg="black", text='\nYou can try to say:')
		self.CommandHelpHeader.pack()
		self.CommandHelp=Label(self,font=('Helvetica', 12), fg="white", bg="black",text='Search youtube for\nShow me the forecast\nSearch wikipedia for\nStart the calibration')
		self.CommandHelp.pack()
		self.getPosluh()
	def getPosluh(self):
		print('TEST123')
		my_thread=threading.Thread(target=self.Listening_test)
		my_thread.start()
	def listening_function(self):
		r = sr.Recognizer()
		razgovor=''
		
		with sr.Microphone() as source:
			print("Say something12345678!")
			print(Frame)
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			print(audio)

		try:
			print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
			razgovor=r.recognize_google(audio).lower()
			razgovor_search=""
			
			if ("mirror" in razgovor):
				print('LETS GO')
				Queue_listening.put("listening")
				print(Queue_listening.get(1))
			
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service;{0}".format(e))
		return razgovor
	def Listening_test(self):
		while(True):
			l=self.listening_function()
			#self.check_if_listening(l)
			self.PosluhFrame.config(text=str(l))
			if l != "":
				print(l)
				send_command_thread=threading.Thread(target=send_command.Do_for_command(l.lower()))
				send_command_thread.start()

class Time(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.label1=Label(self, font=('Helvetica', 100), fg="white", bg="black")
		self.label1.pack(side=TOP,anchor=E)
		self.day=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.day.pack()
		self.hello=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.hello.pack()
		self.update_time()
	def update_time(self):
		ti=time.strftime('%H:%M:%S')
		day=time.strftime('%A')
		self.update_clock(ti,day)
		#print('TEST: ' + ti)
		# calls itself every 1000 milliseconds to update the time display as needed could use >200 ms, but display gets jerky
		self.label1.after(1000, self.update_time)
	def update_clock(self,ti,d):
		self.label1.config(text=ti)
		self.day.config(text=d)

class Weather(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='green', padx=0, pady=0)
		self.LabelMain=Label(self, font=('Helvetica', 40), fg='white', bg='black', text="Weather:")
		self.LabelMain.pack()
		self.label1=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getWeather()
		self.label1.after(10000, self.getWeather)
	def getWeather(self):
		City = "Novo mesto"
		Country = "SI"
		get_api=get_api_keys()
		APIK=get_api['weather_api']
		URL = "https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK
		r = requests.get(URL)
		read_weather = r.json()
		temp="Temp: " + str(read_weather['main']['temp'])
		humidity="Humidity: " + str(read_weather['main']['humidity'])
		temp_min="Temp_min: " + str(read_weather['main']['temp_min'])
		temp_max="Temp_max: " + str(read_weather['main']['temp_max'])
		weather=temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max
		self.update_weather(weather)
	def update_weather(self,data):
		self.label1.config(text=data)

class News(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.NewsFrame=Frame(self, background='Black')
		self.NewsFrame.pack(side=RIGHT)
		self.labelMain=Label(self.NewsFrame, font=('Helvetica', 30), fg='white', bg='black', text="News:")
		self.labelMain.pack()
		self.label1=Label(self.NewsFrame, font=('Helvetica', 12), fg="white", bg="black")
		self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getNews()
		self.label1.after(300000, self.getNews)
	def getNews(self):
		NewsList=[]
		News=""
		News=""
		select_news=""
		get_api=get_api_keys()
		APIK=get_api['news_api']
		URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+APIK
		News=requests.get(URLnews)
		News=News.json()
		NewsList=News['articles']
		for i in NewsList:
			Nov = str(i['title']).split("- ")
			#print(Nov)
			if (Nov[1]=='24ur.com' or Nov[1]=='RTV Slovenija' or Nov[1]=='Računalniške News' or Nov[1]=='Siol.net'):
				#self.label1.config(text="")
				select_news+=str(i['title']) + '\n'
		self.update_news(select_news)
	def update_news(self,data):
		self.label1.config(text=data)
		
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
		self.get_home()
		#self.getCamera()
	def getCamera(self):
		# .local is inside home directory
		try:
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		except:
			face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Capture frame-by-frame
		global user
		#global login
		cap = cv2.VideoCapture(0)
		ret, frame = cap.read()
		user_name=''
		#detect face
		faces = face_front.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
		for (x, y, w, h) in faces:
			#user_name=str(x)+', '+str(y)+', '+str(w)+', '+str(h)
			
			#print (x)
			roi_color=frame[y:y+h, x:x+w]
			
			#image = face_recognition.load_image_file('./Images/stevejobs.png')
			image_encoding = face_recognition.face_encodings(frame)[0]
			#while (user_name==''):
			for root, dirs, files in os.walk(image_dir):
				for d in dirs:
					print(d)
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
									user_name=d
									path, dirs, files = next(os.walk(image_dir+'/'+d))
									file_count = len(files)
									print(d)
									img_item2=str(image_dir)+'/Users/'+d+'/'+d+'_'+str(file_count+1)+'.jpg'
									cv2.imwrite(img_item2, roi_color)
									self.update_user(user_name)
									break# test
								else:
									continue
			user=user_name
			cap.release()
			self.get_home()
			
		if len(faces)==0:
			#self.label1.config(text='Empty')
			self.label1.after(600, self.getCamera)
	def update_user(self,user):
		text123='Hello ' + user
		self.labelMain.config(text=text123)
		self.label1.config(text=user)

	def get_home(self):
		#time.sleep(10)
		self.labelMain.config(text='')
		self.TopFrame = Frame(self, background='black', padx=0, pady=0)
		#self.BottomFrame = Frame(self, background='yellow')
		self.TopLeftFrame=Frame(self.TopFrame, background='black')
		#self.BottomLeftFrame=Frame(self.BottomFrame, background='yellow')
		self.TopRightFrame=Frame(self.TopFrame, background='black')
		#self.BottomRightFrame=Frame(self.BottomFrame, background='yellow')
		
		self.TopFrame.pack(side=TOP, fill=BOTH)
		self.TopLeftFrame.pack(side = LEFT, fill=BOTH, padx=50)
		self.TopRightFrame.pack(side = RIGHT, fill=BOTH)

		self.ura=Time(self.TopRightFrame)
		self.ura.pack(side=TOP)
		self.Weather=Weather(self.TopLeftFrame)
		self.Weather.pack(side=TOP)
		self.news=News(self)
		self.news.pack(side=BOTTOM)
		self.asistant=Asistant(self)
		self.asistant.pack(side=TOP)
		
class Window:
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
	
win=Window()
win.tk.mainloop()

	