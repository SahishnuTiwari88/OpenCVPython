# Resizing & croping
import cv2
img = cv2.imread("C:/Users/Sahishnu/Pictures/Screenshots/ada.png")
print(img.shape) # it gives height,width and no. for your channels i.e. BGR i.e. colors
imgResize = cv2.resize(img,(300,250)) # used to resize the image into desired height and width (width,height)

imgCrop = img[0:350,350:750] # first range of height followed by range of width

cv2.imshow("image",img)
cv2.imshow("Resize image",imgResize)
cv2.imshow("Crop Image",imgCrop)
cv2.waitKey(0)