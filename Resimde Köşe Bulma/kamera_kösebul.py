import cv2
import numpy as np
kamera=cv2.VideoCapture(0)

while 1:
    ret,foto=kamera.read()
    foto_gray=cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY)
    cv2.imshow("üst", foto_gray)
    # ret, foto_gray = cv2.threshold(foto_gray, 40, 255, cv2.THRESH_BINARY) belirli bir renk algılıyorsan kalite artıyor
    foto_gray=np.float32(foto_gray)
    cv2.imshow("alt",foto_gray)

    foto_gray=cv2.GaussianBlur(foto_gray,(5,5),0)
    corner=cv2.goodFeaturesToTrack(foto_gray,1000,0.01,20)
    corner=np.int0(corner)
    for kose in corner:
        x,y=kose.ravel()
        cv2.circle(foto,(x,y),3,255,-1)
    cv2.imshow("koseler",foto)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()