#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: 69_threshold.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-24 08:40:06
############################################################################### 

import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('./img_0090.jpg',0)
img = cv2.imread('../../../../data/board.jpg',0)

img = cv2.medianBlur(img, 7)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,13,4)

_,contours,hierarchy = cv2.findContours(th3.copy(), cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(th3,contours,-1,(0,255,0),3)

img = cv2.medianBlur(img, 7)
th3 = cv2.adaptiveThreshold(th3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,13,4)

_,contours,hierarchy = cv2.findContours(th3.copy(), cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(th3,contours,-1,(0,255,0),3)

cv2.imwrite('./a.jpg',th3,)

