import os
#from PIL import ImageTk
#import PIL
import multiprocessing
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

from PIL import ImageTk
#import PIL.Image as Image
from PIL import Image

class show_pictures:
	def __call__():
		try: 
			print('test:     ')
		except:
			print('')
	def __init__(self,user):
		self.tk=tk.Tk()
		self.tk.geometry("1920x1000")
		#self.tk.overrideredirect(True)
		self.Frame=Frame(self.tk, background="red")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.Canvas=Canvas(self.Frame, background="yellow")
		self.Canvas.pack(fill=BOTH, expand=YES,padx=0,pady=0)
		#self.Canvas.grid(sticky=W)
		#self.pic=show_pictures(self.Canvas)
		#self.pic.pack(fill=BOTH, expand=YES)
		#Frame.__init__(self, parent)
		
		geox=100
		geoy=100
		count_in_row=0
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, '../taken_pictures/'+user)
		for root, dirs, files in os.walk(image_dir):
			for f in files:
				print(f)
				load=Image.open(image_dir+'/'+f)
				load.show()
				image_final=load.resize((300,250), Image.ANTIALIAS)
				render = ImageTk.PhotoImage(image_final)
				img = Label(self.Canvas, image=render, width=300, height=250, background="black")
				img.image = render
				img.place(x=geox, y=geoy)
				if(count_in_row==2):
					count_in_row=0
					geoy=geoy+500
					geox=100
				else:
					geox=geox+400
					count_in_row=count_in_row+1
				

		self.tk.mainloop()
		'''rows=4
		starty=0
		while(rows>0):
			startx=0
			for i in range(5):
				self.Frame.create_rectangle(startx,starty, startx+300, starty+350, fill="black", outline="white")
				startx=startx+350
			starty=starty+400
			rows=rows-1'''
			

class Window:
	def __init__(self):
		self.tk=tk.Tk()
		#self.tk.geometry("1920x1000")
		#self.tk.overrideredirect(True)
		self.Frame=Frame(self.tk, background="red")
		self.Frame.pack(fill=BOTH, expand=YES)
		self.Canvas=Canvas(self.Frame, background="yellow")
		#self.Canvas.pack(fill=BOTH, expand=YES,padx=0,pady=0)
		self.Canvas.grid(sticky=W)
		self.pic=show_pictures(self.Canvas)
		self.pic.pack(fill=BOTH, expand=YES)

root=show_pictures('nejc')
