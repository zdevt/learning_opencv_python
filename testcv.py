#!/usr/bin/env python
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: testcv.py
#          Author:
#            Mail: 
#    Created Time: 2017-10-21 14:25:51
############################################################################### 

import cv2

img = cv2.imread("/Users/devz/data/apple.jpg")

cv2.namedWindow("img")
cv2.imshow("img",img)
cv2.waitKey(0)

cv2.destroyAllWindows()

