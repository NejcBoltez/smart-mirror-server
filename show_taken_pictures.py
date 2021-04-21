import os
from PIL import ImageTk
import PIL.Image
import multiprocessing
try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
class show_pictures(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.Frame=Canvas(background="purple")
        self.Frame.pack(fill=BOTH, expand=YES, side=TOP)
        '''rows=4
        starty=0
        while(rows>0):
            startx=0
            for i in range(5):
                self.Frame.create_rectangle(startx,starty, startx+300, starty+350, fill="black", outline="white")
                startx=startx+350
            starty=starty+400
            rows=rows-1'''
            

class Window:
    def __init__(self):
        self.tk=tk.Tk()
        #self.tk.geometry("1920x1000")
        #self.tk.overrideredirect(True)
        self.Frame=Frame(self.tk, background="red")
        self.Frame.pack(fill=BOTH, expand=YES)
        self.Canvas=Canvas(self.Frame, background="yellow")
        #self.Canvas.pack(fill=BOTH, expand=YES,padx=0,pady=0)
        self.Canvas.grid(sticky=W)
        self.pic=show_pictures(self.Canvas)
        self.pic.pack(fill=BOTH, expand=YES)

root=Window()
root.tk.mainloop()
