
import argparse
import datetime
import imutils
import time
import cv2

camera = cv2.VideoCapture(0)
#camera = cv2.VideoCapture('../../../test/vtest.avi')
#camera = cv2.VideoCapture("http://192.168.0.117:8080/?action=stream?dummy=param.mjpg")
#camera = cv2.VideoCapture('~/data/vtest.avi')
#camera = cv2.VideoCapture("rtsp://admin:XGRTZW@192.168.0.114:554")

firstFrame = None
i = 1

while True:
    (ret, frame) = camera.read()

    i = i + 1
    if (i % 0x4) == 0:
        print(i)
        #frame = imutils.resize(frame, width=800)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if firstFrame is None:
            firstFrame = gray
            continue

        frame = cv2.bilateralFilter(frame,9,75,75)
        frameDelta = cv2.absdiff(firstFrame, gray)

        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        #thresh = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))
        (b,cnts, h) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours( thresh.copy(),cnts,-1,(0,255,0),3)

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            if ( w >30 and h > 40):
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("video", frame)
        cv2.moveWindow('video',10,10)

        key = cv2.waitKey(30) & 0xFF

        if key == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()


