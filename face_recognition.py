import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

persons=[]
for i in os.listdir(r'C:\Users\Asif\Downloads\train'):
    persons.append(i)


img = cv.imread("Photos/fuv1.jpg")


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {persons[label]} with a confidence of {confidence}')
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.putText(img,persons[label],(x,y-5),cv.FONT_HERSHEY_COMPLEX,1.5,(255,255,255),2)

cv.imshow("Detected Faces",img)

cv.waitKey(0)

