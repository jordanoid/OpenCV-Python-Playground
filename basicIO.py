# Basic usage example of input and output in openCV

import cv2

# video capture media
cap = cv2.VideoCapture(0) # numbers for camera id or video file directory

cap.set(3, 1280) # set width to 1280, 3 is id for width
cap.set(4, 720) # set height to 720, 4 is id for height

while True:
    _, frame = cap.read() # read frame
    cv2.imshow("webcam", frame)
    key = cv2.waitKey(1) # in milliseconds, 0 means infinite
    if key == 27: #27 = escape key
        break

cap.release() # stop cap.read()
cv2.destroyAllWindows() #destroy windows
