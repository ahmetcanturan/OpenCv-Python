import pytesseract
import cv2
import numpy as np
from PIL import Image
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
kaynak_yolu=""

def metin_oku(img_yolu):
    img=cv2.imread(img_yolu)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,img=cv2.threshold(img,25,255,cv2.THRESH_BINARY)
    cv2.imwrite(kaynak_yolu+"gurultusuz.jpg",img)
    sonuc=pytesseract.image_to_string(Image.open(kaynak_yolu+'gurultusuz.jpg'),lang='tur')
    return sonuc

print("--------------------------------------")
print("metin okuma")
print("--------------------------------------")
print(metin_oku("foto.jpg"))
print("--------------------------------------")
print("Tamamlandı")