import cv2
import numpy as np
kamera=cv2.VideoCapture(0)
while True:
    ret,ss=kamera.read()
    ss=cv2.flip(ss,1)
    hsv=cv2.cvtColor(ss,cv2.COLOR_BGR2HSV)
    dusuk_kirmizi = np.array([150, 30, 30])
    yuksek_kirmizi = np.array([190,255,255])
    mask=cv2.inRange(hsv,dusuk_kirmizi,yuksek_kirmizi)
    son_resim=cv2.bitwise_and(ss,ss,mask=mask)
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=2) # gürültüleri siliyor
    dilation=cv2.dilate(mask,kernel,iterations=2)#gürültüleri büyütüyor
    erosion = cv2.bitwise_and(ss, ss, mask=erosion)
    dilation = cv2.bitwise_and(ss, ss, mask=dilation)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilation)
    cv2.imshow("mavi renkler",son_resim)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()