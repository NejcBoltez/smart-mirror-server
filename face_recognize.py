from types import FrameType
import cv2
import face_recognition
import os
import sys
import threading
from PIL import ImageTk
import PIL.Image
try:
	import tkinter as tk
	from tkinter import *
	#from tkinter import Frame
except:
	import Tkinter as tk
	from Tkinter import *
	from Tkinter import Frame


class Get_face:
	def User_auth():
		BASE_DIR= os.path.dirname(os.path.abspath(__file__))
		image_dir=os.path.join(BASE_DIR, '../Users')
			# .local is inside home directory
		try:
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		except:
			face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
		# Capture frame-by-frame
		#global login
		cap = cv2.VideoCapture(-1)
		ret, frame = cap.read()
		user_name=''
		#detect face
		faces = face_front.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
		for (x, y, w, h) in faces:
			#user_name=str(x)+', '+str(y)+', '+str(w)+', '+str(h)
			
			#print (x)
			roi_color=frame[y:y+h, x:x+w]
			
			#image = face_recognition.load_image_file('./Images/stevejobs.png')
			image_encoding = face_recognition.face_encodings(frame)[0]
			#while (user_name==''):
			for root, dirs, files in os.walk(image_dir):
				for d in dirs:
					print(d)
					#print(image_dir+'/'+d)
					for root, dirs, files in os.walk(image_dir+'/'+d):
						print(files)
						for file in files:
							#print('File: '+file)
							unknown_image = face_recognition.load_image_file(image_dir+'/'+d+'/'+file)
							#print(unknown_image)
							unknown_encoding=face_recognition.face_encodings(unknown_image)
							#print(len(unknown_encoding))
							if (len(unknown_encoding)>0):
								unknown_encoding1=face_recognition.face_encodings(unknown_image)[0]

								results=face_recognition.compare_faces([image_encoding], unknown_encoding1)

								if results[0]:
									user_name=d
									print(user_name)
									path, dirs, files = next(os.walk(image_dir+'/'+d))
									file_count = len(files)
									print(d)
									img_item2=str(image_dir)+'/Users/'+d+'/'+d+'_'+str(file_count+1)+'.jpg'
									cv2.imwrite(img_item2, roi_color)
									break# test
								else:
									continue
			#user=user_name
			cap.release()
			return user_name
			#return user

	
#class User_create:
	def user_create(user):
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
					img_item='../Users/'+user+'/'+user+'.png'

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

#class User_calibration:
	def user_calibration(self, user):
		self.win=tk.Tk()
		self.win.configure(background='black')
		self.win.title("Pozdravljeni")
		self.win.geometry("1920x1080")
		self.img = Label(self.win, width=700, height=700, bg="black")
		self.img.pack(padx=20, pady=20)
		self.cap = cv2.VideoCapture(-1)
		self.camera_stream=threading.Thread(target=self.get_camera_stream_calibrate(user))
		self.camera_stream.start()
		self.win.mainloop()
		
		#cap = cv2.VideoCapture(0)
	def get_camera_stream_calibrate(self,user):
		try:
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		except:
			face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
		
		
		# Capture frame-by-frame
		#ret, frame = cap.read()
		count=0
		found_faces=[10]
		
		while(count<10):
			self.ret, self.frame = self.cap.read()
			# Our operations on the frame come here
			gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

			faces = face_front.detectMultiScale(self.frame, scaleFactor=1.5, minNeighbors=5)
			# Display the resulting frame
			for (x, y, w, h) in faces:
				face_coordinates=str(x)+", "+str(y)+","+str(w)+", "+str(h)
				if face_coordinates not in found_faces:
					print (x,y,w,h)
					found_face=[w,h]
					count+=1
					roi_gray=gray[y:y+h, x:x+w]
					roi_color=self.frame[y:y+h, x:x+w]
					img_item1='jaz_gray.png'
					img_item2='jaz_color.png'

					#save the image
					cv2.imwrite(img_item1, roi_gray)
					cv2.imwrite(img_item2, roi_color)

					# frame
					color=(255,0,0)
					stroke=2
					width=x+y
					height=y+h
					cv2.rectangle(self.frame, (x, y), (width, height), color, stroke)
					found_faces.append(face_coordinates)

			cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
			image = PIL.Image.fromarray(cv2image)
			render = ImageTk.PhotoImage(image=image)

			self.img.imgtk = render
			self.img.configure(image=render)
		self.cap.release()
		
	def get_camera_stream(self):
		try:
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		except:
			face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
		
		
		# Capture frame-by-frame
		#ret, frame = cap.read()
		count=0
		found_faces=[10]
		
		while(count<10):
			self.ret, self.frame = self.cap.read()
			# Our operations on the frame come here
			gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

			faces = face_front.detectMultiScale(self.frame, scaleFactor=1.5, minNeighbors=5)
			# Display the resulting frame
			for (x, y, w, h) in faces:
				face_coordinates=str(x)+", "+str(y)+","+str(w)+", "+str(h)
				if face_coordinates not in found_faces:
					print (x,y,w,h)
					found_face=[w,h]
					count+=1
					roi_gray=gray[y:y+h, x:x+w]
					roi_color=self.frame[y:y+h, x:x+w]
					img_item1='jaz_gray.png'
					img_item2='jaz_color.png'

					#save the image
					cv2.imwrite(img_item1, roi_gray)
					cv2.imwrite(img_item2, roi_color)

					# frame
					color=(255,0,0)
					stroke=2
					width=x+y
					height=y+h
					cv2.rectangle(self.frame, (x, y), (width, height), color, stroke)
					found_faces.append(face_coordinates)

			cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
			image = PIL.Image.fromarray(cv2image)
			render = ImageTk.PhotoImage(image=image)

			self.img.imgtk = render
			self.img.configure(image=render)
		self.cap.release()