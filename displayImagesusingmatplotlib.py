import cv2
import matplotlib.pyplot as plt
image=cv2.imread('chrisfoot.jpeg')
img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()