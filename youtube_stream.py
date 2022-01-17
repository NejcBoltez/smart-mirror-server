import vlc
import pafy
import sys
from youtube_search import YoutubeSearch
import json
import os
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *


arguments = list(sys.argv)

#Youtube video https://www.youtube.com/watch?v=qmQr0Uyi0Ls
class Video(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent)
		self.start_w_animation=14
		self.end_w_animation=1400
		self.start_h_animation=6.5
		self.end_h_animation=650
		self.videoframe=Frame(self, background="black", width=1400, height=700)
		self.videoframe.pack(fill=BOTH, expand=YES)
		self.video_name=Label(self.videoframe, fg="white", background="black")
		self.video_name.pack(side=TOP)
		self.video_play=Frame(self.videoframe, background="black", width=1400, height=650)
		self.video_play.pack(fill=BOTH, expand=YES)
		self.url= self.get_URL()
		self.video=pafy.new(self.url) #pip3 install youtube-dl    
		self.best=self.video.getbest()
		self.playurl=self.best.url
		self.instance=vlc.Instance()
		self.player=self.instance.media_player_new()
		self.player.set_xwindow(self.GetHandle())
		self.media=self.instance.media_new(self.playurl)
		self.media.get_mrl()
		self.player.set_media(self.media)
		self.player.play()


	def get_URL(self):
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		get_yt_data=os.path.join(BASE_DIR, "youtube_data.json")
		with open(get_yt_data, "r") as f_r:
			yt_data=json.load(f_r)#.read()
		print(yt_data)
		c=1
		selected_url=''
		for i in yt_data['videos']:
			if (c == int(arguments[2])):
				self.video_name.config(text=str(i['title']))
				selected_url='https://www.youtube.com'+i['url_suffix']
			c=c+1
		return selected_url
	def GetHandle(self):
		return self.video_play.winfo_id()
class Window:
	def __init__(self):
		self.tk=tk.Tk()
		#self.tk.geometry("1500x1000")
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.Canvas=Canvas(self.Frame)
		#self.Canvas.pack()
		self.Canvas.grid(padx=300, pady=150, sticky=W)
		self.yt=Video(self.Canvas)
		self.yt.pack()


root=Window()
root.tk.mainloop()
