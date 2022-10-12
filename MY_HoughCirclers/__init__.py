# Method:Kullanılan metod tek metod vardır cv2.HOUGH_GRADIENT
# dp: Çözünürlüğün tersi 1:%100 , 2: %50 demektir.
# minDist: Bulunan çember merkezleri arası asgari uzaklık.
# param1=ön tanımşı değeri 100 dür. çoğunlukla yeterlidir.
# param2=ön tanımlı değeri 100 dür. çoğunlukla yeterlidir. Düşürüldüğünde daha çok çember daha az hassaslıkla bulunur yükseltildiğinde tam tersi
import cv2
import numpy as np
img = cv2.imread("coin.png")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, output) = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)
output1 = cv2.GaussianBlur(output, (5, 5), 1)
output2 = cv2.Canny(output1, 180, 255)
circles = cv2.HoughCircles(output2, cv2.HOUGH_GRADIENT, 1, 10, param1=180, param2=27, minRadius=20, maxRadius=60)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imshow("thres",output)
cv2.imshow("blur",output1)
cv2.imshow("canny",output2)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()