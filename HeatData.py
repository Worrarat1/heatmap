# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:55:23 2019

@author: ASUS FX504G
"""

import numpy as np
import os
import cv2
from f_HeatNorm import HeatThreshVal

# Obj found
pathObj = os.path.abspath("")
listRoi = [pathObj + "/" + i for i in os.listdir(pathObj) if i.endswith(".npy")]

# selected roi
path = os.path.abspath("layout_select")
selRoi = [path + "/" + i for i in os.listdir(path) if i.endswith(".npy")]
showSelRoi = [path + "/" + i for i in os.listdir(path) if i.endswith(".jpg")]

path = os.path.abspath("layout")
getLayout = [path + "/" + i for i in os.listdir(path) if i.endswith(".jpg")]


# get max heat value
valThresh = 5
scaleThresh = 3
normType = "max"
threshVal = HeatThreshVal("","layout","layout_select","heat_data_int",normType)

for i in range(0,len(listRoi)):
#for i in range(0,1):
    
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
        
        
        # normalize and set cap value
        mask_select = (mask/threshVal)*255
        valSel = np.argwhere(mask_select>255)
        for vs in valSel:
            mask_select[vs[0],vs[1]] = 255
        mask_select = mask_select.astype("uint8")
        
        # set normalize
        if normType == "max":
            getVal = np.argwhere(mask_select>valThresh)
            for v in getVal:
                newVal = int(mask_select[v[0],v[1]]*scaleThresh)
                if newVal > 255:
                    newVal = 255
                mask_select[v[0],v[1]] = newVal
                
        # contour
        mask_con, cnts, hierarchy = cv2.findContours(mask_select.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(mask_con, cnts, -1, (255,255,255), 3)
        
        # select largest contour if found more than 1 in the area
        if len(cnts) > 1:
            cnts = [max(cnts,key=cv2.contourArea)]
            
        # find extreme points
        cnt_get = cnts[0][:,0]
        c_topleft = np.sum(cnt_get, axis = 1).argmin()
        c_topright = np.diff(cnt_get, axis = 1).argmin()
        c_bottomright = np.sum(cnt_get, axis = 1).argmax()
        c_bottomleft = np.diff(cnt_get, axis = 1).argmax()
        

        rect = np.zeros([4,2],np.dtype("float32"))
        rect[0] = tuple(cnts[0][c_topleft][0])
        rect[1] = tuple(cnts[0][c_topright][0])
        rect[2] = tuple(cnts[0][c_bottomright][0])
        rect[3] = tuple(cnts[0][c_bottomleft][0])

        (tl, tr, br, bl) = rect
        
        extreme = mask_select.copy()
        cv2.circle(extreme,tuple(tl), 20, (255,255,255), -1)
        cv2.circle(extreme,tuple(tr), 20, (255,255,255), -1)
        cv2.circle(extreme,tuple(bl), 20, (255,255,255), -1)
        cv2.circle(extreme,tuple(br), 20, (255,255,255), -1)
        
        # warp 
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
         
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
         
        maxWidth = max(int(widthA), int(widthB))
        maxHeight = max(int(heightA), int(heightB))
         
        dst = np.array([
        	[0, 0],
        	[maxWidth - 1, 0],
        	[maxWidth - 1, maxHeight - 1],
        	[0, maxHeight - 1]], dtype = "float32")
         
        M = cv2.getPerspectiveTransform(rect, dst)
        warp = cv2.warpPerspective(mask_select.copy(), M, (maxWidth, maxHeight))
        
        # save heat data
        np.save("heat_data/HeatData{}_{}".format(i+1,r),warp)
#        np.save("heat_data_int/HeatData{}_{}".format(i+1,r),mask_int)
        
        #heatmap
        applyHeat = cv2.applyColorMap(mask_select, cv2.COLORMAP_JET)
        warpHeat = cv2.applyColorMap(warp, cv2.COLORMAP_JET)
        cv2.imshow("heat orig",applyHeat)
        cv2.imshow("heat warp",warpHeat)
        
        
        cv2.imshow("selected ROI",cv2.imread(showSelRoi[i]))
        cv2.imshow("Mask",mask_select)
        cv2.imshow("Mask con",mask_con)
        cv2.imshow("Mask extreme",extreme)
        cv2.imshow("Mask Warp",warp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

os.system("python Heatmap.py")