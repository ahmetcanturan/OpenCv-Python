import cv2
fener=cv2.imread("fener_logo.jpg")
adidas=cv2.imread("adidas2.jpg",0)# 0 ı eklemezsem bitwise_and hata veriyor mask kısmını sadece 2 kanallı istiyor
alex=cv2.imread("alex.jpg")
# satir,sutun=adidas.shape
# ret,mask=cv2.threshold(adidas,180,255,cv2.THRESH_BINARY)
# img_bg=alex[0:satir,0:sutun]
# toplam1=cv2.bitwise_and(img_bg,img_bg,mask=mask)
# alex[0:satir,0:sutun]=toplam1
# cv2.imwrite("alex_adidas_dark.jpg",alex)
# cv2.imshow("toplam1",toplam1)
# cv2.imshow("mask",mask)
# cv2.imshow("sonuç",alex)
#######################################buraya kadar farklı program
# satir,sutun,kanal=fener.shape
# img_bg=alex[0:satir,0:sutun]
# fener_gray=cv2.cvtColor(fener,cv2.COLOR_BGR2GRAY)
# ret,mask=cv2.threshold(fener_gray,230,255,cv2.THRESH_BINARY)
# mask_inv=cv2.bitwise_not(mask)
# toplam1=cv2.bitwise_and(fener,fener,mask=mask_inv)
# toplam2=cv2.add(toplam1,img_bg)
# alex[0:satir,0:sutun]=toplam2
# cv2.imwrite("alex_fenerlogo.jpg",alex)
# cv2.imshow("fener",fener)
# cv2.imshow("fener_gray",fener_gray)
# cv2.imshow("mask_inv",mask_inv)
# cv2.imshow("toplam1",toplam1)
# cv2.imshow("toplam2",toplam2)
# cv2.imshow("final",alex)
cv2.waitKey()
cv2.destroyAllWindows()