import cv2
import numpy as np
liste=[1,3,5]
img=cv2.imread("ana_resim.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
nesne=cv2.imread("template.jpg",0)
h,w=nesne.shape # shapenin y,x değeri x,y olarak çevrildi
res=cv2.matchTemplate(img_gray,nesne,cv2.TM_CCOEFF_NORMED) #
threshold=0.8 #eşleşme minimum yüzde 80 olsun.
loc=np.where(res>threshold) # eşleşmenin %80den büyük olduğu noktaları loc değişkeninde tut
for n in zip(*loc[::-1]):
    cv2.rectangle(img,n,(n[0]+w,n[1]+h),(0,255,255),2)

cv2.imshow("bulunan nesneler",img)
cv2.waitKey()
cv2.destroyAllWindows()