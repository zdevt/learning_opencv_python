#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: 99_convex.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-24 16:51:08
############################################################################### 

import cv2
import numpy as np


img = cv2.imread('/Users/devz/data/shape_sample/20.png',0)

ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

_,contours,hierarchy = cv2.findContours(thresh,2,1)

cnt = contours[0]

hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range( defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyWindow()

