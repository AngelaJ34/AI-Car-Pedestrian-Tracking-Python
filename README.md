# Overview

 AI car &amp; pedestrian tracking in python utilizing computer vision. This program detects people and automotive vechicles using visual input based on the youtube videos to showc the programs ability to distinguish between the two. This process starts by first placing the image in a classifier file to identify said object whether it be a person or automotive vechile. This image will then be converted as a black and white photograph so that it is easier to train the program to identify which object it is.
 
 
 # 1. Instructions for installation
 
 Install the latest version of Python to your operating system of choice before running this program.
 
 Python Website Link: https://www.python.org 
 
 Please download all image and videos links for this project found in the AI_CAR_TRACK folder
 
# 2. Packages Required
 
 Computer vision package
 
 1.) Implement this command in terminal: 
 
 pip3 install opencv-python 
 
 <strong> OR </strong>
 
 pip3 install opencv-python-headless
 
 
 2.) Implement computer vision 2 command in terminal: 
 
 import cv2  
 
 **This command above checks to ensure you installed the following without error**
 
 
# Machine Learning Files(Haar Cascade xml files)
 
Pedestrians:
https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_fullbody.xml

Cars:
https://raw.githubusercontent.com/andrewssobral/vehicle_detection_haarcascades/master/cars.xml

# Video of cars and pedestrians 

Tesla Dashcam: https://www.youtube.com/watch?v=d4L1Pte7zVc

Motorcycle Dashcam of pedestrians : https://www.youtube.com/watch?v=WriuvU1rXkc   

**PLEASE SKIP TO THIS TIMESTAMP FOR MOTORCYCLE VIDEO ABOVE 0:09**
 
 # Dataset
 
 <b>OpenCV Documentation</b>:
 
 https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html?highlight=detectmultiscale
 
 <p></p>
 
 <b>Cars Dataset (Cal Tech)</b>:
 
Link: https://www.researchgate.net/figure/Car-dataset-taken-by-Brad-Philip-and-Paul-Updike-California-Institute-of-Technology-It_fig5_267863282
 
# 3. Run Program Instructions


