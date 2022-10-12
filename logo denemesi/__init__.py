import cv2
prison=cv2.imread("prison.jpg")
showtv=cv2.imread("showtv.jpg")
small_logo=cv2.pyrDown(showtv) #logoyu küçülttük
satir,sutun,kanal=small_logo.shape
roi=prison[0:satir,0:sutun] #prisondan arka planı aldık
logo_gray=cv2.cvtColor(small_logo,cv2.COLOR_BGR2GRAY) #bitwise işlemleri için logoyu 2 kanala düşürdük
ret,mask=cv2.threshold(logo_gray,25,255,cv2.THRESH_BINARY_INV) # logonun arka planını beyaz yaptık çünkü beyaz bitwisede etkisizdir
toplam1=cv2.bitwise_and(roi,roi,mask=mask)#prisonun arka planıyla siyah showtv logosunu ekledik
toplam2=cv2.add(small_logo,toplam1)#siyah renk add de geçersizdir bu sayede showtvnin renkli logosu siyah kısma geldi,orjinal show tvninde arka planı siyah olduğu için prison arka planı korundu
prison[0:satir,0:sutun]=toplam2
cv2.imwrite("final.jpg",prison)
cv2.imshow("gray",logo_gray)
cv2.imshow("thres",mask)
cv2.imshow("toplam2",toplam2)
cv2.imshow("toplam1",toplam1)
cv2.imshow("final",prison)
cv2.waitKey()
cv2.destroyAllWindows()