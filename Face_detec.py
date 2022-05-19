# for Face Detection we need to convert the image into gray scale as face detection does not depend on the color or skin tone, but depends only on the edges of the face
import cv2 as cv
import numpy as np
img=cv.imread('openCV\pic\Aswin.jpeg')
cv.imshow('Aswin',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
haar_cascade=cv.CascadeClassifier('Haar_face.xml') # tpe the folder name in which the classifier is stored within the quatation marks
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f'Number of faces={len(faces_rect)}')
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected Faces',img)



cv.waitKey(0)