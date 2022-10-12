import cv2
import numpy as np


cizim = False #Fareye tıklandıysa True

mod = True #Eğer True ise dikdörtgen çiz. 'm' ye basılıysa eğrili çiz

ix, iy = -1, -1

def daireCiz(event, x,y,flags,param):
    global ix, iy,cizim,mod

    if event == cv2.EVENT_LBUTTONDOWN:
        cizim = True
        ix, iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if cizim == True:
           if mod == True:
               cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
           else:
               cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        cizim = False
        if mod == True:
            pass
            #cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image',daireCiz)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mod = not mod
    elif k == 27:
        break


cv2.destroyAllWindows()
