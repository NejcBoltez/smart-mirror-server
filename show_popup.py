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
		self.popup.geometry("500x200")
		self.popup.configure(bg="black")
		self.label = tk.Label(self.popup, text="Start to listen", bg="black",fg="white")
		self.label.pack(side="top", fill="x", pady=10)
		self.labelText = tk.Label(self.popup, text="Search youtube for ...\n Search Wikipedia for ...\n Show me the forecast for tommorow \n Show me the news", bg="black",fg="white")
		self.labelText.pack(side="top", fill="x", pady=20)
		self.popup.lift()
		self.popup.mainloop()
#Popup_window()
