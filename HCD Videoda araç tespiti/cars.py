import cv2
cap=cv2.VideoCapture("video2.avi")
car_cascade=cv2.CascadeClassifier("cars.xml")
while True:
    _,img=cap.read()
    griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(griton,1.2,1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),3)
    cv2.imshow("cars",img)
    if cv2.waitKey(2) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()