import cv2
test_img = cv2.imread("test_img.jpeg")
low_threshold = 50
high_threshold = 70
canny_edge_filter = cv2.Canny(test_img, low_threshold, high_threshold)
cv2.imshow('original', test_img)
cv2.imshow('edge', canny_edge_filter)
cv2.waitKey(0)
cv2.destroyAllWindows()