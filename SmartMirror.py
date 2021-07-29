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


def to_say(besedilo):
    print(besedilo)
    speech_engine.say(besedilo)
    speech_engine.runAndWait()
def restart_window():
	global win
	#print(win.tk.title)
	#win.join()
	win.tk.destroy
	win=Window()
	win.tk.mainloop()
	return win

class Popup_window(Frame):
	def __init__(self):	
		print("POPUP WINDOW")
		self.popup = tk.Tk()
		self.popup.geometry("500x100")
		self.label = tk.Label(self.popup, text='Start to listen')
		self.label.pack(side="top", fill="x", pady=10)
		self.popup.mainloop()
	def close(self):
		self.popup.destroy()
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

	def popup_win(self):
		#self.popup=Popup_window()
		#return popup
		print("POPUP WINDOW")
		self.popup = tk.Tk()
		self.popup.geometry("500x100")
		self.label = tk.Label(self.popup, text='Start to listen')
		self.label.pack(side="top", fill="x", pady=10)
		self.popup.mainloop()
		return self.popup
		#time.wait(10)
		#self.popup.destroy()
    		
	def Listening_test(self):
		global user
		global win
		start_to_listen=False
		self.popup_id=''
		l=''
		try:
			while(True):
				print('START LISTENING WHILE LOOP')
				l=self.listening_function()
				#self.check_if_listening(l)
				#self.PosluhFrame.config(text=str(l))
				if ("mirror" in l.lower()):
					start_to_listen=True
					to_say('OK. I AM LISTENING.')
					#self.start_popup=threading.Thread(target=self.popup_win)
					#self.start_popup.setDaemon(True)
					#self.start_popup.start()
					#print("IS active:"+str(threading.get_ident()))
					start_popup=subprocess.Popen(["python3", "show_popup.py"])
					#Open_news.start()
					self.popup_id=str(start_popup.pid)
					#open_processes.append("Open_news:"+str(Open_news.pid))
					
				elif (l.lower() != "" and l.lower() != "mirror" and start_to_listen==True):
					print(l.lower())
					print(user)
					if('log out' in l.lower() or 'log off' in l.lower() or 'exit' in l.lower()):
						if (len(self.popup_id)>0):
							os.kill(int(self.popup_id), signal.SIGKILL)
						#win.tk.destroy()
						#restart_window()
						#print(str(self.master.destroy()))
						#self.master.destroy()
						self.master.master.destroy()
						#print(str(self.master.name))
						#self.master.get_camera()
						#self.close()
						#self.tk.destroy()
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
		#self.get_home()
		self.get_camera()
	def get_camera(self):
		while (True):
			self.get_user=Get_face.User_auth()
			if (self.get_user is not None and len(self.get_user)>0):
				self.get_home()
				break
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
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		#self.tk.mainloop()
		self.recognize()
		#self.tk.mainloop()
	def recognize(self):
		self.cam=Camera(self.Frame)
		self.cam.pack()
	def close(self):
		print(win.tk.title)
		list = self.tk.grid_slaves()
		for l in list:
			l.destroy()
		#self.master.quit()
	
win=Window()
win.tk.mainloop()
#win=multiprocessing.Process(target=Window(), args=(10,))
#win.start()
