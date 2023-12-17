import cv2 as cv
import numpy as np
from functions.roi import roi
from functions.yellow_white_filter import yellow_white_filter
from functions.gaussian_blurring import gaussian_blurring
from functions.canny import canny
from functions.hough import hough
from functions.size_and_slope_filter import size_and_slope_filter


def main():
    cap = cv.VideoCapture("car_driving_on_road.mp4")
    fourcc = cv.VideoWriter_fourcc(*"XVID")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        ro = roi(frame)
        yellow_white = yellow_white_filter(ro)
        gau = gaussian_blurring(yellow_white)
        # ca = canny(gau)
        hou = hough(gau)
        # size_slope = size_and_slope_filter(hou)

        
       
        cv.imshow('frame', hou) 
        if cv.waitKey(4) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
