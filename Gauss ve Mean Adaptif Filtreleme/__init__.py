import cv2
import numpy as np
### Durumu göre gauss ve mean farkı fazla oluyor
from matplotlib import pyplot as plt
sudoku=cv2.imread("sudoku.JPG",0)
sudoku=cv2.medianBlur(sudoku,5)
ret , th1= cv2.threshold(sudoku,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(sudoku,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(sudoku,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
basliklar=["orjinal","binary","adaptive","gaussian"]
resimler=[sudoku,th1,th2,th3]
for i in range(4):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],"gray")
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])
plt.show()
