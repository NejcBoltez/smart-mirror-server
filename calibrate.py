import sys
import os
from face_recognize import Get_face, User_calibration

arguments = list(sys.argv)
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Uporabniki')
tekst123=''
class Calibrate:
	def __init__(self):
	#def getCamera(self):
		while (True):
			get_user="nejc"#Get_face.user_auth_GUI()
			if (get_user is not None):
				self.calibrate(get_user)
				break
	#face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
	#face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
	#face_eye=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_profileface.xml')'''
	def calibrate(self,user):
		self.calibrate_user=User_calibration(user)
Calibrate()
