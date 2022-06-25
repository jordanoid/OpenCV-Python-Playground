import cv2
import numpy as np
 
img = cv2.imread("resources/cards.jpg")
 
width,height = 250,350 # the size of the card
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) # each corner of the card pixel point
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # new point for card
matrix = cv2.getPerspectiveTransform(pts1,pts2) 
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) # wrap image perspecive
 
 
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
 
cv2.waitKey(0)