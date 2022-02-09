# importing tkinter module
from tkinter import * 
from tkinter import ttk
import time
import sys


arguments = list(sys.argv)
# creating tkinter window
root = Tk()
root.geometry("500x90")
# Progress bar widget
label=Label(root,font=("Helvetica", 12), fg="white", bg="black",text=arguments[1])
label.pack()
progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 500, mode = 'indeterminate')
  
# Function responsible for the updation
# of the progress bar value

def bar():
    while(True):
        x=0
        while (x<=100):
            progress['value'] = x
            print(x)
            root.update_idletasks()
            time.sleep(0.5)
            x=x+20
        i=100
        while (i>-1):
            progress['value'] = i
            print(i)
            root.update_idletasks()
            time.sleep(0.5)
            i=i-20
  
   
      
  
progress.pack(pady = 10, fill=BOTH, expand=YES)
  
# This button will initialize
# the progress bar
bar()
#Button(root, text = 'Start', command = bar).pack(pady = 10)
  
# infinite loop
mainloop()