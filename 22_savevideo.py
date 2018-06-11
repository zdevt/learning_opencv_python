#!/usr/bin/env python  
#-*- coding:utf-8 -*-  

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#fourcc = cv2.cv.FOURCC(*'XVID')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('a.avi',fourcc,20,(640,480))

while ( cap.isOpened()):
    _,frame = cap.read()
    #frame = cv2.flip(frame, 0)
    out.write( frame )
    cv2.imshow('frame', frame )
    if cv2.waitKey(1) & 0xff == ord('q'):
        break;

cap.release();
out.release()

cv2.destroyAllWindows()

