from tkinterweb import HtmlFrame #import the HTML browser
try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2

root = tk.Tk() #create the tkinter window
frame = HtmlFrame(root) #create HTML browser
frame.load_website("https://www.delo.si/novice/svet/odprte-obcinske-meje-in-vse-trgovine-ucenci-v-soli-ali-na-pocitnicah/") #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()
