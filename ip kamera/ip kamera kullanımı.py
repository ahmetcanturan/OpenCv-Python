import cv2
url="http://192.168.1.5:8080/shot.jpg" # ip kameranın anlık resim yolu
kamera = cv2.VideoCapture(url)
while True:
    kamera = cv2.VideoCapture(url)
    ret,ss=kamera.read()
    ss=cv2.flip(ss,-1)
    cv2.imshow("kamera",ss)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()