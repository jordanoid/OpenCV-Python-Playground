import cv2

path = "resources/shapes.png"

def grayscale(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image to grayscale
    return imgGray

def gaussianBlur(img, ksize = (7,7), sigmaX = 1):
    #sigmaX value must be odd number
    imgBlur = cv2.GaussianBlur(img, ksize, sigmaX) # gives gaussian blur effect
    return imgBlur

def cannyFilter(img, threshold1, threshold2): # canny filter
    imgCanny = cv2.Canny(img, threshold1, threshold2)
    return imgCanny

def getContour(img):
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contour:
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        # print(area)
        if area > 300:
            cv2.drawContours(imgContour, c, -1, (255, 0, 0), 1)
            approx = cv2.approxPolyDP(c, 0.03*perimeter, True)
            # print(len(approx)) # sum of edges
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objType = "Triangle"
            elif objCor == 4:
                aspRatio = w/h
                if aspRatio >= 0.95 and aspRatio <= 1.05: objType = "Square"
                else: objType = "Rectangle" 
            else: objType = "Circle"
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objType, (x+(w//2)-10,y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

if __name__ == "__main__":
    img = cv2.imread(path)
    imgContour = img.copy()
    img = cannyFilter(gaussianBlur(grayscale(img)), 50, 50)
    getContour(img)

    cv2.imshow("Image", imgContour)

    cv2.waitKey(0)