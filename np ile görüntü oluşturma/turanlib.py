import math
import cv2
def line_derece(img,baslangic_x,baslangic_y,line_uzunluk,derece,blue,green,red,kalinlik):
    x_konum = (baslangic_x / 2) + (line_uzunluk * round(math.cos(math.radians(derece)), 3))
    y_konum = baslangic_y - (line_uzunluk * round(math.sin(math.radians(derece)), 3))
    cv2.line(img,(baslangic_x,baslangic_y),(int(x_konum),int(y_konum)),(blue,green,red),kalinlik)