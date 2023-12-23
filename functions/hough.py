import math
import cv2 as cv
import numpy as np

def hough(frame):
    lines = cv.HoughLinesP(frame, 1, np.pi / 180, 50, None, 20, 10)
    return lines
