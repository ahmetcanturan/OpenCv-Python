import cv2
import numpy as np
kamera=cv2.VideoCapture(0)
metre=cv2.imread("metre.jpg",0)
metre1=cv2.pyrDown(metre)
metre2=cv2.pyrDown(metre1)

h,w=metre.shape
h1,w1=metre1.shape
h2,w2=metre2.shape
while True:
    ret,goruntu=kamera.read()
    img_gray = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    res=cv2.matchTemplate(img_gray,metre,cv2.TM_CCOEFF_NORMED)
    threshold=0.50
    loc = np.where(res > threshold)  # eşleşmenin %80den büyük olduğu noktaları loc değişkeninde tut
    for n in zip(*loc[::-1]):
        cv2.rectangle(goruntu, n, (n[0] + w, n[1] + h), (0, 255, 255), 2)
    res1= cv2.matchTemplate(img_gray, metre1, cv2.TM_CCOEFF_NORMED)
    loc1 = np.where(res1 > threshold)
    for n1 in zip(*loc1[::-1]):
        cv2.rectangle(goruntu, n1, (n1[0] + w1, n1[1] + h1), (0, 255, 255), 2)
    res2 = cv2.matchTemplate(img_gray, metre2, cv2.TM_CCOEFF_NORMED)
    loc2 = np.where(res2 > threshold)
    for n2 in zip(*loc2[::-1]):
        cv2.rectangle(goruntu, n2, (n2[0] + w2, n2[1] + h2), (0, 255, 255), 2)
    cv2.imshow("kamera",goruntu)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()