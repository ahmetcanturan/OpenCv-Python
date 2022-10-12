import cv2

cap=cv2.VideoCapture("video.mp4")
human_cascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    _,frame=cap.read()
    griton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    insan=human_cascade.detectMultiScale(griton,1.2,2)

    for (x,y,w,h) in insan:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),3)
    cv2.imshow("insanlar",frame)
    if cv2.waitKey(2) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
