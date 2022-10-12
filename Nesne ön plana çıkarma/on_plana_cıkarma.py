import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("on_plan.jpg")
mask=np.zeros(img.shape[:2],np.uint8,) # resim boyutunda siyah çerçeve oluşturduk

bgdModel=np.zeros((1,65),np.float64) # bunların neden yapıldığını anlamadım
fgdModel=np.zeros((1,65),np.float64)

diktortgen=(250,105,200,260) # ilk iki değer x,y ikinci iki değer ilk noktanın sıfır noktası kabul edilmiş hali # odak buradan ayarlanır
cv2.grabCut(img,mask,diktortgen,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()