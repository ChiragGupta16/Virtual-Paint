import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

Color_HSV = [[20,20,120,30,255,255]]
Color_BGR = [[0,215,255]]

point_list = []


def findPoints(img,Color_HSV, Color_BGR):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints= []
    for color in Color_HSV:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),15,Color_BGR[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            x, y, w, h = cv2.boundingRect(cnt)
    return (x+w//2), y

def paint(point_list,Color_BGR):
    for point in point_list:
        cv2.circle(imgResult, (point[0], point[1]), 10, Color_BGR[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = np.copy(img)
    newPoints = findPoints(img,Color_HSV,Color_BGR)
    if len(newPoints)!=0:
        for newP in newPoints:
            point_list.append(newP)
    if len(point_list)!=0:
        paint(point_list,Color_BGR)

    r = cv2.flip(imgResult, 1)
    cv2.imshow("Result", r)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        point_list = []

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()