# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:36:16 2019

@author: ASUS FX504G
"""

import numpy as np
import cv2

def blueprint(matrix=None):
    
    try: 
        matrix.size
        bg = matrix.copy()
    except:
        bg = np.zeros([600,900,3],np.dtype("uint8"))
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    

    cv2.putText(bg,'Area0',(375,100), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area1',(185,510), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area2',(65,300), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area3',(215,300), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area4',(365,300), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area5',(515,300), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area6',(585,510), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area7',(665,300), font, 0.8,(255,255,255),2)
    cv2.putText(bg,'Area8',(815,520), font, 0.8,(255,255,255),2)

    # s0
    bg[0:50,0:900,0] = 0
    bg[0:50,0:900,1] = 255 
    bg[0:50,0:900,2] = 0
    cv2.rectangle(bg,(0,0),(900,50),(255,255,255),3)
    cv2.putText(bg,'Shelf',(400,35), font, 1,(255,255,255),2)
    
    # s1
    bg[50:450,0:50,0] = 0
    bg[50:450,0:50,1] = 255 
    bg[50:450,0:50,2] = 0
    cv2.rectangle(bg,(0,50),(50,450),(255,255,255),3)
    #    cv2.putText(bg,'S1',(7,400), font, 1,(255,255,255),2)
    cv2.putText(bg,'S',(13,210), font, 1,(255,255,255),2)
    cv2.putText(bg,'h',(13,240), font, 1,(255,255,255),2)
    cv2.putText(bg,'e',(13,270), font, 1,(255,255,255),2)
    cv2.putText(bg,'l',(16,300), font, 1,(255,255,255),2)
    cv2.putText(bg,'f',(16,330), font, 1,(255,255,255),2)
    
    # s2
    bg[150:450,150:200,0] = 0
    bg[150:450,150:200,1] = 255 
    bg[150:450,150:200,2] = 0
    cv2.rectangle(bg,(150,150),(200,450),(255,255,255),3)
#    cv2.putText(bg,'S2',(156,300), font, 1,(255,255,255),2)
    cv2.putText(bg,'S',(163,250), font, 1,(255,255,255),2)
    cv2.putText(bg,'h',(163,280), font, 1,(255,255,255),2)
    cv2.putText(bg,'e',(163,310), font, 1,(255,255,255),2)
    cv2.putText(bg,'l',(167,340), font, 1,(255,255,255),2)
    cv2.putText(bg,'f',(167,370), font, 1,(255,255,255),2)
    
    # s3
    bg[150:450,300:350,0] = 0
    bg[150:450,300:350,1] = 255 
    bg[150:450,300:350,2] = 0
    cv2.rectangle(bg,(300,150),(350,450),(255,255,255),3)
#    cv2.putText(bg,'S3',(306,300), font, 1,(255,255,255),2)
    cv2.putText(bg,'S',(313,250), font, 1,(255,255,255),2)
    cv2.putText(bg,'h',(313,280), font, 1,(255,255,255),2)
    cv2.putText(bg,'e',(313,310), font, 1,(255,255,255),2)
    cv2.putText(bg,'l',(317,340), font, 1,(255,255,255),2)
    cv2.putText(bg,'f',(317,370), font, 1,(255,255,255),2)
    
    
    # s4
    bg[150:450,450:500,0] = 0
    bg[150:450,450:500,1] = 255 
    bg[150:450,450:500,2] = 0 
    cv2.rectangle(bg,(450,150),(500,450),(255,255,255),3)
#    cv2.putText(bg,'S4',(456,300), font, 1,(255,255,255),2)
    cv2.putText(bg,'S',(463,250), font, 1,(255,255,255),2)
    cv2.putText(bg,'h',(463,280), font, 1,(255,255,255),2)
    cv2.putText(bg,'e',(463,310), font, 1,(255,255,255),2)
    cv2.putText(bg,'l',(467,340), font, 1,(255,255,255),2)
    cv2.putText(bg,'f',(467,370), font, 1,(255,255,255),2)
    
    
    # s5
    bg[150:450,600:650,0] = 0
    bg[150:450,600:650,1] = 255 
    bg[150:450,600:650,2] = 0
    cv2.rectangle(bg,(600,150),(650,450),(255,255,255),3)
#    cv2.putText(bg,'S5',(606,300), font, 1,(255,255,255),2)
    cv2.putText(bg,'S',(613,250), font, 1,(255,255,255),2)
    cv2.putText(bg,'h',(613,280), font, 1,(255,255,255),2)
    cv2.putText(bg,'e',(613,310), font, 1,(255,255,255),2)
    cv2.putText(bg,'l',(617,340), font, 1,(255,255,255),2)
    cv2.putText(bg,'f',(617,370), font, 1,(255,255,255),2)
    
    # s6
    bg[50:450,750:800,0] = 0
    bg[50:450,750:800,1] = 255 
    bg[50:450,750:800,2] = 0
    cv2.rectangle(bg,(750,50),(800,450),(255,255,255),3)
#    cv2.putText(bg,'S6',(756,250), font, 1,(255,255,255),2)
    cv2.putText(bg,'S',(763,210), font, 1,(255,255,255),2)
    cv2.putText(bg,'h',(763,240), font, 1,(255,255,255),2)
    cv2.putText(bg,'e',(763,270), font, 1,(255,255,255),2)
    cv2.putText(bg,'l',(767,300), font, 1,(255,255,255),2)
    cv2.putText(bg,'f',(767,330), font, 1,(255,255,255),2)
    
    # counter / s7
    bg[550:600,0:800,0] = 0
    bg[550:600,0:800,1] = 255 
    bg[550:600,0:800,2] = 0
    
    bg[550:600,445:450,0] = 255
    bg[550:600,445:450,1] = 255 
    bg[550:600,445:450,2] = 255
    cv2.rectangle(bg,(0,550),(800,600),(255,255,255),3)
    cv2.putText(bg,'Checkout counter',(85,585), font, 1,(255,255,255),2)
    cv2.putText(bg,'Shelf',(585,585), font, 1,(255,255,255),2)
    
    # door staff
    bg[453:547,795:800,0] = 0
    bg[453:547,795:800,1] = 0 
    bg[453:547,795:800,2] = 255
    
    return bg

    
if  __name__ =="__main__":
    show = blueprint()
    cv2.imshow("Store Layout",show)
    cv2.waitKey(0)
    cv2.destroyAllWindows()