#multiple event by mouse
import cv2 as cv
import numpy as np
def click_event(event,x,y,flags,param):
    if event==cv.EVENT_MOUSEMOVE:
        cv.circle(img,(x,y),30,(255,0,0),-1)
        cv.imshow('Image',img)
def click_event1(event,x,y,flags,param):
    if event==cv.EVENT_MOUSEMOVE:
        cv.rectangle(img,(x,y),(x+40,y+40),(255,0,0),5)
        cv.imshow('Image',img)
def click_event2(event,x,y,flags,param):
    if event==cv.EVENT_MOUSEMOVE:
        cv.line(img,(x,y),(40,40),(255,0,0),5)
        cv.imshow('Image',img)
img=np.zeros((512,512,3),np.uint8)
cv.imshow('Image',img)
ch=input()
if ch=='c' or ch=='C':
    cv.setMouseCallback('Image',click_event)
elif ch=='r' or ch=='R':
    cv.setMouseCallback('Image',click_event1)
elif ch=='l' or ch=='L':
    cv.setMouseCallback('Image',click_event2)
cv.waitKey(0)
cv.destroyAllWindows()
