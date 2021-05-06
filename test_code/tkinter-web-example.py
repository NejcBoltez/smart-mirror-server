from tkinterweb import HtmlFrame #import the HTML browser
try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2

root = tk.Tk() #create the tkinter window
frame = HtmlFrame(root) #create HTML browser
#frame.load_website("https://www.delo.si/novice/svet/odprte-obcinske-meje-in-vse-trgovine-ucenci-v-soli-ali-na-pocitnicah/") #load a website
frame.load_website("https://www.google.com/maps/place/8000+Novo+mesto/@45.8035832,15.1346662,13z/data=!3m1!4b1!4m8!1m2!2m1!1sgoogle+maps!3m4!1s0x47645557e323d15f:0x102d55e340217bd4!8m2!3d45.8010824!4d15.1710089")
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()
