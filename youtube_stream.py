import vlc
import pafy
import sys
import json
import os
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from tkinter import ttk


arguments = list(sys.argv)

#Youtube video https://www.youtube.com/watch?v=qmQr0Uyi0Ls
class Video(Frame):
	async def main(self,parent, tabControl):
		Frame.__init__(self, parent)
		self.start_w_animation=14
		self.end_w_animation=1400
		self.start_h_animation=6.5
		self.end_h_animation=650
		self.videoframe=Frame(self, background="black", width=1400, height=700)
		self.videoframe.pack(fill=BOTH, expand=YES)
		pla_yt_tab = ttk.Frame(tabControl)
		tabControl.add(self.videoframe, text ="PLAYING YOUTUBE VIDEO")
		tabControl.select(len(tabControl.tabs())-1)
		self.video_name=Label(self.videoframe, fg="white", background="black")
		self.video_name.pack(side=TOP)
		self.video_play=Frame(self.videoframe, background="black", width=1400, height=650)
		self.video_play.pack(fill=BOTH, expand=YES)
		self.url= "https://www.youtube.com/watch?v=qmQr0Uyi0Ls"#self.get_URL(arguments[1])
		self.video=pafy.new(self.url) #pip3 install youtube-dl    
		self.best=self.video.getbest()
		self.streams=self.video.streams
		for s in self.streams:
			print(s.url)
		print(self.streams[0])
		self.playurl=self.best.url
		self.instance=vlc.Instance()
		self.player=self.instance.media_player_new()
		self.player.video_set_scale(0.6)
		self.player.set_xwindow(self.GetHandle())
		self.media=self.instance.media_new(self.playurl)
		self.media.get_mrl()
		self.player.set_media(self.media)
		self.player.play()
		


	def get_URL(self, num):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		get_yt_data=os.path.join(BASE_DIR, "youtube_data.json")
		with open(get_yt_data, "r") as f_r:
			yt_data=json.load(f_r)
		print(num)
		c=1
		selected_url=""
		for i in yt_data["videos"]:
			if (c == num):
				self.video_name.config(text=str(i["title"]))
				print(i)
				selected_url="https://www.youtube.com"+i["url_suffix"]
			c=c+1
		return selected_url
	def GetHandle(self):
		return self.video_play.winfo_id()
