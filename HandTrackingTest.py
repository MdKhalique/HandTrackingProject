# Serves as testing the module in other files
# Simply use the code of the main function and import the same imports as well as the module file to access the class

import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


# main code

pTime = 0
cTime = 0
cam = cv2.VideoCapture(1)
detector = htm.handDetector()
while True:
    success, img = cam.read()
    detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])  # prints desired node/landmark (lm)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)