import cv2
alex=cv2.imread("alex.jpg")
alex=cv2.pyrDown(alex)
kenarlar=cv2.Canny(alex,100,100)
alex_gray=cv2.cvtColor(alex,cv2.COLOR_BGR2GRAY)

th3=cv2.adaptiveThreshold(alex_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
th3=cv2.bitwise_not(th3)
cv2.imshow("alex",kenarlar)
cv2.imshow("thres",th3)
cv2.waitKey()
cv2.destroyAllWindows()