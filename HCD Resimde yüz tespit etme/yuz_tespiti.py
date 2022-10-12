import cv2
img=cv2.imread("kalabalik.jpg")
yuz_casd=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
yuzler=yuz_casd.detectMultiScale(griton,1.1,3) #!(1.1) nekadar bir skalalama yapsın demek ----- (3) kaç kere orada yüz var mı diye teyit etsin
# detecetMultiScale bulduğu her yüzün sol üst x,y noktasının ve dikdörtgenin uzun ve kısa kenarını bulur.
for (x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("yuzler",img)
cv2.waitKey()
cv2.destroyAllWindows()