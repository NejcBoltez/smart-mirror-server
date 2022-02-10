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
		day_label=Label(self, font=("Helvetica", 20), fg="white", bg="black")
		day_label.pack()
		self.update_time()

	def update_time(self):
		ti=time.strftime("%H:%M:%S")
		day=time.strftime("%A, %B %d %Y ")
		self.update_clock(ti,day)
		print("TEST TIME SECONDS")
		#current_time.after(1000, update_time)
		
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
		try:
			icon=weather_data["weather"][0]["icon"]
			BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			image_dir=os.path.join(BASE_DIR, "Weather_widgets")
			image_byt = str(image_dir+os.path.sep+icon+".PNG")
			load = PIL.Image.open(image_byt)
			image_final=load.resize((150,100), PIL.Image.ANTIALIAS)
		except:
			icon="13d"#weather_data["weather"][0]["icon"]
			BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			image_dir=os.path.join(BASE_DIR, "Weather_widgets")
			image_byt = str(image_dir+"/"+icon+".PNG")
			load = PIL.Image.open(image_byt)
			image_final=load.resize((150,100), PIL.Image.ANTIALIAS)
		render = ImageTk.PhotoImage(image_final)
		try:
			self.img.config(image=render)
		except AttributeError:
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
		#NewsShow.after(60000000000, getNews)

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
		user=user
		tabs=tabs
		isListening=True
		self.HomeFrame=Frame(tabs, background="black")
		self.HomeFrame.pack(fill=BOTH, expand=YES)
		home_tab = ttk.Frame(tabs)
		tasks=[]
		tabs.add(self.HomeFrame, text ="HOME SCREEN")
		
		loop = asyncio.get_event_loop()
		tasks.append(loop.create_task(get_home(self, user, tabs)))
		
		tasks.append(loop.create_task(get_thread(self, listening_q, user, tabs, loop, tasks)))
		loop.run_until_complete(asyncio.gather(*tasks))
		#loop.run_forever()
		#loop.run_until_complete(get_home(self, user, tabs))
		#loop.run_until_complete(get_thread(self, listening_q, user, tabs))
		while(True):
			if(len(tabs.tabs())==0):
				print("STOPING TASKS")
				for task in tasks:
					task.cancel()
				#loop.stop()

				break
					#destroy()
async def get_thread(self, thread_q, user, tabControl, loop, tasks):
	is_listening=False
	popup_id=0
	while(len(tabControl.tabs())>0):
		await asyncio.sleep(5)
		l= await thread_value(thread_q)
		displayed=5
		print("TEST:  " + l)
		if ("mirror" in l.lower()):
			Speaking.to_say('OK. I AM LISTENING.')
			start_popup=subprocess.Popen(["python3", "./show_popup.py"])
			popup_id=str(start_popup.pid)
			is_listening=True	
		elif (is_listening==True and len(l.lower())>0):
			print("TEST1234321 WORKING OK")
			os.kill(int(popup_id), signal.SIGKILL)
			loop.create_task(Do_for_command.main(self, l.lower(), user, str(displayed), tabControl, loop, tasks))

		else:
			continue
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

	Clock=Time(self.TopLeftFrame)
	Clock.pack(side=TOP)
	Weather=Weather(self.TopRightFrame)
	Weather.pack(side=TOP)
	News=News(self.HomeFrame)
	News.pack(side=BOTTOM)
	
	CommandHelpHeader=Label(self.HomeFrame,font=("Helvetica", 40), fg="white", bg="black", text="HELLO "+user.upper())
	CommandHelpHeader.pack()
	CommandHelp=Label(self.HomeFrame,font=("Helvetica", 12), fg="white", bg="black",text="First say 'Hey Mirror' then you can try to say:")#Search youtube for\nShow me the forecast\nSearch wikipedia for\nStart the calibration")
	CommandHelp.pack()

	while(len(tabs.tabs())>0):
		await asyncio.sleep(1)
		print(len(tabs.tabs()))
		print(tabs.tabs())
		Clock.update_time()
		Clock.update()
	#	tabs.update()
		
class Window:
	def __init__(self, user):
		self.tk=tk.Tk()
		tk.configure(background="black")
		tk.title("Pozdravljeni")
		tk.geometry("1920x1000")
		Frame=tk.Frame(self.tk, background="black")
		Frame.pack(fill=BOTH, expand=YES)
		#tabControl = ttk.Notebook(Frame, height=100)
		#tabControl.pack(expand = 1, fill ="both")
		self.recognize(user)
		tk.mainloop()
	def recognize(self, user):
		cam=Home_screen(Frame, user)#, tabControl)
		cam.pack()
	
#win=Window("nejc")
