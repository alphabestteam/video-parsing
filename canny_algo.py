import cv2
def canny_algo(car_drivinG_video):
    frames = []
    frame_rate = 20.0
    video_cap = cv2.VideoCapture(car_drivinG_video)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter('car_driving_on_road_canny.mp4', fourcc, 20.0, (640, 460))
    while True:
        video_playing, frame = video_cap.read()
        if not video_playing:
            break
        low_threshold = 50
        high_threshold = 150
        canny_edge_filter = cv2.Canny(frame, low_threshold, high_threshold)
        output.write(frame)
        cv2.imshow('original', frame)
        cv2.imshow('edge', canny_edge_filter)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    video_cap.release()
    return frames, frame_rate


if __name__ == "__main__":
    canny_algo('car_driving_on_road.mp4')