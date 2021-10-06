import json
import requests
import datetime
from PIL import ImageTk, Image
import base64
from urllib.request import urlopen
from PIL import ImageTk
import PIL.Image
import time
import io
import os
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import sys
import pyttsx3 as pyttsx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import asyncio
#from aiohttp import ClientSession


#from tkinter.ttk import *

import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use("TkAgg")
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#import time



days_table=[]
day_selected=""
arguments = list(sys.argv)
#print(arguments[1])
days_in_week=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
current_day=[]
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
def get_api_keys():
	api_keys_dir=os.path.join(BASE_DIR, '../api_keys.json')
	with open(api_keys_dir, 'r') as f:
		d=json.load(f)
	#print(len(d))
	#print(d['weather_api'])
	return d


def govor(besedilo):
	speech_engine = pyttsx.init()
	speech_engine.say(besedilo)
	speech_engine.runAndWait()


class weather_GUI:
	def __enter__(self):
		return self
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self,command):
		#global arguments
		#Frame.__init__(self, parent)
		self.BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		self.image_dir=os.path.join(self.BASE_DIR, 'Weather_widgets')
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1080")
		self.Frame=Frame(self.tk, background="black", width=1920, height=1080)
		self.Frame.pack(fill=BOTH, expand=YES, anchor='w')
		logo_w=300
		logo_h=500
		days_w=100
		days_h=1000
		day_weather_w=1800
		day_weather_h=100
		forecast_w=1600
		forecast_h=1080
		self.days=Canvas(self.Frame, width=days_w, height=days_h, bg="black", highlightthickness=0)
		self.days.pack(side=LEFT, fill=BOTH, expand= TRUE, pady=80)
		self.day_weather=Canvas(self.Frame, width=day_weather_w, height=day_weather_h, highlightthickness=0)
		self.forecast=Canvas(self.Frame, width=forecast_w, height=forecast_h, bg="black", highlightthickness=0)
		self.forecast.pack(side=RIGHT, fill=BOTH, expand= TRUE, anchor='w')
		self.topFrame=Frame(self.forecast, height=forecast_h-300, background="black", highlightthickness=0)
		self.topFrame.pack(side=TOP, fill=BOTH, expand= TRUE)
		self.logo=Canvas(self.topFrame, width=logo_w, height=logo_h, background='black', highlightthickness=0)
		self.logo.pack(side=LEFT, fill=BOTH, anchor='w', padx=50, pady=50)
		self.data=Canvas(self.forecast,width=forecast_w, height=400, bg="black", border=0, highlightthickness=0)
		self.data.pack(side=BOTTOM, fill=BOTH, expand= TRUE, anchor='w')
		self.chart=Canvas(self.topFrame, bg="black", border=0, highlightthickness=0)
		self.chart.pack(side=RIGHT, fill=BOTH, expand= TRUE, anchor='w')
		self.get_weather_data()
		self.populate_data(command)
		self.tk.mainloop()
	def get_weather_data(self):
		'''days_table=[]
		day_selected=""
		#arguments = list(sys.argv)
		#print(arguments[1])
		days_in_week=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
		current_day=[]'''
		self.City = "Novo mesto"
		self.Country = "SI"
		self.get_api=get_api_keys()
		print(self.get_api)
		self.APIK=self.get_api['weather_api']
		self.URL = "https://api.openweathermap.org/data/2.5/forecast?q="+self.City+","+self.Country+"&appid="+self.APIK+'&units=metric'
		self.main_URL="https://api.openweathermap.org/data/2.5/weather?q="+self.City+","+self.Country+"&appid="+self.APIK+'&units=metric'
		self.r = requests.get(self.URL)
		self.r_main=requests.get(self.main_URL)
		self.read = self.r.json()
		self.read_day=self.r_main.json()
		self.main_icon=self.read_day['weather'][0]['icon']
	def populate_data(self,command):
		weather=''
		t=[]
		h=[]
		ws=[]
		hours=[]
		coordinate=50
		coordinatey=100
		#print(str(self.read['list']['main']))
		print(self.image_dir+'/'+self.main_icon+'.png')
		image_byt = str(self.image_dir+'/'+self.main_icon+'.PNG')# urlopen("https://openweathermap.org/img/wn/"+self.main_icon+"@2x.png").read()
		load = PIL.Image.open(image_byt)
		image_final=load.resize((300,200), PIL.Image.ANTIALIAS)
		render = ImageTk.PhotoImage(image_final)
		img = Label(self.logo, image=render, width=300, height=200, background="black")
		img.image = render
		img.place(x=10, y=150)

		for d in self.read['list']:
			if (str(d['dt_txt']).split(' ')[0] not in days_table):
				days_table.append(str(d['dt_txt']).split(' ')[0])
				
		for f in days_table:
			day_name=datetime.datetime.strptime(f, '%Y-%m-%d')
			b_string= str(day_name.strftime("%A")) + '\n' + str(f)
			d_n=str(day_name.strftime("%A")) 
			print(time.strftime('%A')+" test: " + d_n.lower())
			if (str(day_name.strftime("%A")).lower()==command):
				self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="silver", fg="black")
				self.daysb.pack()
			elif(command=="today" and str(day_name.strftime("%A")).lower()==time.strftime('%A').lower()):
				self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="silver", fg="black")
				self.daysb.pack()	
			elif(command=="tommorow"):
				self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="silver", fg="black")
				self.daysb.pack()	
			else:
				self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="black", fg="white")
				self.daysb.pack()

		day_selected=self.day_position(command)
			#days_table.append(str(d['dt_txt']).split(' ')[0])
		#else:
		#	 day_selected=days_table[0]
		for i in self.read['list']:
			date=str(i['dt_txt']).split(' ')[0]
			if (date == day_selected):
				cels=int(i['main']['temp'])
				temp="Temp: " + str(cels)
				humidity="Humidity: " + str(i['main']['humidity'])
				temp_min="Temp_min: " + str(i['main']['temp_min'])
				temp_max="Temp_max: " + str(i['main']['temp_max'])
				day_forecast=str(i['dt_txt']) + '\n' + temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max +'\n\n'
				weather=weather + str(i['dt_txt']) + '\n' + temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max +'\n\n' #+'\n' + days_table
				
				t.append(cels)
				h.append(int(i['main']['humidity']))
				ws.append(float(i['wind']['speed']))
				hours.append(str(i['dt_txt']).split(' ')[1])
				#self.data.create_text(coordinate,500, text=weather, width=100, fill="white")
				#self.data.create_window(285, 280, window=frm, anchor=CENTER)
				self.data.create_rectangle(coordinate,50, coordinate+170, 350, fill="black", outline="white")#create_rectangle(startx,starty,endx,endy, fill="blue", outline="red")
				self.data.create_text(coordinate+80,155, width=200, text=day_forecast, fill="white")
				icon_id=i['weather'][0]['icon']
				#print("Icon ID: "+str(icon_id))
				image_byt = urlopen("https://openweathermap.org/img/wn/"+icon_id+"@2x.png").read()
				load = PIL.Image.open(io.BytesIO(image_byt))
				image_final=load.resize((150,100), PIL.Image.ANTIALIAS)
				render = ImageTk.PhotoImage(image_final)
				img = Label(self.data, image=render, width=150, height=100, background="black")
				img.image = render
				img.place(x=coordinate+10, y=200)

				coordinate=coordinate+190
				#print(coordinate)
				#print(weather)
		#self.data.create_text(150,500, text=weather, width=200, fill="white")
		
		self.create_graph(hours, t, h, ws)
	def day_position(self, arg):
		day_number=0
		print(days_table)
		day_name=datetime.datetime.strptime(days_table[0], '%Y-%m-%d')
		day_name_txt= str(day_name.strftime("%A")).lower()
		if (arg=="tomorrow"):
			#day_selected=days_table[1]
			day_number=1
		elif(arg=="today"):
			day_number=0
		elif (arg!=""):
			day_index=days_in_week.index(day_name_txt)
			print(day_index)
			if (arg==days_in_week[day_index-1]):
				govor("I don't have Data for that day")
				#self.tk.destroy
			else:
				for day in days_in_week:
					print(day)
					if (day_name_txt==day):
						day_number=0
					elif(day==arg):
						day_number=day_number+1
						break
					elif (day_number==4):
						break
				
					else:
						day_number=day_number+1
		print(day_number)

		return days_table[int(day_number)]

	def create_graph(self,hours,t,h,ws):
		f = Figure(figsize=(8, 4), dpi=100,facecolor='black', edgecolor="black")
		temp = f.add_subplot(111,facecolor='black')
		temp.scatter(hours,t, color='red', marker="X", s=200)
		temp.scatter(hours,h, color='purple', marker="X", s=200)
		temp.scatter(hours,ws, color='blue', marker="X", s=200)
		#temp.spines['bottom'].set_color('red')
		#temp.xaxis.label.set_color('red')
		temp.xaxis.label.set_color('white')#set x axis value color to white        https://stackoverflow.com/questions/4761623/how-to-change-the-color-of-the-axis-ticks-and-labels-for-a-plot-in-matplotlib
		temp.tick_params(axis='x', colors='white')#set x axis  value color to white
		temp.yaxis.label.set_color('white')
		temp.tick_params(axis='y', colors='white')
		temp.set_title('WEATHER DATA',color="white")
		temp.set_xlabel('HOURS',color="white")
		temp.set_ylabel('VALUES',color="white")
		temp.plot(hours,t, color='red',linewidth=3,label="temp")
		temp.plot(hours,h,color='purple',linewidth=3,label="humidity")
		temp.plot(hours,ws,color='blue',linewidth=3,label="wind speed")
		temp.legend()
		f.tight_layout()

		canvas = FigureCanvasTkAgg(f,self.chart)
		canvas.get_tk_widget().pack(pady=100)

try:
	if (len(arguments)>1):
		print(len(arguments))
		if (arguments[1]=='today'):
			weather_GUI('')
		else:
			weather_GUI(arguments[1])
	else: 
		weather_GUI('today')
except EXCEPTION as e:
	print(e)

#weather_GUI(arguments[1])

