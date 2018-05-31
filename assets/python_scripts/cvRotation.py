import os
import cv2
import random
import numpy as np

src_dir = "make/"
name_idx = 22000
dest_img_dir = "make_rotation/image/"
dest_txt_dir = "make_rotation/txt/"

img_list = os.listdir(src_dir)

def write_label(old_name, new_name, ratio, src_height, r_height, rangle):
    old_obj = open(src_dir+old_name)
    new_obj = open(dest_txt_dir+new_name, 'w')
    old_txt = old_obj.read()
    
    rrad = rangle * 3.1415926 / 180.
    writeline_str = ''
    gt_split = old_txt.split('\n')
    for gt_line in gt_split:
        gt_ind = gt_line.split(',')
        cordiante_str = []
        if len(gt_ind) > 8:
            for i in range(0, 8, 2):
                x = float(gt_ind[i])*ratio
                y = src_height - 1 - float(gt_ind[i+1])*ratio
                l = np.sqrt(x**2 + y**2)
                srad = np.arcsin(y/(float)(l))   #rad
                x_ = src_height * np.sin(rrad) + l * np.cos(rrad+srad)
                y_ = r_height - 1 - l * np.sin(rrad+srad)
                cordiante_str.append(str(x_))
                cordiante_str.append(str(y_))
            writeline_str = cordiante_str[0] + ',' + cordiante_str[1] + ',' + cordiante_str[2] + ',' + cordiante_str[3] + ',' + cordiante_str[6] + ',' + cordiante_str[7] + ',' + cordiante_str[4] + ',' + cordiante_str[5] + ',' + gt_ind[8] + '\n'
            new_obj.write(writeline_str)
    old_obj.close()
    new_obj.close()
    
pi = 3.1415926   
def new_image(old_img, theta):
    theta_rad = theta*pi/180.
    h, w, c = old_img.shape
    dw = int(h * np.sin(theta_rad))
    dh1 = int(h * np.cos(theta_rad))
    dh2 = int(w * np.sin(theta_rad))
    width = dw + w
    height = dh1 + dh2-
    new_img = np.zeros((height, width, 3), dtype=np.uint8)
    #new_img = np.uint8(255 * np.random.random((height, width, 3)))
    new_img[height-h:, dw:, :] = old_img[:, :, :]
    return new_img, height, width, dw
    
       
for img_name in img_list:
    if '.txt' in img_name:
        continue
    print img_name
    txt_name = img_name.rstrip('jpg') + 'txt'
    new_txt_name = str(name_idx).zfill(6) + '.txt'
    src_img = cv2.imread(src_dir+img_name)
    height, width, c = src_img.shape
    scale_ratio = 0.8
    img = cv2.resize(src_img, (int(width*scale_ratio), int(height*scale_ratio)), interpolation=cv2.INTER_AREA)
    height, width, c = img.shape
    
    theta = 30
    spand_img, new_height, new_width, dwidth = new_image(img, theta)
    
    M = cv2.getRotationMatrix2D((dwidth-1, new_height-1), theta, 1)
    rotation_img = cv2.warpAffine(spand_img, M, (new_width, new_height))
    crop_width = dwidth + int(width*np.cos(theta*pi/180.))
    crop_img = rotation_img[:, 0:crop_width-1, :]
    #cv2.imshow('spand_img', crop_img)
    #cv2.waitKey(0)
    
    write_label(txt_name, new_txt_name, scale_ratio, height, new_height, theta)
    cv2.imwrite(dest_img_dir+str(name_idx).zfill(6)+'.jpg', crop_img)
    name_idx += 1
    #print hratio, wratio
    if name_idx == 20030:
        #break
        pass


    
    
    
    
    
    
    
    
    
    
    
    
    
