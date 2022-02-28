from datetime import datetime, timedelta, timezone
import urllib
import m3u8
import streamlink
import time
import cv2 #openCV
import vlc
import sys
import json
import os
import pafy
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from tkinter import ttk
import asyncio


arguments = list(sys.argv)

#Youtube video https://www.youtube.com/watch?v=qmQr0Uyi0Ls
class Video(Frame):
	def main(self,pos, tabControl):
		self.videoframe=Frame(tabControl, background="black", width=1400, height=700)
		self.videoframe.pack(fill=BOTH, expand=YES)
		play_yt_tab = ttk.Frame(tabControl)
		tabControl.add(self.videoframe, text ="PLAYING YOUTUBE VIDEO")
		tabControl.select(len(tabControl.tabs())-1)
		self.update()
		self.video_name=Label(self.videoframe, fg="white", background="black")
		self.video_name.pack(side=TOP)
		self.video_play=Frame(self.videoframe, background="black", width=1400, height=650)
		self.video_play.pack(fill=BOTH, expand=YES)
		video_URL=get_URL(self,pos)
		video= pafy.new(get_URL(self,pos)) #pip3 install youtube-dl  
		video_streams=streamlink.streams(video_URL)
		lowest_resolution=1000000
		lowest_resolution_link=''
		streams=video.streams
		for s in streams:
			try:
				if (int(s.resolution.split('x')[0])<lowest_resolution or int(s.resolution.split('x')[0])<720):
					lowest_resolution=int(s.resolution.split('x')[0])
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
	print(num)
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
		#tk.geometry("1500x1000")
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
