import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture=cv2.VideoCapture(0)
while True:
    #capture frame-by-frame , frame c notre video , ret variable d'etat ta3tina l'etat de votre camera 
    ret, frame=video_capture.read()
    #our operations on the frame come here , conversion mel BGR to gray 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #display the resulting frame
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
       cv2.putText(frame,'ooo',(x,y-30),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,300)
    cv2.imshow('application ',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
