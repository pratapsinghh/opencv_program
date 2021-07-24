#draw a line one location to another location
import cv2 as cv
import numpy as np
def click_event(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),3,(0,255,0),5)
        points.append((x,y))
        if len(points)>=2:
            a=-1
            b=-2
            cv.line(img,points[a],points[b],(0,255,123),3)
            a=0
            b=0
            cv.imshow('Image',img)
img=np.zeros((512,512,3),np.uint8)
cv.imshow('Image',img)
points=[]
cv.setMouseCallback('Image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()
