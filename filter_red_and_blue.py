import cv2
import numpy as np
filter = cv2.imread('redBlue.jpeg')
cv2.imshow("original",filter)
filter = cv2.resize(filter, (300, 300))
hsv = cv2.cvtColor(filter, cv2.COLOR_BGR2HSV)
lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)
result = cv2.bitwise_and(filter, filter, mask=mask)
cv2.imshow("filtered image",filter)
