import cv2

def gaussian_blurring(frame):

    # apply guassian blur on frame image
    gaussian_frame = cv2.GaussianBlur(frame,(3,3),cv2.BORDER_DEFAULT)

    return gaussian_frame

