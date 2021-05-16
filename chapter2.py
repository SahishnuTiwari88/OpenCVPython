import cv2
import numpy as np
# important function in opencv
img = cv2.imread("C:/Users/Sahishnu/Pictures/Screenshots/ada.png")
kernel = np.ones((5,5),np.uint8) # all value to be 1's & (5,5) is size of matrix  then define type of object which is np.uint8 (unsigned integer of 8 bits
#i.e. value in range 0-255 )


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # it converts our image color to gray scale
# cvtColor converts img into d/f color spaces

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # to blur the image (7,7 ) is kernel size & it has be to odd number

imgCanny = cv2.Canny(img,150,200)  # edge detector to find edge in our image we use Canny function
# 150 & 200 are threshold & to reduce edges in images we can increase the threshold value

## Dilation = sometimes we detect an edge but b/c of gap or it is not joint properly it doesn't detect it as proper line so we increase thickness of
# our edge##

imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) # we use imgCanny b/c we have to deal with edges then add kernel(it is a matrix whose size & value has to define)
# then define how many iteration we want kernel to move around i.e. how much thickness we actually need

# to make picture thinner we use opposite of Dilation which is "Erosion"

imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

#cv2.imshow("Gray Image",imgGray)
#cv2.imshow("Blur Image",imgBlur)
#cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilation Image",imgDilation)
cv2.imshow("Erosion Image",imgEroded)
cv2.waitKey(0)