import cv2
import numpy as np
kamera=cv2.VideoCapture(1)
kernel = np.ones((5, 5), np.uint8)
fontscale = 0.5
color = (0, 0, 0)
fontface = cv2.FONT_HERSHEY_COMPLEX
paralar=["5 kurus","10 kurus","25 kurus","50 kurus","1 TL"]
while 1:
    _,para=kamera.read()
    blur = cv2.GaussianBlur(para, (5, 5), 1)
    canny = cv2.Canny(blur, 100, 155)
    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 10, param1=180, param2=28, minRadius=18, maxRadius=60)
    circles = np.uint16(np.around(circles))
    para2 = para.copy()
    for i in circles[0, :]:
        # draw the outer circle
        para2 = cv2.circle(para2, (i[0], i[1]), i[2], (255, 255, 255), -1)
        # draw the center of the circle
    img_hsv = cv2.cvtColor(para2, cv2.COLOR_BGR2HSV)
    dusuk_beyaz = np.array([0, 0, 140])
    yuksek_beyaz = np.array([256, 60, 256])
    mask = cv2.inRange(img_hsv, dusuk_beyaz, yuksek_beyaz)
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    lengt=[]
    for k in range (len(contours)):
        lengt.append(cv2.arcLength(contours[k], True))
    lengt.sort(reverse=False)
    for j in range(len(contours)):
        (x, y, w, h) = cv2.boundingRect(contours[j])
        uzunluk=cv2.arcLength(contours[j], True)
        if lengt[0]==uzunluk:
            cv2.putText(para, "5 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
        elif lengt[1]==uzunluk:
            cv2.putText(para, "10 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
        elif lengt[2]==uzunluk:
            cv2.putText(para, "25 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
        elif lengt[3]==uzunluk:
            cv2.putText(para, "50 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
        else:
            cv2.putText(para, "1 TL", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)


    cv2.imshow("canny", canny)
    cv2.imshow("para2", para2)
    cv2.imshow("para", para)
    cv2.imshow("mask", mask)
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
kamera.release()