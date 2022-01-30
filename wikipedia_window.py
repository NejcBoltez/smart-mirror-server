try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import wikipedia

import sys
import requests
import json
from PIL import ImageTk
from PIL import Image
import os
import subprocess
from tkinter import ttk


class Wikipedia_show:
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self, command, tabControl):
		def save_image(url_of_image):
			response = requests.get(url_of_image)
			url_split=url_of_image.split('.')
			file_end=url_split[len(url_split)-1]
			BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			wiki=os.path.join(BASE_DIR, './wiki_pictures/wiki.jpg')
			with open(wiki, 'w') as f_w:
				f_w.write(str(response.content))
			file_path='wiki.jpg'
			file_name='./wiki_pictures/wiki.'+str(file_end)
			if(os.path.isfile(file_name)):
				os.remove(file_name)
			try:
				start_popup=subprocess.Popen(["wget", "-O",file_name, url_of_image])
				start_popup.wait() #WAIT FOR THE PROCESS TO FINISH
			except Exception as e:
				print(url_of_image)
				print(e)
			#time.sleep(0.1)
			place_image(file_name)

		def place_image(file_name):
			load = Image.open(file_name)
			image_final=load.resize((500,400), Image.ANTIALIAS)
			render = ImageTk.PhotoImage(image_final)
			img = Label(FrameWiki, image=render, width=500, height=400, background="black")
			img.image = render
			img.place(x=1100, y=300)

		vpras=command

		title=['']
		print(vpras)
		#root=tk.Tk()
		#root.geometry("1920x1080")
		#tabControl = ttk.Notebook(root)
		#tabControl.pack(expand = 1, fill ="both")
		
		#root.attributes('-fullscreen', True)  
		#root.fullScreenState = False
		FrameWiki=Canvas(tabControl, background="black", width=400, height=280)
		FrameWiki.pack(fill=BOTH, expand= TRUE)
		tab = ttk.Frame(tabControl)
		tabControl.add(FrameWiki, text ='WIKIPEDIA')
		tabControl.select(len(tabControl.tabs())-1)
		try:
			wiki_api_url="https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageimages&exsentences=7&pithumbsize=500&exintro&explaintext&redirects=1&titles="+str(vpras.replace('_', ' '))#str(title[0])
			print(wiki_api_url)
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
		
		#root.mainloop()
'''arguments = list(sys.argv)
try:
	Wikipedia_show(arguments[1])
except Exception  as e:
	print(e)'''