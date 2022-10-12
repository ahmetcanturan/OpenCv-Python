import cv2
img=cv2.imread("saat.jpg")
print(str(img[20,30]))
bölge=img[30:120,100:200]
img[0:90,0:100]=bölge
#cv2.rectangle(img,(100,30),(200,120),(0,255,255),2)
cv2.imshow("saat",img)
cv2.imshow("bölge",bölge)
cv2.waitKey()
cv2.destroyAllWindows()