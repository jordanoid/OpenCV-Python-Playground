import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) # create image pixel array with value 0

# img[:] = 255, 0, 0 # bgr color value for every pixel

cv2.line(img, (255, 255), (512, 512), (0, 0, 255), 2) # create a line
cv2.rectangle(img, (0,0), (255,255), (255, 0, 0), cv2.FILLED) # create a rectangle
cv2.circle(img, (255,255), 30, (0 , 255, 255)) # create a circle
cv2.putText(img, "OPENCV", (0, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 3) # put a text

cv2.imshow("image", img)

print(img.shape)

cv2.waitKey(0)