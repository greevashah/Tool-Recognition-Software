import cv2,time

video=cv2.VideoCapture(0)       # implies use inbuilt camera, else we can put file path here 

a=1
while True:
    a=a+1
    check,frame=video.read()
    #check is bolean value,telling us whether we've captured any image or not
    #frame captures first image of the video
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Captured_Frames",gray)      #we can directly write frame here instead of gray, then we'll get colored video

    key= cv2.waitKey(1) #Delay for which to wait
    if key == ord('q'):
        break

print(a)    #Number of frames in video
video.release()
cv2.destroyAllWindows()