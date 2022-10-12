import cv2
import numpy as np
kamera=cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_BRIGHTNESS,-50)

while 1:
    ret , frame=kamera.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F,0,1,ksize=5)
    kenarlar=cv2.Canny(frame,50,200)
    cv2.imshow("orjinal",frame)
    cv2.imshow("Canny",kenarlar)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Sobelx",sobelx )
    cv2.imshow("Sobely", sobely)

    if cv2.waitKey(25) & 0xFF== ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()