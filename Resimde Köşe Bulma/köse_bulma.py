import cv2
import numpy as np
img=cv2.imread("img.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray) # uint8 den float32 formatına dönüştürdük
corner=cv2.goodFeaturesToTrack(gray,5000,0.011,10)
corner=np.int0(corner)
for kose in corner:
    x,y=kose.ravel()
    cv2.circle(img,(x,y),3,255,-1)
cv2.imshow("köse",img)
cv2.waitKey()
cv2.destroyAllWindows()

