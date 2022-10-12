import cv2
import numpy as np
### blunıklaştırmanın maskeden önce veya sonra olması fark yaratıyor.....
kamera=cv2.VideoCapture(0)
while True:
    ret,ss=kamera.read()
    hsv=cv2.cvtColor(ss,cv2.COLOR_BGR2HSV)
    dusuk_mavi = np.array([100, 60, 60])
    yuksek_mavi = np.array([140, 255, 255])
    mask=cv2.inRange(hsv,dusuk_mavi,yuksek_mavi)
    mask1=cv2.inRange(hsv,dusuk_mavi,yuksek_mavi)
    son_resim=cv2.bitwise_and(ss,ss,mask=mask)
    blur = cv2.GaussianBlur(son_resim, (15,15),0)
    bilateral=cv2.bilateralFilter(son_resim,15,75,75)
    cv2.imshow("filtresiz", son_resim)
    cv2.imshow("Gaussian",blur)
    cv2.imshow("Median",bilateral)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()