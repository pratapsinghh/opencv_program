# how to change image format by track bar
import cv2 as cv
import numpy as np
img=cv.imread('Lenna.png')
cv.namedWindow('Image')
cv.createTrackbar('cp','Image',10,400,nothing)
switch='color/Gray'
cv.createTrackbar(switch,'Image',0,1,nothing)
while True:
    img=cv.imread('Lenna.png')
    pos=cv.getTrackbarPos('cp','Image')
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(100,130),font,8,(0,0,255),10)
    if cv.waitKey(0)==ord('q'):
        break
    s=cv.getTrackbarPos(switch,'Image')
    if s==0:
        pass
    else:
        img=cv.imread('Lenna.png',0)
    img=cv.imshow('Image',img)
cv.destroyAllWindows()
