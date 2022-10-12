import cv2
import turanlib

kamera=cv2.VideoCapture(0)
while True:
    _,img=kamera.read()
    img=cv2.flip(img,1)
    cv2.imshow("kamera",img)
    if turanlib.akilli_kapatma(kamera)==1 &  cv2.waitKey(10):
        break
cv2.destroyAllWindows()
kamera.release()