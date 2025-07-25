import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 


img = cv.imread("Photos/group 1.jpg")
cv.imshow("Group 1",img)
blank = np.zeros(img.shape[:2],dtype="uint8")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
# circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),img.shape[0]//2,255,-1)

# masked  = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow("Masked",masked)
# GrayScale histogram 
# gray_his = cv.calcHist([gray],[0],None,[256],[0,256])


# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_his)
# plt.xlim([0,256])
# plt.show()

#Color histogram
plt.figure()
plt.title("Color scale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
color = ("b","g","r")
for i,col in enumerate(color):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])

plt.show()





cv.waitKey(0)

