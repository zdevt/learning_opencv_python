#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  face_eye_detect.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-11 13:26:21
#  Last Modified:  2018-06-11 13:58:28
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


def face_eye():
    import numpy as np
    import cv2
    import cv2.data

    face_cascade = cv2.CascadeClassifier(
        '/Users/devz/PycharmProjects/py2_venv/venv/lib/python2.7/site-packages/cv2/data/haarcascade_frontalface_default.xml'
    )
    eye_cascade = cv2.CascadeClassifier(
        '/Users/devz/PycharmProjects/py2_venv/venv/lib/python2.7/site-packages/cv2/data/haarcascade_eye.xml'
    )

    # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while (True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh),
                              (0, 255, 0), 2)

        cv2.imshow('img', img)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


face_eye()
