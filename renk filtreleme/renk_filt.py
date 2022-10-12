import cv2
import numpy as np
kamera=cv2.VideoCapture(0)
while True:
    ret,ss=kamera.read()
    ss=cv2.flip(ss, 1)
    hsv=cv2.cvtColor(ss,cv2.COLOR_BGR2HSV)
    # dusuk_kirmizi=np.array([150,30,30])
    # yuksek_kirmizi = np.array([190,255,255])
    dusuk_mavi = np.array([100, 60, 60])
    yuksek_mavi = np.array([140, 255, 255])
    # dusuk_beyaz = np.array([0, 0,140])
    # yuksek_beyaz = np.array([256, 60, 256])
    mask=cv2.inRange(hsv,dusuk_mavi,yuksek_mavi)
    son_resim=cv2.bitwise_and(ss,ss,mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("hsv",hsv)
    cv2.imshow("son",son_resim)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()