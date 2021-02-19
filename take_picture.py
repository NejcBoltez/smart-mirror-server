import numpy as np
import cv2
import sys
import time
from PIL import ImageTk
import PIL.Image
try:
    import tkinter as tk
    from tkinter import *
except:
    import Tkinter as tk
    from Tkinter import *

time.sleep(5)
arguments = list(sys.argv)

'''try:
    face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
except:'''
#face_front=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#face_front=cv2.CascadeClassifier('../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#face_eye=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_profileface.xml')
class get_video(Frame):
     def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.Frame=Frame(self, width=1800, height=1000, background="black")
        self.Frame.pack()
        self.cap = cv2.VideoCapture(0)

        self.ret, self.frame = self.cap.read()
        count=0
        found_faces=[10]
        #while(count<10):
            # Capture frame-by-frame
        #    ret, frame = cap.read()
        #cv2.imshow('frame',self.frame)
        #    if (cv2.waitKey(1) & 0xFF == ord('q')) or sys.stdin == str.encode('q') :
        #        break

        # When everything done, release the capture

        '''image_byt = urlopen('https:'+image_url).read()
        load = PIL.Image.open(io.BytesIO(image_byt))
        image_final=load.resize((370,200), PIL.Image.ANTIALIAS)'''
        self.image = PIL.Image.fromarray(self.frame)
        render = ImageTk.PhotoImage(self.image)

        img = Label(self.Frame, image=render, width=310, height=200)
        img.image = render
        img.place(x=20, y=100)
        img.pack()


        #cap.release()
        #cv2.destroyAllWindows()
class Window:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.configure(background='black')
        self.tk.title("Pozdravljeni")
        self.tk.geometry("1000x600")
        self.Frame=Frame(self.tk, background='black')
        self.Frame.pack(fill=BOTH, expand=YES)
        #self.video=Canvas(self.Frame, background="black", width="600", height="400")
        #self.video.pack()
        self.news_label=get_video(self.Frame)
        self.news_label.pack()
        #get_news(self)
        

window=Window()
window.tk.mainloop()
