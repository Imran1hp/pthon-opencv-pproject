import cv2 as cv
img = cv.imread("Photos/cats.jpg")

cv.imshow("cats",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thresholding

threshold_value , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("simple threshold",thresh)
threshold_value ,thresh_inverse = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)

cv.imshow("simple threshold inverse",thresh_inverse)

#adaptive thresholding

adaptive_thres = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,9)

cv.imshow("adaptive threshold",adaptive_thres)

cv.waitKey(0)

