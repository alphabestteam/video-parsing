import numpy as np
import cv2 as cv

def hough(frame):

    
    edges = cv.Canny(frame,50,150,apertureSize = 3)
    lines = cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        lin =cv.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
    return lin
    