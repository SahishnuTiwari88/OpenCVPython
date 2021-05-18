# Contour/Shape Detection
import cv2
import numpy as np
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        Area = cv2.contourArea(cnt)
        print(Area)
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        # now check for minimum area
        if Area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) # to check area of each image
            # Now calculate curve length it helps us to approx. corners of our images shape
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)   # to approx corner points i.e. how many corner points we have,we use True to show condition that all images are closed
            #print(approx) # it gives us corner point of each shapes
            print(len(approx)) # it gives us idea about what the shape is,i,e, triangle,rectangle
            objCor = len(approx) # create bounding box around our object/image
            x,y,w,h = cv2.boundingRect(approx) # it gives x,y,width,height each of objects shape

            if objCor == 3:objectType = "Triangle"
            elif objCor == 4:
                aspectRatio = w/float(h)   # to check it is square b/c in square we divide w/h and get 1
                if aspectRatio>0.95 and aspectRatio<1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor>4: objectType = "Circle"

            else:objectType="None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),3) # it draw rectangle around the shapes
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

path="C:/Users/Sahishnu/Pictures/Screenshots/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)
#cv2.imshow("Original",img)
#cv2.imshow("ImgGray",imgGray)
#cv2.imshow("Blur Image",imgBlur)
#cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Contour Image",imgContour)
cv2.waitKey(0)
# NOTE : object having more than 4 corners are mainly considered to be circle