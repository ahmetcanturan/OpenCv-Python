import cv2
import numpy as np
messi=cv2.imread("messi.jpg")
print(str(messi[:,:,2]))
messi[:,:,0]=100
messi[:,:,1]=10
cv2.imshow("mavi",messi)
cv2.waitKey()
cv2.destroyAllWindows()