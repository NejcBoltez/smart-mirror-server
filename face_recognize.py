import cv2
import face_recognition
import os
import threading
from PIL import ImageTk
import PIL.Image
import time
import numpy as np
from working_with_files import Work_with_files
import time
import asyncio
from multiprocessing import Process
import threading
from queue import Queue
try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *

def count_pics_for_user(user):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	image_dir=os.path.join(BASE_DIR, "../Users/"+user)
	count_files=0
	path, dirs, files = next(os.walk(image_dir))
	count_files = len(files)
	return count_files
def get_user_from_stream(self, loop, q):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	image_dir=os.path.join(BASE_DIR, "Users")
	datasets=image_dir
	self.face_front=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
	user_name=""
	faces = self.face_front.detectMultiScale(self.frame, scaleFactor=1.05, minNeighbors=6)	
	print("STARTING RECOGNITION: "+ time.strftime("%H:%M:%S"))
	
	tasks=[]
	#while(True):

	#Training model
	(images, labels, names, id) = ([], [], {}, 0)
	for (subdirs, dirs, files) in os.walk(datasets):
		for subdir in dirs:
			names[id] = subdir
			subjectpath = os.path.join(datasets, subdir)
			for filename in os.listdir(subjectpath):
				path = subjectpath + '/' + filename
				label = id
				images.append(cv2.imread(path, 0))
				labels.append(int(label))
			id += 1
	to_wait=0
	print("RECOGNIZE: "+self.user_name)
	if (self.user_name==""):
		#if (len(faces)==0):
		path, dirs, files = next(os.walk(image_dir))
		for d in dirs:
			if (self.user_name==""):
				print(d)
				#asyncio.run()
				to_wait=to_wait+1.25
				tasks.append(loop.create_task(check_for_user(self,image_dir,d,q, to_wait)))
				print("USER: "+self.user_name)
					#user_check.start()
			
		'''else:
			for (x, y, w, h) in faces:
				print("TEST")
				roi_color=frame[y:y+h, x:x+w]
				image_encoding = face_recognition.face_encodings(frame)[0]
				path, dirs, files = next(os.walk(image_dir))
				for d in dirs:
					if (self.user_name==""):
						#print(d)
						#user_check=threading.Thread(target=check_for_user, args=(self,image_dir,d,roi_color,image_encoding,))
						#user_check.start()
						
						#asyncio.run()
						to_wait=to_wait+1
						tasks.append(loop.create_task(check_for_user(self,image_dir,d,roi_color,image_encoding,to_wait)))
						#user_check.start()	'''
	#loop.run_until_complete(asyncio.gather(*tasks))
	#return self.user_name

async def check_for_user(self, img_dir, user_dir,queue, wait):
	print("USER_NAME: "+self.user_name)
	print("STARTING RECOGNITION 1: " + user_dir + "       " + time.strftime("%H:%M:%S"))
	path_users, dirs_users, files_users = next(os.walk(img_dir+"/"+user_dir))
	if (self.user_name==""):
		for file in files_users:
			cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)#cv2.COLOR_RGBA2BGR)
			image_gray=cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
			faces = self.face_front.detectMultiScale(image_gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))	
			print(faces)
			print ("CHECKING_FOR_USER: " + user_dir)
			await asyncio.sleep(wait/4)
			image = PIL.Image.fromarray(cv2image)
			render = ImageTk.PhotoImage(image=image)
			self.img.imgtk = render
			self.img.configure(image=render)
			self.update()
			print("IF:" +file)
			print(user_dir)
			#unknown_image = face_recognition.load_image_file(img_dir+"/"+user_dir+"/"+file)
			#unknown_encoding=face_recognition.face_encodings(unknown_image)
			for (x, y, w, h) in faces:
				roi_color=self.frame[y:y+h, x:x+w]
				image_encoding = face_recognition.face_encodings(self.frame)[0]
				face_coordinates=str(x)+","+str(y)+","+str(w)+","+str(h)
				print(face_coordinates)
				roi_color=self.frame[y:y+h, x:x+w]
				unknown_image = face_recognition.load_image_file(img_dir+'/'+user_dir+'/'+file)
				unknown_encoding=face_recognition.face_encodings(unknown_image)
				if (len(unknown_encoding)>0):
					unknown_encoding1=face_recognition.face_encodings(unknown_image)[0]
					results=face_recognition.compare_faces([image_encoding], unknown_encoding1)
					if results[0]:
						if (self.user_name==""):
							self.user_name=user_dir
							#queue.put(user_dir)
						root, dirs, files = next(os.walk(img_dir+'/'+user_dir))
						file_count = len(files)
						color=(255,0,0)
						stroke=2
						width=x+y
						height=y+h
						rectangle=cv2.rectangle(self.frame, (x, y), (width, height), color, stroke)
						img_item=str(img_dir)+'/'+user_dir+'/'+user_dir+'_'+str(file_count+1)+'.jpg'
						cv2.imwrite(img_item, roi_color)
						break
					else:
						continue
			else:
				break
	#return self.user_name
