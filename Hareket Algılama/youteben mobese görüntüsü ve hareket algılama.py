import cv2
import pafy
#url='https://www.youtube.com/watch?v=9gT5BZmolgQ'
#vPafy=pafy.new(url)
#play=vPafy.getbest(preftype="mp4")

cap=cv2.VideoCapture(0)
capsize=cv2.pyrDown(cap.read()[1])
frame1 = capsize
frame2 = capsize

print(frame1.shape)
while cap.isOpened():
    capsize = cv2.pyrDown(cap.read()[1])
    diff = cv2.absdiff(frame1, frame2) #işi yapan komut
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=3)
    image = cv2.resize(frame1, (1280,720))
    cv2.imshow("orginal", capsize)
    cv2.imshow("gri",dilated)
    frame1 = frame2
    frame2 = capsize

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()