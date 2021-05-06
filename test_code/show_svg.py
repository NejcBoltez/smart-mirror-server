import tkinter as tk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk
 
def get_svg(svg_file):
	drawing = svg2rlg(svg_file)
	renderPM.drawToFile(drawing, "wiki.png", fmt="PNG")
 
 
 
class Root:
	def __init__(self):
		root = tk.Tk()
		img = Image.open("wiki.png")
		pimg = ImageTk.PhotoImage(img)
		size = img.size
		frame = tk.Canvas(root, background="black")
		frame.pack()
		frame.create_image(0,0,anchor='nw',image=pimg)
		root.mainloop()
 
get_svg("belgian.svg")
root = Root()