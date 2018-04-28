#-*- coding: utf-8 -*-

import cv2
import sys

cascPath = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt2.xml"

from PIL import Image

def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    cap = cv2.VideoCapture(camera_idx)

    #����OpenCVʹ������ʶ�������
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

                #����ǰ֡����ΪͼƬ
                img_name = '%s/%d.jpg'%(path_name, num)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image)

                num += 1
                if num > (catch_pic_num):
                    break

                #�������ο�
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

