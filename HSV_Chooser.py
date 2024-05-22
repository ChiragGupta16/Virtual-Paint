import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3,300)
cam.set(4,300)
cam.set(10,100)


def empty(a):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 280)
cv2.createTrackbar("Hmin", "HSV", 0, 179, empty)
cv2.createTrackbar("Hmax", "HSV", 179, 179, empty)
cv2.createTrackbar("Smin", "HSV", 0, 255, empty)
cv2.createTrackbar("Smax", "HSV", 255, 255, empty)
cv2.createTrackbar("Vmin", "HSV", 0, 255, empty)
cv2.createTrackbar("Vmax", "HSV", 255, 255, empty)


while True:
    isOk,img = cam.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hmin", "HSV")
    h_max = cv2.getTrackbarPos("Hmax", "HSV")
    s_min = cv2.getTrackbarPos("Smin", "HSV")
    s_max = cv2.getTrackbarPos("Smax", "HSV")
    v_min = cv2.getTrackbarPos("Vmin", "HSV")
    v_max = cv2.getTrackbarPos("Vmax", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
