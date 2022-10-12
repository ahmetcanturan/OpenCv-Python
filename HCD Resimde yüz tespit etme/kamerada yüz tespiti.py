import cv2
kamera=cv2.VideoCapture(0)
yuz_casd = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret,img=kamera.read()
    griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    yuzler = yuz_casd.detectMultiScale(griton, 1.3, 3)
    for (x, y, w, h) in yuzler:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("kamera",img)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()