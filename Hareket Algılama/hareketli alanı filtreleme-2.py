import cv2
import numpy as np

cap = cv2.VideoCapture("video3.avi")
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2) #işi yapan komut
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    erosion=cv2.erode(thresh, None, iterations=3)
    image = cv2.resize(frame1, (1280,720))
    cv2.imshow("feed", cap.read()[1])
    cv2.imshow("gri",diff)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()