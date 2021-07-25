import speech_recognition as sr
import subprocess
import os
import signal
import numpy as np
import cv2
import time
import multiprocessing
from multiprocessing import Queue
from face_recognize import Get_face
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
def check_for_user():
	new_user=Get_face.getUser()
	'''try:
		face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	except:
		face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# Capture frame-by-frame
	global user
	#global login
	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()
	tekst=''
	#detect face
	faces = face_front.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
		#tekst=str(x)+', '+str(y)+', '+str(w)+', '+str(h)
		
		#print (x)
		roi_color=frame[y:y+h, x:x+w]
		
		#image = face_recognition.load_image_file('./Images/stevejobs.png')
		image_encoding = face_recognition.face_encodings(frame)[0]
		#while (tekst==''):
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
								#print(file)
								tekst=d
								#print('tekst: '+tekst)
								#save the image
								path, dirs, files = next(os.walk(image_dir+'/'+d))
								file_count = len(files)
								print(d)
								#print(image_dir+'/'+d)
								#print(file_count)
								img_item2=str(image_dir)+'/Users/'+d+'/'+d+'_'+str(file_count+1)+'.jpg'
								cv2.imwrite(img_item2, roi_color)
								update_user(tekst)
								break# test
							else:
								continue
		user=tekst
		cap.release()'''
def new_user_name():
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
				user_create=Get_face.User_creation(user_name)
				#create_new_user(user_name)
			else:
				continue
		except OSError as error:
			print('test')
			#print(str(sys.exc_info()[0]))
			print(error)
			continue



def create_new_user(user_name):
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
'''
def listening():
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

for root, dirs, files in os.walk(image_dir):
	print(root)
	print(dirs)
	if len(dirs)==0 and len(files)==0:
		new_user_name()
		break
	else:
		listening()
		break'''
new_user_name()
#check_for_user()
