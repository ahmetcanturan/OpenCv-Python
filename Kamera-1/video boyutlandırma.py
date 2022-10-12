import cv2
import time
kamera=cv2.VideoCapture(0,0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,150)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,150)

while True: #video değişkeni aslında bir resimdir ve resimlerin sürekli ekrana basılmasından video oluşur
    ret,video=kamera.read()
    # time.sleep(0.5) #fps ayarı bu şekildede yapılabilir
    griton=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    video[100:200,100:200]=[255,0,0]
    cv2.putText(griton,"Ahmet Can Turan",(36,400),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),4,cv2.LINE_AA)
    cv2.imshow("kamera2",video)
    cv2.imshow("kamera",griton)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()