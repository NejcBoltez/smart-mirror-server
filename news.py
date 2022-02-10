import json
import io
import requests
from urllib.request import urlopen
from PIL import ImageTk
import PIL.Image
import sys
import os
from working_with_files import Work_with_files
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from tkinter import ttk

class display_news:
	def __call__(args):
		try: 
			print("test:     "+args)
		except:
			print("")
	def main(self, displayed, tabControl):
		print("TESTING NEWS")
		Frame=Frame(tabControl, background="black")
		Frame.pack(fill=BOTH, expand=YES)
		newstab = ttk.Frame(tabControl)
		tabControl.add(Frame, text ="NEWS")
		tabControl.select(len(tabControl.tabs())-1)
		title=Label(Frame, font=("Helvetica", 60), fg="white", bg="black", text="NEWS",anchor="w")
		title.pack(padx=0, pady=25)
		n=0
		NewsList=[]
		News=Work_with_files.read_news_data()
		NewsList=News["articles"]
		w=350
		h=600
		NewsFrame=Frame(Frame, width=1920, height=1000, bg="black",padx=25,pady=50)
		NewsFrame.pack()
		NewsDir1=Canvas(NewsFrame, width=w, height=h, bg="black")
		NewsDir1.pack(side=LEFT, padx=10, pady=0) 
		NewsDir2=Canvas(NewsFrame, width=w, height=h, bg="black")
		NewsDir2.pack(side=LEFT, padx=10)
		NewsDir3=Canvas(NewsFrame, width=w, height=h, bg="black")
		NewsDir3.pack(side=LEFT, padx=10) 
		NewsDir4=Canvas(NewsFrame, width=w, height=h, bg="black")
		NewsDir4.pack(side=LEFT, padx=10)
		NewsDir5=Canvas(NewsFrame, width=w, height=h, bg="black")
		NewsDir5.pack(side=LEFT, padx=10)
		update()
		NewsD=1
		displayed=int(displayed)
		start= displayed-5
		end=displayed
		for i in NewsList:
			Nov = str(i["title"]).split("- ")
			if start<=n<end:
				
				news_title=str(i["title"]).split("-")
				image_url=str(i["urlToImage"])
				render=""
				try:
					if ("https" in image_url):
						image_byt = urlopen(image_url).read()
						load = PIL.Image.open(io.BytesIO(image_byt))
						image_final=load.resize((300,200), PIL.Image.BOX, reducing_gap=1)
						render = ImageTk.PhotoImage(image_final)
					elif ("//" in image_url):
						image_byt = urlopen("https:"+image_url).read()
						load = PIL.Image.open(io.BytesIO(image_byt))
						image_final=load.resize((300,200), PIL.Image.BOX, reducing_gap=1)
						render = ImageTk.PhotoImage(image_final)
					elif("dnevnik" in str(i["url"])):
						image_byt = urlopen("https://www.dnevnik.si"+image_url).read()
						load = PIL.Image.open(io.BytesIO(image_byt))
						image_final=load.resize((300,200), PIL.Image.ANTIALIAS)
						render = ImageTk.PhotoImage(image_final)
				except:
					load = PIL.Image.open("jaz_color.png")
					render = ImageTk.PhotoImage(load)
				
				if NewsD==1:
					NewsDir1.create_rectangle(1,1, w-1, h-1,fill="black")
					NewsDir1.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					NewsDir1.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(NewsDir1, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					NewsDir1.create_text(30,400,width=w-30, text=str(i["description"]), fill="white", font=("verdana", 12), anchor="w")
					

				elif NewsD==2:
					NewsDir2.create_rectangle(3,3, w-1, h-1,fill="black")
					NewsDir2.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					NewsDir2.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(NewsDir2, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					NewsDir2.create_text(30,400,width=w-30, text=str(i["description"]), fill="white", font=("verdana", 12), anchor="w")

				elif NewsD==3:
					NewsDir3.create_rectangle(3,3, w-1, h-1,fill="black")
					NewsDir3.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					NewsDir3.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(NewsDir3, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					NewsDir3.create_text(30,400,width=w-30, text=str(i["description"]).replace(" - ", "\n"), fill="white", font=("verdana", 12), anchor="w")

				elif NewsD==4:
					NewsDir4.create_rectangle(3,3, w-1, h-1,fill="black")
					NewsDir4.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					NewsDir4.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(NewsDir4, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					NewsDir4.create_text(30,400,width=w-30, text=str(i["description"]).replace(" - ", "\n"), fill="white", font=("verdana", 12), anchor="w")

				elif NewsD==5:
					NewsDir5.create_rectangle(3,3, w-1, h-1,fill="black")
					NewsDir5.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					NewsDir5.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(NewsDir5, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					NewsDir5.create_text(30,400,width=w-30, text=str(i["content"]), fill="white", font=("verdana", 12), anchor="w")
				NewsD=NewsD+1
				n=n+1
			else:
				n=n+1
