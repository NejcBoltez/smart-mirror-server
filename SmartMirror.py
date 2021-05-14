try:
	import tkinter as tk
	from tkinter import *
except:
	import Tkinter as tk
	from Tkinter import *
import time
import json
import requests
import urllib
import cv2
import numpy as np
from urllib3 import *
from PIL import Image, ImageTk
import dlib
import os
import face_recognition
import pyttsx3 as pyttsx
import speech_recognition as sr
import subprocess #as call
import posluh1 as listening
from multiprocessing import Queue
import multiprocessing
import speech_recognition as sr
import threading
import send_command




BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Users')
user = ''
speech_engine = pyttsx.init()
#q=Queue()
#q.cancel_join_thread()
#global listening_bool
global Queue_listening
#listening_bool='False'
Queue_listening=Queue()
def get_api_keys():
	api_keys_dir=os.path.join(BASE_DIR, '../api_keys.json')
	with open(api_keys_dir, 'r') as f:
		d=json.load(f)
	#print(len(d))
	#print(d['weather_api'])
	return d
class Asistant(Frame):
	def __init__(self, parent, *args, **kwargs):
		#global Queue_listening
		#if (len(self.listening_bool)==0):
		#	self.listening_bool=False
		self.listening_bool : str
		Frame.__init__(self, parent, bg='black')
		#self.q=Queue()
		self.PosluhFrame=Label(self, font=('Helvetica', 40), fg="white", bg="yellow", text=user)
		self.PosluhFrame.pack(side=RIGHT)
		#self.text_wid = Text(self, height=100,width=100)
		#self.text_wid.pack(expand=YES,fill=BOTH)
		#self.text_label=Label(self, font=('Helvetica', 40), fg="white", bg="yellow", text='')
		#self.text_label.pack()
		#self.getPosluh()
		#self.after(1000,self.check_if_listening(self.q))
		#self.text_wid.after(100, self.check_if_listening(self.q))#(Queue_listening))
		#self.callListen=0
		#if (self.callListen==0):
		self.getPosluh()
		#self.PosluhFrame.after(3000,self.getPosluh)
		#	self.callListen=self.callListen+1
		#self.getPosluh()
		#self.Listening_test()
		#finally:
		#	self.text_wid.after(100, self.check_if_listening(q))
		#self.check_if_listening()
		#self.after(1000,self.check_if_listening(Queue_listening))
	'''def check_if_listening(self, test):#,q):
		#global Queue_listening,
		#global listening_bool
		print('TEST!"#$%&/')
		#listen_bool=self.get_list_bool()
		#q=Queue_listening
		#Queue_listening.cancel_join_thread()
		#print('TESTS QUEUE VALUE:' + q.get(1))
		q_value=test
		print('fdbsahfgzewrskcb xvbyxsaj')
		try:
			#print(q.get(0))
			#for i in range(20):
			#	print(q.get(i))
			print('dsajdklsadfhas')
			print('listen_bool 123456 ------------>' + test)
			#print(Queue_listening.qsize())
			#if(str(Queue_listening.empty())=='false'):
			#	q_value = str(Queue_listening.get(1))#"test1234$(&/"#Queue_listening.get(1)
			#else:
			#	q_value=str(listening_bool)
			print('IT WORKS, OH YEAH')
			print(q_value)
			self.text_wid.insert('end',q_value)
		except:
			print('QUEUE IS EMPTY')
			pass
		#self.after(2000,self.check_if_listening)
		'''
	def getPosluh(self):
		#AI()
		#Listen=subprocess.Popen(["python3", "posluh1.py", self.parent])
		#subprocess.Popen(["python3", "posluh1.py"])
		print('TEST123')
		my_thread=threading.Thread(target=self.Listening_test)
		my_thread.start()
		#print('test123')
		
		#self.q.put([self])

		'''self.start_listening=multiprocessing.Process(name="listen_function", target=listening.Listen,args=(self.PosluhFrame,))
		self.start_listening.start()
		self.q=multiprocessing.Queue()
		print('TEST')
		self.start_listening=multiprocessing.Process(name="listen_function", target=self.listening_function, args=(self.q,))
		self.start_listening.start()
		print('TEST ---->>>>' + self.q.get(1))
		self.check_if_listening(str(self.q.get(1)))'''
		#self.start_listening.map()




		#self.start_listening.lock()
		#self.start_listening.join()
		#self.start_listening=Listen(self)
		#self.start_listening.pack()
		#listen_value=Listen.communicate()[0]
		#print(listen_value)
		#with subprocess.Popen(["python3", "posluh1.py"]) as Listen:#, "test"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
			#if (Listen.communicate())
		#    listen_value=Listen.communicate()[0]
		#    print(listen_value)
	'''def set_list_bool(self,value):
		#global listening_bool
		self.listening_bool=value
		print('listening_bool kfldosfoids: --------->>>>>' + str(self.listening_bool))
		return self.listening_bool
	def print_list_bool(self):
		#global listening_bool
		print('listening_bool: --------->>>>>' + str(self.listening_bool))
	def get_list_bool(self):
		global listening_bool
		print('listening_bool 987654: --------->>>>>' + str(self.listening_bool))
		return self.listening_bool'''
	def listening_function(self):#,Queue_listening):
		#global Queue_listening
		#global listening_bool
		#global text_listening
		r = sr.Recognizer()
		#Frame.__init__(self, parent, bg='black')
		#self.label_listen=Label(self, font=('Helvetica', 100), fg="white", bg="purple", text="THIS IS A STRING")
		#self.label_listen.pack()#side=TOP,anchor=E)
		#while(True):
		razgovor=''
		#print('OK')
		
		#while listened<5:

		#while razgovor=='':
		with sr.Microphone() as source:
			print("Say something12345678!")
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
			# to use another API ke, use `r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
			# instead of `r.recognize_google(audio)`
			print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
			razgovor=r.recognize_google(audio).lower()
			razgovor_search=""
			
			if ("mirror" in razgovor):
				#global Queue_listening
				#global listening_bool
				print('LETS GO')
				#self.label_listen.config(text="DELA TO MI DELI")
				#listen=1
				#text_listening.insert("end","OK start listening")
				Queue_listening.put("listening")
				send_command_thread=threading.Thread(target=send_command.Do_for_command(razgovor))
				send_command_thread.start()
				#Queue_listening.
				#listening_bool='True'
				print(Queue_listening.get(1))
				#return Queue_listening, listening_bool
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
			#listened+=1
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service;{0}".format(e))
			#listened+=1
		#return Queue_listening, listening_bool
		return razgovor
	def Listening_test(self):
		while(True):
			l=self.listening_function()
			'''self.set_list_bool(l)
			self.print_list_bool()'''
			#self.check_if_listening(l)
			self.PosluhFrame.config(text=str(l))

