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
import numpy
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

def load_dataset(self, data_dir):
	datasets=data_dir
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
	
	(width, height) = (130, 100)

	# Create a Numpy array from the two lists above
	(images, labels) = [numpy.array(lis) for lis in [images, labels]]
	self.model = cv2.face.LBPHFaceRecognizer_create()
	self.model.train(images, labels)

def save_images(f_faces, user):
	BASE_DIR= os.path.dirname(os.path.abspath(__file__))
	save_image_dir=os.path.join(BASE_DIR, "../Users")
	t=time.strftime("%Y%m%d%H%M%S")
	new_file_count=count_pics_for_user(user)
	img_item2=save_image_dir+"/"+user+"/"+user+"_"+t+".png"
	while (new_file_count >= 100):
		last_mod_file=Work_with_files.get_last_mod_file(save_image_dir+"/"+user)
		Work_with_files.remove_file(last_mod_file)
		new_file_count=count_pics_for_user(user)
	cv2.imwrite(img_item2, f_faces)
	
def most_common(lst):
    return max(set(lst), key=lst.count)

class User_auth_GUI ():
	def main(self):
		self.main_label=Label(self, text="Recognizing the user.", font=("Helvetica", 60), fg="white", bg="black")
		self.main_label.pack(padx=20, pady=20)
		self.img = Label(self, width=700, height=700, bg="black")
		self.img.pack(padx=150, pady=150)
		self.user_name=""
		self.update()
		get_camera_stream_calibrate(self)
		return self.user_name

def get_camera_stream_calibrate(self):
	try:
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, "Users")
		width=130
		height=100
		datasets = image_dir

		# Create a list of images and a list of corresponding names
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
		(images, labels) = [numpy.array(lis) for lis in [images, labels]]
		
		# OpenCV trains a model from the images
		self.model = cv2.face.LBPHFaceRecognizer_create()
		self.model.train(images, labels)
		recognized_users=[]
		# Part 2: Use fisherRecognizer on camera stream
		haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
		face_front = cv2.CascadeClassifier(haar_file)
		record_cam = cv2.VideoCapture(0)
		while (len(recognized_users)<=10):
			(ret, self.video_frame) = record_cam.read()
			
			cv2image = cv2.cvtColor(self.video_frame, cv2.COLOR_BGR2RGBA)
			image_gray=cv2.cvtColor(self.video_frame, cv2.COLOR_BGR2GRAY)
			faces = face_front.detectMultiScale(image_gray, 1.89, 5)
			for (x, y, w, h) in faces:
				cv2.rectangle(self.video_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
				face = image_gray[y:y + h, x:x + w]
				face_color = cv2image[y:y + h, x:x + w]
				face_resize = cv2.resize(face, (width, height))
				# Try to recognize the face
				prediction = self.model.predict(face_resize)
		
				if prediction[1]<500:
					recognized_users.append(str(names[prediction[0]]))
					cv2.putText(self.video_frame, names[prediction[0]], (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (36,255,12), 2)
					self.take_picture=threading.Thread(target=save_images, args=(face_color, str(names[prediction[0]]),))
					self.take_picture.start()
			cv2image = cv2.cvtColor(self.video_frame, cv2.COLOR_BGR2RGBA)
			image = PIL.Image.fromarray(cv2image)
			render = ImageTk.PhotoImage(image=image)
			self.img.imgtk = render
			self.img.configure(image=render)
			self.update()
		self.user_name=most_common(recognized_users)
		print(self.user_name)
			
	except Exception as e:
		get_camera_stream_calibrate(self)
	record_cam.release()
	self.main_label.pack_forget()
	self.img.pack_forget()
	self.update()
