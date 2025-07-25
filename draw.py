import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = "uint8")
# cv.imshow("Black",blank)

# draw rectangle
cv.rectangle(blank,(100,100),(300,300),(255,0,0),cv.FILLED)
# cv.imshow("Rectangle",blank)
# draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),cv.FILLED)
# cv.imshow("Circle",blank)

# draw line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
# cv.imshow("Line",blank)

# text 
cv.putText(blank,"HELLO",(225,330),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("Text",blank)
cv.waitKey(0)