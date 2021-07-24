#thresholding of image
import numpy as np
import cv2 as cv
def nothing(x):
    pass
cv.namedWindow('track')
cv.createTrackbar('LH','track',0,255,nothing)
cv.createTrackbar('LS','track',0,255,nothing)
cv.createTrackbar('LV','track',0,255,nothing)
cv.createTrackbar('UH','track',255,255,nothing)
cv.createTrackbar('US','track',255,255,nothing)
cv.createTrackbar('UV','track',255,255,nothing)
while True:
    frame1=cv.imread('smarties.png')
    frame=cv.resize(frame1,(250,250))
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_h=cv.getTrackbarPos('LH','track')
    l_s=cv.getTrackbarPos('LS','track')
    l_v=cv.getTrackbarPos('LV','track')
    u_h=cv.getTrackbarPos('UH','track')
    u_s=cv.getTrackbarPos('US','track')
    u_v=cv.getTrackbarPos('UV','track')
    l_b=np.array([l_h,l_s,l_v])
    u_p=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,l_b,u_p)
    res=cv.bitwise_and(frame,frame,mask=mask)
    #cv.imshow('frame',frame)
    cv.imshow('Mask',mask)
    cv.imshow('Result',res)
    cv.imshow('Image',frame)
    if cv.waitKey(0)==27:
        break
cv.destroyAllWindows()
