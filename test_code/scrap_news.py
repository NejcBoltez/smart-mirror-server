from goose3 import Goose
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

class get_data_from_website(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.news_Frame=Canvas(self, background='black',width=1400, height=800)
        self.news_Frame.pack(fill=BOTH, expand= TRUE, padx=200, pady=200)
        API = "fe1f07fb06114c9a94c9c8ced3f83f8d"
        URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+API
        News=requests.get(URLnews)
        Novice=News.json()
        NewsList=Novice['articles']
        news_URL=''
        content_for_test=""
        print("Args: "+arguments[1])
        for i in range(len(NewsList)):
            print(i)
            if (i==int(arguments[1])):
                print('HELP')
                print(NewsList[i]['title'])
                news_URL=NewsList[i]['url']
                print(news_URL)
                content_for_test=NewsList[i]['content'].split('… [+')
                print(NewsList[i]['content'].encode('ascii', 'ignore'))
        get_data=Goose().extract(news_URL)

        '''image_byt = urlopen(str(get_data.image)).read()
        load = PIL.Image.open(io.BytesIO(image_byt))
        image_final=load.resize((370,200), PIL.Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image_final)
        print(content_for_test[0])'''
        print(get_data.opengraph)
        #print(get_data.top_image)
        print(get_data.meta_keywords)
        print(str(get_data.raw_doc))
        #print(str(get_data.raw_html))
        html_data=str(get_data.raw_html.encode('utf-8')).split('<article')
        article_data=str(html_data[0]).split('</article>')
        print(content_for_test)
        content_split_by_dot=content_for_test[0].split('.')
        print(content_split_by_dot[0].encode('utf-8'))
        print(article_data[0])
        #print(html_data)
        '''for i in html_data:
            print(i+'/n')
            if(content_split_by_dot[0] in i):
            #if(i.__contains__(content_for_test[0])):
                print("test:    " + i)'''
        #image_URL=get_data.top_image.src
        #print(image_URL)
        self.news_Frame.create_text(600,100, text=str(get_data.title), fill="white", font=('verdana', 20, 'bold'))
        self.news_Frame.create_text(900,300, text=str(get_data.cleaned_text.encode('utf-8')),fill="white", font=('verdana', 12))

class web_scrapper:
    def __init__(self):
        self.tk=tk.Tk()
        self.tk.configure(background='black')
        self.tk.title("Pozdravljeni")
        #self.tk.geometry("1000x600")
        self.Frame=Frame(self.tk, background='black')
        self.Frame.pack(fill=BOTH, expand=YES)
        self.news_label=get_data_from_website(self.Frame)
        self.news_label.pack()


web_scrapping_window=web_scrapper()
web_scrapping_window.tk.mainloop()

