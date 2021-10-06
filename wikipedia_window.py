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
import wget
import os

'''import rsvg
import cairo
import StringIO'''
import pyvips

speech_engine = pyttsx.init()
class Wikipedia_show:
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self, command):
		def govor(besedilo):
			speech_engine.say(besedilo)
			speech_engine.runAndWait()

		#vpras=str(sys.argv[1])
		vpras=command
		print("Vprasanje: "+vpras)

		def get_svg(svg_file):
			image = pyvips.Image.new_from_file(svg_file, dpi=300)
			image.write_to_file("x.png")
			'''svg = rsvg.Handle(data=svg_file)
			img = cairo.ImageSurface(cairo.FORMAT_ARGB32, 
			svg.props.width, 
			svg.props.height)
			ctx = cairo.Context(img)
			svg.render_cairo(ctx)

			# Write to StringIO
			png_io = StringIO.StringIO()
			img.write_to_png(png_io)'''
			'''
			print('TEST')
			
			print(svg_file)
			print('TEST')
			drawing = svg2rlg(svg_file)#, background="black")
			print(drawing)
			#renderPM.drawToFile(drawing, "wiki.jpg", fmt="JPG")
			#renderPDF.drawToFile(drawing, "wiki.pdf")'''

		def get_image(wiki_url):
			response=requests.get(wiki_url)
			wiki_response=json.loads(response.text)
			
			print(wiki_response)
			image_url=str(wiki_response['query']['pages'])#.values())[0]['original']['source']
			print('IMG: '+image_url)
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
			#time.sleep(120)
			file_end=url_split[len(url_split)-1]
			#file = open("wiki.txt","w")
			#print("Response: "+str(response.content))
			print(response.text)
			file_path='wiki.jpg'
			file_name='wiki.'+str(file_end)
			if(os.path.isfile(file_name)):
				os.remove(file_name)
			#if (file_end in 'jpg'):
			#os.
			
			wget.download(url_of_image,out=file_name)
				
			#else:
			if(file_end in ('svg','png','gif')):
    				get_svg(file_name)
					
			#place_image(file_path)
			#with open('wiki.jpg', 'wb') as f:
			#	f.write(response.content)
			#file.write(response.content)
			#print(response.content)
			#file.close()
			#file_path="wiki.jpg"
			'''g=Image.new('RGB', (450,300), (0,0,0,0))
			g.paste(file, (0,0))
			g.save("novo.png", format="PNG")'''
			#file_path="belgian.svg"
			#time.sleep(5)
			'''if(file_end in ('svg','png','gif')):
				get_svg('wiki.jpg')
			place_image(file_path)'''

		def place_image(file_name):
			#try:
			#image_open=Image.open(file_name)
			#image_bytes=io.BytesIO(image_byt.content)
			load = Image.open(file_name)
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
		root=tk.Tk()
		root.geometry("1920x1080")
		FrameWiki=Canvas(root, background="black")
		FrameWiki.pack(fill=BOTH, expand= TRUE, anchor='w')
		try:
			wiki_api_url="https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageimages&exsentences=7&piprop=original&exintro&explaintext&redirects=1&titles="+str(vpras.replace('_', ' '))#str(title[0])
			read_wiki=requests.get(wiki_api_url)
			wiki_response=json.loads(read_wiki.text)
			print(wiki_response)
			title=list(wiki_response['query']['pages'].values())[0]["title"]
			#title=''
			answer=list(wiki_response['query']['pages'].values())[0]["extract"]
			odgovor=''
			FrameWiki.create_text(600,300, text=title, fill="white", font=("verdana", 25, "bold"))
			FrameWiki.create_text(600,500,width=800, text=answer, fill='white', font=('verdana', 15))
			wiki_api_url=list(wiki_response['query']['pages'].values())[0]["original"]["source"]#"http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles="+str(vpras.replace('_', ' '))#str(title[0])
			print(wiki_api_url)
			save_image(wiki_api_url)
		except wikipedia.exceptions.PageError as e:
			possible_matches=wikipedia.search(vpras.replace('_', ' '))
			matches=""
			for i in possible_matches:
				matches = matches + i + '\n'
			FrameWiki.create_text(600,300, text="Sorry no matches for "+vpras.replace('_',' '), fill="white", font=("verdana", 25, "bold"))
			FrameWiki.create_text(600,350,width=80, text="Here are some other possible matches", fill='white', font=('verdana', 15, "bold"))
			FrameWiki.create_text(650,500,width=800, text=matches, fill='white', font=('verdana', 15))
		
		root.mainloop()
arguments = list(sys.argv)
try:
	Wikipedia_show(arguments[1])
except EXCEPTION as e:
	print(e)