import time
import vlc
import pafy
import sys
from youtube_search import YoutubeSearch
import json
try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
arguments = list(sys.argv)
print(arguments)
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
        #self.url= self.get_URL()
        self.url="https://www.youtube.com/watch?v=EUBWcad1U0c"#=xAg7z6u4NE8"
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
        #time.sleep(1)
        #self.player.pause()
        #self.start_animation()
    def start_animation(self):
        if(self.start_w_animation<=self.end_w_animation and self.start_h_animation<=self.end_h_animation):
            self.video_play.configure(width=self.start_w_animation, height=self.start_h_animation, background="black")
            self.start_w_animation=self.start_w_animation+10
            self.start_h_animation=self.start_h_animation+10
            self.start=self.video_play.after(1, self.start_animation)
        else:
            self.video_play.after_cancel(self.start)
            #self.player.play()


    def get_URL(self):
        self.results_yt = YoutubeSearch(arguments[1], max_results=10).to_json()
        self.get_json=json.loads(self.results_yt)
        self.yt=self.get_json['videos']
        c=0
        selected_url=''
        for i in self.yt:
            print(c)
            if (c == int(arguments[2])):
                print(i['url_suffix'])
                print(i['title'])
                self.video_name.config(text=str(i['title']))
                selected_url='https://www.youtube.com'+i['url_suffix']
                print(selected_url)
            c=c+1
        return selected_url
    def GetHandle(self):
        print (self.video_play.winfo_id())
        return self.video_play.winfo_id()
        #time.sleep(50)
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
