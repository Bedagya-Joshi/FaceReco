import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('C:\Users\bedag\OneDrive\Documents\Project\Images')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

cv2.imshow