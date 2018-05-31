import cv2
import os
import numpy as np

dir = r'JPEGImages/'
list = os.listdir(dir)

R_sum = 0
G_sum = 0
B_sum = 0
im_num = 0

for im_name in list:
    im_num += 1
    img = cv2.imread(dir+im_name)
    imgr = img[:,:,2]
    imgg = img[:,:,1]
    imgb = img[:,:,0]
    R_sum += np.sum(imgr) / 308 / 202
    G_sum += np.sum(imgg) / 308 / 202
    B_sum += np.sum(imgb) / 308 / 202
    #print R_sum, G_sum, B_sum
R_sum /= im_num
G_sum /= im_num
B_sum /= im_num
print R_sum, G_sum, B_sum
