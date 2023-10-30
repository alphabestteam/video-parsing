import cv2
def canny(car_drivinG_video):
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

