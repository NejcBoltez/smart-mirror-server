try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
#import wikipedia

#import requests
import json
from PIL import ImageTk
from PIL import Image
import os
import subprocess
from tkinter import ttk
import sys
from urllib import request
from urllib import parse

class Wikipedia_show:
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	
	def main(self, command, tabControl):
		def save_image(url_of_image):
			url_split=url_of_image.split('.')
			file_end=url_split[len(url_split)-1]
			BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			wiki=os.path.join(BASE_DIR, './wiki_pictures/wiki.jpg')
			file_name='./wiki_pictures/wiki.'+str(file_end)
			if(os.path.isfile(file_name)):
				os.remove(file_name)
			try:
				start_popup=subprocess.Popen(["wget", "-O",file_name, url_of_image])
				start_popup.wait()
			except Exception as e:
				print(e)
			place_image(file_name)

		def place_image(file_name):
			load = Image.open(file_name)
			image_final=load.resize((500,400), Image.ANTIALIAS)
			render = ImageTk.PhotoImage(image_final)
			img = Label(FrameWiki, image=render, width=500, height=400, background="black")
			img.image = render
			img.place(x=1100, y=300)

		question=command

		title=['']
		FrameWiki=Canvas(tabControl, bg="black", width=400, height=280)
		FrameWiki.pack(fill=BOTH, expand= TRUE)
		wiki_tab = ttk.Frame(tabControl)
		tabControl.add(FrameWiki, text ="WIKIPEDIA")
		tabControl.select(len(tabControl.tabs())-1)
		try:
			wiki_api_url="https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageimages&exsentences=6&pithumbsize=500&exintro&explaintext&redirects=1&titles="+str(question.replace('_', '%20'))#str(title[0])
			print(wiki_api_url)
			with request.urlopen(wiki_api_url) as wiki_resp:
				read_wiki=json.loads(wiki_resp.read().decode())
				print("TEST")
				print(read_wiki)
			
			wiki_response=read_wiki#json.loads(read_wiki.text)
			print(wiki_response)
			title=list(wiki_response["query"]["pages"].values())[0]["title"]
			answer=list(wiki_response["query"]["pages"].values())[0]["extract"]
			FrameWiki.create_text(600,300, text=title, fill="white", font=("verdana", 25, "bold"))
			FrameWiki.create_text(600,500,width=800, text=answer, fill='white', font=('verdana', 15))
			print(wiki_response["query"]["pages"].values())
			wiki_api_url=list(wiki_response["query"]["pages"].values())[0]["thumbnail"]["source"]
			print('WIKI_API: '+wiki_api_url)
			print(type(wiki_api_url))
			save_image(wiki_api_url)
		except Exception as e:#wikipedia.exceptions.PageError as e:
			'''possible_matches=wikipedia.search(question.replace('_', ' '))
			matches=""
			for i in possible_matches:
				matches = matches + i + '\n'
			'''
			print(e)
			FrameWiki.create_text(600,300, text="Sorry no matches for '"+question.replace('_',' ') + "'", fill="white", font=("verdana", 25, "bold"))
			'''FrameWiki.create_text(600,350,width=80, text="Here are some other possible matches", fill='white', font=('verdana', 15, "bold"))
			FrameWiki.create_text(650,500,width=800, text=matches, fill='white', font=('verdana', 15))'''
		
class Window:
	def __init__(self, user):
		self.tk=tk.Tk()
		self.tk.configure(background="black")
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		self.Frame=Frame(self.tk, background="black")
		self.Frame.pack(fill=BOTH, expand=YES)
		tabControl = ttk.Notebook(self.Frame, height=100)
		tabControl.pack(expand = 1, fill ="both")
		self.recognize(user, tabControl)
		self.tk.update()
		self.tk.mainloop()

	def recognize(self, user, tabControl):
		cam=Wikipedia_show.main(self.Frame, user, tabControl)
		#cam.pack()


#arguments = list(sys.argv)	
#win=Window(arguments[1])