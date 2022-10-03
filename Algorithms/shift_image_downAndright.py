import cv2
import numpy as np

image = cv2.imread('chrisfoot.jpeg')
shift = 40

for i in range(image.shape[1] -1, image.shape[1] - shift, -1):
    image = np.roll(image, -1, axis=1)
    image[:, -1] = 0

cv2.imshow('image', image)
cv2.waitKey()
