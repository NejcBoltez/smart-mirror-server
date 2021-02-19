import numpy as np
import cv2
import sys
import time

arguments = list(sys.argv)

'''try:
    face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
except:'''
'''face_front=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')'''
face_front=cv2.CascadeClassifier('../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#face_eye=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_profileface.xml')
cap = cv2.VideoCapture(0)

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
    '''if len(faces) == 0:
        print('prazno')
        faces2 = face_eye.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
        print (faces2)'''
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
    time.sleep(100)
    cv2.imshow('frame',frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')) or sys.stdin == str.encode('q') :
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()