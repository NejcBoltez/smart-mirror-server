'''try:
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
    okno.tk.mainloop()'''
    #requests 2.25.1 has requirement idna<3,>=2.5, but you'll have idna 3.1 which is incompatible. reši z naslednjim komentarjem
    #pip install urllib3[secure] requests --force-reinstall
    #pip install jupyterlab
    #pip install gmaps
    #pip install --upgrade --force-reinstall pyzmq fixa problem 'Install tornado itself to use zmq with the tornado IOLoop.'
'''import gmaps
gmaps.configure(api_key='AIzaSyB7y011brEzIHTaUiDBdSESDEymeCwcaY8')
new_york_coordinates = (40.75, -74.00)
gmaps.figure(center=new_york_coordinates, zoom_level=12)'''
import gmaps
import gmaps.datasets
# Use google maps api
gmaps.configure(api_key='AIzaSyB7y011brEzIHTaUiDBdSESDEymeCwcaY8') # Fill in with your API key
# Get the dataset
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
#Get the locations from the data set
locations = earthquake_df[['50', '10']]
#Get the magnitude from the data
weights = earthquake_df['magnitude']
#Set up your map
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig