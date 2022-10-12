import time
import cv2
import numpy as np
import math
çubuk=400
genislik=620
yükseklik=400

def x_ekseni(açı):
    if(açı<=90):
        x_konum=(genislik/2)+(çubuk*round(math.cos(math.radians(açı)),3))
    else:
        x_konum=(genislik/2)+(çubuk*round(math.cos(math.radians(açı)),3))
    r_x=int(x_konum)
    return r_x

def y_ekseni(açı):
    if (açı<=90):
        y_konum=yükseklik-(çubuk*round(math.sin(math.radians(açı)),3))
    else:
        y_konum=yükseklik-(çubuk*round(math.sin(math.radians(açı)),3))
    r_y=int(y_konum)
    return r_y
img=np.zeros((400,620,3),dtype='uint8')
img2=cv2.imread("cicek.png")
while 1:
    for i in range(180):
        print(i)
        img[0:, 0:] = [0, 0, 0]
        x=x_ekseni(i)
        y=y_ekseni(i)
        cv2.line(img, (310, 400), (x, y), (255, 255, 255), 4)
        toplam = cv2.add(img, img2)
        cv2.imshow("img", toplam)
        cv2.waitKey(100)
    for j in range(180, -1, -1):
        print(j)
        img[0:, 0:] = [0, 0, 0]
        x = x_ekseni(j)
        y = y_ekseni(j)
        cv2.line(img, (310, 400), (x, y), (255, 255, 255), 4)
        toplam = cv2.add(img, img2)
        cv2.imshow("img", toplam)
        cv2.waitKey(100)
cv2.destroyAllWindows()