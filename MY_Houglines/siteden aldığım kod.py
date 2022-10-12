import cv2
import numpy as np
kernel=np.ones((2,2),np.uint8)
img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,5)
adapt = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
erode=cv2.erode(adapt,kernel,iterations=1)
dilation=cv2.dilate(erode,kernel,iterations=2)

minLineLength = 40
maxLineGap = 5
lines = cv2.HoughLinesP(dilation,1,np.pi/180,90,minLineLength=minLineLength,maxLineGap=maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(12,255,45),2)
cv2.imshow('adapt',adapt)
cv2.imshow('hough',img)
cv2.imshow('erode',erode)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)