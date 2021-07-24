#mouse click left print rectangle and right click print circle
import cv2 as cv
import numpy as np
def click_event(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+20,y+20),(0,255,0),-1)
        cv.imshow('Image',img)
    if event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),20,(255,0,0),-1)
        cv.imshow('Image',img)
img=np.zeros((512,512,3),np.uint8)
cv.imshow('Image',img)
cv.setMouseCallback('Image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()
