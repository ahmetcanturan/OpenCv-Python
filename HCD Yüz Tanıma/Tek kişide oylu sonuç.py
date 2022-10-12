import cv2
i=0
k=0
giris=0
tarama=0
bir=0
iki=0
uc=0
dort=0
bes=0
bilinmeyen=0
def isim_yaz(kisi):
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 255)
    cv2.putText(im, str(kisi), (x, y + h), fontFace, fontScale, fontColor)
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'yuzverileri'

cam = cv2.VideoCapture(0)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    print("Ahmet:" + str(bir) + " " + "Aziz:" + str(iki) + " " + "Annem:" + str(uc)+ " " + "Osai:" + str(dort)+ " " + "Alperen:" + str(bes)+ " " + "Bilinmeyen:" + str(bilinmeyen))
    if faces!=(): tarama=tarama+1
    for(x,y,w,h) in faces:
        if giris == 1:
            isim_yaz(kisi)
        tahminEdilenKisi, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        if(tahminEdilenKisi==1):
            bir = bir + 1
        elif (tahminEdilenKisi == 2):
            iki = iki + 1
        elif (tahminEdilenKisi == 3):
            uc = uc + 1
        elif (tahminEdilenKisi == 4):
            dort = dort + 1
        elif (tahminEdilenKisi == 5):
            bes = bes + 1
        else:
            bilinmeyen=bilinmeyen+1
        if 13>tarama>10 :
            giris=1
            buyuk=max(bir,iki)
            buyuk=max(buyuk,uc)
            buyuk=max(buyuk,dort)
            buyuk=max(buyuk,bes)
            buyuk=max(buyuk,bilinmeyen)
            if buyuk == bir : kisi="Ahmet Can"
            elif buyuk == iki: kisi= "Aziz Sancar"
            elif buyuk == uc: kisi = "Annem"
            elif buyuk == dort: kisi = "Osai Samuel"
            elif buyuk == bes: kisi = "Alperen"
            elif buyuk == bilinmeyen: kisi = "Bilinmeyen Kisi"
            tarama,bir,iki,uc,dort,bes,bilinmeyen=(0,0,0,0,0,0,0)
            isim_yaz(kisi)
    i=0

    cv2.imshow('im',im)
    if cv2.waitKey(2) & 0xFF==ord("q"):
        break









