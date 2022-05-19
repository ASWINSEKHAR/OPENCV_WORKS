import cv2 as cv
import numpy as np
img=cv.imread('openCV\pic\Aswin.jpeg')
cv.imshow('Aswin',img)

# translation

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimentions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimentions)

# -x -->  Left Translation
# -y -->  Up translation
#  x -->  Right
#  y -->  Down

translated=translate(img,100,-100)  # negative and positive values of x and y can be assigned on the basis of to where we need to move the image
cv.imshow('Translated',translated)

  
# Rotation

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,180)
cv.imshow('Rotated',rotated)


#mirror imaging

# 0 ---> 180 degree mirroring
# 1 ---> exact mirroring
#-1 ---> 180 degree mirroring

flip=cv.flip(img,0)
cv.imshow('Flip',flip)
cv.waitKey(0)




    

