import cv2 as cv
import numpy as np
img=cv.imread('openCV\pic\Aswin.jpeg')
cv.imshow('ASWIN',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)
canny=cv.Canny(img,125,175)
cv.imshow('CANNY',canny)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
#  cv.RETR_EXTERNAL ----> countours of all external parts of the image
# cv.RETR_LIST ------> contours of all parts of the image
# cv.RETR_TREE ----> contours of all the heirarchical order

# for approximating the contours:
#       *CHAIN_APPROX_NONE ---> it will gives all of the coordinates of the image
print(f'{len(contours)} contour(s) found!')   # we will get the number of contours

# to draw the contours 

cv.drawContours(img,contours,-1,(255,255,0))
cv.imshow("image",img)

cv.drawContours(blank,contours,-1,(255,0,0),2)
cv.imshow('Contours Drawn in Blank',blank)

# for converting image to binary

ret,thresh=cv.threshold(gray,123,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
cv.waitKey(0)
