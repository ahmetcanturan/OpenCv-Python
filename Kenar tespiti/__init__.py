import cv2
camii=cv2.imread("mevlana.jpg")
camii=cv2.pyrDown(camii)
camii_gray=cv2.cvtColor(camii,cv2.COLOR_BGR2GRAY)
kenarlar=cv2.Canny(camii_gray,60,100)
kenarlar=cv2.bitwise_not(kenarlar)
camii_gray=cv2.blur(camii_gray,(2,2))
th3=cv2.adaptiveThreshold(camii_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
toplam=cv2.bitwise_and(camii,camii,mask=th3)
topla=cv2.bitwise_and(camii,camii,mask=kenarlar)
cv2.imshow("th3",toplam)
cv2.imshow("kenarlar",topla)
cv2.waitKey()
cv2.destroyAllWindows()
