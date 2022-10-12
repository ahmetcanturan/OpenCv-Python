import cv2
import numpy as np
backsub = cv2.createBackgroundSubtractorMOG2() #harekette arka plan temizleme yontemi
capture = cv2.VideoCapture("video.avi")
i = 0
minArea=2600 #minimum ağırlıklı alan değeri
while True:
    ret, frame = capture.read()
    fgmask = backsub.apply(frame, None, 0.02)
    erode=cv2.erode(fgmask,None,iterations=4) # maske kırpma
    moments=cv2.moments(erode,True) #herbir hareketli nesnenin ağırlık merkezini oluşturur.
    # print("Moment:",moments)
    area=moments['m00']
    #dikey ust sol şerit
    cv2.line(frame,(40,0),(40,176),(255,0,0),2)
    cv2.line(frame, (55, 0), (55, 176), (255, 0, 0), 2)
    #yatay ust
    cv2.line(frame,(0,50),(320,50),(255,0,0),2)
    cv2.line(frame, (0, 65), (320, 65), (255, 0, 0), 2)
    #dikey alt sağ şerit
    cv2.line(frame, (100, 0), (100, 176), (0, 255, 255), 2)
    cv2.line(frame, (115, 0), (115, 176), (0, 255, 255), 2)
    # yatay alt
    cv2.line(frame, (0, 105), (320, 105), (0, 255, 255), 2)
    cv2.line(frame, (0, 130), (320, 130), (0, 255, 255), 2)

    if moments['m00'] >=minArea: #eğer moment minAreadan büyükse araba geçmiştir.
        x=int(moments['m10']/moments['m00']) # geçen arabanın ağırlıklı merkezinin x bileşeni
        y=int (moments['m01']/moments['m00']) # geçen arabanın ağırlıklı merkezinin y bileşeni
        # print("mom :" + str(moments['m00']) + "x :" + str(x) + " y : " + str(y)) #herhangi bir araç geçtiğinde moment değerini ekrana yazdır ve minAreanın belirlenmesinde buradan yardım al
        if x>40 and x<55 and y>50 and y<65: # 30. satirdan x y değerlerine karar verildi
            i=i+1

            print("ust"+str(i))
        elif x>102 and x<110 and y>105 and y<130:
            i=i+1
            # print("alt"+str(i))

        cv2.putText(frame,'Sayi: %r' %i, (200,30), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 2)
        cv2.imshow("frame", frame)
        cv2.imshow("fgmask", fgmask)

    key = cv2.waitKey(25)
    if key == ord('q'):
            break

capture.release()

cv2.destroyAllWindows()

