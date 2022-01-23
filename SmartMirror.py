try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import time
import requests
from urllib3 import *
import os
import pyttsx3 as pyttsx
import speech_recognition as sr
import threading
#import send_command
from send_command import Do_for_command
from face_recognize import Get_face
import signal
import subprocess
from speech_listen import Speaking
from working_with_files import Work_with_files
from PIL import ImageTk
import PIL.Image
from speech_listen import Listening
import sys



BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Users')
user = ''
speech_engine = pyttsx.init()

class Asistant(Frame):
	def __init__(self, parent, *args, **kwargs):
		self.listening_bool : str
		Frame.__init__(self, parent, bg='black')
		self.CommandHelpHeader=Label(self,font=('Helvetica', 40), fg="white", bg="black", text='\nFirst say "Hey Mirror" then you can try to say:')
		self.CommandHelpHeader.pack()
		self.CommandHelp=Label(self,font=('Helvetica', 12), fg="white", bg="black",text='Search youtube for\nShow me the forecast\nSearch wikipedia for\nStart the calibration')
		self.CommandHelp.pack()
		self.getPosluh()
	def getPosluh(self):
		my_thread=threading.Thread(target=self.Listening_test)
		my_thread.start()
    		
	def Listening_test(self):
		self.start_to_listen=False
		self.popup_id=''
		self.displayed=5
		self.previous_search=''
		self.l=''
		self.save_p_search=["next","back","previous","1","2","3","4","5","6","7","8","9","10","one","two","three","four","five","six","seven","eight","nine","ten","first", "second","thirth","fourth","fifth","sixth","seventh","eighth","nineth","tenth"]
		try:
			while(True):
				print('START LISTENING WHILE LOOP')
				self.l=Listening.listening_function()
				if ("mirror" in self.l.lower()):
					self.start_to_listen=True
					Speaking.to_say('OK. I AM LISTENING.')
					start_popup=subprocess.Popen(["python3", "./show_popup.py"])
					self.popup_id=str(start_popup.pid)
					
				elif (self.l.lower() != "" and self.l.lower() != "mirror" and self.start_to_listen==True):
					if('log out' in self.l.lower() or 'log off' in self.l.lower() or 'exit' in self.l.lower()):
						'''if (len(self.popup_id)>0):
							os.kill(int(self.popup_id), signal.SIGKILL)
						self.master.master.destroy()'''
						sys.exit()
					else:
						if ("next" in self.l.lower()):
							self.displayed=self.displayed+5
						self.send_command_thread=threading.Thread(target=Do_for_command(self.l.lower(), user, str(self.displayed), self.previous_search))
						self.send_command_thread.start()
					self.start_to_listen=False
					if (len(self.popup_id)>0):
						os.kill(int(self.popup_id), signal.SIGKILL)
					if(self.l not in self.save_p_search):
						self.previous_search=self.l
					else:
						continue

		except Exception as e:
			print(e)

class Time(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg='black')
		self.current_time=Label(self, font=('Helvetica', 100), fg="white", bg="black")
		self.current_time.pack(side=TOP,anchor=E)
		self.day_label=Label(self, font=('Helvetica', 20), fg="white", bg="black")
		self.day_label.pack()
		self.update_time()
	def update_time(self):
		self.ti=time.strftime('%H:%M:%S')
		self.day=time.strftime('%A, %B %d %Y ')
		self.update_clock(self.ti,self.day)
		self.current_time.after(1000, self.update_time)
	def update_clock(self,ti,d):
		self.current_time.config(text=ti)
		self.day_label.config(text=d)

