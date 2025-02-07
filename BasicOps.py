import cv2 as cv

image = cv.imread("pics.jpg") # the original big photo
cv.imshow("Initial Image", image) # show the original photo

resized = cv.resize(image, (500, 500)) # resized version of the photo
cv.imshow("Resized Photo", resized) # display the resized photo

cv.waitKey(0) # wait for a key press



#resize the vid

video = cv.VideoCapture("vid.mp4")

while True:
    isTrue, frame = video.read()
    if isTrue:
        resized_frame = cv.resize(frame, (500, 500)) # resize each frame
        cv.imshow("Video", resized_frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows() # clean up

