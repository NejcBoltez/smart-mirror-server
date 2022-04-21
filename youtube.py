import tkinter as tk
from tkinter import *
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
	results = YoutubeSearch(str(search_for).replace("_", " "), max_results=20).to_json()
	get_results=json.loads(results)
	Work_with_files.save_youtube_data(get_results)
	#print(get_results)
	return get_results

class yt_search(Frame):
	def main(self, search_command, tabControl):
		#Frame.__init__(self, parent)
		search_frame=Frame(self, bg="black", bd=0, highlightthickness=0)
		search_frame.pack(fill=BOTH, expand=YES)

		yt_tab = ttk.Frame(tabControl)
		tabControl.add(search_frame, text ="SEARCH YOUTUBE FOR " + search_command.upper())
		tabControl.select(len(tabControl.tabs())-1)
		self.update()
		search_text=Label(search_frame, text=str(search_command).replace("_", " ").upper(), font=("verdana", 30, "bold"), fg="white", bg="black", bd=0, highlightthickness=0, anchor="center")
		search_text.pack(side=TOP)
		search_frame_top=Canvas(search_frame, bg="black", bd=0, highlightthickness=0)
		search_frame_top.pack(side=TOP, fill=BOTH, expand= TRUE)
		search_frame_bottom=Canvas(search_frame,  bg="black", bd=0, highlightthickness=0)
		search_frame_bottom.pack(side=BOTTOM, fill=BOTH, expand= TRUE)
		get_json=get_yt_data(search_command)
		yt=get_json["videos"]
		coordinate=70
		c=0
		for i in yt:
			image_byt = urlopen(i["thumbnails"][0]).read()
			load = PIL.Image.open(io.BytesIO(image_byt))
			image_final=load.resize((250,200), PIL.Image.ANTIALIAS)
			render = ImageTk.PhotoImage(image_final)
			if (c<5):
				search_frame_top.create_rectangle(coordinate,10, coordinate+300, 350, fill="black", outline="white")
				try:
					search_frame_top.create_text(coordinate+150,60, width=230, text=str(i["title"]), fill="white", font=("verdana", 12, "bold"))
					img = Label(search_frame_top, image=render, width=250, height=200)
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
					search_frame_bottom.create_rectangle(coordinate,10, coordinate+300, 350, fill="black", outline="white")
					search_frame_bottom.create_text(coordinate+150,60, width=230, text=str(i["title"]), fill="white", font=("verdana", 12, "bold"))
					img = Label(search_frame_bottom, image=render, width=250, height=200)
					img.image = render
					img.place(x=coordinate+20, y=120)
					coordinate=coordinate+320
					c=c+1
				except:
					c=c-1
					continue

