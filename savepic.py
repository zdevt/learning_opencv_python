#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: savepic.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-22 08:51:32
############################################################################### 


import cv2

cap = cv2.VideoCapture(0)

size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

print( cap.isOpened())

print (size)
