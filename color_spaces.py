import cv2 as cv

img = cv.imread ("Photos/park.jpg")
cv.imshow("parks",img)

# converting to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#BGR TO HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR TO LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)
# BGR TO RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
# HSV TO BGR
bgr =cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("hsv ---> bgr",bgr)
cv.waitKey(0)