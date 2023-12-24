import cv2 as cv

def dilation_erosion(img):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    return closing