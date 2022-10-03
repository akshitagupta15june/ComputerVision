import cv2
import matplotlib.pyplot as plt
image = cv2.imread('person.jpg')
image_temp = image.copy()
full_body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
body = full_body_cascade.detectMultiScale(gray_image, 1.02, 3)
for (x, y, w, h) in body:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("final",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
