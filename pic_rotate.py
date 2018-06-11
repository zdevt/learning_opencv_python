#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  cv2.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-06-11 11:01:45
#  Last Modified:  2018-06-11 11:21:47
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import cv2
from math import *
import numpy as np

img = cv2.imread('./sprite.png')
h, w = img.shape[:2]

d = 45

hn = int((w * fabs(sin(radians(d)))) + (h * fabs(cos(radians(d)))))
wn = int((h * fabs(sin(radians(d)))) + (w * fabs(cos(radians(d)))))

mr = cv2.getRotationMatrix2D((w / 2, h / 2), d, 1)
mr[0, 2] += (wn - w) / 2
mr[1, 2] += (hn - h) / 2

imgr = cv2.warpAffine(img, mr, (wn, hn), borderValue=(255, 255, 255))

cv2.imshow("img", img)
cv2.imshow("imgr", imgr)
cv2.waitKey(0)
