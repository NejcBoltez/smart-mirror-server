import os
import threading
from speech_listen import Listening
from working_with_files import Work_with_files
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *


class Say_start_phrase_GUI:
    def __init__(self, user):
        tk=tk.Tk()
        tk.geometry("1920x1000")
        Frame=Frame(tk, background="black")
        Frame.pack(fill=BOTH, expand=YES)
        Label_main=Label(Frame, text="Please say 'HEY MIRROR' 5 times", font=('verdana', 30, 'bold'), fg="white", bg="black", bd=0, highlightthickness=0, anchor="center")
        Label_main.pack()
        Label_count=Label(Frame, text="0", font=('verdana', 30, 'bold'), fg="white", bg="black", bd=0, highlightthickness=0, anchor="center")
        Label_count.pack()
        tk.update()
        count=0
        phrases=[]
        while(count<10):
            l=Listening.listening_function()
            print(l)
            if (l is not None and len(l)>2):
                count=count+1
                Label_count.config(text=str(count))
                phrases.append(l)
                tk.update()
            if (count==5):
                Label_main.config(text="Please say 'HI MIRROR' 5 times")
        tk.quit()
        Work_with_files.save_start_phrases(phrases, user)
root=Say_start_phrase_GUI("nejc")
tk.mainloop()