import numpy as np
import cv2 as cv

def yellow_white_filter(frame):
        bgr = cv.cvtColor(frame, cv.COLOR_GRAY2BGR)
        hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 0], np.uint8)
        upper_yellow = np.array([255, 100, 180], np.uint8)
        
        yellow_white_frame = cv.inRange(hsv, lower_white, upper_yellow)
        return yellow_white_frame
      