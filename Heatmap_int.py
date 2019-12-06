# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 01:29:42 2019

@author: ASUS FX504G
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:22:28 2019

@author: ASUS FX504G
"""
import os
import numpy as np
import cv2
from storeLayout import blueprint

hPath = os.path.abspath("heat_data_int")
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

maxVal = np.mean([np.max(area0),np.max(area1),np.max(area2),np.max(area3),
        np.max(area4),np.max(area5),np.max(area6),np.max(area7),np.max(area8)])

# normalize
area0 = ((area0/maxVal)*255).astype("uint8")
area1 = ((area1/maxVal)*255).astype("uint8")
area2 = ((area2/maxVal)*255).astype("uint8")
area3 = ((area3/maxVal)*255).astype("uint8")
area4 = ((area4/maxVal)*255).astype("uint8")
area5 = ((area5/maxVal)*255).astype("uint8")
area6 = ((area6/maxVal)*255).astype("uint8")
area7 = ((area7/maxVal)*255).astype("uint8")
area8 = ((area8/maxVal)*255).astype("uint8")


area0 = cv2.resize(area0,(650,100))
area1 = cv2.resize(area1,(450,100))
area2 = cv2.resize(area2,(100,300))
area3 = cv2.resize(area3,(100,300))
area4 = cv2.resize(area4,(100,300))
area5 = cv2.resize(area5,(100,300))
area6 = cv2.resize(area6,(400,100))
area7 = cv2.resize(area7,(100,300))
area8 = cv2.resize(area8,(100,150))


store = np.zeros([600,900],np.dtype("uint8"))

store[50:150,50:700] = area0
store[450:550,0:450] = area1
store[150:450,50:150] = area2
store[150:450,200:300] = area3
store[150:450,350:450] = area4
store[150:450,500:600] = area5
store[450:550,400:800] = area6
store[150:450,650:750] = area7
store[400:550,800:900] = area8

#heatmap
heatmap = cv2.applyColorMap(store, cv2.COLORMAP_JET)

#applay heat to store
applyHeat = blueprint(heatmap)

cv2.imshow("store",store)
cv2.imshow("heatmap",heatmap)
cv2.imshow("Store + heatmap",applyHeat)
cv2.waitKey(0)
cv2.destroyAllWindows()

