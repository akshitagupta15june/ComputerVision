import cv2
import numpy as np
import matplotlib.pyplot as plt
image = np.zeros((512,512,3), np.uint8)
img=image.copy()
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
ellipse=cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
plt.imshow(img)
plt.show()
