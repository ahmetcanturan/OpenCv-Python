import cv2
yuz_casde=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz_casde=cv2.CascadeClassifier("haarcascade_eye.xml")
kamera=cv2.VideoCapture(0)

while True:
    _,goruntu=kamera.read()
    griton=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_casde.detectMultiScale(griton,1.1,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,255,0),3) # çizilen yüz çercevesinin içinde göz arıyacağız
        roi_griton=griton[y:y+h,x:x+w]
        roi_renkli=goruntu[y:y+h,x:x+w]# x,y sıfırı yüzün içi olduğundan direk goruntuye çizdiremeyiz
        gozler=goz_casde.detectMultiScale(roi_griton,1.2,7)
        for (ex,ey,ew,eh) in gozler: #sadece yüz bulunduğunda göz arıyacak
            cv2.rectangle(roi_renkli, (ex, ey), (ex + ew, ey + eh), (0, 158, 0), 3)
        # goruntu[y:y + h, x:x + w]=roi_renkli # bu kod çalışmadan nasıl ana görüntüye göz dikdrörtgeni çizdirdik anlamadım
    cv2.imshow("yuz_goz_tespiti",goruntu)
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break
kamera.release()
cv2.destroyAllWindows()

