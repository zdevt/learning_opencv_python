#!/usr/bin/env python  
#-*- coding:utf-8 -*-  

import cv2
import numpy as np


img1 = cv2.imread('/Users/devz/data/lena.jpg')


e1 = cv2.getTickCount()

for i in range(5,26,2):
    img1 = cv2.medianBlur(img1,i)

e2 = cv2.getTickCount()

t = (e2-e1)/cv2.getTickFrequency()

print (t)

cv2.imshow('img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

