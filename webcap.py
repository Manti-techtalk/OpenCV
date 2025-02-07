import cv2 as cv

webcam = cv.VideoCapture(0)

while True:
    isTrue, frame = webcam.read()

    if isTrue:
        cv.imshow("Live Camera", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

webcam.release()
cv.destroyAllWindows()
