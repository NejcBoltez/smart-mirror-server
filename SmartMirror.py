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
import show_popup


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
		self.ti=time.strftime("%H:%M:%S")
		self.day=time.strftime("%A, %B %d %Y ")
		self.update_clock(self.ti,self.day)
		print("TEST TIME SECONDS")
		#self.current_time.after(1000, self.update_time)
		
	def update_clock(self,ti,d):
		self.current_time.config(text=ti)
		self.day_label.config(text=d)	

class Weather(Frame):
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
		self.read_weather=Work_with_files.read_weather_main()
		self.read_weather_h=Work_with_files.read_weather_data()
		self.update_weather_main(self.read_weather)
		self.update_weather_hours(self.read_weather_h)

	def update_weather_main(self,weather_data):
		self.temp="Temp: " + str(weather_data["main"]["temp"])
		self.humidity="Humidity: " + str(weather_data["main"]["humidity"])
		self.temp_min="Temp_min: " + str(weather_data["main"]["temp_min"])
		self.temp_max="Temp_max: " + str(weather_data["main"]["temp_max"])
		self.weather=self.temp +"\n" + self.humidity + "\n" + self.temp_min + "\n" + self.temp_max
		try:
			self.icon=weather_data["weather"][0]["icon"]
			self.BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			self.image_dir=os.path.join(self.BASE_DIR, "Weather_widgets")
			self.image_byt = str(self.image_dir+os.path.sep+self.icon+".PNG")
			self.load = PIL.Image.open(self.image_byt)
			image_final=self.load.resize((150,100), PIL.Image.ANTIALIAS)
		except:
			self.icon="13d"#weather_data["weather"][0]["icon"]
			self.BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			self.image_dir=os.path.join(self.BASE_DIR, "Weather_widgets")
			self.image_byt = str(self.image_dir+"/"+self.icon+".PNG")
			self.load = PIL.Image.open(self.image_byt)
			image_final=self.load.resize((150,100), PIL.Image.ANTIALIAS)
		self.render = ImageTk.PhotoImage(image_final)
		try:
			self.img.config(image=self.render)
		except AttributeError:
			self.img = Label(self.WeatherIcon, image=self.render, width=150, height=100, background="red")
			self.img.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor="w")
		self.WeatherData.config(text=self.weather)

	def update_weather_hours(self,data):
		day=time.strftime("%Y-%m-%d")
		w_data=""
		for d in data["list"]:
			if (day in d["dt_txt"]):
				w_data=w_data+"\n"+d["dt_txt"].split(" ")[1]+"   Temp: " + str(d["main"]["temp"])+"   Desc:"+d["weather"][0]["description"]
		self.WeatherDataHours.config(text=w_data)

class News(Frame):
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
		self.NewsList=[]
		self.News=Work_with_files.read_news_data()
		self.NewsList=self.News["articles"]
		self.update_news(self.NewsList)
		#self.NewsShow.after(60000000000, self.getNews)

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
	def main(self, user, tabs, listening_q):
		#Frame.__init__(self, parent, bg="black", padx=0, pady=0)
		self.user=user
		tabs=tabs
		self.isListening=True
		self.HomeFrame=Frame(tabs, background="black")
		self.HomeFrame.pack(fill=BOTH, expand=YES)
		home_tab = ttk.Frame(tabs)
		self.tasks=[]
		tabs.add(self.HomeFrame, text ="HOME SCREEN")
		
		loop = asyncio.get_event_loop()
		self.tasks.append(loop.create_task(get_home(self, user, tabs)))
		
		self.tasks.append(loop.create_task(get_thread(self, listening_q, user, tabs, loop)))
		loop.run_until_complete(asyncio.gather(*self.tasks))
		#self.loop.run_forever()
		#self.loop.run_until_complete(get_home(self, user, self.tabs))
		#self.loop.run_until_complete(get_thread(self, listening_q, user, self.tabs))
		while(True):
			if(len(tabs.tabs())==0):
				print("STOPING TASKS")
				for task in self.tasks:
					task.cancel()
				#loop.stop()

				break
					#self.destroy()
async def get_thread(self, thread_q, user, tabControl, loop):
	is_listening=False
	popup_id=0
	while(len(tabControl.tabs())>0):
		await asyncio.sleep(5)
		l= await thread_value(thread_q)
		displayed=5
		print("TEST:  " + l)
		if ("mirror" in l.lower()):
			Speaking.to_say('OK. I AM LISTENING.')
			popup=show_popup.Popup_window()
			#start_popup=subprocess.Popen(["python3", "./show_popup.py"])
			#popup_id=str(start_popup.pid)
			is_listening=True	
		elif ("exit" not in l.lower() and is_listening==True):
			print("TEST1234321 WORKING OK")
			#os.kill(int(popup_id), signal.SIGKILL)
			loop.create_task(Do_for_command.main(self, l.lower(), user, str(displayed), tabControl, loop))

		else:
			print("EXITING")
			#break
async def thread_value(q):
	value=q.get()
	return value
async def get_home(self, user, tabs):
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
	
	#self.ast=Asistant(self.HomeFrame, thread_q)
	#self.ast.pack(side=BOTTOM)
	self.CommandHelpHeader=Label(self.HomeFrame,font=("Helvetica", 40), fg="white", bg="black", text="HELLO "+user.upper())
	self.CommandHelpHeader.pack()
	self.CommandHelp=Label(self.HomeFrame,font=("Helvetica", 12), fg="white", bg="black",text="First say 'Hey Mirror' then you can try to say:")#Search youtube for\nShow me the forecast\nSearch wikipedia for\nStart the calibration")
	self.CommandHelp.pack()

	print(len(tabs.tabs()))
	print(tabs.tabs())
	while(len(tabs.tabs())>0):
		await asyncio.sleep(1)
		print(len(tabs.tabs()))
		print(tabs.tabs())
		self.Clock.update_time()
		self.Clock.update()
	#	tabs.update()
		
class Window:
	def __init__(self, user):
		self.user=user
		self.tk=tk.Tk()
		self.tk.configure(background="black")
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		#self.tabControl = ttk.Notebook(self.Frame, height=100)
		#self.tabControl.pack(expand = 1, fill ="both")
		self.recognize()
		self.tk.mainloop()
	def recognize(self):
		self.cam=Home_screen(self.Frame, self.user)#, self.tabControl)
		self.cam.pack()
	
#win=Window("nejc")

s