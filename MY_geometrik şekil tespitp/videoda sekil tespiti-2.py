import cv2
import numpy as np
import time
url="http://192.168.1.7:8080/shot.jpg"
while True:
    kamera = cv2.VideoCapture(url)
    _,img=kamera.read()
    img=cv2.flip(img,-1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold = cv2.Canny(img_gray,30,100)

    # Find the contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # For each contour approximate the curve and
    # küçük mesafe kortinatlarını pas gec
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)  # dikdörtgen sınırlarını bulur
        if cv2.contourArea(cnt) < 5000:  # küçük gürültüler için dikdörtgen çizdirmiyor
            continue
        epsilon = 0.04 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(img, [approx], 0, (0), 5)
        # Position for writing text
        x, y = approx[0][0]
        # anladığım kadarıyla düzelttiği çizimlerden köşe sayısını arıyor.
        if len(approx) == 3:
            cv2.putText(img, "Ucgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
        elif len(approx) == 4:
            cv2.putText(img, "Dikdortgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
        # elif len(approx) == 5:
        #     cv2.putText(img, "Besgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
        # elif 6 < len(approx) < 15:
        #     cv2.putText(img, "Elips", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
        # else:
        #     cv2.putText(img, "Daire", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    time.sleep(0.1)
    cv2.imshow("final", img)
    cv2.imshow("mask",threshold)
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break
cv2.destroyAllWindows()
kamera.release()

