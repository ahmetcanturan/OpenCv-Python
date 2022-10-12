import cv2
# #tüm eventleri görüntüledik
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print (events)
import cv2
import numpy as np
cizim=False
mod=False
xi=0
yi=0
i=0
# Mouse kontrol fonkisyonu(mouse callback function)
def draw_circle(event,x,y,flags,param):
    global cizim , mod ,xi ,yi ,i
    if event == cv2.EVENT_RBUTTONDOWN:
        fontscale = 0.5
        color = (255, 0, 0)
        fontface = cv2.FONT_HERSHEY_COMPLEX
        i+=1
        if i==1:
            cv2.putText(img_move, "Daire", (x,y), fontface, fontscale, color)
        elif i==2:
            cv2.putText(img_move, "Dikdortgen", (x, y), fontface, fontscale, color)
        elif i==3:
            cv2.putText(img_move, "Cizgi", (x, y), fontface, fontscale, color)
        else:
            i=0
    # if event == cv2.EVENT_LBUTTONDBLCLK:
    #     cv2.circle(img,(x,y),50,(255,0,0),-1)
    if event == cv2.EVENT_LBUTTONDOWN and mod==False:
        xi, yi = x,y
        mod=True
    elif event == cv2.EVENT_MOUSEMOVE and mod == True:
        img_move[:,:]=(0,0,0)
        cv2.rectangle(img_move, (xi, yi), (x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP and mod==True:
        cizim=True
    if event == cv2.EVENT_LBUTTONDOWN and cizim==True:
        cizim=False
        mod=False
        cv2.rectangle(img, (xi, yi), (x, y), (0, 255, 0), -1)
# Siyah bir panel oluştur ve fonksiyonu birleştir
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
img_move = np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback('image',draw_circle) #image üzerindeki mouse olaylarını izler ve yazdığın fonksiyona gider

while(1):
    son=cv2.add(img,img_move)
    cv2.imshow('image' , son)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()