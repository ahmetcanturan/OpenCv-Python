import cv2
import numpy as np
img1=cv2.imread("resim.jpg")
img2=cv2.imread("logo.jpg")
toplam=cv2.addWeighted(img1,0.3,img2,0.7,0)
cv2.imshow("toplam",toplam)
cv2.waitKey()
cv2.destroyAllWindows()