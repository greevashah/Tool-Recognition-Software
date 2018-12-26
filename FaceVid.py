import cv2,time

video=cv2.VideoCapture('09-1.avi')       # implies use inbuilt camera, else we can put file path here 
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

while (video.isOpened()):
    check,frame=video.read()
    rframe=cv2.resize(frame, (int(frame.shape[1]*2),int(frame.shape[0]*2)))
    gray=cv2.cvtColor(rframe, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray)

    for x,y,w,h in faces:
        rframe= cv2.rectangle(rframe,(x,y),((x+w),(y+h)),(0,0,255),3)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color= rframe[y:y+h, x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            roi_color= cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow("Captured_Frames",roi_color)

    cv2.imshow("Captured_Frames",rframe)      #we can directly write frame here instead of gray, then we'll get colored video
    # key= cv2.waitKey(1) #Delay for which to wait
    key= cv2.waitKey(30)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()