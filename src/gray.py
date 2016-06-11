import numpy as np
import cv2
img = cv2.imread('image/123.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('image', res)
cv2.WaitKey("w")