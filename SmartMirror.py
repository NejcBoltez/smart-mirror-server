try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import time
import json
import requests
#import urllib
#import cv2
#import numpy as np
from urllib3 import *
#from PIL import Image, ImageTk
#import dlib
import os
#import face_recognition
import pyttsx3 as pyttsx
import speech_recognition as sr
#import subprocess #as call
#import posluh1 as listening
from multiprocessing import Queue
import multiprocessing
import threading
import send_command
from send_command import Do_for_command
from face_recognize import Get_face
import signal
import subprocess
import psutil
from speech_listen import Speaking
from datetime import datetime




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
#win=None

def get_api_keys():
	api_keys_dir=os.path.join(BASE_DIR, '../api_keys.json')
	with open(api_keys_dir, 'r') as f:
		d=json.load(f)
	#print(len(d))
	#print(d['weather_api'])
	return d


def restart_window():
	global win
	#print(win.tk.title)
	#win.join()
	win.tk.destroy
	win=Window()
	win.tk.mainloop()
	return win

class Asistant(Frame):
	def __init__(self, parent, *args, **kwargs):
		self.listening_bool : str
		Frame.__init__(self, parent, bg='black')
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
		print("Say something12345678--TEST!")
		
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
		start_to_listen=False
		self.popup_id=''
		l=''
		try:
			while(True):
				print('START LISTENING WHILE LOOP')
				l=self.listening_function()
				if ("mirror" in l.lower()):
					start_to_listen=True
					Speaking.to_say('OK. I AM LISTENING.')
					start_popup=subprocess.Popen(["python3", "show_popup.py"])
					self.popup_id=str(start_popup.pid)
					for proc in psutil.process_iter():
						print(proc.name())
						'''if 'Forecast_process' in proc.name():
							pid = proc.pid
							print(proc.name()+" : "+pid)'''
					#open_processes.append("Open_news:"+str(Open_news.pid))
					
				elif (l.lower() != "" and l.lower() != "mirror" and start_to_listen==True):
					print(l.lower())
					print(user)
					if('log out' in l.lower() or 'log off' in l.lower() or 'exit' in l.lower()):
						if (len(self.popup_id)>0):
							os.kill(int(self.popup_id), signal.SIGKILL)
						self.master.master.destroy()
						print('TEST')
					else:
						self.send_command_thread=threading.Thread(target=send_command.Do_for_command(l.lower(), user))
						self.send_command_thread.start()
					start_to_listen=False
					print(start_to_listen)
					if (len(self.popup_id)>0):
						os.kill(int(self.popup_id), signal.SIGKILL)

		except Exception as e:
			print(e)

class Time(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg='black')
		self.label1=Label(self, font=('Helvetica', 100), fg="white", bg="black")
		self.label1.pack(side=TOP,anchor=E)
		self.day_label=Label(self, font=('Helvetica', 20), fg="white", bg="black")
		self.day_label.pack()
		self.update_time()
	def update_time(self):
		self.ti=time.strftime('%H:%M:%S')
		self.day=time.strftime('%Y.%m.%d - %A')
		self.update_clock(self.ti,self.day)
		# calls itself every 1000 milliseconds to update the time display as needed could use >200 ms, but display gets jerky
		self.label1.after(1000, self.update_time)
	def update_clock(self,ti,d):
		self.label1.config(text=ti)
		self.day_label.config(text=d)

class Weather(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='green', padx=0, pady=0)
		self.LabelMain=Label(self, font=('Helvetica', 40), fg='white', bg='black', text="Weather:")
		self.LabelMain.pack()
		self.weather_data=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.weather_data.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getWeather()
		self.weather_data.after(10000, self.getWeather)
	def getWeather(self):
		self.City = "Novo mesto"
		self.Country = "SI"
		self.get_api=get_api_keys()
		self.APIK=self.get_api['weather_api']
		self.URL = "https://api.openweathermap.org/data/2.5/weather?q="+self.City+","+self.Country+"&appid="+self.APIK
		self.r = requests.get(self.URL)
		self.read_weather = self.r.json()
		self.temp="Temp: " + str(self.read_weather['main']['temp'])
		self.humidity="Humidity: " + str(self.read_weather['main']['humidity'])
		self.temp_min="Temp_min: " + str(self.read_weather['main']['temp_min'])
		self.temp_max="Temp_max: " + str(self.read_weather['main']['temp_max'])
		self.weather=self.temp +'\n' + self.humidity + '\n' + self.temp_min + '\n' + self.temp_max
		self.update_weather(self.weather)
	def update_weather(self,data):
		self.weather_data.config(text=data)

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
		self.NewsList=[]
		self.News=""
		self.News=""
		self.select_news=""
		self.get_api=get_api_keys()
		self.APIK=self.get_api['news_api']
		self.URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+self.APIK
		self.News_request=requests.get(self.URLnews)
		self.News=self.News_request.json()
		self.NewsList=self.News['articles']
		for i in range(len(self.NewsList)):
			Nov = str(self.NewsList[i]['title']).split("- ")
			if (Nov[1]=='24ur.com' or Nov[1]=='RTV Slovenija' or Nov[1]=='Računalniške News' or Nov[1]=='Siol.net'):
				self.select_news+=str(self.NewsList[i]['title']) + '\n'
			if (i==10):
				break
			
		self.update_news(self.select_news)
	def update_news(self,data):
		self.label1.config(text=data)
		
class Camera(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, background='Black')
		self.pack(side=LEFT, fill=BOTH, expand=YES)
		self.CamFrame=Frame(self, background='Black')
		self.CamFrame.pack(side=TOP,anchor=E)
		self.labelMain=Label(self.CamFrame, font=('Helvetica', 60), fg='white', bg='black', text="Please LOGIN",anchor='w')
		self.labelMain.pack()
		self.label1=Label(self.CamFrame, font=('Helvetica', 9), fg="white", bg="black",anchor='w')
		self.label1.pack()
		self.get_home()
		#self.get_camera()
	def get_camera(self):
		while (True):
			self.get_user=Get_face.User_auth()
			if (self.get_user is not None and len(self.get_user)>0):
				self.get_home()
				break
	def get_home(self):
		self.labelMain.config(text='')
		self.TopFrame = Frame(self, background='black', padx=0, pady=0)
		self.TopLeftFrame=Frame(self.TopFrame, background='black')
		self.TopRightFrame=Frame(self.TopFrame, background='black')
		
		self.TopFrame.pack(side=TOP, fill=BOTH)
		self.TopLeftFrame.pack(side = LEFT, fill=BOTH, padx=50)
		self.TopRightFrame.pack(side = RIGHT, fill=BOTH)

		self.ura=Time(self.TopRightFrame)
		self.ura.pack(side=TOP)
		self.Weather=Weather(self.TopLeftFrame)
		self.Weather.pack(side=TOP)
		self.news=News(self)
		self.news.pack(side=BOTTOM)
		#self.asistant=Asistant(self)
		#self.asistant.pack(side=TOP)
		
class Window:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.recognize()
	def recognize(self):
		self.cam=Camera(self.Frame)
		self.cam.pack()
	
win=Window()
win.tk.mainloop()
