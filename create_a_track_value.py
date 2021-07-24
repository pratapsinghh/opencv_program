# this program for increase the color power
import numpy as np
import cv2 as cv
def nothing(x):
    print(x)
img=np.zeros((512,512,3),np.uint8)
cv.namedWindow('Image')
cv.createTrackbar('Blue','Image',0,255,nothing)    #create a track bar for blue
cv.createTrackbar('Red','Image',0,255,nothing)     #create a track bar for Red
cv.createTrackbar('Green','Image',0,255,nothing)   #create a track bar for Green
while (1):
    if cv.waitKey(0)==27:
        break
    b=cv.getTrackbarPos('Blue','Image')   #get track value for color
    r=cv.getTrackbarPos('Red','Image')
    g=cv.getTrackbarPos('Green','Image')
    img[:,:,:]=[b,g,r]
    cv.imshow('Image',img)
cv.destroyAllWindows()
