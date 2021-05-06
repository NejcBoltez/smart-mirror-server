import json
import io
import requests
import base64
from urllib.request import urlopen
from PIL import ImageTk
import PIL.Image
import sys
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


class display_news(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        global displayed
        n=0
        NewsList=[]
        Novice=""
        News=""
        IzborNovic=""
        API = "fe1f07fb06114c9a94c9c8ced3f83f8d"
        URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+API
        News=requests.get(URLnews)
        Novice=News.json()
        NewsList=Novice['articles']
        w=350
        h=600
        self.NewsFrame=Frame(self, width=1800, height=1000, background="black")
        self.NewsFrame.pack(fill=BOTH, expand= TRUE, anchor='w', pady=200)
        self.NewsDir1=Canvas(self.NewsFrame, width=w, height=h)
        self.NewsDir1.pack(side=LEFT, padx=10) 
        self.NewsDir2=Canvas(self.NewsFrame, width=w, height=h)
        self.NewsDir2.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w', padx=10)
        self.NewsDir3=Canvas(self.NewsFrame, width=w, height=h)
        self.NewsDir3.pack(side=LEFT, padx=10) 
        self.NewsDir4=Canvas(self.NewsFrame, width=w, height=h)
        self.NewsDir4.pack(side=LEFT, padx=10)
        self.NewsDir5=Canvas(self.NewsFrame, width=w, height=h)
        self.NewsDir5.pack(side=LEFT, padx=10)


        '''for i in Novice['articles']:
            if n < 5 or n <10 or n <15:
                NewsList=NewsList+i
            n+=1'''
        NewsD=1
        start= displayed-5
        end=displayed
        for i in NewsList:
            Nov = str(i['title']).split("- ")
            ##print(n)
            #if n > displayed-5 and n < displayed:
            #print(displayed)
            if displayed-6<n<displayed:
                #print('test')
            ##print(Nov)
            #if (Nov[1]=='24ur.com' or Nov[1]=='RTV Slovenija' or Nov[1]=='Računalniške Novice' or Nov[1]=='Siol.net'):
                #self.label1.config(text="")
                
                '''IzborNovic+=str(i['title']) + '\n'
                image_url = "http://i46.tinypic.com/r9oh0j.gif"
                image_byt = urlopen(image_url).read()
                image_b64 = base64.encodestring(image_byt)'''
                #print(n)
                image_url=str(i['urlToImage'])
                render=''
                try:
                    if ("https" in image_url):
                        #image_url = "https://images.24ur.com/media//images/600xX/Jan2021/f861ec2c611cba45038d_62508806.jpg?v=1611159757"
                        image_byt = urlopen(image_url).read()
                        #image_b64 = base64.encodestring(image_byt)
                        load = PIL.Image.open(io.BytesIO(image_byt))
                        #load1 = Image.
                        image_final=load.resize((370,200), PIL.Image.ANTIALIAS)
                        render = ImageTk.PhotoImage(image_final)
                        #img = PhotoImage(data='images_icons_linux-bsd.gif')
                        #img = ImageTk.PhotoImage(Image.open("images_icons_linux-bsd.gif"))
                    elif ("//" in image_url):
                        image_byt = urlopen('https:'+image_url).read()
                        load = PIL.Image.open(io.BytesIO(image_byt))
                        image_final=load.resize((370,200), PIL.Image.ANTIALIAS)
                        render = ImageTk.PhotoImage(image_final)
                    elif("dnevnik" in str(i['url'])):
                        image_byt = urlopen('https://www.dnevnik.si'+image_url).read()
                        load = PIL.Image.open(io.BytesIO(image_byt))
                        image_final=load.resize((370,200), PIL.Image.ANTIALIAS)
                        render = ImageTk.PhotoImage(image_final)
                except:
                    load = PIL.Image.open("jaz_color.png")
                    render = ImageTk.PhotoImage(load)
                
                if NewsD==1:
                    #print(1)
                    
                    self.NewsDir1.create_rectangle(3,3, w-1, h-1,fill='black')
                    self.NewsDir1.create_text(20, 50, width=w-20, text=str(i['title']).replace(' - ', '\n'),fill='white', font=('verdana', 12, 'bold'), anchor=W)
                    #self.NewsDir1.create_text(width=w-15, text=str(i['description']), fill="white", font=('verdana', 12, 'bold'), anchor=W)
                    #l=Label(self.NewsDir1, image=img)
                    #self.NewsDir1.create_image(30,50, image=img, width=w-20, anchor=CENTER)
                    img = Label(self.NewsDir1, image=render, width=310, height=200)
                    img.image = render
                    img.place(x=20, y=100)
                    #print(str(i['description']))
                    desc=str(i['description'])
                    self.NewsDir1.create_text(30,400,width=w-30, text=str(i['description']), fill="white", font=('verdana', 12), anchor=W)
                    

                elif NewsD==2:
                    #print(2)
                    self.NewsDir2.create_rectangle(3,3, w-1, h-1,fill='black')
                    self.NewsDir2.create_text(20,50, width=w-20, text=str(i['title']),fill='white', font=('verdana',12, 'bold'), anchor=W)#NewsList[i+1])
                    #self.NewsDir2.create_text(width=w-15, text=str(i['description']), fill="white", font=('verdana', 12, 'bold'), anchor='W')
                    img = Label(self.NewsDir2, image=render, width=310, height=200)
                    img.image = render
                    img.place(x=20, y=100)
                    self.NewsDir2.create_text(30,400,width=w-30, text=str(i['description']), fill="white", font=('verdana', 12), anchor=W)

                elif NewsD==3:
                    #print(3)
                    self.NewsDir3.create_rectangle(3,3, w-1, h-1,fill='black')
                    self.NewsDir3.create_text(20,50, width=w-20, text=str(i['title']),fill='white', font=('verdana', 12, 'bold'), anchor=W)#NewsList[i+2])
                    #self.NewsDir3.create_text(width=w-15, text=str(i['description']), fill="white", font=('verdana', 12, 'bold'), anchor=W)
                    img = Label(self.NewsDir3, image=render, width=310, height=200)
                    img.image = render
                    #img.size(370,200)
                    img.place(x=20, y=100)
                    self.NewsDir3.create_text(30,400,width=w-30, text=str(i['description']), fill="white", font=('verdana', 12), anchor=W)

                elif NewsD==4:
                    #print(4)
                    self.NewsDir4.create_rectangle(3,3, w-1, h-1,fill='black')
                    self.NewsDir4.create_text(20,50, width=w-20, text=str(i['title']),fill='white', font=('verdana', 12, 'bold'), anchor=W)#NewsList[i+3])
                    img = Label(self.NewsDir4, image=render, width=310, height=200)
                    img.image = render
                    img.place(x=20, y=100)
                    self.NewsDir4.create_text(30,400,width=w-30, text=str(i['description']), fill="white", font=('verdana', 12), anchor=W)

                elif NewsD==5:
                    #print(5)

                    self.NewsDir5.create_rectangle(3,3, w-1, h-1,fill='black')
                    self.NewsDir5.create_text(20,50, width=w-20, text=str(i['title']),fill='white', font=('verdana', 12, 'bold'), anchor=W)#NewsList[i+4])
                    img = Label(self.NewsDir5, image=render, width=310, height=200)
                    img.image = render
                    img.place(x=20, y=100)
                    self.NewsDir5.create_text(30,400,width=w-30, text=str(i['content']), fill="white", font=('verdana', 12), anchor=W)
                NewsD=NewsD+1
                n=n+1
            
            #NewsD=NewsD+1
            # else:
            #    continue
            else:
                n=n+1
            #return n
        #self.news_label.config(text=IzborNovic)
        '''self.NewsDir=Canvas(self)
        self.NewsDir.create_text()
        self.NewsDir.pack()'''
           

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
        self.news_label=display_news(self.Frame)
        self.news_label.pack()
        #get_news(self)
        

window=News()
window.tk.mainloop()
