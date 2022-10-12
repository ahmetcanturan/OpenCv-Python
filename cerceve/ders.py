import cv2
import numpy as np
from matplotlib import pyplot as plt
mavi=[255,0,0]
logo=cv2.imread("opencv.JPG")
replicate=cv2.copyMakeBorder(logo,10,10,10,10,cv2.BORDER_REPLICATE)
reflective=cv2.copyMakeBorder(logo,10,10,10,10,cv2.BORDER_REFLECT)
reflective101=cv2.copyMakeBorder(logo,10,10,10,10,cv2.BORDER_REFLECT101)
wrap=cv2.copyMakeBorder(logo,10,10,10,10,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(logo,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)
plt.subplot(231),plt.imshow(logo,"gray"),plt.title("original")
plt.subplot(232),plt.imshow(replicate,"gray"),plt.title("replicate")
plt.subplot(233),plt.imshow(reflective,"gray"),plt.title("reflective")
plt.subplot(234),plt.imshow(reflective101,"gray"),plt.title("reflective101")
plt.subplot(235),plt.imshow(wrap,"gray"),plt.title("wrap")
plt.subplot(236),plt.imshow(constant,"gray"),plt.title("constant")
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()