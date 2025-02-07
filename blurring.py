import cv2 as cv

image = cv.imread("another.jpg")
resized = cv.resize(image, (500, 500))
cv.imshow("Original Image", resized) # Show the original resized image

# Blurring the image (takes the averages)
blurred = cv.blur(resized, (10, 10)) # takes 2 parameters
cv.imshow("Blurred Image", blurred) # Show the averaged blurred image

# Applying Gaussian Blur (takes 3 parameters)
gaussian_blur = cv.GaussianBlur(resized, (10, 10), 5)
cv.imshow("Gaussian Blurred Image", gaussian_blur) # Show the Gaussian blurred image

cv.waitKey(0)
cv.destroyAllWindows()
