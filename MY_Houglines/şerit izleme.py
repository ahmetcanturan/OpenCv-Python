import cv2
import numpy as np
yol=cv2.imread("yol.jpeg")
gray=cv2.cvtColor(yol,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,5)
_,th=cv2.threshold(blur,205,255,cv2.THRESH_BINARY)
lines = cv2.HoughLinesP(th, 1, np.pi/180,20)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(yol,(x1,y1),(x2,y2),(0,255,0),4)
cv2.imshow("thresh",yol)
cv2.imshow("thh",th)
cv2.waitKey()
cv2.destroyAllWindows()