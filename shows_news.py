import json
import io
import requests
import base64
from urllib.request import urlopen
from PIL import ImageTk
import PIL.Image
import sys
from tkinterweb import HtmlFrame
try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *

arguments = list(sys.argv)
if (len(arguments)==2):
    displayed=int(arguments[1])
else:
    displayed=5

class show_news(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.Canvas= HtmlFrame(self) #create HTML browser
        self.Canvas.load_website("https://www.24ur.com/sport/nogomet/serie-a-milan-odgovarja-na-zmagi-interja-in-juventusa-proti-crotoneju-parma-bologna-lazio-cagliari.html") #load a website
        self.Canvas.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
class News:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.configure(background='black')
        self.tk.title("Pozdravljeni")
        #self.tk.geometry("1000x600")
        self.Frame=Frame(self.tk, background='black')
        self.Frame.pack(fill=BOTH, expand=YES)
        #self.video=Canvas(self.Frame, background="black", width="600", height="400")
        #self.video.pack()
        self.news_label=show_news(self.Frame)
        self.news_label.pack()
        #get_news(self)
        

window=News()
window.tk.mainloop()
