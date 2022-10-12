import cv2

kamera=cv2.VideoCapture(1)

while True:
    ret,goruntu=kamera.read()
    goruntu=cv2.flip(goruntu,1)
    cv2.imshow("kamera",goruntu)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        cv2.imwrite("../resim eşleştirme/goruntu.jpg", goruntu)
        break
kamera.release()
cv2.destroyAllWindows()