import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray , (5,5), 0)
	edge = cv2.Canny(blur, 70, 100)
	ret, thresh = cv2.threshold(edge,250, 255, cv2.THRESH_BINARY_INV)
	cv2.imshow("final",thresh)

	if cv2.waitKey(33) == 27:
		break;
cap.release()
cv2.destroyAllWindows()