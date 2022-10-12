import cv2
img=cv2.imread("r2.jpg")
body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies=body_cascade.detectMultiScale(griton,1.8 ,2)
for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("vücut",img)
cv2.waitKey()
cv2.destroyAllWindows()