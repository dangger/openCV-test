import cv2.cv as cv

image=cv.LoadImage('image/123.JPG', cv.CV_LOAD_IMAGE_COLOR)#Load the image

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE) #Facultative
cv.ShowImage('a_window', image) #Show the image

cv.SaveImage("thumb.png", thumb)
cv.WaitKey(0) #Wait for user input and quit