import cv2

def main():
    img=cv2.imread("cicek.png")
    ekran_cözünürlükleri=1280,720
    skala_genislik=ekran_cözünürlükleri[0]/img.shape[1]
    skala_yükseklik=ekran_cözünürlükleri[1]/img.shape[0]
    skala=min(skala_genislik,skala_yükseklik)
    pencere_genislik=int(img.shape[1]*skala)
    pencere_yükseklik=int(img.shape[0]*skala)
    cv2.namedWindow("boyulanabilir Pencere",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("boyulanabilir Pencere",pencere_genislik,pencere_yükseklik)
    cv2.imshow("boyulanabilir Pencere",img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
