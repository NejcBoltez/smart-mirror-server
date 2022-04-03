import io
from urllib.request import urlopen
from PIL import ImageTk
import PIL.Image
from working_with_files import Work_with_files
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from tkinter import ttk

import sys

class display_news:
	def __call__(args):
		try: 
			print("test:     "+args)
		except:
			print("")
	def main(self, displayed, tabControl):
		print("TESTING NEWS")
		self.Frame=Frame(tabControl, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		newstab = ttk.Frame(tabControl)
		tabControl.add(self.Frame, text ="NEWS")
		tabControl.select(len(tabControl.tabs())-1)
		title=Label(self.Frame, font=("Helvetica", 60), fg="white", bg="black", text="NEWS",anchor="w")
		title.pack(padx=0, pady=25)
		n=0
		NewsList=[]
		News=Work_with_files.read_news_data()
		NewsList=News["articles"]
		w=350
		h=600
		self.NewsFrame=Frame(self.Frame, width=1920, height=1000, bg="black",padx=25,pady=50)
		self.NewsFrame.pack()
		self.NewsDir1=Canvas(self.NewsFrame, width=w, height=h, bg="black")
		self.NewsDir1.pack(side=LEFT, padx=10, pady=0) 
		self.NewsDir2=Canvas(self.NewsFrame, width=w, height=h, bg="black")
		self.NewsDir2.pack(side=LEFT, padx=10)
		self.NewsDir3=Canvas(self.NewsFrame, width=w, height=h, bg="black")
		self.NewsDir3.pack(side=LEFT, padx=10) 
		self.NewsDir4=Canvas(self.NewsFrame, width=w, height=h, bg="black")
		self.NewsDir4.pack(side=LEFT, padx=10)
		self.NewsDir5=Canvas(self.NewsFrame, width=w, height=h, bg="black")
		self.NewsDir5.pack(side=LEFT, padx=10)
		self.update()
		NewsD=1
		displayed=int(displayed)
		start= displayed-5
		end=displayed
		print("START: " + str(start))
		print("END: " + str(end))
		for i in NewsList:
			Nov = str(i["title"]).split("- ")
			news_source=i["source"]["name"]
			#print(i)
			print(news_source)
			if (news_source.lower() in ("24ur.com", "rtvslo.si", "siol.net", "racunalniske-novice.com") and start<=n<end):
				print(NewsD)
				print(n)
				news_title=str(i["title"]).split("-")
				image_url=str(i["urlToImage"])
				render=""
				try:
					if ("http" in image_url):
						image_byt = urlopen(image_url).read()
						load = PIL.Image.open(io.BytesIO(image_byt))
						image_final=load.resize((300,200), PIL.Image.BOX, reducing_gap=1)
						render = ImageTk.PhotoImage(image_final)
					elif ("//" in image_url):
						try:
							image_byt = urlopen("https:"+image_url).read()
							load = PIL.Image.open(io.BytesIO(image_byt))
							image_final=load.resize((300,200), PIL.Image.BOX, reducing_gap=1)
							render = ImageTk.PhotoImage(image_final)
						except:
							image_byt = urlopen("http:"+image_url).read()
							load = PIL.Image.open(io.BytesIO(image_byt))
							image_final=load.resize((300,200), PIL.Image.BOX, reducing_gap=1)
							render = ImageTk.PhotoImage(image_final)
					elif("dnevnik" in str(i["url"])):
						image_byt = urlopen("https://www.dnevnik.si"+image_url).read()
						load = PIL.Image.open(io.BytesIO(image_byt))
						image_final=load.resize((300,200), PIL.Image.ANTIALIAS)
						render = ImageTk.PhotoImage(image_final)
				except:
					load = PIL.Image.open("no_image.PNG")
					render = ImageTk.PhotoImage(load)
				
				if NewsD==1:
					self.NewsDir1.create_rectangle(1,1, w-1, h-1,fill="black")
					self.NewsDir1.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir1.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(self.NewsDir1, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					self.NewsDir1.create_text(30,400,width=w-30, text=str(i["description"]), fill="white", font=("verdana", 12), anchor="w")
					

				elif NewsD==2:
					self.NewsDir2.create_rectangle(3,3, w-1, h-1,fill="black")
					self.NewsDir2.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir2.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(self.NewsDir2, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					self.NewsDir2.create_text(30,400,width=w-30, text=str(i["description"]), fill="white", font=("verdana", 12), anchor="w")

				elif NewsD==3:
					self.NewsDir3.create_rectangle(3,3, w-1, h-1,fill="black")
					self.NewsDir3.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir3.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(self.NewsDir3, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					self.NewsDir3.create_text(30,400,width=w-30, text=str(i["description"]).replace(" - ", "\n"), fill="white", font=("verdana", 12), anchor="w")

				elif NewsD==4:
					self.NewsDir4.create_rectangle(3,3, w-1, h-1,fill="black")
					self.NewsDir4.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir4.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(self.NewsDir4, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					self.NewsDir4.create_text(30,400,width=w-30, text=str(i["description"]).replace(" - ", "\n"), fill="white", font=("verdana", 12), anchor="w")

				elif NewsD==5:
					self.NewsDir5.create_rectangle(3,3, w-1, h-1,fill="black")
					self.NewsDir5.create_text(20, 50, width=w-20, text=news_title[0],fill="white", font=("verdana", 12, "bold"), anchor="w")
					self.NewsDir5.create_text(20, 90, width=w-20, text=news_title[len(news_title) - 1],fill="white", font=("verdana", 12), anchor="w")
					img = Label(self.NewsDir5, image=render, width=310, height=200)
					img.image = render
					img.place(x=20, y=110)
					self.NewsDir5.create_text(30,400,width=w-30, text=str(i["content"]), fill="white", font=("verdana", 12), anchor="w")
				NewsD=NewsD+1
				n=n+1
			else:
				if (NewsD==1 and news_source.lower() in ("24ur.com", "rtvslo.si", "siol.net", "racunalniske-novice.com")):
					n=n+1
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
		cam=display_news.main(self.Frame, user, tabControl)
		#cam.pack()


#arguments = list(sys.argv)	
#win=Window(arguments[1])