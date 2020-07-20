import cv2
img1=cv2.imread("input2.png")
img2 = cv2.imread('open.png')
dest_xor = cv2.bitwise_xor(img1, img2, mask=None)
cv2.imshow('Bitwise XOR', dest_xor)
dest_not1 = cv2.bitwise_not(img1, mask=None)
dest_not2 = cv2.bitwise_not(img2, mask=None)

cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()