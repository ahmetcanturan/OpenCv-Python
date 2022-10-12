import cv2
import numpy as np
### ro:piksel olarak çözünürlük
### theta:radyan açı
### thresh:Çizgi kabul etmek için asgari kesişim sayısı
### minLineLength:Çizgi kabul etmek için asgari uzunluk
### maxLineGap:İki noktanın aynı çizgide sayılması için azami uzaklığı
img=cv2.imread("sudoku.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,5)
adapt = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
### Hougline bulma
rho, theta, thresh = 2, np.pi/180, 200
lines = cv2.HoughLinesP(adapt, rho, theta, thresh)
print(len(lines))
for ln in range(0,len(lines)):
    xy=lines[ln]
    cv2.line(img,(xy[0][0],xy[0][1]),(xy[0][2],xy[0][3]),(0,23,89,3),2)
cv2.imshow("adapt",adapt)
cv2.imshow("img",img)
# cv2.imshow("lines",lines)
cv2.waitKey()
cv2.destroyAllWindows()