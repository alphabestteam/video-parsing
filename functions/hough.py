import numpy as np
import cv2 as cv2

def hough(frame):
    import cv2
import numpy as np

def hough(frame):
    edges = cv2.Canny(frame, 50, 100, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        if y1>y2:
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame


