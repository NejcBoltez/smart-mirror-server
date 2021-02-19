import time
import vlc
import pafy
import webbrowser
import urllib
import subprocess
import sys
import os
import requests
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
import base64
from PIL import ImageTk
import PIL.Image
from urllib.request import urlopen
arguments = list(sys.argv)
class yt_search(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.search_frame=Canvas(self, width=1800, height=800, background="black", borderwidth=0, highlightthickness=0)
        self.search_frame.pack(fill=BOTH, expand=YES)
        self.search_text=Label(self.search_frame, text=str(arguments[1]).replace('_', ' ').upper(), font=('verdana', 30, 'bold'), fg="white", background="black", borderwidth=0, highlightthickness=0)
        self.search_text.pack(side=TOP, anchor='w')
        self.search_frame_top=Canvas(self.search_frame, width=1700, height=400, background="black", borderwidth=0, highlightthickness=0)
        self.search_frame_top.pack(side=TOP, fill=BOTH, expand= TRUE)
        self.search_frame_bottom=Canvas(self.search_frame, width=1500, height=400, background="black", borderwidth=0, highlightthickness=0)
        self.search_frame_bottom.pack(side=BOTTOM, fill=BOTH, expand= TRUE)
        self.results = YoutubeSearch(str(arguments[1]).replace('_', ' '), max_results=10).to_json()
        self.get_json=json.loads(self.results)
        self.yt=self.get_json['videos']
        coordinate=70
        c=0
        #print(type(get_json))
        for i in self.yt:
            image_byt = urlopen(i['thumbnails'][0]).read()
            #image_b64 = base64.encodestring(image_byt)
            load = PIL.Image.open(io.BytesIO(image_byt))
            #load1 = Image.
            image_final=load.resize((250,200), PIL.Image.ANTIALIAS)
            render = ImageTk.PhotoImage(image_final)
            if (c<5):
                self.search_frame_top.create_rectangle(coordinate,10, coordinate+300, 350, fill="black", outline="white")
                try:
                    self.search_frame_top.create_text(coordinate+150,60, width=230, text=str(i['title']), fill="white", font=('verdana', 12, 'bold'))
                except:
                    continue
                img = Label(self.search_frame_top, image=render, width=250, height=200)
                img.image = render
                img.place(x=coordinate+20, y=120)
                coordinate=coordinate+320
                print(i['id']+'\n'+i['title']+'\n'+i['thumbnails'][0])
                c=c+1
            else:
                if (c==5):
                    coordinate=70
                self.search_frame_bottom.create_rectangle(coordinate,10, coordinate+300, 350, fill="black", outline="white")
                try:
                    self.search_frame_bottom.create_text(coordinate+150,60, width=230, text=str(i['title']), fill="white", font=('verdana', 12, 'bold'))
                except:
                    continue
                img = Label(self.search_frame_bottom, image=render, width=250, height=200)
                img.image = render
                img.place(x=coordinate+20, y=120)
                coordinate=coordinate+320
                print(i['id']+'\n'+i['title']+'\n'+i['thumbnails'][0])
                c=c+1

class Window:
    def __init__(self):
        self.tk=tk.Tk()
        #self.tk.geometry("1500x1000")
        self.Frame=Frame(self.tk, background="black")
        self.Frame.pack(fill=BOTH, expand=YES)
        self.Canvas=Canvas(self.Frame)
        #self.Canvas.pack()
        self.Canvas.grid(padx=150, pady=150, sticky=W)
        self.yt=yt_search(self.Canvas)
        self.yt.pack()

root=Window()
root.tk.mainloop()

