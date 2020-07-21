import cv2
img=cv2.imread("DINO.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaussian = cv2.GaussianBlur(img.copy(), (7,7), 0)
edge = cv2.Canny(gaussian, 90, 130)
cv2.imshow("FINAL",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()