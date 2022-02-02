import sys
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
#Youtube video https://www.youtube.com/watch?v=qmQr0Uyi0Ls

from youtube_search import YoutubeSearch
import json
import io
from PIL import ImageTk
import PIL.Image
from urllib.request import urlopen
from working_with_files import Work_with_files
from tkinter import ttk

def get_yt_data(search_for):
	results = YoutubeSearch(str(search_for).replace('_', ' '), max_results=20).to_json()
	get_results=json.loads(results)
	Work_with_files.save_youtube_data(get_results)
	print(get_results)
	return get_results

class yt_search(Frame):
	async def main(self, search_command, tabControl):
		#Frame.__init__(self, parent)
		self.search_frame=Frame(self, width=1920, height=1080, bg="black", bd=0, highlightthickness=0)
		self.search_frame.pack(fill=BOTH, expand=YES)

		yt_tab = ttk.Frame(tabControl)
		tabControl.add(self.search_frame, text ='SEARCH YOUTUBE FOR ' + search_command.upper())
		tabControl.select(len(tabControl.tabs())-1)

		self.search_text=Label(self.search_frame, text=str(search_command).replace('_', ' ').upper(), font=('verdana', 30, 'bold'), fg="white", bg="black", bd=0, highlightthickness=0, anchor="center")
		self.search_text.pack(side=TOP)
		self.search_frame_top=Canvas(self.search_frame,width=1700, height=400, bg="black", bd=0, highlightthickness=0)
		self.search_frame_top.pack(side=TOP, fill=BOTH, expand= TRUE)
		self.search_frame_bottom=Canvas(self.search_frame, width=1700, height=400, bg="black", bd=0, highlightthickness=0)
		self.search_frame_bottom.pack(side=BOTTOM, fill=BOTH, expand= TRUE)
		self.get_json=get_yt_data(search_command)
		self.yt=self.get_json['videos']
		coordinate=70
		c=0
		for i in self.yt:
			image_byt = urlopen(i['thumbnails'][0]).read()
			load = PIL.Image.open(io.BytesIO(image_byt))
			image_final=load.resize((250,200), PIL.Image.ANTIALIAS)
			render = ImageTk.PhotoImage(image_final)
			if (c<5):
				self.search_frame_top.create_rectangle(coordinate,10, coordinate+300, 350, fill="black", outline="white")
				try:
					self.search_frame_top.create_text(coordinate+150,60, width=230, text=str(i['title']), fill="white", font=('verdana', 12, 'bold'))
					img = Label(self.search_frame_top, image=render, width=250, height=200)
					img.image = render
					img.place(x=coordinate+20, y=120)
					coordinate=coordinate+320
					c=c+1
				except:
					continue
			elif (c==10):
				break
			else:
				if (c==5):
					coordinate=70
				
				try:
					self.search_frame_bottom.create_rectangle(coordinate,10, coordinate+300, 350, fill="black", outline="white")
					self.search_frame_bottom.create_text(coordinate+150,60, width=230, text=str(i['title']), fill="white", font=('verdana', 12, 'bold'))
					img = Label(self.search_frame_bottom, image=render, width=250, height=200)
					img.image = render
					img.place(x=coordinate+20, y=120)
					coordinate=coordinate+320
					c=c+1
				except:
					c=c-1
					continue

'''class Window:
	def __init__(self):
		self.tk=tk.Tk()
		#self.tk.geometry("1920x1000")
		self.tk.attributes('-fullscreen', True)  
		self.fullScreenState = False
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.Canvas=Canvas(self.Frame)
		self.Canvas.grid(padx=150, pady=150)
		self.yt=yt_search(self.Canvas)
		self.yt.pack()

root=Window()
root.tk.mainloop()'''

