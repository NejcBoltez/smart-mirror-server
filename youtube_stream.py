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
	def pause_video(self):
		self.player.pause()
	def main(self,pos, tabControl):#, tabControl):
		#Frame.__init__(self, parent)
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
		#https://www.youtube.com/embed/jNQXAC9IVRw?vq=large
		video_URL=get_URL(self,pos)
		video= pafy.new(get_URL(self,pos)) #pip3 install youtube-dl  
		video_streams=streamlink.streams(video_URL)
		lowest_resolution=1000000
		lowest_resolution_link=''
		#print(video_streams)  
		'''best=video.getbest()
		print(best.resolution)
		streams=video.streams'''
		for s in video_streams:
			try:
				print(video_streams[s].url)
				print(int(s.split('p')[0]))
				if (int(s.split('p')[0])<lowest_resolution or int(s.split('p')[0])<720):
					lowest_resolution=int(s.split('p')[0])
					lowest_resolution_link=video_streams[s].url

			except Exception as e:
				print(e)
				continue
		print(lowest_resolution)
		'''playurl=video_streams["720p"].url#best.url
		print(playurl)'''
		# creating vlc media player object
		#media = vlc.MediaPlayer(video_URL)
		
		# start playing video
		#media.play()
		#Media = vlc.Instance.media_new(video)
		#Media.get_mrl()
		#Media_list = Instance.media_list_new([url])
		#time.sleep(2)
		self.instance=vlc.Instance()
		self.player=self.instance.media_player_new()
		
		self.player.set_xwindow(GetHandle(self))
		self.media=self.instance.media_new(lowest_resolution_link)
		self.media.get_mrl()
		self.player.set_media(self.media)
		self.player.set_rate(0.5)
		#self.player.set_mrl(video_URL)
		self.player.play()
		
		# Adjust label
		#my_label.pack(pady=20, padx=20)
		


def get_URL(self,num):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	get_yt_data=os.path.join(BASE_DIR, "json_data/youtube_data.json")
	with open(get_yt_data, "r") as f_r:
		yt_data=json.load(f_r)
	print(num)
	c=0
	selected_url=""
	for i in yt_data["videos"]:
		#print(i)
		#selected_url="https://www.youtube.com/embed/"+i["url_suffix"].replace("/watch?v=","")+"?vq=large"
		#print(selected_url)
		if (int(c) == int(num)):
			self.video_name.config(text=str(i["title"]))
			print(i)
			#selected_url="https://www.youtube.com/embed/"+i["url_suffix"].replace("/watch?v=","")+"?vq=small"
			selected_url="https://www.youtube.com/watch?v=vK928kqYUPI"#"https://www.youtube.com"+i["url_suffix"]
			#selected_url="https://www.youtube.com/watch?v=oZLKBHAa5tw&amp;feature=emb_imp_woyt"
			#https://www.youtube.com/watch?v=HXJx8j7JpKY&amp;feature=emb_imp_woyt
			print(selected_url)
		c=c+1
	return selected_url
def GetHandle(self):
	return self.video_play.winfo_id()
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
root=Window()
root.tk.mainloop()
