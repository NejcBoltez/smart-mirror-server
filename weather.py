import datetime
from PIL import ImageTk
from PIL import ImageTk
import PIL.Image
import time
import os
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from working_with_files import Work_with_files
import sys
from tkinter import ttk

class weather_GUI:
	def __enter__(self):
		return self
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def main(self,command, tabControl):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, 'Weather_widgets')
		
		self.Frame=Frame(self, background="black", width=1920, height=1080)
		self.Frame.pack(fill=BOTH, expand=YES, anchor='w')
		self.days_table=[]
		weather_tab = ttk.Frame(tabControl)
		tabControl.add(self.Frame, text ='WEATHER FORECAST')
		tabControl.select(len(tabControl.tabs())-1)
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
		
		read=Work_with_files.read_weather_data()
		read_day=Work_with_files.read_weather_main()
		weather=''
		t=[]
		t_max=[]
		t_min=[]
		h=[]
		ws=[]
		hours=[]
		icons=[]
		coordinate=50
		coordinatey=100
		for d in read['list']:
			if (str(d['dt_txt']).split(' ')[0] not in self.days_table):
				self.days_table.append(str(d['dt_txt']).split(' ')[0])
		
		day_selected=day_position(self,command)

		for f in self.days_table:
			day_name=datetime.datetime.strptime(f, '%Y-%m-%d')
			b_string= str(day_name.strftime("%A")) + '\n' + str(f)
			d_n=str(day_name.strftime("%A")) 
			print(f)
			print(time.strftime('%A')+" test: " + d_n.lower())
			if (f==day_selected):#str(day_name.strftime("%A")).lower()==command):
				self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="silver", fg="black")
				self.daysb.pack()
			else:
				self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="black", fg="white")
				self.daysb.pack()
		for i in read['list']:
			date=str(i['dt_txt']).split(' ')
			if (day_selected in date):
				print(date)
				temp=str(i['main']['temp'])
				humidity=str(i['main']['humidity'])
				temp_min=str(i['main']['temp_min'])
				temp_max=str(i['main']['temp_max'])
				hour_wind_speed= str(float(i['wind']['speed']))
				day_forecast=str(str(i['dt_txt']).split(' ')[1]) + '\n' + "Temp: " + temp +'\n' +"Humidity: " +  humidity + '\n' +"Temp_min: " +  temp_min + '\n' +"Temp_max: " +  temp_max + '\n' +"Wind speed: " + hour_wind_speed + '\n\n'
				
				t.append(float(temp))
				t_max.append(float(temp_max))
				t_min.append(float(temp_min))
				h.append(float(humidity))
				ws.append(float(hour_wind_speed))
				hours.append(str(i['dt_txt']).split(' ')[1])
				self.data.create_rectangle(coordinate,10, coordinate+170, 350, fill="black", outline="white")										#create_rectangle(startx,starty,endx,endy, fill="blue", outline="red")
				self.data.create_text(coordinate+80,90, width=200, text=day_forecast, fill="white", font=('Helvetica', 12))
				icon_id=i['weather'][0]['icon']
				icons.append(icon_id)
				BASE_DIR= os.path.dirname(os.path.abspath(__file__))
				image_dir=os.path.join(BASE_DIR, "Weather_widgets")
				image_byt = str(image_dir+os.path.sep+icon_id+".PNG")
				load = PIL.Image.open(image_byt)
				image_final=load.resize((150,100), PIL.Image.ANTIALIAS)
				render = ImageTk.PhotoImage(image_final)
				img = Label(self.data, image=render, width=150, height=100, background="black")
				img.image = render
				img.place(x=coordinate+10, y=200)
				coordinate=coordinate+190
		
		
		main_icon=most_common_weather(icons)
		print(image_dir+'/'+main_icon+'.png')
		image_byt = str(image_dir+'/'+main_icon+'.PNG')# urlopen("https://openweathermap.org/img/wn/"+main_icon+"@2x.png").read()
		load = PIL.Image.open(image_byt)
		image_final=load.resize((300,200), PIL.Image.ANTIALIAS)
		render = ImageTk.PhotoImage(image_final)
		overall_temp="Temp: " + average_weather(t)
		#str(read_day['main']['temp'])
		overall_humidity="Humidity: " + average_weather(h)#str(read_day['main']['humidity'])
		overall_temp_min="Temp_min: " + average_weather(t_min)#str(read_day['main']['temp_min'])
		overall_temp_max="Temp_max: " + average_weather(t_max)#str(read_day['main']['temp_max'])
		wind_speed="Wind speed: " + average_weather(ws)#str(float(read_day['wind']['speed']))
		overall_forecast=overall_temp +'\n' + overall_humidity + '\n' + overall_temp_min + '\n' + overall_temp_max + '\n' + wind_speed + '\n\n'
		img = Label(self.logo, image=render, width=300, height=200, background="black")
		img.image = render
		img.place(x=10, y=50)
		self.logo.create_text(150,350, width=300, text=overall_forecast, fill="white", font=('Helvetica', 20))
		create_graph(self, hours, t, h, ws)
