import tkinter as tk
from tkinter import *

class Popup_window:
	def __init__(self):	
		self.popup = tk.Tk()
		self.popup.title("LISTENING")
		self.popup.geometry("600x200")
		self.popup.configure(bg="black")
		self.label = tk.Label(self.popup,font=("Helvetica", 15), text="PLEASE SAY SOMETHING LIKE: ", bg="black",fg="white")
		self.label.pack(side="top", fill="x")
		self.labelText = tk.Label(self.popup,font=("Helvetica", 15), text="- SEARCH YOUTUBE FOR ...\n- SEARCH WIKIPEDIA FOR ...\n- SHOW ME THE FORECAST FOR ...\n- SHOW ME THE NEWS\n- CLOSE WINDOW\n- EXIT APPLICATION", bg="black",fg="white")
		self.labelText.pack(side="top", fill="x", pady=11)
		self.textSaid=tk.Label(self.popup, text="", bg="black",fg="white")
		self.textSaid.pack(side="top", fill="x", pady=80)
		self.popup.lift()
		self.popup.mainloop()
	
	def change_what_is_said(self, text):
		self.textSaid.config(text=text)
	
	def close(self):
		self.destroy()

Popup_window()
