import json
import requests
import datetime
from PIL import ImageTk, Image
import base64
from urllib.request import urlopen
from PIL import ImageTk
import PIL.Image
import io
try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
import sys
import pyttsx3 as pyttsx



#from tkinter.ttk import *

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
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



speech_engine = pyttsx.init()
def govor(besedilo):
    speech_engine.say(besedilo)
    speech_engine.runAndWait()


class display_weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        global arguments
        Frame.__init__(self, parent)
        self.Frame=Frame(self, background="black", width=1920, height=1080)
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
        City = "Novo mesto"
        Country = "SI"
        APIK = "10fe78b8435d01d64ad7203ac4b87fe8"
        URL = "https://api.openweathermap.org/data/2.5/forecast?q="+City+","+Country+"&appid="+APIK
        #https://api.openweathermap.org/data/2.5/forecast?q=Novo mesto,SI&appid=10fe78b8435d01d64ad7203ac4b87fe8
        main_URL="https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK
        r = requests.get(URL)
        r_main=requests.get(main_URL)
        preberi = r.json()
        preberi_day=r_main.json()
        main_icon=preberi_day['weather'][0]['icon']
        days_string=""
        weather=''
        t=[]
        hours=[]
        coordinate=50
        coordinatey=100
        #print(str(preberi['list']['main']))
        image_byt = urlopen("https://openweathermap.org/img/wn/"+main_icon+"@2x.png").read()
        load = PIL.Image.open(io.BytesIO(image_byt))
        image_final=load.resize((300,200), PIL.Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image_final)
        img = Label(self.logo, image=render, width=300, height=200, background="black")
        img.image = render
        img.place(x=10, y=150)

        for d in preberi['list']:
            #print (d['dt_txt']) 
            if (str(d['dt_txt']).split(' ')[0] not in days_table):
                days_table.append(str(d['dt_txt']).split(' ')[0])
            #break
        #print(days_table)
        for f in days_table:
            day_name=datetime.datetime.strptime(f, '%Y-%m-%d')
            b_string= str(day_name.strftime("%A")) + '\n' + str(f)
            d_n=str(day_name.strftime("%A")) 
            print("test: " + d_n.lower())
            if (str(day_name.strftime("%A")).lower()==arguments[1]):
                print("It is working")
                self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="silver", fg="black")
                self.daysb.pack()
            else:
                self.daysb=Button(self.days, text=b_string, width=15, height=7, bg="black", fg="white")
                self.daysb.pack()
            #print(f.strftime("%A"))
        if (len(arguments)==2):
            day_selected=self.day_position(arguments[1])#days_table[1]
            #days_table.append(str(d['dt_txt']).split(' ')[0])
        else:
             day_selected=days_table[0]
        for i in preberi['list']:
            date=str(i['dt_txt']).split(' ')[0]
            if (date == day_selected):
                temp="Temp: " + str(i['main']['temp'])
                humidity="Humidity: " + str(i['main']['humidity'])
                temp_min="Temp_min: " + str(i['main']['temp_min'])
                temp_max="Temp_max: " + str(i['main']['temp_max'])
                day_forecast=str(i['dt_txt']) + '\n' + temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max +'\n\n'
                weather=weather + str(i['dt_txt']) + '\n' + temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max +'\n\n' #+'\n' + days_table
                t.append(str(i['main']['temp']))
                hours.append(str(i['dt_txt']).split(' ')[1])
                #self.data.create_text(coordinate,500, text=weather, width=100, fill="white")
                #self.data.create_window(285, 280, window=frm, anchor=CENTER)
                self.data.create_rectangle(coordinate,50, coordinate+170, 350, fill="black", outline="white")#create_rectangle(startx,starty,endx,endy, fill="blue", outline="red")
                self.data.create_text(coordinate+80,155, width=200, text=day_forecast, fill="white")
                icon_id=i['weather'][0]['icon']
                print("Icon ID: "+str(icon_id))
                image_byt = urlopen("https://openweathermap.org/img/wn/"+icon_id+"@2x.png").read()
                load = PIL.Image.open(io.BytesIO(image_byt))
                image_final=load.resize((150,100), PIL.Image.ANTIALIAS)
                render = ImageTk.PhotoImage(image_final)
                img = Label(self.data, image=render, width=150, height=100, background="black")
                img.image = render
                img.place(x=coordinate+10, y=200)

                coordinate=coordinate+190
                print(coordinate)
                #print(weather)
        #self.data.create_text(150,500, text=weather, width=200, fill="white")
        
        self.create_graph(hours, t)
    def day_position(self, arg):
        day_number=0
        print(days_table)
        day_name=datetime.datetime.strptime(days_table[0], '%Y-%m-%d')
        day_name_txt= str(day_name.strftime("%A")).lower()
        if (arg=="tomorrow"):
            #day_selected=days_table[1]
            day_number=1
        elif(arg==""):
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

    def create_graph(self,x,y):
        #self.graph=self.forecast.create_window(1000,1000)
        
        figure = Figure(figsize=(15, 7), dpi=70, facecolor="black") # https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.figure.html
        plot = figure.add_subplot(1, 1, 1)
        chart = FigureCanvasTkAgg(figure, self.chart)#, width=1400, height=300)
        chart.get_tk_widget().grid(row=0, column=00, padx=100, pady=50)#, width=1400, height=300)
        #plot.plot(0.5, 0.3, color="#C41E3A", marker="o", linestyle="")


        #x = [ 0.1, 0.2, 0.3 ]
        #y = [ -0.1, -0.2, -0.3 ]
        plt.plot(y)
        #plt.plot([1,2,3,4])
        #plt.show()


class Weather:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.configure(background='black')
        self.tk.title("Pozdravljeni")
        self.tk.geometry("1920x1080")
        self.Frame=Frame(self.tk, background='black')
        self.Frame.pack(fill=BOTH, expand=YES)
        #self.video=Canvas(self.Frame, background="black", width="600", height="400")
        #self.video.pack()
        self.news_label=display_weather(self.Frame)
        self.news_label.pack()
        #get_news(self)
        

window=Weather()
window.tk.mainloop()

