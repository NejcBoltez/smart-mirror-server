import sys
sys.path.append('../service')
sys.path.append('../repository')
#import streamlink
import vlc
import sys
import json
import os
import pafy
try:
	import tkinter as tk
	from tkinter import *
	from tkinter import ttk
except:
	import tk
	from tk import *
	from tk import ttk
import asyncio


arguments = list(sys.argv)

#Youtube video https://www.youtube.com/watch?v=qmQr0Uyi0Ls
class Video(Frame):
	def main(self,pos, tabControl):
		self.videoframe=Frame(tabControl, bg="black", width=1400, height=700)
		self.videoframe.pack(fill=BOTH, expand=YES)
		play_yt_tab = ttk.Frame(tabControl)
		tabControl.add(self.videoframe, text ="PLAYING YOUTUBE VIDEO")
		tabControl.select(len(tabControl.tabs())-1)
		self.update()
		self.video_name=Label(self.videoframe,font=("Helvetica", 40), fg="white", bg="black", width=1000)
		self.video_name.pack(fill=BOTH, side=TOP)
		self.video_play=Frame(self.videoframe, bg="black", width=1400, height=650)
		self.video_play.pack(fill=BOTH, expand=YES)
		video_URL=get_URL(self,pos)
		video= pafy.new(get_URL(self,pos)) #pip3 install youtube-dl  
		#video_streams=streamlink.streams(video_URL)
		lowest_resolution=1000000
		lowest_resolution_link=""
		streams=video.streams
		for s in streams:
			try:
				if (int(s.resolution.split("x")[0])<lowest_resolution or int(s.resolution.split("x")[0])<720):
					lowest_resolution=int(s.resolution.split("x")[0])
					lowest_resolution_link=s.url

			except Exception as e:
				continue
		self.instance=vlc.Instance()
		self.player=self.instance.media_player_new()
		
		self.player.set_xwindow(self.video_play.winfo_id())
		self.media=self.instance.media_new(lowest_resolution_link)
		self.media.get_mrl()
		self.player.set_media(self.media)
		self.player.set_rate(0.5)
		self.player.play()

def get_URL(self,num):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	get_yt_data=os.path.join(BASE_DIR, "json_data/youtube_data.json")
	with open(get_yt_data, "r") as f_r:
		yt_data=json.load(f_r)
	#print(num)
	c=0
	selected_url=""
	for i in yt_data["videos"]:
		if (int(c) == int(num)):
			self.video_name.config(text=str(i["title"]))
			selected_url="https://www.youtube.com"+i["url_suffix"]
		c=c+1
	return selected_url

class Window:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.geometry("1920x1000")
		#tk.attributes("-fullscreen", True)  
		#fullScreenState = False
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		tabControl = ttk.Notebook(self.Frame, height=10)
		tabControl.pack(fill=BOTH, expand=YES)
		#self.Canvas=Canvas(self.Frame)
		#Canvas.pack()
		#self.Canvas.grid(padx=300, pady=150, sticky=W)
		yt=Video.main(self.Frame, arguments[1], tabControl)
		#yt.pack()
#get_URL(arguments[1])
#root=Window()
#root.tk.mainloop()
