import cv2 as cv
import numpy as np
img  =cv.imread("Photos/park.jpg")

# -x = left
# +x = right
# -y = up
# +y = down


def tranlate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    diamnsions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,diamnsions)


translated = tranlate(img,-100,100)
cv.imshow("Translated",translated)

cv.waitKey(0)