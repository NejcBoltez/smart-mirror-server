import os
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

class Popup_window:
	def __init__(self):	
		print("POPUP WINDOW")
		self.popup = tk.Tk()
		self.popup.geometry("500x100")
		self.label = tk.Label(self.popup, text='Start to listen')
		self.label.pack(side="top", fill="x", pady=10)
		self.popup.mainloop()
	def close(self):
		self.popup.destroy()
Popup_window()