class Ura(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.label1=Label(self, font=('Helvetica', 100), fg="white", bg="black")
		self.label1.pack(side=TOP,anchor=E)
		self.dan=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.dan.pack()
		self.pozdrav=Label(self, font=('Helvetica', 15), fg="white", bg="black")
		self.pozdrav.pack()
		self.klik()
	def klik(self):
		ti=time.strftime('%H:%M:%S')
		dan=time.strftime('%A')
		self.update_clock(ti,dan)
		#print('TEST: ' + ti)
		# calls itself every 1000 milliseconds to update the time display as needed could use >200 ms, but display gets jerky
		self.label1.after(1000, self.klik)
	def update_clock(self,ti,dan):
		self.label1.config(text=ti)
		self.dan.config(text=dan)
class Vreme(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.LabelMain=Label(self, font=('Helvetica', 30), fg='white', bg='black', text="Vreme:")
		self.LabelMain.pack()
		self.label1=Label(self, font=('Helvetica', 25), fg="white", bg="black")
		self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getVreme()
		self.label1.after(10000, self.getVreme)
	def getVreme(self):
		City = "Novo mesto"
		Country = "SI"
		get_api=get_api_keys()
		APIK=get_api['weather_api']
		URL = "https://api.openweathermap.org/data/2.5/weather?q="+City+","+Country+"&appid="+APIK
		r = requests.get(URL)
		preberi = r.json()
		temp="Temp: " + str(preberi['main']['temp'])
		humidity="Humidity: " + str(preberi['main']['humidity'])
		temp_min="Temp_min: " + str(preberi['main']['temp_min'])
		temp_max="Temp_max: " + str(preberi['main']['temp_max'])
		weather=temp +'\n' + humidity + '\n' + temp_min + '\n' + temp_max
		self.update_weather(weather)
	def update_weather(self,data):
		self.label1.config(text=data)
class Novice(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, bg='black')
		self.NewsFrame=Frame(self, background='Black')
		self.NewsFrame.pack(side=RIGHT)
		self.labelMain=Label(self.NewsFrame, font=('Helvetica', 30), fg='white', bg='black', text="Novice:")
		self.labelMain.pack()
		self.label1=Label(self.NewsFrame, font=('Helvetica', 12), fg="white", bg="black")
		self.label1.pack(side=LEFT, fill=BOTH, expand= TRUE, anchor='w')
		self.getNovice()
		self.label1.after(100000, self.getNovice)
	def getNovice(self):
		NewsList=[]
		Novice=""
		News=""
		IzborNovic=""
		get_api=get_api_keys()
		APIK=get_api['news_api']
		URLnews = "https://newsapi.org/v2/top-headlines?country=si&apiKey="+APIK
		News=requests.get(URLnews)
		Novice=News.json()
		NewsList=Novice['articles']
		for i in NewsList:
			Nov = str(i['title']).split("- ")
			#print(Nov)
			#if (Nov[1]=='24ur.com' or Nov[1]=='RTV Slovenija' or Nov[1]=='Računalniške Novice' or Nov[1]=='Siol.net'):
				#self.label1.config(text="")
			IzborNovic+=str(i['title']) + '\n'
			#if len(IzborNovic) == 5:
			#	break
		   # else:
			#    continue
		self.update_news(IzborNovic)
	def update_news(self,data):
		self.label1.config(text=data)
'''class Is_Listening(Frame):
	def __init__(self, parent, *args, **kwargs):
		global Queue_listening
		Frame.__init__(self, parent, bg='black')
		self.PosluhFrame=Label(self, font=('Helvetica', 40), fg="white", bg="yellow", text=user)
		self.PosluhFrame.pack(side=RIGHT)
		self.text_wid = Text(self,height=100,width=100)
		self.text_wid.pack(expand=YES,fill=BOTH)
		self.check_if_listening()
		#self.after(1000,self.check_if_listening(Queue_listening))
	def check_if_listening(self):#,q):
		#global Queue_listening,
		global listening_bool
		print('TEST!"#$%&/')
		listen_bool=get_list_bool()
		#q=Queue_listening
		Queue_listening.cancel_join_thread()
		#print('TESTS QUEUE VALUE:' + q.get(1))
		q_value=""
		print('fdbsahfgzewrskcb xvbyxsaj')
		try:
			#print(q.get(0))
			#for i in range(20):
			#	print(q.get(i))
			print('dsajdklsadfhas')
			print('listen_bool 123456 ------------>' + listen_bool)
			print(Queue_listening.qsize())
			if(str(Queue_listening.empty())=='false'):
				q_value = str(Queue_listening.get(1))#"test1234$(&/"#Queue_listening.get(1)
			else:
				q_value=str(listening_bool)
			print('IT WORKS, OH YEAH')
			print(q_value)
			self.text_wid.insert('end',q_value)
		except:
			print('QUEUE IS EMPTY')
			pass
		self.after(2000,self.check_if_listening)'''


		
class Camera(Frame):
	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, background='Black')
		self.pack(side=LEFT, fill=BOTH, expand=YES)
		self.CamFrame=Frame(self, background='Black')
		self.CamFrame.pack(side=TOP,anchor=E)
		self.labelMain=Label(self.CamFrame, font=('Helvetica', 60), fg='white', bg='black', text="Please LOGIN")
		self.labelMain.pack(anchor='w')
		self.label1=Label(self.CamFrame, font=('Helvetica', 9), fg="white", bg="black")
		self.label1.pack(anchor='w')
		self.get_home()
		#self.getCamera()
	def getCamera(self):
		# .local is inside home directory
		try:
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
									self.update_user(tekst)
									break# test
								else:
									continue
							
			#cv2.imwrite(img_item2, roi_color)
			
			#this.user=tekst
			#self.home_window()
			user=tekst
			#self.labelMain.after(700, self.home_window)
			#home=Okno()
#             root.destroy()
			#home.tk.mainloop()
			cap.release()
			self.get_home()
			#self.labelMain.after(100, self.get_home())
			#self.labelMain.after(1000, AI())
			
		if len(faces)==0:
			self.label1.config(text='Prazno')
			self.label1.after(600, self.getCamera)
	def update_user(self,user):
		teskst123='Pozdravljen ' + user
		self.labelMain.config(text=teskst123)
		self.label1.config(text=user)

	def get_home(self):
		#time.sleep(10)
		self.labelMain.config(text='')
		self.TopFrame = Frame(self, background='red')
		self.BottomFrame = Frame(self, background='yellow')
		self.TopLeftFrame=Frame(self.TopFrame, background='red')
		self.BottomLeftFrame=Frame(self.BottomFrame, background='yellow')
		self.TopRightFrame=Frame(self.TopFrame, background='red')
		self.BottomRightFrame=Frame(self.BottomFrame, background='yellow')
		
		self.TopFrame.pack(side=TOP, fill=BOTH, expand=YES)
		#self.BottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
		self.TopLeftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
		#self.BottomLeftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
		self.TopRightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)
		#self.BottomRightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)

		self.ura=Ura(self.TopRightFrame)
		self.ura.pack(side=RIGHT)
		self.vreme=Vreme(self.TopLeftFrame)
		self.vreme.pack(side=LEFT)
		#self.news=Novice(self.BottomRightFrame)
		#self.news.pack(side=RIGHT, fill=BOTH, expand=YES)
		self.news=Novice(self)
		self.news.pack(side=BOTTOM)
		#self.label1234=Label(self.BottomFrame, text="Hello2", fg="white", bg="black")
		#self.label1234.pack()
		#self.cam=Label(self.BottomFrame, text="Hello234", fg="white", bg="black")
		#self.cam.pack()
		self.asistant=Asistant(self)
		self.asistant.pack(side=TOP)
		#self.is_listening=Is_Listening(self)
		#self.is_listening.pack(side=BOTTOM)
		
class Okno:
	def __init__(self):
		self.tk=tk.Tk()
		self.tk.configure(background='black')
		self.tk.title("Pozdravljeni")
		self.tk.geometry("1920x1000")
		#self.tk.attributes('-fullscreen', True)  
		#self.fullScreenState = False
		self.Frame=Frame(self.tk, background='Purple')
		self.Frame.pack(fill=BOTH, expand=YES)
		
		self.recognize()
	def recognize(self):
		self.cam=Camera(self.Frame)
		self.cam.pack()
	
okno=Okno()
#text_listening=tk.Text(okno)
#text_listening.pack()
okno.tk.mainloop()

#get_api_keys()


#class Okno:
#def __init__(self):
'''
if __name__ == '__main__':
	okno=tk.Tk()
	
	okno.configure(background='black')
	okno.title("Pozdravljeni")
	okno.geometry("1920x1000")
	#self.tk.attributes('-fullscreen', True)  
	#self.fullScreenState = False
	Frame=Frame(okno, background='Purple')
	Frame.pack(fill=BOTH, expand=YES)
	text_listening=tk.Text(okno)
	text_listening.pack()

	cam=Camera(okno.tk)
	cam.pack()
	okno.tk.mainloop()'''
	