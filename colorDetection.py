import cv2
import numpy as np

def trackbar_callback(x): # callback function to get trackbar value
    global h_low, h_upp, s_low, s_upp, v_low, v_upp
    h_low = cv2.getTrackbarPos("Hue - L", "Trackbar")
    h_upp = cv2.getTrackbarPos("Hue - U", "Trackbar")
    s_low = cv2.getTrackbarPos("Sat - L", "Trackbar")
    s_upp = cv2.getTrackbarPos("Sat - U", "Trackbar")
    v_low = cv2.getTrackbarPos("Val - L", "Trackbar")
    v_upp = cv2.getTrackbarPos("Val - U", "Trackbar")

h_low = 0
h_upp = 179
s_low = 0
s_upp = 255
v_low = 0
v_upp = 255

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 400)

# Trackbars for HSV
cv2.createTrackbar("Hue - L", "Trackbar", 0, 179, trackbar_callback)
cv2.createTrackbar("Hue - U", "Trackbar", 179, 179, trackbar_callback)
cv2.createTrackbar("Sat - L", "Trackbar", 0, 255, trackbar_callback)
cv2.createTrackbar("Sat - U", "Trackbar", 255, 255, trackbar_callback)
cv2.createTrackbar("Val - L", "Trackbar", 0, 255, trackbar_callback)
cv2.createTrackbar("Val - U", "Trackbar", 255, 255, trackbar_callback)

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
    while True:
        _, frame = cap.read()
        cv2.imshow("Webcam", frame)

        hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsvLow = np.array([h_low, s_low, v_low], np.uint8) # lower threshold
        hsvUp = np.array([h_upp, s_upp, v_upp], np.uint8) # upper threshold
        mask = cv2.inRange(hsvImg, hsvLow, hsvUp)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Mask", mask)
        cv2.imshow("Result", result)

        key = cv2.waitKey(1) # in milliseconds, 0 means infinite
        if key == 27: #27 = escape key
            break

cap.release() # stop cap.read()
cv2.destroyAllWindows() #destroy windows