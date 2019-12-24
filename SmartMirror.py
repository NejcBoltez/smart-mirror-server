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
#import Virtual-asistent
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, 'Uporabniki')
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
        
        # calls itself every 200 milliseconds to update the time display as needed could use >200 ms, but display gets jerky
        self.label1.after(200, self.klik)
class Vreme(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.LabelMain=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="Vreme:")
        self.LabelMain.pack()
        self.label1=Label(self, font=('Helvetica', 25), fg="white", bg="black")
        self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
        self.getVreme()
        self.label1.after(5000, self.getVreme)
    def getVreme(self):
        City = "Novo mesto"
        Country = "SI"
        APIK = "10fe78b8435d01d64ad7203ac4b87fe8"
        URL = "https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK
        r = requests.get(URL)
        preberi = r.json()
        temp="Temp: " + str(preberi['main']['temp'])
        humidity="Humidity: " + str(preberi['main']['humidity'])
        temp_min="Temp_min: " + str(preberi['main']['temp_min'])
        temp_max="Temp_max: " + str(preberi['main']['temp_max'])
        weather=temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max
        #for i in preberi['main']:
         #   weather += i+' : ' +str(preberi['main'][i]) + '\n'
        self.label1.config(text=weather)
class Novice(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.NewsFrame=Frame(self, background='Black')
        self.NewsFrame.pack(side=RIGHT)
        self.labelMain=Label(self.NewsFrame, font=('Helvetica', 30), fg='white', bg='black', text="Novice:")
        self.labelMain.pack()
        self.label1=Label(self.NewsFrame, font=('Helvetica', 9), fg="white", bg="black")
        self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
        self.getNovice()
        self.label1.after(5000000, self.getNovice)
    def getNovice(self):
        NewsList=[]
        Novice=""
        News=""
        IzborNovic=""
        API = "fe1f07fb06114c9a94c9c8ced3f83f8d"
        URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+API
        News=requests.get(URLnews)
        Novice=News.json()
        NewsList=Novice['articles']
        for i in NewsList:
            Nov = str(i['title']).split("- ")
            #print(Nov)
            #if (Nov[1]=='24ur.com' or Nov[1]=='RTV Slovenija' or Nov[1]=='Računalniške Novice' or Nov[1]=='Siol.net'):
                #self.label1.config(text="")
            IzborNovic+=str(i['title']) + '\n'
           # else:
            #    continue
        self.label1.config(text=IzborNovic)
        
class Camera(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.CamFrame=Frame(self, background='Black')
        self.CamFrame.pack(side=RIGHT)
        self.labelMain=Label(self.CamFrame, font=('Helvetica', 30), fg='white', bg='black', text="Camera")
        self.labelMain.pack(anchor='w')
        self.label1=Label(self.CamFrame, font=('Helvetica', 9), fg="white", bg="black")
        self.label1.pack(anchor='w')
        self.getCamera()
                    
        #self.label1.after(10, self.getCamera)
    def getCamera(self):
        # .local is inside home directory
        try:
            face_front=cv2.CascadeClassifier('../.local/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
        except:
            face_front=cv2.CascadeClassifier('../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Capture frame-by-frame
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        tekst=''
        #detect face
        faces = face_front.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            #tekst=str(x)+', '+str(y)+', '+str(w)+', '+str(h)
            
            #print (x)
            roi_color=frame[y:y+h, x:x+w]
            
            #image = face_recognition.load_image_file('./Images/stevejobs.png')
            image_encoding = face_recognition.face_encodings(frame)[0]
            for root, dirs, files in os.walk(image_dir):
                for d in dirs:
                    print(d)
                    print(image_dir+'/'+d)
                    for root, dirs, files in os.walk(image_dir+'/'+d):
                        print(files)
                        for file in files:
                            print('File: '+file)
                            unknown_image = face_recognition.load_image_file(image_dir+'/'+d+'/'+file)
                            '''print(unknown_image)
                            unknown_encoding=face_recognition.face_encodings(unknown_image)
                            print(len(unknown_encoding))
                            if (len(unknown_encoding)>0):
                                unknown_encoding1=face_recognition.face_encodings(unknown_image)[0]
                                
                                results=face_recognition.compare_faces([image_encoding], unknown_encoding1)
'''
                                if results[0]:
                                    #print(file)
                                    tekst=file
                                    print('tekst'+tekst)
                                    #save the image
                                    path, dirs, files = next(os.walk(image_dir+'/'+d))
                                    file_count = len(files)
                                    print(file_count)
                                    img_item2='./Uporabniki/'+d+'/'+d+'_'+str(file_count+1)+'.png'
                                    cv2.imwrite(img_item2, roi_color)
                                    break
                                else:
                                    continue
                            
            #cv2.imwrite(img_item2, roi_color)
            self.label1.config(text=tekst)
        if len(faces)==0:
            self.label1.config(text='Prazno')
        self.label1.after(600, self.getCamera)

class Okno:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.configure(background='black')
        self.tk.title("Pozdravljeni")
        self.tk.geometry("400x400")

        self.Frame=Frame(self.tk, background='Black')
        self.Frame.pack(fill=BOTH, expand=YES)
        self.TopFrame = Frame(self.Frame, background='Black')
        self.BottomFrame = Frame(self.Frame, background='Black')

        self.TopFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.BottomFrame.pack(side=BOTTOM, fill=BOTH)
        self.TopLeftFrame=Frame(self.TopFrame, background='Black')
        self.TopLeftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
        self.BottomLeftFrame=Frame(self.BottomFrame, background='Black')
        self.BottomLeftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
        self.TopRightFrame=Frame(self.TopFrame, background='Black')
        self.TopRightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)
        self.BottomRightFrame=Frame(self.BottomFrame, background='Black')
        self.BottomRightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)

        '''self.state=FALSE
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

        def toggle_fullscreen(self, event=None):
            self.state = not self.state  # Just toggling the boolean
            self.tk.attributes("-fullscreen", self.state)
            #Jayne.Jay()
            return "break"
 
        def end_fullscreen(self, event=None):
            self.state = False
            self.tk.attributes("-fullscreen", False)
            return "break"'''
        self.window()
    def window(self):
        self.label123=Label(self.TopFrame, text="Hello", fg="white", bg="black")
        self.label123.pack()
        self.cam=Camera(self.BottomLeftFrame)
        self.cam.pack()
        '''self.Ura=Ura(self.BottomLeftFrame)
        self.ura.pack()'''
        self.ura=Ura(self.Frame)
        self.ura.pack(side=BOTTOM)
        self.vreme=Vreme(self.TopRightFrame)
        self.vreme.pack(side=RIGHT)
        self.news=Novice(self.BottomRightFrame)
        self.news.pack(side=RIGHT, fill=BOTH, expand=YES)
        self.label1234=Label(self.BottomFrame, text="Hello2", fg="white", bg="black")
        self.label1234.pack()
        #self.cam.after(200, self.window)

window=Okno()
window.tk.mainloop()