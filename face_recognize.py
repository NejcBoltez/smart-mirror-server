from types import FrameType
import cv2
import face_recognition
import os
import sys
import threading
from PIL import ImageTk
import PIL.Image
import time
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

def count_pics_for_user(user):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	image_dir=os.path.join(BASE_DIR, '../Users/'+user)
	count_files=0
	path, dirs, files = next(os.walk(image_dir))
	count_files = len(files)
	return count_files
def get_user_from_stream(frame):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	image_dir=os.path.join(BASE_DIR, '../Users')
	face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	faces = face_front.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
	user_name=''
	for (x, y, w, h) in faces:
		roi_color=frame[y:y+h, x:x+w]
		image_encoding = face_recognition.face_encodings(frame)[0]
		for root, dirs, files in os.walk(image_dir):
			for d in dirs:
				for root, dirs, files in os.walk(image_dir+'/'+d):
					for file in files:
						unknown_image = face_recognition.load_image_file(image_dir+'/'+d+'/'+file)
						unknown_encoding=face_recognition.face_encodings(unknown_image)
						if (len(unknown_encoding)>0):
							unknown_encoding1=face_recognition.face_encodings(unknown_image)[0]
							results=face_recognition.compare_faces([image_encoding], unknown_encoding1)
							if results[0]:
								if (user_name==''):
									user_name=d
								root, dirs, files = next(os.walk(image_dir+'/'+d))
								file_count = len(files)
								img_item=str(image_dir)+'/'+d+'/'+d+'_'+str(file_count+1)+'.jpg'
								cv2.imwrite(img_item, roi_color)
								break
							else:
								continue
		
		print(user_name)
		return user_name
def save_images(self, f_faces, user):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	image_dir=os.path.join(BASE_DIR, '../Users')
	file_count=count_pics_for_user(user)
	print(f_faces)
	for f in f_faces:
		print(f)
		f_split=str(f).replace("'","").split(",")
		try:
			print(f_split)
			f_x=f_split[0]
			f_y=f_split[1]
			f_w=f_split[2]
			f_h=f_split[3]
			print(type(f_split[0]))
			roi_color=self.frame[f_y:f_y+f_h, f_x:f_x+f_w]
			new_file_count=file_count+1
			img_item2=image_dir+'/'+user+'/'+user+'_'+new_file_count+'.png'
			print(img_item2)

			#save the image
			cv2.imwrite(img_item2, roi_color)
		except Exception as e:
			print(e)
			continue

class User_auth_GUI (Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg='black')
		self.user_name=''
		self.main_label=Label(self, text="Calibrating the user123454321", font=('Helvetica', 60), fg='white', bg='black')
		self.main_label.pack(padx=20, pady=20)
		self.img = Label(self, width=700, height=700, bg="black")
		self.img.pack(padx=150, pady=150)
		self.cap = cv2.VideoCapture(-1)
		
		self.camera_stream=threading.Thread(target=self.get_camera_stream_calibrate)
		self.camera_stream.start()

	def get_camera_stream_calibrate(self):
		time.sleep(1)
		try:
			BASE_DIR= os.path.dirname(os.path.abspath(__file__))
			image_dir=os.path.join(BASE_DIR, '../Users')
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
			self.user_name=''
			self.count=0
			self.found_faces=[10]
			self.file_count=0
			#self.ret, self.frame = self.cap.read()
			#if (self.user_name==''):
			#	self.user_name=get_user_from_stream(self.frame)
			while(self.count<10):
				self.ret, self.frame = self.cap.read()
				print(self.user_name)
				if (self.user_name !='' and self.user_name != None):
					faces = face_front.detectMultiScale(self.frame, scaleFactor=1.5, minNeighbors=5)
					for (x, y, w, h) in faces:
						face_coordinates=str(x)+","+str(y)+","+str(w)+","+str(h)
						if face_coordinates not in self.found_faces:
							print (x,y,w,h)
							self.count+=1
							color=(255,0,0)
							stroke=2
							width=x+y
							height=y+h
							rectangle=cv2.rectangle(self.frame, (x, y), (width, height), color, stroke)
							cv2.putText(rectangle, self.user_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
							self.file_count=self.file_count+1
							self.found_faces.append(face_coordinates)
							print(self.count)
							
				else:
					self.user_name=get_user_from_stream(self.frame)
					self.main_label.config(text=self.user_name)
					#self.file_count=count_pics_for_user(self.user_name)
					#print(self.file_count)
					
				cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
				image = PIL.Image.fromarray(cv2image)
				render = ImageTk.PhotoImage(image=image)

				self.img.imgtk = render
				self.img.configure(image=render)
				#time.sleep(0.5)
				
		except:
			self.get_camera_stream_calibrate()
		self.cap.release()
		self.quit()
		save_images(self,self.found_faces,self.user_name)
class Get_face:
	def User_auth():
		cap = cv2.VideoCapture(0)
		user_name=''
		while(user_name==''):
			ret, frame = cap.read()
			user_name=get_user_from_stream(frame)
		cap.release()
		return user_name
		

	
class User_create():
    def __init (self, parent):
    	print('test')
class User_calibration(Frame):
	def __init__(self, parent, user):
		Frame.__init__(self, parent, bg='black')
		#self.win.configure(background='black')
		#self.win.title("Pozdravljeni")
		#self.win.geometry("1920x1080")
		self.user=user
		self.main_label=Label(self, text="Starting calibration for user "+self.user, font=('Helvetica', 60), fg='white', bg='black')
		self.main_label.pack(padx=20, pady=20)
		self.img = Label(self, width=700, height=700, bg="black")
		self.img.pack(padx=150, pady=150)
		self.cap = cv2.VideoCapture(-1)
		
		
		self.camera_stream=threading.Thread(target=self.get_camera_stream_calibrate)
		self.camera_stream.start()
		#self.win.mainloop()
		
		#cap = cv2.VideoCapture(0)
	def get_camera_stream_calibrate(self):
		time.sleep(1)
		'''try:
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		except:
			face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')'''
		face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		count=0
		self.found_faces=[10]
		
		while(count<10):
			self.ret, self.frame = self.cap.read()
			# Our operations on the frame come here
			gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

			faces = face_front.detectMultiScale(self.frame, scaleFactor=1.5, minNeighbors=5)
			# Display the resulting frame
			
			for (x, y, w, h) in faces:
				face_coordinates=str(x)+","+str(y)+","+str(w)+","+str(h)
				if face_coordinates not in self.found_faces:
					print (x,y,w,h)
					count+=1

					# frame
					color=(255,0,0)
					stroke=2
					width=x+y
					height=y+h
					rectangle=cv2.rectangle(self.frame, (x, y), (width, height), color, stroke)
					cv2.putText(rectangle, self.user, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
					self.found_faces.append(face_coordinates)
			cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
			image = PIL.Image.fromarray(cv2image)
			render = ImageTk.PhotoImage(image=image)

			self.img.imgtk = render
			self.img.configure(image=render)
				
		self.cap.release()
		time.sleep(2)
		save_images(self.found_faces,self.user)
		#self.win.destroy()
