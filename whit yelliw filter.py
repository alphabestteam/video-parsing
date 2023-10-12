import numpy as np
import cv2 as cv

def white_yellow_filter(video):
    cap = video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 0], np.uint8)
        upper_yellow = np.array([255, 70, 240], np.uint8)
        
        mask = cv.inRange(hsv, lower_white, upper_yellow)
        
        cv.imshow('mask', mask) 
        if cv.waitKey(4) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    


if __name__ == "__main__":
    new_video = white_yellow_filter(cv.VideoCapture('car_driving_on_road.mp4'))
    
