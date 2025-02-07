import cv2 as cv

img = cv.imread("pics.jpg")
resized = cv.resize(img, (500, 500))
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
greyresized = cv.resize(grey, (500, 500))

# Apply threshold to the grayscale image
ret, threshed = cv.threshold(greyresized, 80, 255, cv.THRESH_BINARY)

cv.imshow("Original Image", resized)
cv.imshow("Grayscale Image", greyresized)
cv.imshow("Thresholded Image", threshed)
cv.waitKey(0)
cv.destroyAllWindows()
