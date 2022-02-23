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
import asyncio
from tkhtmlview import HTMLLabel


arguments = list(sys.argv)

#Youtube video https://www.youtube.com/watch?v=qmQr0Uyi0Ls
class Video(Frame):
	def __init__(self, parent,pos):#, tabControl):
		Frame.__init__(self, parent)
		self.start_w_animation=14
		self.end_w_animation=1400
		self.start_h_animation=6.5
		self.end_h_animation=650
		self.videoframe=Frame(self, background="black", width=1400, height=700)
		self.videoframe.pack(fill=BOTH, expand=YES)
		'''play_yt_tab = ttk.Frame(tabControl)
		tabControl.add(self.videoframe, text ="PLAYING YOUTUBE VIDEO")
		tabControl.select(len(tabControl.tabs())-1)'''
		self.video_name=Label(self.videoframe, fg="white", background="black")
		self.video_name.pack(side=TOP)
		self.video_play=Frame(self.videoframe, background="black", width=1400, height=650)
		self.video_play.pack(fill=BOTH, expand=YES)
		#https://www.youtube.com/embed/jNQXAC9IVRw?vq=large
		video_URL=get_URL(self,pos)
		'''self.video= pafy.new(get_URL(self,pos)) #pip3 install youtube-dl    
		self.best=self.video.getbest()
		#print(self.best.resolution)
		self.streams=self.video.streams
		for s in self.streams:
			print(s.url)
		print(self.streams[0])
		self.playurl=self.best.url'''
		# creating vlc media player object
		'''media = vlc.MediaPlayer(video_URL)
		
		# start playing video
		media.play()'''
		instance=vlc.Instance()
		player=instance.media_player_new()
		#player.video_set_scale(1)
		#player.set_xwindow(GetHandle(self))
		media=instance.media_new(video_URL)
		media.get_mrl()
		player.set_media(media)
		player.play()
		
		'''my_label = HTMLLabel(self.video_play, html="""
				<video width="320" height="240" controls>
					<source src="https://www.youtube.com/embed/jNQXAC9IVRw?vq=large" type="video/mp4">
					Your browser does not support the video tag.
					</video>
			""")'''
		
		# Adjust label
		#my_label.pack(pady=20, padx=20)
		


def get_URL(self,num):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	get_yt_data=os.path.join(BASE_DIR, "json_data/youtube_data.json")
	with open(get_yt_data, "r") as f_r:
		yt_data=json.load(f_r)
	print(num)
	c=1
	selected_url=""
	for i in yt_data["videos"]:
		#print(i)
		#selected_url="https://www.youtube.com/embed/"+i["url_suffix"].replace("/watch?v=","")+"?vq=large"
		#print(selected_url)
		if (int(c) == int(num)):
			self.video_name.config(text=str(i["title"]))
			print(i)
			selected_url="https://www.youtube.com/embed/"+i["url_suffix"].replace("/watch?v=","")+"?vq=small"
			#selected_url="https://www.youtube.com/watch?v=CxwJrzEdw1U&amp;feature=emb_imp_woyt"
			#https://www.youtube.com/watch?v=HXJx8j7JpKY&amp;feature=emb_imp_woyt
			print(selected_url)
		c=c+1
	return selected_url
def GetHandle(self):
	return self.video_play.winfo_id()
class Window:
	def __init__(self):
		self.tk=tk.Tk()
		#self.tk.geometry("1500x1000")
		self.tk.geometry("1920x1000")
		#self.tk.attributes("-fullscreen", True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.Canvas=Canvas(self.Frame)
		#self.Canvas.pack()
		self.Canvas.grid(padx=300, pady=150, sticky=W)
		self.yt=Video(self.Canvas, arguments[1])
		self.yt.pack()
#get_URL(arguments[1])
root=Window()
root.tk.mainloop()
