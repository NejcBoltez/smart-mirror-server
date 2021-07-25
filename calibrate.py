import numpy as np
import cv2
import sys
import time
import os
from face_recognize import Get_face

arguments = list(sys.argv)
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Uporabniki')
tekst123=''
def getCamera():
    while (True):
        get_user=Get_face.getUser()
        if (get_user is not None):
            calibrate(get_user)
            break
#face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#face_eye=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_profileface.xml')'''
def calibrate(user):
    calibrate_user=Get_face.User_calibration(user)
getCamera()
