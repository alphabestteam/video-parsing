import cv2
def canny(car_driving_frame):
    # output_image = cv2.imread(car_driving_frame)
    # output_gray = cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY)
    low_threshold = 100
    high_threshold = 250
    canny_edge_filter = cv2.Canny(car_driving_frame, low_threshold, high_threshold)
    return canny_edge_filter


