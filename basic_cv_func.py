import cv2 as cv

img  = cv.imread("Photos/park.jpg")
cv.imshow("Baston",img)
# converting to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

# edge cascade
canny = cv.Canny(img,125,175)
cv.imshow("Canny",canny)

# dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)

# eroding
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Eroded",eroded)

# croping
cropped = img[50:200,200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)