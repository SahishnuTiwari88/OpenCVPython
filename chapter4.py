# Shapes & Texts
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # matrix with # zeros (black)
#img[:] = 255,0,0 # for coloring the entire image, (255,0,0) = blue color

cv2.line(img,(0,0),(300,300),(0,255,0),3) # (0,0) & (300,300) starting & ending point of line, (0,255,0) for define color & 3 to show thickness

cv2.rectangle(img,(0,0),(300,400),(0,0,255),5) # to fill the area we can use cv2.FILLED instead of using thickness

cv2.circle(img,(250,250),100,(255,255,0),cv2.FILLED)

cv2.putText(img,"OPENCV",(250,350),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2) #(img,text,origin,fonttype,scale,color,thickness)
cv2.imshow("image",img)

cv2.waitKey(0)