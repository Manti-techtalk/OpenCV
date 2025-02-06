import cv2 as cv
# working with images
image = cv.imread("pic.jpg")
cv.imshow("Image",image)
cv.waitKey(0)
cv.destroyAllWindows()

#convert the image to the greyscale
grey_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Grey Image",grey_image)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("Saved.jpg",grey_image)