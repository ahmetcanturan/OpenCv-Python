import cv2
import numpy as np
zemin=np.zeros((500,500,3),'uint8')
cv2.putText(zemin,"Ahmet Can Turan",(36,400),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),4,cv2.LINE_AA)
cv2.imshow("zemin",zemin)
cv2.waitKey()
cv2.destroyAllWindows()