# kortür çıkarma önemli bir konu
import cv2

import numpy as np
img=cv2.imread("gul.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
dusuk_kirmizi=np.array([150,70,30])
yuksek_kirmizi = np.array([190,255,255])
mask=cv2.inRange(hsv,dusuk_kirmizi,yuksek_kirmizi)
kernel = np.ones((2, 2), np.uint8)#bulurlaştırdık
erod = cv2.erode(mask, kernel, iterations=1)
dilate = cv2.dilate(erod, kernel, iterations=3)  # gürültüleri siliyor

cntr,_=cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #External dış kısmını çizer --CCOMP hem iç Hem dış--Hepsi
for contour in cntr:
    (x, y, w, h) = cv2.boundingRect(contour)  # dikdörtgen sınırlarını bulur
    if cv2.contourArea(contour) < 1000:#küçük gürültüler için dikdörtgen çizdirmiyor
        continue
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("mask",mask)
cv2.imshow("erode+dilate",dilate)
# cv2.imshow("closing",closing)
cv2.imshow("Erode",erod)
cv2.waitKey()
cv2.destroyAllWindows()