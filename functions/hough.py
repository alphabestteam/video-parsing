import math
import cv2 as cv
import numpy as np

def hough(frame):
   
    cdstP = np.copy(frame)
    
    lines = cv.HoughLines(frame, 1, np.pi / 180, 150, None, 0, 0)
    
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(frame, pt1, pt2, (0,255,0), 3, cv.LINE_AA)
    
    
    linesP = cv.HoughLinesP(frame, 1, np.pi / 180, 50, None, 20, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            line = cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (255,255,0), 3, cv.LINE_AA)
            return line
