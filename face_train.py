import os 
import cv2 as cv
import numpy as np

persons=[]

for i in os.listdir(r'C:\Users\Asif\Downloads\train'):
    persons.append(i)

DIR = r'C:\Users\Asif\Downloads\train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')


features=[]
labels=[]
def create_train():
    for person in persons:
        path =os.path.join(DIR,person)
        label =persons.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rec =haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rec:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training Done..................")


face_recognizer = cv.face.LBPHFaceRecognizer_create()
factures =np.array(features,dtype="object")
labels =np.array(labels)

#Train the Recognizer on the features list and the labels list
face_recognizer.save('face_trained.yml')


face_recognizer.train(features, np.array(labels))
np.save('features.npy', np.array(features, dtype=object))
np.save('labels.npy',labels)






