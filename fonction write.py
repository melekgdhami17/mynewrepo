import numpy as np
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
def write_data():
    nb=0
    while 1:
        ret,img=cap.read()
        only_face=np.array(10)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
             cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             only_face=gray[y:y+h,x:x+w]
             cv2.imwrite("data/user"+str(nb)+".jpg",only_face)
        nb=nb+1
        cv2.imshow('live video',img)
        cv2.waitKey(1)
        if nb==20:
             cap.release()
             cv2.destroyAllWindows()
             break
write_data()
             
             
