
#drawing on top of the image
import cv2 as cv 

#load the image
image = cv.imread("demure.png")
resized = cv.resize(image,(500,500))

#line
cv.line(resized,(250,450),(451,499),3)# takes 4 arguements, refere to documenation for more

#rectangle
cv.rectangle(resized,(100,200),(210,280),(0,0,255),5)

#circle
cv.circle(resized,(100,100),15,(0,255,0),10)
cv.imshow("IMG",resized) #show the image
cv.waitKey(0)
cv.destroyAllWindows()


"""
We will be darwing
1. Lines
2.Rectangles
3.text
"""
