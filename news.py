import json
import io
import requests
from urllib.request import urlopen
from PIL import ImageTk
import PIL.Image
import sys
import os
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

arguments = list(sys.argv)


displayed=0

def get_api_keys():
	read_api=""
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	api_keys_dir=os.path.join(BASE_DIR, "../api_keys.json")
	with open(api_keys_dir, "r") as f_api:
		read_api=json.load(f_api)
	return read_api

class display_news:
	def __call__(args):
		try: 
			print("test:     "+args)
		except:
			print("")
	def __init__(self, displayed):
		self.tk=tk.Tk()
		self.tk.configure(background="black")
		self.tk.title("Pozdravljeni")
		#self.tk.geometry("1920x1000")
		self.tk.attributes('-fullscreen', True)  
		self.fullScreenState = False
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.title=Label(self.Frame, font=("Helvetica", 60), fg="white", bg="black", text="NEWS",anchor="w")
		self.title.pack(padx=0, pady=25)
		self.n=0
		self.NewsList=[]
		self.Novice=""
		self.News=""
		self.IzborNovic=""
		self.get_api=get_api_keys()
		self.APIK=self.get_api["news_api"]
		self.URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+self.APIK
		self.News=requests.get(self.URLnews)
		self.Novice=self.News.json()
		self.NewsList=self.Novice["articles"]
		self.w=350
		self.h=600
		self.NewsFrame=Frame(self.Frame, width=1920, height=1000, bg="black",padx=25,pady=50)
		self.NewsFrame.pack()
		self.NewsDir1=Canvas(self.NewsFrame, width=self.w, height=self.h, bg="black")
		self.NewsDir1.pack(side=LEFT, padx=10, pady=0) 
		self.NewsDir2=Canvas(self.NewsFrame, width=self.w, height=self.h, bg="black")
		self.NewsDir2.pack(side=LEFT, padx=10)
		self.NewsDir3=Canvas(self.NewsFrame, width=self.w, height=self.h, bg="black")
		self.NewsDir3.pack(side=LEFT, padx=10) 
		self.NewsDir4=Canvas(self.NewsFrame, width=self.w, height=self.h, bg="black")
		self.NewsDir4.pack(side=LEFT, padx=10)
		self.NewsDir5=Canvas(self.NewsFrame, width=self.w, height=self.h, bg="black")
		self.NewsDir5.pack(side=LEFT, padx=10)

		self.NewsD=1
		self.displayed=int(displayed)
		self.start= self.displayed-5
		self.end=self.displayed
		for i in self.NewsList:
			Nov = str(i["title"]).split("- ")
			if self.start<=self.n<self.end:
				
				self.news_title=str(i["title"]).split("-")
				self.image_url=str(i["urlToImage"])
				self.render=""
				try:
					if ("https" in self.image_url):
						self.image_byt = urlopen(self.image_url).read()
						self.load = PIL.Image.open(io.BytesIO(self.image_byt))
						self.image_final=self.load.resize((300,200), PIL.Image.BOX, reducing_gap=1)
						self.render = ImageTk.PhotoImage(self.image_final)
					elif ("//" in self.image_url):
						self.image_byt = urlopen("https:"+self.image_url).read()
						self.load = PIL.Image.open(io.BytesIO(self.image_byt))
						self.image_final=self.load.resize((300,200), PIL.Image.BOX, reducing_gap=1)
						self.render = ImageTk.PhotoImage(self.image_final)
					elif("dnevnik" in str(i["url"])):
						self.image_byt = urlopen("https://www.dnevnik.si"+self.image_url).read()
						self.load = PIL.Image.open(io.BytesIO(self.image_byt))
						self.image_final=self.load.resize((300,200), PIL.Image.ANTIALIAS)
						self.render = ImageTk.PhotoImage(self.image_final)
				except:
					self.load = PIL.Image.open("jaz_color.png")
					self.render = ImageTk.PhotoImage(self.load)
				
				if self.NewsD==1:
					self.NewsDir1.create_rectangle(1,1, self.w-1, self.h-1,fill="black")
					self.NewsDir1.create_text(20, 50, width=self.w-20, text=self.news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir1.create_text(20, 90, width=self.w-20, text=self.news_title[len(self.news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					self.img = Label(self.NewsDir1, image=self.render, width=310, height=200)
					self.img.image = self.render
					self.img.place(x=20, y=110)
					self.NewsDir1.create_text(30,400,width=self.w-30, text=str(i["description"]), fill="white", font=("verdana", 12), anchor="w")
					

				elif self.NewsD==2:
					self.NewsDir2.create_rectangle(3,3, self.w-1, self.h-1,fill="black")
					self.NewsDir2.create_text(20, 50, width=self.w-20, text=self.news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir2.create_text(20, 90, width=self.w-20, text=self.news_title[len(self.news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					self.img = Label(self.NewsDir2, image=self.render, width=310, height=200)
					self.img.image = self.render
					self.img.place(x=20, y=110)
					self.NewsDir2.create_text(30,400,width=self.w-30, text=str(i["description"]), fill="white", font=("verdana", 12), anchor="w")

				elif self.NewsD==3:
					self.NewsDir3.create_rectangle(3,3, self.w-1, self.h-1,fill="black")
					self.NewsDir3.create_text(20, 50, width=self.w-20, text=self.news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir3.create_text(20, 90, width=self.w-20, text=self.news_title[len(self.news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					self.img = Label(self.NewsDir3, image=self.render, width=310, height=200)
					self.img.image = self.render
					self.img.place(x=20, y=110)
					self.NewsDir3.create_text(30,400,width=self.w-30, text=str(i["description"]).replace(" - ", "\n"), fill="white", font=("verdana", 12), anchor="w")

				elif self.NewsD==4:
					self.NewsDir4.create_rectangle(3,3, self.w-1, self.h-1,fill="black")
					self.NewsDir4.create_text(20, 50, width=self.w-20, text=self.news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir4.create_text(20, 90, width=self.w-20, text=self.news_title[len(self.news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					self.img = Label(self.NewsDir4, image=self.render, width=310, height=200)
					self.img.image = self.render
					self.img.place(x=20, y=110)
					self.NewsDir4.create_text(30,400,width=self.w-30, text=str(i["description"]).replace(" - ", "\n"), fill="white", font=("verdana", 12), anchor="w")

				elif self.NewsD==5:
					self.NewsDir5.create_rectangle(3,3, self.w-1, self.h-1,fill="black")
					self.NewsDir5.create_text(20, 50, width=self.w-20, text=self.news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir5.create_text(20, 90, width=self.w-20, text=self.news_title[len(self.news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					self.img = Label(self.NewsDir5, image=self.render, width=310, height=200)
					self.img.image = self.render
					self.img.place(x=20, y=110)
					self.NewsDir5.create_text(30,400,width=self.w-30, text=str(i["content"]), fill="white", font=("verdana", 12), anchor="w")
				self.NewsD=self.NewsD+1
				self.n=self.n+1
			else:
				self.n=self.n+1
		self.tk.mainloop()

if (len(arguments)==2):
    displayed=int(arguments[1])
else:
	displayed=5		

try:
	display_news(displayed)
except Exception as e:
	print(e)
