import cv2
import matplotlib.pyplot as plt
import numpy as np
resim_aranacak=cv2.imread("kucuk_resim.JPG",0)
resim_buyuk=cv2.imread("buyuk_resim.JPG",0)
orb=cv2.ORB_create() # odaklanmış ve dönmüş resimlerin tespiti için orb değişkeni oluştur
an1,hedef1=orb.detectAndCompute(resim_aranacak,None)#resimleri analiz eder
an2,hedef2=orb.detectAndCompute(resim_buyuk,None)
bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)#ortak noktaların bulunması için cross çapraz sorgu yapma ayarı
eslesmeler=bf.match(hedef1,hedef2) #benzerlikleri bulur
eslesmeler=sorted(eslesmeler,key=lambda x:x.distance) # eşleşmelerin mesafe bilgilerini al
son_resim=cv2.drawMatches(resim_aranacak,an1,resim_buyuk,an2,eslesmeler[:10],None,flags=2) #eşleşmeleri çiz
plt.imshow(son_resim)
plt.show()