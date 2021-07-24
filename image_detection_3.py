import numpy as np
import cv2 as cv
cv.namedWindow('track')
cv.createTrackbar('LH','track',0,255,nothing)
cv.createTrackbar('LS','track',0,255,nothing)
cv.createTrackbar('LV','track',0,255,nothing)
cv.createTrackbar('UH','track',255,255,nothing)
cv.createTrackbar('US','track',255,255,nothing)
cv.createTrackbar('UV','track',255,255,nothing)
while True:
    frame1=cv.imread('w.jpg')
    frame=cv.resize(frame1,(250,250))
    hsv=cv.cvtColor(frame,cv.COLOR_RGB2HSV)
    lh=cv.getTrackbarPos('LH','track')
    ls=cv.getTrackbarPos('LS','track')
    lv=cv.getTrackbarPos('LV','track')
    uh=cv.getTrackbarPos('UH','track')
    us=cv.getTrackbarPos('US','track')
    uv=cv.getTrackbarPos('UV','track')
    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])
    mask=cv.inRange(hsv,lb,ub)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('Frame',frame)
    cv.imshow('Mask',mask)
    cv.imshow('Result',res)
    if cv.waitKey(0)==27:
        break
cv.destroyAllWindows()
