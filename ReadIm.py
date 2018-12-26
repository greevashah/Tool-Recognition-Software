import cv2
import numpy
import matplotlib

# Creating Cascade Object which has features of Face
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Reading the image
img=cv2.imread("DP.jpg",1)
# Reading image as gray scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sEARCHING FOR RECTANGULAR COORDINATES OF IMAGE
faces=face_cascade.detectMultiScale(gray_img, 1.7, 5)
# print(img.shape)

# print(faces)

for x,y,w,h in faces:
    img= cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),3)

# resized=cv2.resize(img, (int(img.shape[1]/4),int(img.shape[0]/4)))
cv2.imshow("Dance",img)

cv2.waitKey(0)
cv2.destroyAllWindows()