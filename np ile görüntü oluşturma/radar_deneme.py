import cv2
import numpy as np
import turanlib

cicek=cv2.imread("cicek.png")
cerceve=np.zeros((400,620,3),dtype='uint8')
turanlib.line_derece(cerceve,200,200,150,90,255,0,0,4)






cv2.imshow("cerceve",cerceve)
cv2.waitKey()
cv2.destroyAllWindows()
