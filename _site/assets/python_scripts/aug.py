import os
import cv2
import numpy as np


dir = r"JPEGImages/"
list = os.listdir(dir)
cnt =0

for i in range(0, len(list)):
    print(list[i])
    img = cv2.imread(dir+list[i])
    img_tmp = img.copy()
    img2 = img.copy()
    img_tmp = img_tmp.dot((0.05, 0.35, 0.6))
    #print(img_tmp.shape)
    img[:,:,0] = img_tmp
    #img[:,:,1] = img_tmp
    #img[:,:,2] = img_tmp
    #print(img.shape)
    #cv2.imshow('img', img)
    #cv2.imshow('aug', img2)
    #cv2.waitKey(0)
    cv2.imwrite(r"aug/"+list[i], img)
    cnt = cnt + 1
print(cnt)
    