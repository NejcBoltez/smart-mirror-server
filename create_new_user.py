import speech_recognition as sr
import subprocess
import os
import numpy as np
import cv2
from face_recognize import Get_face, User_calibration
from speech_listen import Listening
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
	user_check=''
	while(True):
		print("TEST")
		user_check=Get_face.User_auth()
		print("TEST 2")
		if(user_check is not None):
			new_user_name()
			break

def new_user_name():
	new_user_name=Listening.new_user_name()
	print("New user: " + new_user_name)
	user_create=User_calibration(new_user_name)


#new_user_name()
check_for_user()
