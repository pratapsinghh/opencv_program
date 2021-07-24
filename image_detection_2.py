#image detection 
import numpy as np
import cv2 as cv
cv.namedWindow('image')
cv.createTrackbar('LH','image',0,255,nothing)
cv.createTrackbar('LS','image',0,255,nothing)
cv.createTrackbar('LV','image',0,255,nothing)
cv.createTrackbar('UH','image',255,255,nothing)
cv.createTrackbar('US','image',255,255,nothing)
cv.createTrackbar('UV','image',255,255,nothing)
while True:
    frame=cv.imread('Lenna.png')
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lh=cv.getTrackbarPos('LH','image')
    ls=cv.getTrackbarPos('LS','image')
    lv=cv.getTrackbarPos('LV','image')
    uh=cv.getTrackbarPos('UH','image')
    us=cv.getTrackbarPos('US','image')
    uv=cv.getTrackbarPos('UV','image')
    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])
    mask=cv.inRange(hsv,lb,ub)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('Frame',frame)
    cv.imshow('Mask',mask)
    cv.imshow('Result',res)
    if cv.waitKey(0)==ord('q'):
        break
cv.destroyAllWindows()
    
