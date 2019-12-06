######## Video Object Detection Using Tensorflow-trained Classifier #########
#
# Author: Evan Juras
# Date: 1/16/18
# Description: 
# This program uses a TensorFlow-trained classifier to perform object detection.
# It loads the classifier uses it to perform object detection on a video.
# It draws boxes and scores around the objects of interest in each frame
# of the video.

## Some of the code is copied from Google's example at
## https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

## and some is copied from Dat Tran's example at
## https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py

## but I changed it to make it more understandable to me.

# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
from imutils.video import FPS
import time
import sys

# us CPU/GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

if tf.test.gpu_device_name():
    print('GPU Used')
else:
    print("No GPU Used")
    
sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
path = os.path.abspath("Choice-VDO")
listVid = [path + "\\" + i for i in os.listdir(path)]

MODEL_PATH = 'person_store'

# Grab path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_PATH,'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,MODEL_PATH,'labelmap.pbtxt')

# Path to video
for i in range(0,len(listVid)):
    
    chooseVdo = i
    PATH_TO_VIDEO = listVid[chooseVdo]
    NUM_CLASSES = 1
    skip = 20
    fcnt = 0
    writer = None
#    output = None
    minCount = 5
#    start = time.perf_counter()
    output = "output/{}".format(os.listdir(path)[chooseVdo])
    
    # Load the label map.
    # Label maps map indices to category names, so that when our convolution
    # network predicts `5`, we know that this corresponds to `king`.
    # Here we use internal utility functions, but anything that returns a
    # dictionary mapping integers to appropriate string labels would be fine
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    
    # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')
    
        sess = tf.Session(graph=detection_graph)
    
    # Define input and output tensors (i.e. data) for the object detection classifier
    
    # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    
    # Output tensors are the detection boxes, scores, and classes
    # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    
    # Each score represents level of confidence for each of the objects.
    # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    
    # Number of objects detected
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')
    
    # Open video file
    video = cv2.VideoCapture(PATH_TO_VIDEO)
    
    roi = np.empty([0,4],np.dtype(int))
    while(video.isOpened()):
#        now  = time.perf_counter()
#        if (now - start)/60 > minCount:
#            print("Met set time limit")
#            break
#        
        ret, frame = video.read()
        
        if ret is False:
            print('end VDO')
            break
        
        fcnt += 1
        if fcnt % skip == 0:
            # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
            # i.e. a single-column array, where each item in the column has the pixel RGB value
            frame = cv2.resize(frame,(800,600))
            show = frame.copy()
            fps = FPS().start()
            fpsCur = video.get(cv2.CAP_PROP_POS_FRAMES)
            frame_expanded = np.expand_dims(frame, axis=0)
        
            # Perform the actual detection by running the model with the image as input
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})
        
            # Draw the results of the detection (aka 'visulaize the results')
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.50)
            
            
            person_found_idx = np.argwhere(scores[0]>0.5).astype(int)
            h,w = frame.shape[0:2]
            
            for j in person_found_idx:
                ymin = int(boxes[0][j[0]][0]*h)
                xmin = int(boxes[0][j[0]][1]*w)
                ymax = int(boxes[0][j[0]][2]*h)
                xmax = int(boxes[0][j[0]][3]*w)
                roi = np.vstack([roi,[ymin,ymax,xmin,xmax]])
                cv2.rectangle(show,(xmin,ymin),(xmax,ymax),(255,255,0))
            
            fps.update()
            fps.stop()
            cv2.putText(frame, "Using GPU, FPS : " + "{0:.2f}".format(fps.fps()), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3);
#            cv2.imshow('Object detector', show)
            cv2.imshow('Object detector TF', frame)
            key = cv2.waitKey(1) & 0xFF
            # Press 'q' to quit, 'n' to skip
            # the output video to disk initialize the writer
            if writer is None and output is not None:
                fourcc = cv2.VideoWriter_fourcc(*"MJPG")
#                fourcc = cv2.VideoWriter_fourcc(*"MP4V")
                writer = cv2.VideoWriter(output, fourcc, 24,
                                         (frame.shape[1], frame.shape[0]), True)
            
            # if the writer is not None, write the frame with people to disk
            if writer is not None:
                writer.write(frame)
                
            if key == ord('q'):
                break
            elif  key == ord('n'):
                video.set(1,fpsCur+3000)
    
    # Clean up
    video.release()
    cv2.destroyAllWindows()
    
    if writer is not None:
    	writer.release()
       
    np.save("{}.npy".format(i+1),roi)
