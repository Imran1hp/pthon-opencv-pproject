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
#rotation 
def rotate (img, angle , rotPoint =None):

    (height,width)= img.shape[0],img.shape[1]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat =cv.getRotationMatrix2D(rotPoint,angle,1.0) 
    deminsions = (width,height)

    return cv.warpAffine(img,rotMat,deminsions)

rotated = rotate(img,-45)
cv.imshow("Rotated",rotated)

#Resizing

rezied = cv.resize(img ,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",rezied) 

flip  = cv.flip(img,1)
cv.imshow("Flip",flip)

cropped = img [200:400,300:500]
cv.imshow("Cropped",cropped)





cv.waitKey(0)