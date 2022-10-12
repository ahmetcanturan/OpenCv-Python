import cv2
from datetime import datetime


def farkImaj(t0,t1,t2):
    fark1=cv2.absdiff(t2,t1)
    fark2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(fark1,fark2)
# cerceve eni*boyu*3 esitliği baz alınarak eşik değerinin oranı kurulur

esik_deger=3140
kamera=cv2.VideoCapture(0)
_,img=kamera.read()
roi=img[0:70,0:70]
t_eksi=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
t=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
t_arti=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

zamanKontrol=datetime.now().strftime('%Ss')

def akilli_kapatma(kamera):
    global t
    global t_arti
    global t_eksi
    global zamanKontrol
    # cv2.imshow(pencereIsmi,kamera.read()[1])

    if cv2.countNonZero(farkImaj(t_eksi,t,t_arti))>esik_deger and zamanKontrol !=datetime.now().strftime('%Ss'):
        print("Algılandı")
        return 1
    zamanKontrol = datetime.now().strftime('%Ss')
    t_eksi = t
    t = t_arti
    _, img = kamera.read()
    roi = img[0:70, 0:70]
    t_arti = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    cv2.waitKey(10)