import cv2
adidas=cv2.imread("adidas2.jpg")
alex=cv2.imread("alex.jpg")
adidas_inv=cv2.bitwise_not(adidas)
satir,sutun,kanal=adidas_inv.shape
roi=alex[0:satir,0:sutun]
toplam=cv2.add(roi,adidas_inv)
alex[0:satir,0:sutun]=toplam
cv2.imwrite("alex_adidasinv.jpg",alex)
cv2.imshow("inv",adidas_inv)
cv2.imshow("toplam",toplam)
cv2.imshow("final",alex)

cv2.waitKey()
cv2.destroyAllWindows()