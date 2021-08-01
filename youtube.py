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
#from SmartMirror import okno


arguments = list(sys.argv)

def get_yt_data(search_for):
    results = YoutubeSearch(str(search_for).replace('_', ' '), max_results=20).to_json()
    get_results=json.loads(results)
    return get_results

class yt_search(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.search_frame=Frame(self, width=1800, height=800, bg="black", bd=0, highlightthickness=0)
        self.search_frame.pack(fill=BOTH, expand=YES)
        self.search_text=Label(self.search_frame, text=str(arguments[1]).replace('_', ' ').upper(), font=('verdana', 30, 'bold'), fg="white", bg="black", bd=0, highlightthickness=0, anchor="center")
        self.search_text.pack(side=TOP)
        self.search_frame_top=Canvas(self.search_frame,width=1700, height=400, bg="black", bd=0, highlightthickness=0)
        self.search_frame_top.pack(side=TOP, fill=BOTH, expand= TRUE)
        self.search_frame_bottom=Canvas(self.search_frame, width=1700, height=400, bg="black", bd=0, highlightthickness=0)
        self.search_frame_bottom.pack(side=BOTTOM, fill=BOTH, expand= TRUE)
        self.get_json=get_yt_data(arguments[1])
        self.yt=self.get_json['videos']
        self.position_x=1500
        self.x=0
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
            print(c)
            print(i)
        
        self.resize_animation()
        #time.sleep(7)
        
        '''while(self.position_x>=500):
            #self.search_frame.move(self.search_frame_top, self.position_x, 0)
            self.search_frame_top.update()
            self.search_frame.update()
            print(self.position_x)
            self.search_frame_top.pack_configure(padx=self.position_x)
            self.position_x=self.position_x-100
            time.sleep(0.5)'''
            
            
    def resize_animation(self):
        if(self.position_x>=0):
            #self.search_frame_top.update()
            #self.search_frame.update()
            #print(self.position_x)
            self.search_frame_top.pack_configure(side=TOP, fill=BOTH, expand= TRUE, padx=self.position_x)
            self.search_frame_bottom.pack_configure(side=TOP, fill=BOTH, expand= TRUE, padx=self.position_x)
            self.position_x=self.position_x-50
        else:
            self.search_frame.after_cancel(self.move_left)
        self.move_left=self.search_frame.after(100, self.resize_animation)
        return self.position_x
        
        '''if self.x<0:
            position_x=1500
            #while (position_x>=0):
            #    print(position_x)
                #print(self.search_frame_bottom.winfo_width())
            for i in range(15):
                self.search_frame_top.pack_configure(padx=position_x)
                #print(position_x)
                position_x=position_x-100
            #self.position_x=self.position_x-100
            #return self.position_x
        else:
            self.x=1
        return self.x'''

class Window:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.geometry("1920x1000")
        self.Frame=Frame(self.tk, background="black")
        self.Frame.pack(fill=BOTH, expand=YES)
        self.Canvas=Canvas(self.Frame)
        #self.Canvas.pack()
        self.Canvas.grid(padx=150, pady=150)
        self.yt=yt_search(self.Canvas)
        self.yt.pack()

root=Window()
root.tk.mainloop()