def save_images(self, f_faces, user):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	save_image_dir=os.path.join(BASE_DIR, "../Users")
	self.user=user
	for f in f_faces:
		f_split=str(f).replace("'","").split(",")
		try:
			f_x=f_split[0]
			f_y=f_split[1]
			f_w=f_split[2]
			f_h=f_split[3]
			roi_color=self.frame[int(f_y):int(f_y)+int(f_h), int(f_x):int(f_x)+int(f_w)]
			#self.user_name=get_user_from_stream(self, self.frame)
			#if (self.user_name == self.user):
			t=time.strftime("%Y%m%d%H%M%S")
			new_file_count=count_pics_for_user(self.user)
			while (new_file_count >= 100):
				last_mod_file=Work_with_files.get_last_mod_file(save_image_dir+"/"+self.user_name)
				Work_with_files.remove_file(last_mod_file)
				new_file_count=count_pics_for_user(self.user)
			img_item2=save_image_dir+"/"+user+"/"+user+"_"+t+".png"

			#save the image
			cv2.imwrite(img_item2, roi_color)
		except Exception as e:
			print(e)
			continue

class User_auth_GUI ():
	def main(self):
		#Frame.__init__(self, parent, bg="black")
		self.main_label=Label(self, text="Recognizing the user.", font=("Helvetica", 60), fg="white", bg="black")
		self.main_label.pack(padx=20, pady=20)
		self.img = Label(self, width=700, height=700, bg="black")
		self.img.pack(padx=150, pady=150)
		self.cap = cv2.VideoCapture(0)
		self.update()
		self.ret, self.frame = self.cap.read()
		self.camera_stream=threading.Thread(target=get_camera_stream_calibrate(self))
		self.camera_stream.start()
		#save_pic=Process(target=save_images, args=(self,self.found_faces,self.user_name,))
		#save_pic.start()
		return self.user_name
		#get_camera_stream_calibrate(self)

def get_camera_stream_calibrate(self):
	try:
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, "../Users")
		face_front=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
		self.count=0
		self.found_faces=[]
		self.file_count=0
		self.user_name=""
		loop = asyncio.get_event_loop()
		#loop.
		q=Queue()
		while(self.count<5):
			self.ret, self.frame = self.cap.read()
			cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
			image = PIL.Image.fromarray(cv2image)
			render = ImageTk.PhotoImage(image=image)
			self.img.imgtk = render
			self.img.configure(image=render)
			self.update()
			if (self.user_name !="" and self.user_name != None):
				faces = face_front.detectMultiScale(self.frame, scaleFactor=1.05, minNeighbors=6, minSize=(30, 30))
				for (x, y, w, h) in faces:
					face_coordinates=str(x)+","+str(y)+","+str(w)+","+str(h)
					if face_coordinates not in self.found_faces:
						try:
							self.count+=1
							color=(255,0,0)
							stroke=2
							width=x+y
							height=y+h
							rectangle=cv2.rectangle(self.frame, (x, y), (width, height), color, stroke)
							cv2.putText(rectangle, self.user_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
							self.file_count=self.file_count+1
							self.found_faces.append(face_coordinates)
						except Exception as e:
							print(e)
							
			else:
				#count_active_tasks = len(asyncio.all_tasks())
				'''running_threads=[]
				for thread in threading.enumerate(): 
					running_threads.append(thread.name)
					print(thread.name)
				print(running_threads)
				if (len(running_threads)==1):
					user_get=threading.Thread(name="user_recognize", target=get_user_from_stream, args=(self,loop,q,))
					user_get.start()
				else:
					#self.user_name=q.get()
					print("USER_NAME -------------------------->"+self.user_name)'''
				get_user_from_stream(self, loop,q)
				print("USER_NAME -------------------------->"+self.user_name)
				#self.main_label.config(text="Calibrating for user " + user_name)
			cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
			image = PIL.Image.fromarray(cv2image)
			render = ImageTk.PhotoImage(image=image)
			self.img.imgtk = render
			self.img.configure(image=render)
			self.update()
			
	except Exception as e:
		#print("TESTING"+str(e))
		get_camera_stream_calibrate(self)
		#self.get_camera_stream_calibrate()
	self.main_label.config(text="Please wait while saving pictures")
	self.cap.release()
	self.main_label.pack_forget()
	self.img.pack_forget()
	self.update()
