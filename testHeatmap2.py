import numpy as np
import cv2

                     
inname= 'Choice-VDO/1.avi'
    
cap = cv2.VideoCapture(inname)

ret,orig_image = cap.read()
width = np.size(orig_image, 1)
height = np.size(orig_image, 0)
frame_size=(height, width)           

accumulator =  np.zeros((height, width), np.float32) 


cap = cv2.VideoCapture(inname)

fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=80,detectShadows=False)

while(1):
    ret, frame = cap.read()
    
    if not ret:
        cap = cv2.VideoCapture(inname)
        continue;
    
    fgmask = fgbg.apply(frame)
    
    accumulator=accumulator+fgmask
    
    ab=cv2.convertScaleAbs(255-np.array(accumulator,'uint8'))  
    
    ret,acc_thresh=cv2.threshold(ab,ab.mean(),255,cv2.THRESH_TOZERO)
       
    acc_col = cv2.applyColorMap(acc_thresh,cv2.COLORMAP_JET)
         
    real = cv2.addWeighted(np.array(acc_col,"uint8"),0.02,frame,0.55,0)
    
    
    cv2.imshow('fgmask',fgmask)
    cv2.imshow('accumulator',accumulator)
    cv2.imshow('ab',ab)
    cv2.imshow('acc_thresh',acc_thresh)
    cv2.imshow('acc_col',acc_col)
    cv2.imshow('heat',real)
    
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
        

#cv2.imshow('heat',acc_thresh)
#cv2.waitKey(0)
#cv2.destroyAllWindows()