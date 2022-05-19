import cv2 as cv
import numpy as np
img=cv.imread('openCV\pic\Aswin.jpeg')
cv.imshow('Aswin',img)
b,g,r=cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
 
#   to merge the extracted channels

merged = cv.merge([b,g,r])
cv.imshow('MERGED',merged)

cv.waitKey(0)
