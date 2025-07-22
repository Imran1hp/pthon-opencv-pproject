import cv2 as cv



def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    diamensions = (width,height)

    return cv.resize(frame,diamensions,interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue,frame =capture.read()
    rescaleFrame = rescaleFrame(frame)
    cv.imshow("Video",rescaleFrame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()


img = cv.imread('Photos/cat_large.jpg')

rescaleFrame = rescaleFrame(img,scale=0.25)
cv.imshow("cat",rescaleFrame)
cv.waitKey(0)