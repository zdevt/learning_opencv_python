#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: 102_drawcontours.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-24 10:09:46
############################################################################### 


import imutils
import numpy as np
import cv2

im = cv2.imread('/Users/devz/data/templ.png')
#im = imutils.resize(im, width=400)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY)

_,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)

print( contours)

cv2.drawContours(im,contours,1,(0,255,0),3)

cv2.imshow('tet', im)

cv2.waitKey(0)
cv2.destroyWindow()

