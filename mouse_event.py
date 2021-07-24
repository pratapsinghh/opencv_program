#mouse event left button click print coordinate on the screen
import cv2 as cv
import numpy as np
def click_event(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        #print(x,',',y)
        font=cv.FONT_HERSHEY_SIMPLEX
        strxy=str(x)+','+str(y)
        cv.putText(img,strxy,(x,y),font,1,(255,255,0),2)
        cv.imshow('Image',img)
img=np.zeros((512,512,3),np.uint8)
cv.imshow('Image',img)
cv.setMouseCallback('Image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()
