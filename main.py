from functions.roi import roi
from functions.yellow_white_filter import yellow_white_filter
from functions.gaussian_blurring import gaussian_blurring
from functions.canny import canny
from functions.hough import hough
from functions.size_and_slope_filter import size_and_slope_filter
def main():
    ro = roi()
    yellow_white = yellow_white_filter(ro)
    gau = gaussian_blurring(yellow_white)
    ca = canny(gau)
    hou = hough(ca)
    size_slope = size_and_slope_filter(hou)
    
    


if __name__ == '__main__':
    main()