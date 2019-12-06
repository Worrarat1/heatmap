# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:57:53 2019

@author: ASUS FX504G
"""

import cv2
import os
import numpy as np


def draw(event, x, y, flags, param):
    global ix,iy,crop

    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy = x,y
        
    if event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        h1 = min(iy,y)
        h2 = max(iy,y)
        w1 = min(ix,x)
        w2 = max(ix,x)
        crop = np.vstack([crop,[h1,h2,w1,w2]])
        
def nothing(x):
    pass


path = os.path.abspath("layout")
crop = np.empty([0,4],np.dtype(int))
listlay = [path + "\\" + i for i in os.listdir(path) if i.endswith(".jpg")]
out = False

if out == False:
    for i in range(0,len(listlay)):
    #for i in range(0,1):
        img = cv2.imread(listlay[i])
        img_orig = img.copy()
        winName = 'select ROI'
        cv2.namedWindow(winName)
        cv2.setMouseCallback(winName,draw)
        while(True) :
            cv2.imshow(winName, img)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break
            if cv2.waitKey(1) == ord("s"):
                if crop.size == 0 :
                    print("no")
                    continue
                cv2.imwrite("layout_select/{}.jpg".format(i+1),img)
                np.save("layout_select/{}.npy".format(i+1),crop)
                crop = np.empty([0,4],np.dtype(int))
                break
            if cv2.waitKey(1) == ord('r'):
                crop = np.empty([0,4],np.dtype(int)) 
                img = img_orig.copy()
                continue
            if cv2.waitKey(1) == 27:
                out = True
                break