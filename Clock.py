try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *
import time
import json
import requests
import urllib
import cv2
import numpy as np
from urllib3 import *
from PIL import Image, ImageTk
import dlib
import os
import face_recognition
#from Virtual_asistent import AI
import pyttsx3 as pyttsx
import speech_recognition as sr
import subprocess #as call
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, 'Uporabniki')
user = ''
speech_engine = pyttsx.init()
class Ura(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.label1=Label(self, font=('Helvetica', 100), fg="white", bg="black")
        self.label1.pack(side=TOP,anchor=E)
        self.dan=Label(self, font=('Helvetica', 15), fg="white", bg="black")
        self.dan.pack()
        self.pozdrav=Label(self, font=('Helvetica', 15), fg="white", bg="black")
        self.pozdrav.pack()
        self.klik()
    def klik(self):
        ti=time.strftime('%H:%M:%S')
        dan=time.strftime('%A')
        self.label1.config(text=ti)
        self.dan.config(text=dan)
        
        # calls itself every 1000 milliseconds to update the time display as needed could use >200 ms, but display gets jerky
        self.label1.after(1000, self.klik)