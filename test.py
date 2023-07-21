import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    roi = frame #region of interest
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7,7), 0)
    _, threshold = cv2.threshold(gray_roi,5, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("gray", gray_roi)
    cv2.imshow("threshold",threshold)
    key = cv2.waitKey(30)
    if key == 27 :
        break

cv2.destroyAllWindows()