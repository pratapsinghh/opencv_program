#two image marge with weight weight in decimal number
import cv2 as cv
img=cv.imread('messi.jpg')
img2=cv.imread('Lenna.png')
img=cv.resize(img,(512,512))
img2=cv.resize(img2,(512,512))
det=cv.addWeighted(img,.7,img2,.3,0)#first source persent in decimal second source persent in decimal and gama
cv.imshow('Image',det)
cv.waitKey(0)
cv.destroyAllWindows()
