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
import pyttsx3 as pyttsx
import speech_recognition as sr
import subprocess #as call
class Maps:
    def __init__(self):
        
class Okno:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.configure(background='black')
        self.tk.title("Pozdravljeni")
        self.tk.geometry("1000x600")
        self.Frame=Frame(self.tk, background='Purple')
        self.Frame.pack(fill=BOTH, expand=YES)
        self.recognize()
    def recognize(self):
        self.cam=Camera(self.Frame)
        self.cam.pack()
        
def maps():
    okno=Okno()
    okno.tk.mainloop()