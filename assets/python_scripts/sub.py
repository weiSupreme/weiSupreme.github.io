import numpy as np
import cv2

#cap = cv2.VideoCapture('Video_001.avi')
#cap = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2(False)
cv2.namedWindow("sourceImg")
cv2.namedWindow("fgmask")
count = 0
for i in range(1, 23):
    frame = cv2.imread("ball_annotated/camera1_20080409T183943+02_frame%d.png" % (i))
    #ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    cv2.imshow('sourceImg', frame)
    cv2.imshow('fgmask', fgmask)
    #count = i % 10
    #if not count:
    cv2.imwrite("2.fg/camera1_20080409T183943+02_frame%d_fg.png" % (i), fgmask)
    k = cv2.waitKey(100) & 0xff
    #if k == 27:
        #break
#cap.release()
cv2.destroyAllWindows()