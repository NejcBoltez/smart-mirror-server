import cv2
import face_recognition
import os
import sys

class Get_face:
	def getUser():
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
	def User_calibration(user):
		try:
			face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		except:
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

	def User_creation(user):
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