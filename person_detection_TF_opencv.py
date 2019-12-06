import cv2 as cv
import os

MODEL_PATH = 'person_store'
CWD_PATH = os.getcwd()
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_PATH,'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_PATH,'labelmap.pbtxt')
cvNet = cv.dnn.readNetFromTensorflow(PATH_TO_CKPT, PATH_TO_LABELS)

path = os.path.abspath("Choice-VDO")
listVid = [path + "\\" + i for i in os.listdir(path)]

cap = cv.VideoCapture(listVid[0])
while True:
    success,frame = cap.read()
    fpsCur = cap.get(cv.CAP_PROP_POS_FRAMES)
    
    img = frame.copy()
    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    cvOut = cvNet.forward()
    
    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        if score > 0.5:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)
    
    cv.imshow("Frame", cv.resize(img, (800,600)))
    key = cv.waitKey(1) & 0xFF
    
    if key == 27:
        break
    if key == ord('n'):
        cap.set(1,fpsCur+500)
    

cv.destroyAllWindows()
cap.release()