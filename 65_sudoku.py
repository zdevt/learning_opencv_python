#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
############################################################################### 
#       File Name: 65_sudoku.py
#          Author:
#            Mail: 
#    Created Time: 2017-08-23 16:03:17
############################################################################### 
import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread('/Users/devz/data/sudoku.png',0)

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

'''
cv2.imshow('src',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
'''

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')

plt.show()

cv2.waitKey(0)


