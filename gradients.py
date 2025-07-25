import cv2 as cv
import numpy as np

img =cv.imread("Photos/park.jpg")
cv.imshow("Cats",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


#laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("Laplacian",lap)

#sobel
sobel_X= cv.Sobel(gray,cv.CV_64F,1,0)
sobel_Y= cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobel_X,sobel_Y)

cv.imshow("Sobel X",sobel_X)
cv.imshow("Sobel Y",sobel_Y)
cv.imshow("Combined Sobel",combined_sobel)

#canny
canny = cv.Canny(gray,150,175)
cv.imshow("Canny",canny)









cv.waitKey(0)
