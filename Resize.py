import cv2 as cv

image = cv.imread("Saved.jpg")
cv.imshow("MY Image",image)
cv.waitKey(0)
cv.destroyAllWindows()