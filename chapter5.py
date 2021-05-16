# WARP PRESPECTIVE = to get the desired part of the image
import cv2
import numpy as np
img = cv2.imread("C:/Users/Sahishnu/Pictures/Screenshots/ada.png")

width,height=250,350
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2=np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
