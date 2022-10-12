import pyautogui
import cv2
import time
print(pyautogui.size())# ekran çözünürlüğü
# while 1:
#     print(pyautogui.position())#mouse konumu
#     time.sleep(0.5)
# pyautogui.displayMousePosition() # olmadı
pyautogui.moveTo(1000,50)# mouseyi istenen konuma gönderir
pyautogui.moveTo(500,200,duration=3) # mouseyi istenen konuma yavaş bir şekilde götürür
#pyautogui.dragTo(1394,530,duration=4)#Sürükle bırak işlemini yapan methoddur. Mouse o an hangi pozisyonda ise, ordan dragTo içerisindeki konuma sürükle bırak yapar.
pyautogui.click(button='right', clicks=3, interval=0.25) #Tıklama işlemini yapar. ‘left’, ‘middle’, ve ‘right’ . Bir de click parametresi alır, kaç kere tıklansın anlamındadır.
pyautogui.rightClick(x=1393,y=333) # gönderilen kordinatta sağ tıklar
pyautogui.doubleClick(300,200) # gönderilen kortinatta çift tıklar
pyautogui.scroll(10)
#Bu methodlardan ilki olan mouseDown() mouse tıklama işlevini yapar. Ancak bastığınız butonu bırakmaz,
# ta ki siz bırak diyene kadar.
# Peki bırak nasıl deriz, onu da mouseUp() ile yapıyoruz.
#Peki bu tıklamayı sol buton ile mi sağ ile mi yoksa ortadaki buton ile mi yapabiliriz?
# Bunu da parametre olarak geçebilirsiniz.
pyautogui.mouseDown(100, 200, button='left')
pyautogui.mouseUp(100, 200, button='left')
pyautogui.alert(text='Başvurunuz Alındı.', title='www.sinanerdinc.com', button="Tamam") # Ekrana Uyarı gönderir
#Bu kullanışlı method ise bilgisayarınızdaki bir resim, ekranda varsa hangi koordinatlarda olduğunu size döner.
# Ben avatarımı kestim ve bilgisayarıma kaydettim.
x,y = pyautogui.locateCenterOnScreen("sinan.png")
pyautogui.moveTo(x,y,duration=1.5)
