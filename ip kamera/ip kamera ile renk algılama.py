import cv2
import numpy as np
url="http://192.168.1.6:8080/shot.jpg"
kamera=cv2.VideoCapture(url)
while True:
    kamera = cv2.VideoCapture(url)

    ret,ss=kamera.read()
    ss=cv2.flip(ss,-1)
    hsv=cv2.cvtColor(ss,cv2.COLOR_BGR2HSV)
    dusuk_kirmizi = np.array([150, 70, 30])
    yuksek_kirmizi = np.array([190, 255, 255])
    mask=cv2.inRange(hsv,dusuk_kirmizi,yuksek_kirmizi)
    kernel = np.ones((3, 3), np.uint8)
    dilation = cv2.dilate(mask, kernel, iterations=2)  # gürültüleri büyütüyor
    erosion = cv2.erode(mask, kernel, iterations=2)  # gürültüleri siliyor
    dilation2=cv2.dilate(erosion, kernel, iterations=3)
    son_resim=cv2.bitwise_and(ss,ss,mask=dilation2)


    # erosion = cv2.bitwise_and(ss, ss, mask=erosion)
    # dilation = cv2.bitwise_and(ss, ss, mask=dilation)
    cv2.imshow("erosion", erosion)
    cv2.imshow("dilation", dilation)
    cv2.imshow("mask",mask)
    cv2.imshow("dilation2", dilation2)
    cv2.imshow("Kırmızı Renkler",son_resim)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()