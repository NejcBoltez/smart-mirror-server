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


class Window:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.geometry("1920x1000")
        self.Frame=Frame(self.tk, background="black")
        self.Frame.pack(fill=BOTH, expand=YES)
        self.Label_main=Label(self.Frame, text="Please say 'HEY MIRROR' 5 times", font=('verdana', 30, 'bold'), fg="white", bg="black", bd=0, highlightthickness=0, anchor="center")
        self.Label_main.pack()
        self.Label_count=Label(self.Frame, text="0", font=('verdana', 30, 'bold'), fg="white", bg="black", bd=0, highlightthickness=0, anchor="center")
        self.Label_count.pack()
        my_thread=threading.Thread(target=self.start_listening)
        my_thread.start()
    def start_listening(self):
        self.count=0
        self.phrases=[]
        while(self.count<10):
            self.l=Listening.listening_function()
            print(self.l)
            if (self.l is not None and len(self.l)>2):
                self.count=self.count+1
                self.Label_count.config(text=str(self.count))
                self.phrases.append(self.l)
            if (self.count==5):
                self.Label_main.config(text="Please say 'HI MIRROR' 5 times")
        self.tk.quit()
        Work_with_files.save_start_phrases(self.phrases)
root=Window()
tk.mainloop()