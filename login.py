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
from SmartMirror import Okno
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, 'Uporabniki')
user = ''

class Camera(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.CamFrame=Frame(self, background='Black')
        self.CamFrame.pack(side=TOP,anchor=E)
        self.labelMain=Label(self.CamFrame, font=('Helvetica', 60), fg='white', bg='black', text="Please LOGIN")
        self.labelMain.pack(anchor='w')
        self.label1=Label(self.CamFrame, font=('Helvetica', 9), fg="white", bg="black")
        self.label1.pack(anchor='w')
        self.getCamera()
                    
        #self.label1.after(10, self.getCamera)
    def getCamera(self):
        # .local is inside home directory
        try:
            face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        except:
            face_front=cv2.CascadeClassifier('../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Capture frame-by-frame
        global user
        #global login
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
                            print(unknown_image)
                            unknown_encoding=face_recognition.face_encodings(unknown_image)
                            print(len(unknown_encoding))
                            if (len(unknown_encoding)>0):
                                unknown_encoding1=face_recognition.face_encodings(unknown_image)[0]

                                results=face_recognition.compare_faces([image_encoding], unknown_encoding1)

                                if results[0]:
                                    #print(file)
                                    tekst=d
                                    print('tekst: '+tekst)
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
            teskst123='Pozdravljen ' + tekst
            self.labelMain.config(text=teskst123)
            #self.label1.config(text=tekst)
            #this.user=tekst
            #self.home_window()
            user=tekst
            #self.labelMain.after(700, self.home_window)
            home=Okno()
#             root.destroy()
            home.tk.mainloop()
        if len(faces)==0:
            self.label1.config(text='Prazno')
            self.label1.after(600, self.getCamera)
            

    

class Login:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.configure(background='black')
        self.tk.title("Pozdravljeni")
        self.tk.geometry("1000x600")
        #self.tk.attributes('-fullscreen', True)  
        #self.fullScreenState = False
        self.Frame=Frame(self.tk, background='Black')
        self.Frame.pack(fill=BOTH, expand=YES)
        self.login=Camera(self.Frame)
        self.login.pack()

login=Login()
login.tk.mainloop()