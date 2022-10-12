import cv2
import numpy as np

img = cv2.imread("img.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY_INV)
# Find the contours
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# For each contour approximate the curve and
# küçük mesafe kortinatlarını pas gec
for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(img, [approx], 0, (0), 3)
    # Position for writing text
    x, y = approx[0][0]
#anladığım kadarıyla düzelttiği çizimlerden köşe sayısını arıyor.
    if len(approx) == 3:
        cv2.putText(img, "Ucgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    elif len(approx) == 4:
        cv2.putText(img, "Dikdortgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    elif len(approx) == 5:
        cv2.putText(img, "Besgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    elif 6 < len(approx) < 15:
        cv2.putText(img, "Elips", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
    else:
        cv2.putText(img, "Daire", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)
cv2.imshow("final", img)
cv2.waitKey(0)