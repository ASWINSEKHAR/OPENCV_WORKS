import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3), dtype ='uint8') # for generating a blanck black screen
cv.imshow('Blank',blank)

# giving colour to any image

blank[:]= 0,255,0          # giving a green colour
cv.imshow('Green',blank)

# drawing a red rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=3)
cv.imshow('Rectangle',blank)

# drawing a blue rectangle

cv.rectangle(blank,(0,0),(453,453),(255,0,0),thickness=3)
cv.imshow('Rectangle',blank)

# inorder to get the solid rectangle on the half of screen specify thickness=-1

cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=-1)
cv.imshow('Rectangle',blank)

# drawing a circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(255,0,0),thickness=-1) 
cv.imshow('Circle',blank)

# drawing a line 

cv.line(blank,(0,0),(240,563),(0,255,0),thickness=5)
cv.imshow('Line',blank)

# writing text on image

cv.putText(blank,'ASWIN SEKHAR C S',(250,250),cv.FONT_HERSHEY_TRIPLEX,3.0,(255,0,0),3)
cv.imshow('Text',blank)
cv.waitKey(0)