try:
	import tkinter as tk
	from tkinter import *
	from tkinter import ttk
except:
	import Tkinter as tk
	from Tkinter import *
import time
import asyncio
from send_command import Do_for_command
from working_with_files import Work_with_files
from PIL import ImageTk
import PIL.Image
import os
import subprocess
from speech_listen import Speaking
import signal
from queue import Queue
import threading
#import show_popup


class Time(Frame):
	def __call__(args):
		try: 
			print("test:     "+args)
		except:
			print("")
	def __init__(self, parent):#, tabcontrol):
		Frame.__init__(self, parent, bg="black", padx=0, pady=0)
		self.current_time=Label(self, font=("Helvetica", 100), fg="white", bg="black")
		self.current_time.pack(side=TOP,anchor=E)
		self.day_label=Label(self, font=("Helvetica", 20), fg="white", bg="black")
		self.day_label.pack()
		self.update_time()

	def update_time(self):
		ti=time.strftime("%H:%M:%S")
		day=time.strftime("%A, %B %d %Y ")
		self.update_clock(ti,day)
		self.current_time.after(1000, self.update_time)
		
	def update_clock(self,ti,d):
		self.current_time.config(text=ti)
		self.day_label.config(text=d)	

class Weather(Frame):
	def __call__(args):
		try: 
			print("test:     "+args)
		except:
			print("")
	def __init__(self, parent):
		Frame.__init__(self, parent, bg="black", padx=0, pady=0)
		self.WeatherTitle=Label(self, font=("Helvetica", 40), fg="white", bg="black", text="Weather:")
		self.WeatherTitle.pack()
		self.WeatherFrame=Frame(self, bg="black")
		self.WeatherFrame.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor="w")
		self.WeatherTop=Frame(self.WeatherFrame, bg="black")
		self.WeatherTop.pack(side=TOP, fill=BOTH, expand= TRUE, anchor="w")
		self.WeatherIcon=Label(self.WeatherTop,width=17, fg="white", bg="black")
		self.WeatherIcon.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor="w")
		self.WeatherData=Label(self.WeatherTop, font=("Helvetica", 15), fg="white", bg="black")
		self.WeatherData.pack(side=RIGHT, fill=BOTH, expand= TRUE, anchor="w")
		self.WeatherDataHours=Label(self.WeatherFrame, font=("Helvetica", 12), fg="white", bg="black")
		self.WeatherDataHours.pack(side=LEFT, anchor="w")
		self.getWeather()
		
	def getWeather(self):
		read_weather=Work_with_files.read_weather_main()
		read_weather_h=Work_with_files.read_weather_data()
		self.update_weather_main(read_weather)
		self.update_weather_hours(read_weather_h)

	def update_weather_main(self,weather_data):
		temp="Temp: " + str(weather_data["main"]["temp"])
		humidity="Humidity: " + str(weather_data["main"]["humidity"])
		temp_min="Temp_min: " + str(weather_data["main"]["temp_min"])
		temp_max="Temp_max: " + str(weather_data["main"]["temp_max"])
		weather=temp +"\n" + humidity + "\n" + temp_min + "\n" + temp_max
		icon=weather_data["weather"][0]["icon"]
		print(icon)
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, "Weather_widgets")
		image_byt = str(image_dir+os.path.sep+icon+".PNG")
		print(image_byt)
		load = PIL.Image.open(image_byt)
		image_final=load.resize((120,70), PIL.Image.ANTIALIAS)
		render = ImageTk.PhotoImage(image_final)
		try:
			img = Label(self.WeatherIcon, image=render, width=150, height=100, background="black")
			img.image = render
			img.place(x=0, y=0)
		except AttributeError as e:
			print(e)
			img = Label(self.WeatherIcon, image=render, width=150, height=100, background="red")
			img.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor="w")
		self.WeatherData.config(text=weather)

	def update_weather_hours(self,data):
		day=time.strftime("%Y-%m-%d")
		w_data=""
		for d in data["list"]:
			if (day in d["dt_txt"]):
				w_data=w_data+"\n"+d["dt_txt"].split(" ")[1]+"   Temp: " + str(d["main"]["temp"])+"   Desc:"+d["weather"][0]["description"]
		self.WeatherDataHours.config(text=w_data)

