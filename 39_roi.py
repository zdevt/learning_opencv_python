#!/usr/bin/env python  
#-*- coding:utf-8 -*-  

import cv2
import numpy as np

image=cv2.imread('~/data/messi5.jpg')
ball=image[287:338,330:393]
image[287:338,130:193]=ball

cv2.namedWindow('img')
cv2.imshow('img',image)

cv2.waitKey(0)

