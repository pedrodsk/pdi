import cv2 as cv
import numpy as np


image = cv.imread("imag.jpg")                
# Convert BGR to HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

def red_hsv():

    lower_hsv_1 = np.array([0,175,20])
    higher_hsv_1 = np.array([10,255,255])

    lower_hsv_2 = np.array([170,175,20])
    higher_hsv_2 = np.array([180,255,255])

    mask_1 = cv.inRange(hsv, lower_hsv_1,higher_hsv_1)
    mask_2 = cv.inRange(hsv, lower_hsv_2,higher_hsv_2)

    return mask_1 + mask_2

def green_hsv():

    lower_hsv= np.array([40,150,20])
    higher_hsv= np.array([70,255,255])

    mask = cv.inRange(hsv, lower_hsv,higher_hsv)
    

    return mask

def blue_hsv():

    lower_hsv= np.array([0,0,255])
    higher_hsv= np.array([31,153,255])

    mask = cv.inRange(hsv, lower_hsv,higher_hsv)
    

    return mask



mask = red_hsv() + green_hsv() + blue_hsv()

detected_img = cv.bitwise_and(image,image,mask=mask)

cv.imshow("IMg", detected_img)
cv.waitKey(0)
cv.destroyAllWindows



    