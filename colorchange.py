import numpy as np
import cv2
from skimage.color import rgb2gray, rgb2hsv

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   255, # max
                   myfunc) # callback func

cap = cv2.VideoCapture(0)

##fourcc = cv2.VideoWriter_fourcc(*'MJPG')
##out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,  10000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)


while(True):

    ret, frame = cap.read()
    if not ret: continue

    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win

    ## do something by using v

    frame[:,:,2] = frame[:,:,2] + v

    cv2.imshow('title', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()