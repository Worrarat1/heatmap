# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:11:28 2018

@author: ASUS FX504G
"""
import cv2
import os
import time
path = os.path.abspath("Choice-VDO")
listVid = [path + "\\" + i for i in os.listdir(path)]

for i in range(0,len(listVid)):
    cap = cv2.VideoCapture(listVid[i])
    start = time.time()
    while True:
        success,frame = cap.read()
        frame = cv2.resize(frame,(800,600))
        fpsCur = cap.get(cv2.CAP_PROP_POS_FRAMES)
        second  = time.time() - start
        fps = int(fpsCur/second)
        cv2.putText(frame, "FPS : " + str(fps), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2);
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        elif key == ord("s"):
            cv2.imwrite("{}.jpg".format(i+1),frame)
            break
    cv2.destroyAllWindows()
    cap.release()