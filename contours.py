import cv2 as cv 
import numpy as np


img = cv.imread("Photos/cats.jpg")
cv.imshow("Cat",img)

blank = np.zeros(img.shape,dtype="uint8")
cv.imshow("Blank",blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("gray blur",blur)

canny = cv.Canny(img,125,175)
cv.imshow(" gray Canny",canny)


ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contours , hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Contours Drawn",blank)

cv.waitKey(0)