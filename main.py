import cv2 as cv # import the opencv 
# working with images
image = cv.imread("pic.jpg") #imread loeads and displays the oicture and video
cv.imshow("Image",image) # imshow shows the loaded picture
cv.waitKey(0)#wait before pressing a certain key
cv.destroyAllWindows()

#convert the image to the greyscale
grey_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Grey Image",grey_image)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("Saved.jpg",grey_image)