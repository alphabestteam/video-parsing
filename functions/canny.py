import cv2
def canny(car_driving_frame):
    output_image = cv2.imread(car_driving_frame)
    output_gray = cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY)
    low_threshold = 50
    high_threshold = 150
    canny_edge_filter = cv2.Canny(output_gray, low_threshold, high_threshold)
    return canny_edge_filter


