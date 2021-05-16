import cv2
print("Package imported successfully")

# reading image
# img = cv2.imread("C:/Users/Sahishnu/Pictures/Screenshots/ada.png")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)  # video from webcam
cap.set(3,640)  # width=640 at id number 3   and this is
# used to resize or setting video size on laptop screen
cap.set(4,480)  # heigth=480 at id number 4
cap.set(10,100) # for change brightness id = 10 and value 100

while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(100) & 0xFF == ord('d'):
        break

