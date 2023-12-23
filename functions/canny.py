import cv2

def canny(car_driving_frame):
    
    low_threshold = 50
    high_threshold = 150
    canny_edge_filter = cv2.Canny(car_driving_frame, low_threshold, high_threshold)
    return canny_edge_filter


