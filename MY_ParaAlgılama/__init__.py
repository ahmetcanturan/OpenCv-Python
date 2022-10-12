import cv2
import numpy as np
para=cv2.imread("madenipara.JPG")
blur = cv2.GaussianBlur(para, (5, 5), 1)
canny = cv2.Canny(blur, 100, 155)
circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 10, param1=180, param2=28, minRadius=18, maxRadius=60)
circles = np.uint16(np.around(circles))
para2=para.copy()
for i in circles[0, :]:
    # draw the outer circle
    para2=cv2.circle(para2, (i[0], i[1]), i[2], (255, 255, 255), -1)
    # draw the center of the circle
img_hsv = cv2.cvtColor(para2, cv2.COLOR_BGR2HSV)
kernel=np.ones((5,5),np.uint8)
dusuk_beyaz = np.array([0, 0,140])
yuksek_beyaz = np.array([256, 60, 256])
mask = cv2.inRange(img_hsv, dusuk_beyaz, yuksek_beyaz)
contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
fontscale = 0.5
color = (0, 0, 0)
fontface = cv2.FONT_HERSHEY_COMPLEX
for cnt in contours:
    lengt=cv2.arcLength(cnt,True)
    if 158<lengt<172:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.putText(para, "5 kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    elif 172 < lengt < 185:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.putText(para, "10 kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    elif 189 < lengt < 209:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.putText(para, "25 kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    elif 210 < lengt < 238:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.putText(para, "50 kurus", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    elif 239 < lengt < 259:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.putText(para, "1 TL", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
    else:
        cv2.putText(para, "Kamera Ayarı Yap", (x + int(w / 2) - 10, y + h + 10), fontface, fontscale, color)
cv2.imwrite("paratespiti.JPG",para)
cv2.imshow("canny",canny)
cv2.imshow("para2",para2)
cv2.imshow("para",para)
cv2.imshow("mask",mask)
cv2.waitKey()
cv2.destroyAllWindows()