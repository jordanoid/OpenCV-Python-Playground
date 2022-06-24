import cv2

def resize(img, width, height):
    imgResize = cv2.resize(img, (width, height)) # resize image
    return imgResize

if __name__ == "__main__":

    img = cv2.imread("resources/image.jpg") # load image

    imgResize = resize(img, 1280, 720)

    #cropping image
    imgCropped = imgResize[0:200, 200:500] #[height range, width range]

    cv2.imshow("image resize", imgResize) # show image
    cv2.imshow("image cropped", imgCropped) # show image

    cv2.waitKey(0)