class Weather(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg='black', padx=0, pady=0)
		self.WeatherTitle=Label(self, font=('Helvetica', 40), fg='white', bg='black', text="Weather:")
		self.WeatherTitle.pack()
		self.WeatherFrame=Frame(self, bg="black")
		self.WeatherFrame.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.WeatherTop=Frame(self.WeatherFrame, bg="black")
		self.WeatherTop.pack(side=TOP, fill=BOTH, expand= TRUE, anchor='w')
		self.WeatherIcon=Label(self.WeatherTop,width=17, fg="white", bg="black")
		self.WeatherIcon.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.WeatherData=Label(self.WeatherTop, font=('Helvetica', 15), fg="white", bg="black")
		self.WeatherData.pack(side=RIGHT, fill=BOTH, expand= TRUE, anchor='w')
		self.WeatherDataHours=Label(self.WeatherFrame, font=('Helvetica', 12), fg="white", bg="black")
		self.WeatherDataHours.pack(side=LEFT, anchor='w')
		self.getWeather()
		
	def getWeather(self):
		self.City = "Novo mesto"
		self.Country = "SI"
		self.get_api=Work_with_files.get_api_keys()
		self.APIK=self.get_api['weather_api']
		self.URL_main = "https://api.openweathermap.org/data/2.5/weather?q="+self.City+","+self.Country+"&appid="+self.APIK+'&units=metric'
		self.URL_hours = 'https://api.openweathermap.org/data/2.5/forecast?q='+self.City+','+self.Country+'&appid='+self.APIK+'&units=metric'
		self.r = requests.get(self.URL_main)
		self.read_weather = self.r.json()
		Work_with_files.save_weather_data(self.read_weather)
		self.r_hours = requests.get(self.URL_hours)
		self.read_weather_h=self.r_hours.json()
		self.update_weather_main(self.read_weather)
		self.update_weather_hours(self.read_weather_h)
		Work_with_files.save_weather_data(self.read_weather_h)
		self.WeatherTitle.after(60000, self.getWeather)

	def update_weather_main(self,weather_data):
		self.temp="Temp: " + str(weather_data['main']['temp'])
		self.humidity="Humidity: " + str(weather_data['main']['humidity'])
		self.temp_min="Temp_min: " + str(weather_data['main']['temp_min'])
		self.temp_max="Temp_max: " + str(weather_data['main']['temp_max'])
		self.weather=self.temp +'\n' + self.humidity + '\n' + self.temp_min + '\n' + self.temp_max
		'''self.icon='13d'#weather_data['weather'][0]['icon']
		self.BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		self.image_dir=os.path.join(self.BASE_DIR, 'Weather_widgets')
		self.image_byt = str(self.image_dir+'/'+self.icon+'.PNG')
		self.load = PIL.Image.open(self.image_byt)
		image_final=self.load.resize((150,100), PIL.Image.ANTIALIAS)
		self.render = ImageTk.PhotoImage(image_final)
		try:
			self.img.config(image=self.render)
		except AttributeError:
			self.img = Label(self.WeatherIcon, image=self.render, width=150, height=100, background="red")
			self.img.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')'''
		self.WeatherData.config(text=self.weather)

	def update_weather_hours(self,data):
		day=time.strftime('%Y-%m-%d')
		w_data=''
		for d in data['list']:
			if (day in d["dt_txt"]):
				w_data=w_data+"\n"+d["dt_txt"].split(' ')[1]+"   Temp: " + str(d['main']['temp'])+'   Desc:'+d['weather'][0]['description']
		self.WeatherDataHours.config(text=w_data)
class News(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg='black')
		self.NewsFrame=Frame(self, background='Black')
		self.NewsFrame.pack(side=RIGHT)
		self.NewsTitle=Label(self.NewsFrame, font=('Helvetica', 30), fg='white', bg='black', text="News:")
		self.NewsTitle.pack()
		self.NewsShow=Label(self.NewsFrame, font=('Helvetica', 12), fg="white", bg="black")
		self.NewsShow.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getNews()
		
	def getNews(self):
		self.NewsList=[]
		self.get_api=Work_with_files.get_api_keys()
		self.APIK=self.get_api['news_api']
		self.URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+self.APIK
		self.News_request=requests.get(self.URLnews)
		self.News=self.News_request.json()
		Work_with_files.save_news_data(self.News)
		self.NewsList=self.News['articles']
		self.update_news(self.NewsList)
		self.NewsShow.after(60000000000, self.getNews)

	def update_news(self,data):
		select_news=''
		count_news=0
		for i in range(len(data)):
			Nov = str(data[i]['title']).split("- ")
			news_source=data[i]['source']['name']
			if (news_source.lower() in ('24ur.com', 'rtvslo.si', 'siol.net', 'racunalniske-novice.com') and count_news<10):
				select_news+=Nov[0] + '-' + news_source + '\n'
				count_news=count_news+1
			elif (count_news==10):
				break
		self.NewsShow.config(text=select_news)
		
class Camera(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, background='Black')
		self.pack(side=LEFT, fill=BOTH, expand=YES)
		self.CamFrame=Frame(self, background='Black')
		self.CamFrame.pack(side=TOP,anchor=E)
		#self.get_camera()
		self.get_home()
	def get_camera(self):
		while (True):
			self.get_user=Get_face.User_auth()
			if (self.get_user is not None and len(self.get_user)>0):
				print(self.get_user)
				self.get_home()
				break
	def get_home(self):
		#self.NewsTitle.config(text='')
		self.TopFrame = Frame(self, background='black', padx=0, pady=0)
		self.TopLeftFrame=Frame(self.TopFrame, background='black')
		self.TopRightFrame=Frame(self.TopFrame, background='black')
		
		self.TopFrame.pack(side=TOP, fill=BOTH)
		self.TopLeftFrame.pack(side = LEFT, fill=BOTH, padx=50, pady=50)
		self.TopRightFrame.pack(side = RIGHT, fill=BOTH, padx=50, pady=50)

		self.ura=Time(self.TopLeftFrame)
		self.ura.pack(side=TOP)
		self.Weather=Weather(self.TopRightFrame)
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
		#self.tk.geometry("1920x1000")
		self.tk.attributes('-fullscreen', True)  
		self.fullScreenState = False
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.recognize()
		self.tk.mainloop()
	def recognize(self):
		self.cam=Camera(self.Frame)
		self.cam.pack()
	
#win=Window()
#win.tk.mainloop()
