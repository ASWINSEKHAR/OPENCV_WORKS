import cv2 as cv
import numpy as np
img=cv.imread('openCV\pic\Aswin.jpeg')
cv.imshow('ASWIN',img)

# BGR to HSV ---> cv.COLOR_BGR2HSV

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to LAB ---> cv.COLOR_BGR2LAB

lbr=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LBR',lbr)

# BGR to RGB   ---> cv.COLOR_BGR2RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)


# HSV To BGR ------> cv.COlOR_HSV2BGR

cv.waitKey(0)
