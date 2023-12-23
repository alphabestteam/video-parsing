import math
import numpy as np
import cv2
def size_and_slope_filter(lines, frame):
    left_line_x = []
    left_line_y = []
    right_line_x = []
    right_line_y = []
    if lines is None:
        return frame
    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y2 - y1) / (x2 - x1)
            if math.fabs(slope) < 0.5:
                continue
            if slope <= 0:
                left_line_x.extend([x1, x2])
                left_line_y.extend([y1, y2])
            else:
                right_line_x.extend([x1, x2])
                right_line_y.extend([y1, y2])

    min_y = int(frame.shape[0] * (3 / 5))
    max_y = int(frame.shape[0])

    # Add a check before the polynomial fitting
    if not left_line_x or not left_line_y or not right_line_x or not right_line_y:
        # Handle the case where the lists are empty
        return frame  # Or any appropriate action

    poly_left = np.poly1d(np.polyfit(
        left_line_y,
        left_line_x,
        deg=1
    ))

    left_x_start = int(poly_left(max_y))
    left_x_end = int(poly_left(min_y))

    poly_right = np.poly1d(np.polyfit(
        right_line_y,
        right_line_x,
        deg=1
    ))

    right_x_start = int(poly_right(max_y))
    right_x_end = int(poly_right(min_y))

    line_frame = draw_lines(
        frame,
        [
            [
                [left_x_start, max_y, left_x_end, min_y],
                [right_x_start, max_y, right_x_end, min_y],
            ]
        ],
        thickness=5,
    )
    return line_frame

def draw_lines(frame, lines, color=[0, 255, 0], thickness=3):
    frame = np.copy(frame)
    if lines is None:
        return frame
    
    left_line = lines[0][0]
    right_line = lines[0][1]

    # Create a polygon from the endpoints of the lines
    pts = np.array([
        [left_line[0], left_line[1]],  # Top left
        [left_line[2], left_line[3]],  # Bottom left
        [right_line[2], right_line[3]],  # Bottom right
        [right_line[0], right_line[1]]   # Top right
    ], np.int32)
    
    # Reshape the array
    pts = pts.reshape((-1, 1, 2))
    
    # Fill the space between the lines in green
    cv2.fillPoly(frame, [pts], color)
    
    # Draw the lines themselves
    cv2.line(frame, (left_line[0], left_line[1]), (left_line[2], left_line[3]), color, thickness)
    cv2.line(frame, (right_line[0], right_line[1]), (right_line[2], right_line[3]), color, thickness)
    
    return frame