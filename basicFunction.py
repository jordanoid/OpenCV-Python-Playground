import cv2
import numpy as np

# video capture media
cap = cv2.VideoCapture(0) # numbers for camera id or video file directory

cap.set(3, 1280) # set width to 1280, 3 is id for width
cap.set(4, 720) # set height to 720, 4 is id for height

def grayscale(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayscale
    return imgGray

def gaussianBlur(img, ksize = (7,7), sigmaX = 0):
    #sigmaX value must be odd number
    imgBlur = cv2.GaussianBlur(img, ksize, sigmaX) # gives gaussian blur effect
    return imgBlur

def cannyFilter(img, threshold1, threshold2): # canny filter
    imgCanny = cv2.Canny(img, threshold1, threshold2)
    return imgCanny

def dilate(img, kernel, iterations): # dialation
    imgDialation = cv2.dilate(img, kernel, iterations)
    return imgDialation

def erode(img, kernel, iterations): # erode
    imgErode = cv2.erode(img, kernel, iterations)
    return imgErode  

if __name__ == '__main__':
    kernel = np.ones((5,5), np.uint8)
    while True:
        _, frame = cap.read() # read frame
        frame = grayscale(frame)
        frame = gaussianBlur(frame)
        frame = cannyFilter(frame, 50, 100)
        frame = dilate(frame, kernel, 1)
        cv2.imshow("webcam", frame)
        key = cv2.waitKey(1) # in milliseconds, 0 means infinite
        if key == 27: #27 = escape key
            break

    cap.release() # stop cap.read()
    cv2.destroyAllWindows() #destroy windows