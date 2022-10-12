import cv2

gürültülü_resim=cv2.imread("gurultuluresim.JPG",0)
ret,th1=cv2.threshold(gürültülü_resim,125,255,cv2.THRESH_BINARY)
ret,th2=cv2.threshold(gürültülü_resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur=cv2.GaussianBlur(gürültülü_resim,(5,5),0)
ret,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(str(th1.shape))




cv2.imshow("normal thres",th1)
cv2.imshow("otsu",th2)
cv2.imshow("blur",th3)
cv2.waitKey()
cv2.destroyAllWindows()