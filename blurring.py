import cv2 as cv

image = cv.imread("another.jpg")
resized = cv.resize(image,(500,500))
cv.imshow("IMG",resized)

#blurring the image(take the averages )

blured=cv.blur(resized,(10,10))
cv.imshow("Image",blured)
 



cv.waitKey(0)
cv.destroyAllWindows()