#!/usr/bin/env python
#-*- coding:utf-8 -*-  

import argparse
import datetime
import imutils
import time
import cv2

camera = cv2.VideoCapture(0)
#src = "http://192.168.0.117:8080/?action=stream?dummy=param.mjpg"
#camera = cv2.VideoCapture(src)

firstFrame = None

while True:
    camera = cv2.VideoCapture(0)

    (ret, frame) = camera.read()

    if not ret:
        break;

    #frame = imutils.resize(frame, width=240)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    frame = cv2.bilateralFilter(frame,9,75,75)
    frameDelta = cv2.absdiff(firstFrame, gray)

    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_OTSU)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    thresh = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))

    (b,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours( thresh.copy(),cnts,-1,(0,255,0),3)

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if ( w >30 and h > 40):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("video", frame)
    key = cv2.waitKey(200) & 0xFF

    if key == ord("q"):
        break

    camera.release()

cv2.destroyAllWindows()



import cv2
import sys

cascPath = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt2.xml"

from PIL import Image

def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    cap = cv2.VideoCapture(camera_idx)

    #告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier(cascPath)

    num = 0
    while cap.isOpened():
        ok, frame = cap.read()

        if not ok:
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faceRects = classfier.detectMultiScale(grey,
                scaleFactor = 1.2,
                minNeighbors = 3,
                minSize = (32, 32))

        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect

                #将当前帧保存为图片
                img_name = '%s/%d.jpg'%(path_name, num)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image)

                num += 1
                if num > (catch_pic_num):
                    break

                #画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10),
                        (0,255,0), 2)

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'num:%d' % (num),(x + 30, y + 30), font, 1,
                        (255,0,255),4)
        if num > (catch_pic_num):
            break

        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

CatchPICFromVideo("savepic", int(0),int(1000),'./')

