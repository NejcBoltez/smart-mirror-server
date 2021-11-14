try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import pyttsx3 as pyttsx
import wikipedia

import sys
import requests
import json
from PIL import ImageTk
#import PIL.Image as Image
from PIL import Image
import time
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import os
import subprocess
from tkinter import ttk

speech_engine = pyttsx.init()
class Wikipedia_show:
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self, command):

		def save_image(url_of_image):
			response = requests.get(url_of_image)
			url_split=url_of_image.split('.')
			file_end=url_split[len(url_split)-1]
			BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			wiki=os.path.join(BASE_DIR, 'wiki.jpg')
			with open(wiki, 'w') as f_w:
				f_w.write(str(response.content))
			file_path='wiki.jpg'
			file_name='wiki.'+str(file_end)
			if(os.path.isfile(file_name)):
				os.remove(file_name)
			try:
				start_popup=subprocess.Popen(["wget", "-O",file_name, url_of_image])
			except Exception as e:
				print(url_of_image)
				print(e)
			time.sleep(10)
			place_image(file_name)

		def place_image(file_name):
			load = Image.open(file_name)
			image_final=load.resize((450,300), Image.ANTIALIAS)
			render = ImageTk.PhotoImage(image_final)
			img = Label(FrameWiki, image=render, width=450, height=300, background="black")
			img.image = render
			img.place(x=1100, y=350)

		def govor(besedilo):
			speech_engine.say(besedilo)
			speech_engine.runAndWait()

		vpras=command
		print("Vprasanje: "+vpras)

		title=['']
		root=tk.Tk()
		tabControl = ttk.Notebook(root)
		tab1 = ttk.Frame(tabControl)
		tabControl.add(tab1, text ='Tab 1')
		tab2 = ttk.Frame(tabControl)
		tabControl.add(tab2, text ='Tab 2')
		tabControl.pack(expand = 1, fill ="both")
		root.geometry("1920x1080")
		FrameWiki=Canvas(root, background="black")
		FrameWiki.pack(fill=BOTH, expand= TRUE, anchor='w')
		try:
			wiki_api_url="https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageimages&exsentences=7&pithumbsize=500&exintro&explaintext&redirects=1&titles="+str(vpras.replace('_', ' '))#str(title[0])
			read_wiki=requests.get(wiki_api_url)
			wiki_response=json.loads(read_wiki.text)
			print(wiki_response)
			title=list(wiki_response['query']['pages'].values())[0]["title"]
			answer=list(wiki_response['query']['pages'].values())[0]["extract"]
			odgovor=''
			FrameWiki.create_text(600,300, text=title, fill="white", font=("verdana", 25, "bold"))
			FrameWiki.create_text(600,500,width=800, text=answer, fill='white', font=('verdana', 15))
			wiki_api_url=list(wiki_response['query']['pages'].values())[0]["thumbnail"]["source"]#"http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles="+str(vpras.replace('_', ' '))#str(title[0])
			print('WIKI_API: '+wiki_api_url)
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
except Exception  as e:
	print(e)