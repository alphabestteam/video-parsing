# import cv2 as cv
# import numpy as np
# from functions.roi import roi
# from functions.yellow_white_filter import yellow_white_filter
# from functions.gaussian_blurring import gaussian_blurring
# from functions.canny import canny
# from functions.hough import hough
# from functions.size_and_slope_filter import size_and_slope_filter
# from goprocam import GoProCamera, constants
# import socket

# def main():
#     gpCam = GoProCamera.GoPro()
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     gpCam.livestream("start")

#     # setting resolution
#     gpCam.video_settings(res='1080p', fps='30')

#     gpCam.gpControlSet(constants.Stream.WINDOW_SIZE, constants.Stream.WindowSize.R720)


#     cap = cv.VideoCapture("udp://10.5.5.9:8554", cv.CAP_FFMPEG)

#     fourcc = cv.VideoWriter_fourcc(*"XVID")
#     # cv.namedWindow('video', cv.WINDOW_NORMAL)


#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             print("Can't receive frame (stream end?). Exiting ...")
#             break
#         ro = roi(frame)
#         yellow_white = yellow_white_filter(ro)
#         gau = gaussian_blurring(yellow_white)
#         ca = canny(gau)
#         hou = hough(ca)
#         size = size_and_slope_filter(hou, frame)
#         cv.imshow("Modified Frame", size)

#         if cv.waitKey(4) == ord("q"):
#             break

#     cap.release()
#     cv.destroyAllWindows()

# if __name__ == "__main__":
#     main()

import cv2 as cv
import numpy as np
from functions.roi import roi
from functions.yellow_white_filter import yellow_white_filter
from functions.gaussian_blurring import gaussian_blurring
from functions.canny import canny
from functions.hough import hough
from functions.size_and_slope_filter import size_and_slope_filter


def dilation_erosion(img):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    return closing


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
        ca = canny(gau)
        morph = dilation_erosion(ca)
        hou = hough(morph)
        size = size_and_slope_filter(hou, frame)
        cv.imshow("Modified Frame", size)

        if cv.waitKey(4) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
