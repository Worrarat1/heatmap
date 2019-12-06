# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:11:28 2018

@author: ASUS FX504G
"""
import cv2
import os
path = os.path.abspath("Videos")
listVid = [path + "\\" + i for i in os.listdir(path)]

for i in range(0, len(listVid)):
    cap = cv2.VideoCapture(listVid[i])
    cnt = 0
    while True:
        success,frame = cap.read()
        if success == False:
            break
        fpsCur = cap.get(cv2.CAP_PROP_POS_FRAMES)
#        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        cap.set(1,fpsCur+90)
        if cnt % 2 == 0:
            cv2.imwrite("labelimg/image/test/{}_{}.jpg".format(i,cnt),frame)
        else:
            cv2.imwrite("labelimg/image/train/{}_{}.jpg".format(i,cnt),frame)
        cnt += 1
        print("save pics:", cnt)
    cv2.destroyAllWindows()
    cap.release()