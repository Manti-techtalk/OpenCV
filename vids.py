import cv2 as cv

video = cv.VideoCapture("vid.mp4")
 
while True:
    isTrue,frame = video.read()

    if isTrue:
        cv.imshow("Video Reading",frame)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
        else:
            break




video.release()
cv.destroyAllWindows()

    



