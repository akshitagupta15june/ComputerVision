import cv2
import numpy as np
import matplotlib.pyplot as plt
image = np.zeros((512,512,3), np.uint8)
img=image.copy()
line=cv2.line(img,(0,0),(511,511),(255,0,0),5)
rect=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
circle=cv2.circle(img,(447,63), 63, (0,0,255), -1)
plt.imshow(img)
plt.show()



