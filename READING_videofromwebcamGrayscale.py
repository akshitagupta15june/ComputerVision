import cv2
video =cv2.VideoCapture(0)
while(True):
    ret, frame = video.read()
    grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('FinalVideo', grayvideo)
    cv2.waitKey(1)
    if cv2.waitKey(33)==27:
        break
cv2.destroyAllWindows()
video.release()