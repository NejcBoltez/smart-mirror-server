import os
import numpy as np
from PIL import Image
import cv2
import pickle
#import dlib
import face_recognition

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, 'Uporabniki')

face_cascade=cv2.CascadeClassifier('C:/Users/nejcb/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

#recognizer = cv2.face.LBPHFaceRecognizer_create()

image = face_recognition.load_image_file('./Uporabniki/nejc/Nejc_1.png')
image_encoding = face_recognition.face_encodings(image)[0]

for root, dirs, files in os.walk(image_dir):
    for file in files:
        '''print(dirs)
        print(root)
        print(files)
        print(file)'''
        unknown_image = face_recognition.load_image_file(root+'/'+file)
        '''print(unknown_image)'''
        if (len(unknown_image) > 0 ):
            unknown_encoding= face_recognition.face_encodings(unknown_image)
            print('Image: ' + str(unknown_image[0]))
            if (len(unknown_encoding) > 0):
                results=face_recognition.compare_faces([image_encoding], unknown_encoding[0])

                if results[0]:
                    print(file)
                else:
                    print('false')
        '''
        if file.endswith('png') or file.endswith('jpg'):
            print(file)
           
            path=os.path.join(root,file)
            label=os.path.basename(path).replace(".jpg", "").replace(" ","-").lower()
            print(label, path)
            if label not in labels_ids:
                labels_ids[label]=current_id
                current_id += 1
            id_=labels_ids[label]
            print(id_,labels_ids)
            pil_image = Image.open(path).convert('L')
            image_array=np.array(pil_image,'uint8')
            #print(image_array)
            faces=face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi=image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
'''
#print(y_labels)
#print(x_train)
'''
with open ('labels.pickle', 'wb') as f:
    pickle.dump (label_ids, f)

recognizer.train(x_train, np.array)
recognizer.save('trainner.yml')'''