import cv2 as cv
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    cv.waitKey(1) 
    if cv.waitKey(1) & 0xFF==ord('a'):
        break
capture.release()
cv.destroyAllWindows()
        