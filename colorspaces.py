# working with color spaces

#the original picture
import cv2 as cv

image = cv.imread("demure.png")
resized = cv.resize(image,(500,500))
cv.imshow("Image", resized)

# the colored picture

colored_img = cv.cvtColor(image,cv.COLOR_RGB2BGR)
resize_colored = cv.resize(colored_img,(500,500))
cv.imshow("Colored One",resize_colored)

cv.waitKey(0)
cv.destroyAllWindows()



