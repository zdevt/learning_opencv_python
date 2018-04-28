
import numpy as np
import cv2
import imutils

#cap = cv2.VideoCapture("http://192.168.0.117:8080/?action=stream?dummy=param.mjpg")
#cap = cv2.VideoCapture('rtsp://admin:XGRTZW@192.168.0.104:554/h264/ch1/main/av_stream')
#cap = cv2.VideoCapture('rtsp://admin:admin@192.168.0.109:554/cam/realmonitor?channel=1&subtype=0')
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("rtsp://admin:XGRTZW@192.168.0.188:554")

#cap.set(CV_CAP_PROP_FRAME_WIDTH,1280)

print(cap.isOpened())

while cap.isOpened():
    _, frame = cap.read()
    frame = imutils.resize(frame, width=800)
    '''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    '''
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) & 0xff == ord('d'):
        break

cap.release()
#cv2.destroyWindow()


