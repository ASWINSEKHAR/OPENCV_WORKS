import cv2 as cv
img = cv.imread('openCV\pic\Aswin.jpeg')
cv.imshow('Aswin',img)

# converting image to gray scale
 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# blur an image

blur=cv.blur(img,(10,7),cv.BORDER_DEFAULT) #increasing the kernal will increases the blur 
cv.imshow('Blur',blur)


# Edge Cascading

canny=cv.Canny(img,125,175) # instead of img if we are giving blur then it will filters more background noise 
cv.imshow('Canny Edges',canny)

#Dialating the images

dialate=cv.dilate(canny,(7,7),iterations=4)  #on increaing the Interations the edge thickness also gets increased
cv.imshow('Dialate',dialate) 

# Eroding

eroded=cv.erode(dialate,(3,3),iterations=2)
cv.imshow('Eroded',eroded)

# resize image

resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resize',resize)

# crop

crop= img[50:200,200:400]
cv.imshow('Crop',crop)
cv.waitKey(0)


