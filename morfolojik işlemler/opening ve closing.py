import cv2
import numpy as np
url="http://192.168.1.7:8080/shot.jpg"
# kamera=cv2.VideoCapture(0)
while True:
    kamera = cv2.VideoCapture(url)
    ret,ss=kamera.read()
    ss=cv2.flip(ss,1)
    hsv=cv2.cvtColor(ss,cv2.COLOR_BGR2HSV)
    dusuk_mavi = np.array([100, 60, 60])
    yuksek_mavi = np.array([140, 255, 255])
    mask=cv2.inRange(hsv,dusuk_mavi,yuksek_mavi)

    kernel=np.ones((5,5),np.uint8)
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#filtre içinde uymayan kısımları belirginleştirir
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)#filtre içinde uymayan kısımları kapatır
    son_resim = cv2.bitwise_and(ss, ss, mask=closing)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)
    cv2.imshow("mavi renkler",son_resim)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()