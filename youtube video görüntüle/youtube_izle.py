import pafy
import cv2
url='https://www.youtube.com/watch?v=4MRNTOHrJzw'
vPafy=pafy.new(url)
play=vPafy.getbest(preftype="mp4")

kamera=cv2.VideoCapture(play.url)

while True:
    _, video = kamera.read()
    griton = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    cv2.imshow("video", video)
    cv2.imshow("gri", griton)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
