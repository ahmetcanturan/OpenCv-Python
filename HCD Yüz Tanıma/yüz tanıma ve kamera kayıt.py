import cv2

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'yuzverileri'

cam = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
kayit=cv2.VideoWriter("kayit.avi",fourcc,20,(640,480))
while (cam.isOpened()):
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        tahminEdilenKisi, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        if(tahminEdilenKisi==1):
             tahminEdilenKisi= 'Ahmet Can'
        elif (tahminEdilenKisi == 5 or tahminEdilenKisi==6):
            tahminEdilenKisi = 'Alperen'
        elif (tahminEdilenKisi == 2):
            tahminEdilenKisi = 'Aziz Sancar'
        elif (tahminEdilenKisi == 3):
            tahminEdilenKisi = 'Annem'
        elif (tahminEdilenKisi == 4):
            tahminEdilenKisi = 'Osai Samuel'
        else:
            tahminEdilenKisi= "Bilinmeyen kişi"
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255, 255, 255)
        cv2.putText(im, str(tahminEdilenKisi), (x, y + h), fontFace, fontScale, fontColor)
    kayit.write(im)
    cv2.imshow('im', im)
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break
cam.release()
kayit.release()
cv2.destroyAllWindows()





