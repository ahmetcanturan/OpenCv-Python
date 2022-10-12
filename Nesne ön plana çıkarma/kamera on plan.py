import cv2 #####Kendi yapımım
import numpy as np
from matplotlib import pyplot as plt
kamera=cv2.VideoCapture(0)
cerceve=(480,640,3)



diktortgen = (250, 105, 200,260)  # ilk iki değer x,y ikinci iki değer ilk noktanın sıfır noktası kabul edilmiş hali # odak
while True:
    ret,img=kamera.read()
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gray[165:380,195:445]=[0]
    ret,mask=cv2.threshold(img_gray,5,255,cv2.THRESH_BINARY_INV)
    toplam=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("img",toplam)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()