class News(Frame):
	def __call__(args):
		try: 
			print("test:     "+args)
		except:
			print("")

	def __init__(self, parent):	
		Frame.__init__(self, parent, bg="black")
		self.NewsFrame=Frame(self, background="Black")
		self.NewsFrame.pack(side=RIGHT)
		self.NewsTitle=Label(self.NewsFrame, font=("Helvetica", 30), fg="white", bg="black", text="News:")
		self.NewsTitle.pack()
		self.NewsShow=Label(self.NewsFrame, font=("Helvetica", 12), fg="white", bg="black")
		self.NewsShow.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor="w")
		self.getNews()
		
	def getNews(self):
		NewsList=[]
		News=Work_with_files.read_news_data()
		NewsList=News["articles"]
		self.update_news(NewsList)

	def update_news(self,data):
		select_news=""
		count_news=0
		for i in range(len(data)):
			Nov = str(data[i]["title"]).split("- ")
			news_source=data[i]["source"]["name"]
			if (news_source.lower() in ("24ur.com", "rtvslo.si", "siol.net", "racunalniske-novice.com") and count_news<10):
				select_news+=Nov[0] + "-" + news_source + "\n"
				count_news=count_news+1
			elif (count_news==10):
				break
		self.NewsShow.config(text=select_news)

class Home_screen(Frame):
	def __call__(args):
		try: 
			print("test:     "+args)
		except:
			print("")
	def main(self, user, tabs):
		self.HomeFrame=Frame(tabs, background="black")
		self.HomeFrame.pack(fill=BOTH, expand=YES)
		self.popup_id=0
		home_tab = ttk.Frame(tabs)
		self.is_listening=False
		self.listening_word=""
		self.tasks=[]
		tabs.add(self.HomeFrame, text ="HOME SCREEN")
		loop = asyncio.get_event_loop()
		get_home(self, user, tabs, loop)

def get_home(self, user, tabs, loop):
	self.TopFrame = Frame(self.HomeFrame, background="black", padx=0, pady=0)
	self.TopLeftFrame=Frame(self.TopFrame, background="black")
	self.TopRightFrame=Frame(self.TopFrame, background="black")
	
	self.TopFrame.pack(side=TOP, fill=BOTH)
	self.TopLeftFrame.pack(side = LEFT, fill=BOTH, padx=50, pady=50)
	self.TopRightFrame.pack(side = RIGHT, fill=BOTH, padx=50, pady=50)

	self.Clock=Time(self.TopLeftFrame)
	self.Clock.pack(side=TOP)
	self.Weather=Weather(self.TopRightFrame)
	self.Weather.pack(side=TOP)
	self.News=News(self.HomeFrame)
	self.News.pack(side=BOTTOM)
	
	self.CommandHelpHeader=Label(self.HomeFrame,font=("Helvetica", 40), fg="white", bg="black", text="HELLO "+user.upper())
	self.CommandHelpHeader.pack(pady=10)
	self.CommandHelp=Label(self.HomeFrame,font=("Helvetica", 12), fg="white", bg="black",text="First say 'Hey Mirror' then wait for the window to open:")#Search youtube for\nShow me the forecast\nSearch wikipedia for\nStart the calibration")
	self.CommandHelp.pack(pady=10)
	self.update()

	while(len(tabs.tabs())>0):
		time.sleep(1)
		self.update()
		print(self.listening_word)
		l=str(self.listening_word)
		displayed=5
		print("TEST:  " + l)
		if ("hi mirror" in l.lower() and self.is_listening==False):
			try:
				print(type(self.player))
				self.player.set_pause(1)
			except Exception as e:
				print(e)
			speak=threading.Thread(target=Speaking.to_say, args=('OK. I AM LISTENING.',))
			speak.start()
			start_popup=subprocess.Popen(["python3", "./show_popup.py"])
			popup_id=str(start_popup.pid)
			self.is_listening=True	
			self.listening_word=""
		elif (self.is_listening==True and len(l.lower())>0):
			print("TEST1234321 WORKING OK")
			if ("next" in l.lower()):
				displayed=displayed  + 5
			Do_for_command.main(self, l.lower(), str(displayed), tabs, loop, self.tasks)
			
			os.kill(int(popup_id), signal.SIGKILL)
			self.is_listening=False
			self.listening_word=""
		else:
			continue
		self.update()
		#self.Clock.update_time()
		#self.Clock.update()
			
class Window:
	def __init__(self, user):
		self.tk=tk.Tk()
		self.main_q=Queue()
		self.tk.configure(background="black")
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		self.Frame=tk.Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.tabControl = ttk.Notebook(self.Frame, height=100)
		self.tabControl.pack(expand = 1, fill ="both")
		self.recognize(user)
		self.tk.mainloop()
	def recognize(self, user):
		cam=Home_screen.main(self.Frame, user, self.tabControl, self.main_q)
		cam.pack()
	
#win=Window("nejc")
