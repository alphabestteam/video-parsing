import cv2
import numpy as np

def roi(frame):
    
        # shape returns 3 values (height, width and color spectrum (rgb)) :2 slices and only takes the height and width
        height, width = frame.shape[:2]

        # converting the image to grey
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # creating the ROI
        ROI = np.array(
            [[(120, height-30), (390, 290), (480, 290), (800, height-30)]], dtype=np.int32
        )

        # blacking out the whole image
        blank = np.zeros_like(frame_gray)

        # painting the ROI white
        region_of_interest = cv2.fillPoly(blank, ROI, 255)

        # over lap the grey image and the roi (AND)
        region_of_interest_image = cv2.bitwise_and(frame_gray, region_of_interest)

        return region_of_interest_image



# def roi():
#     video = cv2.VideoCapture(
#         r"C:\Users\ezrab\OneDrive\Desktop\video-parsing\car_driving_on_road.mp4"
#     )  # reading the video

#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     output_video = cv2.VideoWriter('roi.mp4', fourcc, 20.0, (960, 720))  

#     while video.isOpened():
#         (
#             ret,
#             frame,
#         ) = (
#             video.read()
#         )  # ret is a var that return a boolean value whether the frame was successfully read.
#         if not ret:
#             break

#         # shape returns 3 values (height, width and color spectrum (rgb)) :2 slices and only takes the height and width
#         height, width = frame.shape[:2]

#         # converting the image to grey
#         frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # creating the ROI
#         ROI = np.array(
#             [[(100, height), (100, 250), (900, 250), (900, height)]], dtype=np.int32
#         )

#         # blacking out the whole image
#         blank = np.zeros_like(frame_gray)

#         # painting the ROI white
#         region_of_interest = cv2.fillPoly(blank, ROI, 255)

#         # over lap the grey image and the roi (AND)
#         region_of_interest_image = cv2.bitwise_and(frame_gray, region_of_interest)

#         # showing result
#         cv2.imshow("Region of Interest", region_of_interest_image)

#         # Write the frame to the output video
#         output_video.write(cv2.cvtColor(region_of_interest_image, cv2.COLOR_GRAY2BGR))

#         # quick break with 'q'
#         if cv2.waitKey(40) & 0xFF == ord("q"):
#             break

#     video.release()
#     cv2.destroyAllWindows()


# if __name__ == "__main__":
#     roi()\\