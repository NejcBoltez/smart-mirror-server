import speech_recognition as sr
import subprocess
import os
import signal
import numpy as np
import cv2
import time
import multiprocessing
from multiprocessing import Queue
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *


listen=0
r = sr.Recognizer()
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Users')
class Create_new_user(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.label=Label(self, font=('Helvetica', 30), fg="white", bg="black", text='Plase say or spell your name without spaces')
		self.label.pack()
		self.get_user_name=Label(self, font=('Helvetica', 30), fg="white", bg="black", text='')
		#time.sleep(5)

		#self.get_user_name.after(1000,self.new_user_name())
		self.get_user_name.bind('<Map>', self.new_user_name())
	def new_user_name(self):
		user_name=''
		while user_name=='':
			with sr.Microphone() as source:
				print("Plase say your name without spaces")
				#q=Queue()
				#print(q.get())
				print(Frame)
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				#audio = r.adjust_for_ambient_noise(source)
				print(audio)
				# recognize speech using Google Speech Recognition

			try:
				# for testing purposes, you're just using the default API key
				# to use another API key, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
				# instead of `r.recognize_google(audio)`
				print("Your name would be " + r.recognize_google(audio).replace(' ', '') + ".Is that OK?")
				user_test=r.recognize_google(audio).replace(' ', '')
				self.get_user_name.configure(text=user_test)
				with sr.Microphone() as source:
					print("Plase say your name without spaces")
					#q=Queue()
					#print(q.get())
					print(Frame)
					r.adjust_for_ambient_noise(source)
					audio = r.listen(source)
					#audio = r.adjust_for_ambient_noise(source)
					print(audio)
				ok_name=r.recognize_google(audio).replace(' ', '')
				if('yes' in ok_name):
					print('Good name')
					user_name=user_test
					dir_path=str(image_dir)+'/'+str(user_name)
					os.mkdir(dir_path)
					os.chmod(dir_path, 0o777)
					self.create_first_user(user_name)
				else:
					continue
			except OSError as error:
				print('test')
				print(str(sys.exc_info()[0]))
				print(error)
				continue
		self.unbind('<Map>')




	def create_first_user(user_name):
		#try:
		#	face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		#except:
		face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
		cap = cv2.VideoCapture(-1)

		ret, frame = cap.read()
		count=0
		found_faces=[10]
		while(count<10):
			# Capture frame-by-frame
			ret, frame = cap.read()

			# Our operations on the frame come here
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			faces = face_front.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
			# Display the resulting frame
			for (x, y, w, h) in faces:
				face_coordinates=str(x)+", "+str(y)+","+str(w)+", "+str(h)
				if face_coordinates not in found_faces:
					print (x,y,w,h)
					found_face=[w,h]
					count+=1
					roi_gray=gray[y:y+h, x:x+w]
					roi_color=frame[y:y+h, x:x+w]
					img_item='../Users/'+user_name+'/'+user_name+'.png'

					#save the image
					cv2.imwrite(img_item, roi_color)

					# frame
					color=(255,0,0)
					stroke=2
					width=x+y
					height=y+h
					cv2.rectangle(frame, (x, y), (width, height), color, stroke)
					found_faces.append(face_coordinates)


				#recognize
			#time.sleep(100)
			cv2.imshow('frame',frame)
			#cv2.moveWindow(winname, 500,500)
			if (cv2.waitKey(1) & 0xFF == ord('q')) or sys.stdin == str.encode('q') :
				break

		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()

class new_user_GUI:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background='black')
		self.Frame.pack(fill=BOTH, expand=YES)
		self.Canvas=Canvas(self.Frame, background='red', width='450', height='150')
		self.Canvas.pack(pady='300')
		self.create_user_rectangle=Create_new_user(self.Canvas)

def start_listening():
	while (True):
		with sr.Microphone() as source:
			print("Say something1234!")
			#q=Queue()
			#print(q.get())
			print(Frame)
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
			#audio = r.adjust_for_ambient_noise(source)
			print(audio)
			# recognize speech using Google Speech Recognition

		try:
			# for testing purposes, you're just using the default API key
			# to use another API key, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
			# instead of `r.recognize_google(audio)`
			print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
			razgovor=r.recognize_google(audio).lower()
			razgovor_search=""
			if('mirror' in razgovor):
				Open_yt_search=subprocess.Popen(["python3","SmartMirror.py"])
				break
		except OSError as error:
			print('test')
			print(str(sys.exc_info()[0]))
			print(error)
			continue


window=new_user_GUI()
window.tk.mainloop()
'''for root, dirs, files in os.walk(image_dir):
	print(root)
	print(dirs)
	if len(dirs)==0 and len(files)==0:
		window=new_user_GUI()
		window.tk.mainloop()	
		break
	else:
		start_listening()
		break'''
