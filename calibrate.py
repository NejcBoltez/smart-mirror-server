import numpy as np
import cv2
import sys
import time
import os

arguments = list(sys.argv)
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, '../Uporabniki')
tekst123=''
def getCamera():
       # .local is inside home directory
    try:
        face_front=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    except:
        face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    # Capture frame-by-frame
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
        for root, dirs, files in os.walk(image_dir):
            for d in dirs:
                #print(d)
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
                                img_item2='./Uporabniki/'+d+'/'+d+'_'+str(file_count+1)+'.png'
                                cv2.imwrite(img_item2, roi_color)
                                teskst123='Pozdravljen ' + tekst
                                break
                            else:
                                continue
    if (len(faces)==0):
        getCamera()
    elif(len(faces)>0):
        calibrate()
							
'''try:
    face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
except:'''
'''face_front=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')'''
#face_front=cv2.CascadeClassifier('../../.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#face_front=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

#face_eye=cv2.CascadeClassifier('/home/nejc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_profileface.xml')
def calibrate():
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
        #time.sleep(100)
        cv2.imshow('frame',frame)
        cv2.moveWindow(winname, 500,500)
        if (cv2.waitKey(1) & 0xFF == ord('q')) or sys.stdin == str.encode('q') :
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
getCamera()
