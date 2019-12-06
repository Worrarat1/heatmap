# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:27:33 2019

@author: ASUS FX504G
"""
import os
import cv2
import numpy as np

path = os.path.abspath("output")
listVid = [path + "\\" + i for i in os.listdir(path)]

pathLay = os.path.abspath("layout_select")
selRoi = [pathLay + "/" + i for i in os.listdir(pathLay) if i.endswith(".npy")]


#output = "output_text"
output = None
cont = True

area = [["Area 1"],["Area 2","Area 3"],["Area 6"],["Area 7"],["Area 0"],["Area 4","Area 5"],["Area 8"]]

for i in range(0,len(listVid)):
    writer = None
    
    if cont == False:
        break
    
    video = cv2.VideoCapture(listVid[i])
    
    # get roi to draw on frame
    selectRoi = np.load(selRoi[i])
    selectRoi = selectRoi[np.argsort(selectRoi[:,3])]
    
    while(video.isOpened()):
        ret, frame = video.read()
        
        if ret is False:
            print('end VDO')
            break
        
#        frame = cv2.resize(frame,(800,600))
        
        for r in range(0,len(selectRoi)):
            cv2.rectangle(frame,(selectRoi[r][2],selectRoi[r][0]),(selectRoi[r][3],selectRoi[r][1]),(255,0,0),3)   
            left = int(selectRoi[r][2]+(selectRoi[r][3]-selectRoi[r][2])/2)-40
            bot = int((selectRoi[r][1]-selectRoi[r][0])/2)
            cv2.putText(frame, "{}".format(area[i][r]), (left,bot), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3);
            
        cv2.imshow('Object detector', frame)
    
        key = cv2.waitKey(1) & 0xFF
        
        if writer is None and output is not None:
#            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            fourcc = cv2.VideoWriter_fourcc(*"MP4V")
            writer = cv2.VideoWriter("{}/{}.mp4".format(output,i+1), fourcc, 24,
                                     (frame.shape[1], frame.shape[0]), True)
        
        if writer is not None:
            writer.write(frame)
        
        if key == 27:
            cont = False
            break
        
        if key == ord("q"):
            break
    
    if writer is not None:
        writer.release()

video.release()
cv2.destroyAllWindows()