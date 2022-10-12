import cv2
from skimage import io
adresler=["https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/1200px-OpenCV_Logo_with_text_svg_version.svg.png",
          "https://setav.org/assets/uploads/2018/06/turkiye-il-haritasi-1024x670.jpg"]
for adres in adresler:
    print("%s yükleniyor."%(adres))
    resim=io.imread(adres)
    cv2.imshow("BGR format",resim)
    cv2.imshow("RGB format",cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)) ### Convert yapılmazsa resim hatalı çekilmiş olur
    cv2.waitKey(0)