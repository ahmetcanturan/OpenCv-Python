import cv2

kamera=cv2.VideoCapture(0)
logo=cv2.imread("img.png")
logo=cv2.pyrDown(logo)
logo=cv2.pyrDown(logo)
logo_gray=cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(logo_gray,25,255,cv2.THRESH_BINARY_INV)
satir,sutun=logo_gray.shape
while True:
    ret,goruntu=kamera.read()
    roi=goruntu[0:satir,0:sutun]
    toplam1=cv2.bitwise_and(roi,roi,mask=mask)
    toplam2=cv2.add(toplam1,logo)
    goruntu[0:satir,0:sutun]=toplam2
    cv2.imshow("kamera",goruntu)
    cv2.imshow("logo", logo_gray)
    cv2.imshow("msk", mask)

    if cv2.waitKey(1) & 0xFF==ord('v'):
        cv2.imwrite("foto_cek.jpg",goruntu)
        cv2.imshow("Cekilen Foto",cv2.imread("foto_cek.jpg"))
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()