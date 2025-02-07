import cv2 as cv
import numpy as np

goatimg = cv.imread("goat.jpg")
resized = cv.resize(goatimg,(600,600))
sketch = cv.Canny(resized,300,300) # this is used for detecting edges
dilated = cv.dilate(resized,np.ones((5,5),dtype=np.int8)) # this also does edge detection but bolder
cv.imshow("IMAGE",resized)
cv.imshow("Sketched IMG",sketch)
cv.imshow("Bolder",dilated)
cv.waitKey(0)
cv.destroyAllWindows()