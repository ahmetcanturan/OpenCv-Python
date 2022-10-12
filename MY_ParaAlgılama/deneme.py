import cv2
import numpy as np
url="http://192.168.1.6:8080/shot.jpg"
kamera=cv2.VideoCapture(url)
kernel = np.ones((5, 5), np.uint8)
fontscale = 0.5
color = (0, 0, 0)
fontface = cv2.FONT_HERSHEY_COMPLEX
paralar=["5 kurus","10 kurus","25 kurus","50 kurus","1 TL"]
# birtl=6470
# elli=birtl-1090
# yirmibes=birtl-2625
# on=birtl-3470
# bes=birtl-3795
x=0
while 1:
    kamera = cv2.VideoCapture(url)
    _,para=kamera.read()
    img_hsv = cv2.cvtColor(para, cv2.COLOR_BGR2HSV)
    dusuk_yesil = np.array([50,40,35])
    yuksek_yesil = np.array([85,255,255])
    mask = cv2.inRange(img_hsv, dusuk_yesil, yuksek_yesil)
    blur = cv2.GaussianBlur(mask, (3, 3), 1)
    dilate=cv2.dilate(blur,kernel,iterations=3)
    erode= cv2.erode(dilate, kernel, iterations=3)
    _,th=cv2.threshold(erode,10,255,cv2.THRESH_BINARY_INV)
    contours, hiyerachi = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(cv2.contourArea(contours[0]))
    # cv2.drawContours(para, contours, -1, (0,255,0), 3)
    # if x==0:
    #     deger=int(input("1 TL yi koydun mu: 1 veya 0"))
    #     if deger==1:
    #         birtl=cv2.contourArea(contours[0])
    #         x=100
    #         elli = birtl - 1090
    #         yirmibes = birtl - 2625
    #         on = birtl - 3470
    #         bes = birtl - 3795
    #     else:
    #         print("1 tl yi koy")
    areas = [cv2.contourArea(c) for c in contours]
    print("cnct",areas)
    # for i in range(len(contours)):
    #     alan=cv2.contourArea(contours[i])
    #     if birtl-200<alan<birtl+200:
    #         (x, y, w, h) = cv2.boundingRect(contours[i])
    #         cv2.putText(para, "1 TL", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    #     elif elli-200<alan<elli+200:
    #         (x, y, w, h) = cv2.boundingRect(contours[i])
    #         cv2.putText(para, "50 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    #     elif yirmibes-200<alan<yirmibes+200:
    #         (x, y, w, h) = cv2.boundingRect(contours[i])
    #         cv2.putText(para, "25 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    #     elif on-100<alan<on+200:
    #         (x, y, w, h) = cv2.boundingRect(contours[i])
    #         cv2.putText(para, "10 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    #     else:
    #         (x, y, w, h) = cv2.boundingRect(contours[i])
    #         cv2.putText(para, "5 Kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)


    cv2.imshow("th", th)
    cv2.imshow("para", para)
    if cv2.waitKey(15) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
kamera.release()