import time
import os
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

class Timer():
	def __call__(args):
		try: 
			print('test:     '+args)
		except:
			print('')
	def __init__(self, command):
        root=tk.Tk()
		root.title("Timer")
        root.geometry("100x100")
