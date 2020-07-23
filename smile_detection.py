import cv2

image = cv2.imread("smile.jpeg")
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
smiles = smile_cascade.detectMultiScale(image, scaleFactor=1.8, minNeighbors=20)

for (sx, sy, sw, sh) in smiles:
    cv2.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 5)

cv2.imshow("Smile Detected", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
