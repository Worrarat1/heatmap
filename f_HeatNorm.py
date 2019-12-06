# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:36:53 2019

@author: ASUS FX504G
"""

import numpy as np
import os
import cv2

def HeatThreshVal(objpath,layPath,selectPath,heatInt,type="max"):
    # Obj found
    pathObj = os.path.abspath(objpath)
    listRoi = [pathObj + "/" + i for i in os.listdir(pathObj) if i.endswith(".npy")]
    
    path = os.path.abspath(selectPath)
    selRoi = [path + "/" + i for i in os.listdir(path) if i.endswith(".npy")]
    
    path = os.path.abspath(layPath)
    getLayout = [path + "/" + i for i in os.listdir(path) if i.endswith(".jpg")]
    
    
    for i in range(0,len(listRoi)):
    #for i in range(1,2):
        
        # get roi of objs
        objectRoi = np.load(listRoi[i])
        
        # get roi to create heatmap
        selectRoi = np.load(selRoi[i])
        selectRoi = selectRoi[np.argsort(selectRoi[:,3])]
        
        layout = cv2.imread(getLayout[i])
        imSize = layout.shape[:2]
        
        for r in range(0,len(selectRoi)):
            
            # create mask
            mask = np.zeros([imSize[0],imSize[1]],np.dtype("int32"))
    
            # column represent ymin,ymax,xmin,xmax
            filter_ROI = objectRoi.copy()
            filter_ROI = filter_ROI[filter_ROI[:,0]>selectRoi[r][0]]
            filter_ROI = filter_ROI[filter_ROI[:,1]<selectRoi[r][1]]
            filter_ROI = filter_ROI[filter_ROI[:,2]>selectRoi[r][2]]
            filter_ROI = filter_ROI[filter_ROI[:,3]<selectRoi[r][3]]
            
    
            for f in filter_ROI:
                mask[f[0]:f[1],f[2]:f[3]] += 1
                
            #before normalize
            mask_int = mask[f[0]:f[1],f[2]:f[3]]
            np.save("{}/HeatData{}_{}".format(heatInt,i+1,r),mask_int)
            
            hPath = os.path.abspath(heatInt)
            hData = [hPath + "/" + i for i in os.listdir(hPath) if i.endswith(".npy")]
            
            #A0
            area0 = np.load(hData[5])
            area1 = np.load(hData[0])
            area2 = np.load(hData[1])
            area3 = np.load(hData[2])
            area4 = np.load(hData[6])
            area5 = np.load(hData[7])
            area6 = np.load(hData[3])
            area7 = np.load(hData[4])
            area8 = np.load(hData[8])
            
            if type == "max":
                threshVal = np.max([np.max(area0),np.max(area1),np.max(area2),np.max(area3),
                        np.max(area4),np.max(area5),np.max(area6),np.max(area7),np.max(area8)])
            else:
                threshVal = np.mean([np.max(area0),np.max(area1),np.max(area2),np.max(area3),
                np.max(area4),np.max(area5),np.max(area6),np.max(area7),np.max(area8)])
                
                
            return threshVal
