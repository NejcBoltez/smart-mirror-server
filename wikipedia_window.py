try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
from tkinterhtml import HtmlFrame
import pyttsx3 as pyttsx
import wikipedia

import urllib.request
import sys
import requests
import json
from PIL import ImageTk
#import PIL.Image as Image
from PIL import Image
import base64
import io
import urllib
import time
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM


speech_engine = pyttsx.init()

def govor(besedilo):
	speech_engine.say(besedilo)
	speech_engine.runAndWait()

vpras=str(sys.argv[1])
print("Vprasanje: "+vpras)

def get_svg(svg_file):
	drawing = svg2rlg(svg_file)#, background="black")
	renderPM.drawToFile(drawing, "wiki.jpg", fmt="JPG")
	renderPDF.drawToFile(drawing, "wiki.pdf")

def get_image(wiki_url):
	response=requests.get(wiki_url)
	wiki_response=json.loads(response.text)
	image_url=list(wiki_response['query']['pages'].values())[0]['original']['source']
	print(image_url)
	save_image(image_url)

	#image_byt = urlopen(image_url, 'wiki.png').read()
	'''if ("svg" in image_url):
		image_byt=requests.get(image_url)
	else:
		image_byt=requests.get(image_url)'''

def save_image(url_of_image):
	response = requests.get(url_of_image)
	#url=response.text
	url_split=url_of_image.split('.')
	file_end=url_split[len(url_split)-1]
	file = open("wiki.jpg","wb")
	file.write(response.content)
	file.close()
	file_path="wiki.jpg"
	'''g=Image.new('RGB', (450,300), (0,0,0,0))
	g.paste(file, (0,0))
	g.save("novo.png", format="PNG")'''
	#file_path="belgian.svg"
	#time.sleep(5)
	if(file_end in ('svg','png','gif')):
		get_svg('wiki.jpg')
	place_image(file_path)

def place_image(file_name):
	#try:
	#image_open=Image.open(file_name)
	#image_bytes=io.BytesIO(image_byt.content)
	load = Image.open('wiki.jpg')
	'''try:
		load = Image.open('wiki.jpg')
	except:
		time.sleep(5)
		load = Image.open('wiki.jpg')
		'''

	#if load.tile[0][0] == "gif":
		# only read the first "local image" from this GIF file
	#	tag, (x0, y0, x1, y1), offset, extra = im.tile[0]
	#	load.size = (x1 - x0, y1 - y0)
	#	load.tile = [(tag, (0, 0) + im.size, offset, extra)]'''

	image_final=load.resize((450,300), Image.ANTIALIAS)
	render = ImageTk.PhotoImage(image_final)
	img = Label(FrameWiki, image=render, width=450, height=300, background="black")
	img.image = render
	img.place(x=1100, y=350)

odgovor=''
p=''
title=['']
odgovor = wikipedia.summary(vpras.replace('_', ' '), sentences = 4)
#p=wikipedia.page(vpras.replace('_', ' '))
title=wikipedia.search(vpras.replace('_', ' '))
img_path=wikipedia.page(vpras.replace('_', ' '))
print(title[0])
print(img_path)
root=tk.Tk()
root.geometry("1900x1000")
FrameWiki=Canvas(root, background="black")
FrameWiki.pack(fill=BOTH, expand= TRUE, anchor='w')
FrameWiki.create_text(600,300, text=title[0], fill="white", font=("verdana", 25, "bold"))
FrameWiki.create_text(600,500,width=800, text=odgovor, fill='white', font=('verdana', 15))
wiki_api_url="http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles="+str(title[0])
print(wiki_api_url)
wiki_img=get_image(wiki_api_url)
root.mainloop()