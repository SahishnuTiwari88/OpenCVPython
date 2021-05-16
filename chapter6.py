# joining images = putting a number of images together in one window
import cv2
import numpy as np
img = cv2.imread("C:/Users/Sahishnu/Documents/WEB DEVELOPMENT LAB FILE/car.jpg")
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)
# issues= we can not resize the image
# both have same number of channels i.e. either both are RGB or both are GRAY not combination of both