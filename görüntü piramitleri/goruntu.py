import cv2

alex=cv2.imread("alex.jpg")
alex1pd=cv2.pyrDown(alex)
alex2pd=cv2.pyrDown(alex1pd)
alex3pd=cv2.pyrDown(alex2pd)
cv2.imshow("alex",alex)
cv2.imshow("alex1pd",alex1pd)
cv2.imshow("alex2pd",alex2pd)
cv2.imshow("alex3pd",alex3pd)
cv2.waitKey()
cv2.destroyAllWindows()