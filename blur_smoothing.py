import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cat",img)
#avwerage blur
average = cv.blur(img,(3,3))
cv.imshow("Average Blur",average)

#Gaussian blur
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian Blur",gaussian)

#median blur
median = cv.medianBlur(img,3)
cv.imshow("Median Blur",median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 10,35,25)
cv.imshow("Bilateral Blur",bilateral)






cv.waitKey(0)