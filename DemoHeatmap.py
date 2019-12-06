# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:27:33 2019

@author: ASUS FX504G
"""
import os
import cv2

path = os.path.abspath("output_text")
listVid = [path + "\\" + i for i in os.listdir(path)]

# vdo 1-7
video1 = cv2.VideoCapture(listVid[0])   
video2 = cv2.VideoCapture(listVid[1])  
video3 = cv2.VideoCapture(listVid[2])  
video4 = cv2.VideoCapture(listVid[3])  
video5 = cv2.VideoCapture(listVid[4])  
video6 = cv2.VideoCapture(listVid[5])  
video7 = cv2.VideoCapture(listVid[6])  

while(True):
    
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    ret3, frame3 = video3.read()
    ret4, frame4 = video4.read()
    ret5, frame5 = video5.read()
    ret6, frame6 = video6.read()
    ret7, frame7 = video7.read()
    
#    if ret is False:
#        print('end VDO')
#        break
#    
    w = 515
    h = 250
    
    try:
    
        if ret1 is True:
            cv2.namedWindow("Area0",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Area0",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow("Area0", 0,0)
            cv2.resizeWindow('Area0', w,h)
            cv2.imshow('Area0',frame5)
        
        if ret2 is True:
            cv2.namedWindow("Area1",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Area1",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow("Area1", w,0)
            cv2.resizeWindow('Area1', w,h)
            cv2.imshow('Area1',frame1)
        
        if ret3 is True:
            cv2.namedWindow("Area2-Area3",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Area2-Area3",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow("Area2-Area3", w*2,0)
            cv2.resizeWindow('Area2-Area3', w,h)
            cv2.imshow('Area2-Area3',frame2)
        
        if ret4 is True:
            cv2.namedWindow("Area4-Area5",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Area4-Area5",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow("Area4-Area5", 0,h)
            cv2.resizeWindow('Area4-Area5', w,h)
            cv2.imshow('Area4-Area5',frame6)
        
        if ret5 is True:
            cv2.namedWindow("Area6",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Area6",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow("Area6", w,h)
            cv2.resizeWindow('Area6', w,h)
            cv2.imshow('Area6',frame3)
        
        if ret6 is True:
            cv2.namedWindow("Area7",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Area7",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow("Area7", w*2,h)
            cv2.resizeWindow('Area7', w,h)
            cv2.imshow('Area7',frame4)
        
        if ret7 is True:
            cv2.namedWindow("Area8",cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Area8",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.moveWindow("Area8", 0,h*2)
            cv2.resizeWindow('Area8', w,h)
            cv2.imshow('Area8',frame7)
    except:
        break

    key = cv2.waitKey(10) & 0xFF
    
    if key == 27:
        break
    
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
    
    
import os
import numpy as np
import cv2
from f_storeLayout import blueprint

hPath = os.path.abspath("heat_data")
hData = [hPath + "/" + i for i in os.listdir(hPath) if i.endswith(".npy")]

#A0
area0 = np.load(hData[5])
area0 = cv2.resize(area0,(650,100))
#A1
area1 = np.load(hData[0])
area1 = cv2.resize(area1,(450,100))
#A2
area2 = np.load(hData[1])
area2 = cv2.resize(area2,(100,300))
#A3
area3 = np.load(hData[2])
area3 = cv2.resize(area3,(100,300))
#A4
area4 = np.load(hData[6])
area4 = cv2.resize(area4,(100,300))
#A5
area5 = np.load(hData[7])
area5 = cv2.resize(area5,(100,300))
#A6
area6 = np.load(hData[3])
area6 = cv2.resize(area6,(350,100))
#A7
area7 = np.load(hData[4])
area7 = cv2.resize(area7,(100,300))
#A8
area8 = np.load(hData[8])
area8 = cv2.resize(area8,(100,150))


store = np.zeros([600,900],np.dtype("uint8"))

store[50:150,50:700] = area0
store[450:550,0:450] = area1
store[150:450,50:150] = area2
store[150:450,200:300] = area3
store[150:450,350:450] = area4
store[150:450,500:600] = area5
store[450:550,450:800] = area6
store[150:450,650:750] = area7
store[400:550,800:900] = area8


kernel = np.ones((5,5),np.uint8)
store = cv2.dilate(store,kernel,iterations = 1)

#heatmap
heatmap = cv2.applyColorMap(store, cv2.COLORMAP_JET)

#applay heat to store
applyHeat = blueprint(heatmap)
cv2.moveWindow("Heatmap", 500,500)
cv2.imshow("Heatmap",applyHeat)
cv2.waitKey(0)
cv2.destroyAllWindows()