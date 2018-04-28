#!/usr/bin/python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: 67_subplot.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-24 08:33:37
############################################################################### 

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('/Users/devz/data/apple.jpg')

_,t1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,t2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,t3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,t4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,t5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['ori','bin','bin_inv','trunc','tozero','tozero_inv']
imgs = [ img,t1,t2,t3,t4,t5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
