import cv2
import numpy as np
kamera=cv2.VideoCapture(0)
resim_aranacak=cv2.imread("metre.jpg",0)
resim_aranacak=cv2.pyrDown(resim_aranacak)

# metre2=cv2.pyrDown(metre1)

h,w=resim_aranacak.shape

while True:
    ret,goruntu=kamera.read()
    resim_buyuk = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    an1, hedef1 = orb.detectAndCompute(resim_aranacak, None)  # resimleri analiz eder
    an2, hedef2 = orb.detectAndCompute(resim_buyuk, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    eslesmeler = bf.match(hedef1, hedef2)
    eslesmeler = sorted(eslesmeler, key=lambda x: x.distance)
    son_resim = cv2.drawMatches(resim_aranacak, an1, resim_buyuk, an2, eslesmeler[:10], None, flags=2)
    cv2.imshow("kamera",son_resim)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()