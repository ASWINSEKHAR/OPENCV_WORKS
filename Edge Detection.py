import cv2 as cv
import numpy as np
img=cv.imread('openCV\pic\Aswin.jpeg')
cv.imshow('Aswin',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# for edge detection first we need to convert the image into Gray scale

# Laplacian Method

lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian ',lap)

# Sobel Method

sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)    # here we will get the Sobel edges detection of X and Y axis respectively

# here we will be combining the two sobels to get the combined sobel edge deteccted image of the gray scale image
Combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('Combined Sobel',Combined_sobel)

cv.waitKey(0)

