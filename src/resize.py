import cv2
import numpy as np
img = cv2.imread('image/123.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(10*width, 10*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('123.jpg',res)
cv2.waitKey()