def most_common_weather(lst):
	return str(max(set(lst), key=lst.count))
def average_weather(lst):
	count_e=0
	for i in lst:
		print(i)
		count_e=count_e+float(i)
	return str('{0:.2f}'.format(count_e/len(lst)))
def day_position(self, arg):
	day_number=0
	day_name=datetime.datetime.strptime(self.days_table[0], '%Y-%m-%d')
	day_name_txt= str(day_name.strftime("%A")).lower()
	days_in_week=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
	#next_day=datetime.

	if ("tomorrow" in arg):
		day_number=1
	elif("today" in arg):
		day_number=0
	elif (arg!=""):
		for d in self.days_table:
			da = datetime.datetime.strptime(d, '%Y-%m-%d')
			day=da.strftime("%A").lower()
			print(day)
			if (day_name_txt==day):
				day_number=0
			elif(day==arg):
				day_number=day_number+1
				break
			else:
				day_number=day_number+1
	return self.days_table[int(day_number)]

def create_graph(self,hours,t,h,ws):
	self.f = Figure(figsize=(8, 4), facecolor='black', edgecolor="black")
	self.temp = self.f.add_subplot(111,facecolor='black')
	#self.temp.spines['left'].set_color('white') #set x axis value color to white
	#self.temp.spines['bottom'].set_color('white')#set y axis  value color to white        		https://stackoverflow.com/questions/4761623/how-to-change-the-color-of-the-axis-ticks-and-labels-for-a-plot-in-matplotlib
	self.temp.tick_params(axis='x', colors='white')
	self.temp.tick_params(axis='y', colors='white')
	self.temp.set_title('WEATHER DATA',color="white")
	self.temp.set_xlabel('HOURS',color="white")
	self.temp.set_ylabel('VALUES',color="white")
	self.temp.plot(hours,t, 'rX')
	self.temp.plot(hours,h, 'yX')
	self.temp.plot(hours,ws, 'bX')
	self.temp.plot(hours,t, color='red',linewidth=3,label="Temperature")
	self.temp.plot(hours,h,color='yellow',linewidth=3,label="Humidity")
	self.temp.plot(hours,ws,color='blue',linewidth=3,label="Wind speed")
	self.temp.legend(bbox_to_anchor=(1, 1),loc='upper left')
	self.f.tight_layout()

	self.canvas = FigureCanvasTkAgg(self.f,self.chart)
	self.canvas.get_tk_widget().pack(pady=100)
class Window:
	def __init__(self, user):
		self.tk=tk.Tk()
		self.tk.configure(background="black")
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		tabControl = ttk.Notebook(self.Frame, height=100)
		tabControl.pack(expand = 1, fill ="both")
		self.recognize(user, tabControl)
		self.tk.update()
		self.tk.mainloop()
	def recognize(self, user, tabControl):
		cam=weather_GUI.main(self.Frame, user, tabControl)
		#cam.pack()


#arguments = list(sys.argv)	
#win=Window(arguments[1])