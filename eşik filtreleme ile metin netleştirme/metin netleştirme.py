import cv2
metin=cv2.imread("sayfa.jpg",0)
ret,th1=cv2.threshold(metin,7,255,cv2.THRESH_BINARY)
ret,th2=cv2.threshold(metin,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th3=cv2.adaptiveThreshold(metin,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)
th4=cv2.adaptiveThreshold(metin,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
# cv2.imshow("binary",th1)
# cv2.imshow("otsu",th2)
cv2.imshow("mean",th3)
# cv2.imshow("gauss",th4)
# cv2.imshow("metin",metin)
cv2.waitKey()
cv2.destroyAllWindows()