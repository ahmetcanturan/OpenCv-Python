import pytesseract
import cv2
import numpy as np
from PIL import Image

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

kaynak_yolu=""
def metin_oku(img_yolu):
    img=cv2.imread(img_yolu)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((1,1),np.uint0)
    img=cv2.erode(img,kernel,iterations=1)
    img= cv2.dilate(img, kernel, iterations=1)
    img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2) #bu filtreyi kaldırınca a1 ve a2 için daha iyi okuyor
    sonuc=pytesseract.image_to_string(img,lang='tur')
    return sonuc

print("--------------------------------------")
print("metin okuma")
print("--------------------------------------")
print(metin_oku("a2.png"))
print("--------------------------------------")
print("Tamamlandı")