capture = cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue,frame =capture.read()
    rescaleFrame = rescaleFrame(frame)
    cv.imshow("Video",rescaleFrame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
