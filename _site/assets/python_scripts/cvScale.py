import os
import cv2
import random

src_dir = "select2000/"
name_idx = 6000
dest_img_dir = "scale/image/"
dest_txt_dir = "scale/txt/"

img_list = os.listdir(src_dir)

def write_label(old_name, new_name, hratio_, wratio_):
    old_obj = open(src_dir+old_name)
    new_obj = open(dest_txt_dir+new_name, 'w')
    old_txt = old_obj.read()
    
    
    writeline_str = ''
    gt_split = old_txt.split('\n')
    for gt_line in gt_split:
        gt_ind = gt_line.split(',')
        cordiante_str = []
        if len(gt_ind) > 8:
            for i in range(0, 8):
                if i % 2 == 0:
                    cordiante_str.append(str(float(gt_ind[i])*wratio_))
                else:
                    cordiante_str.append(str(float(gt_ind[i])*hratio_))
            writeline_str = cordiante_str[0] + ',' + cordiante_str[1] + ',' + cordiante_str[2] + ',' + cordiante_str[3] + ',' + cordiante_str[4] + ',' + cordiante_str[5] + ',' + cordiante_str[6] + ',' + cordiante_str[7] + ',' + gt_ind[8] + '\n'
            new_obj.write(writeline_str)
    old_obj.close()
    new_obj.close()
    
    
for img_name in img_list:
    if '.txt' in img_name:
        continue
    print img_name
    txt_name = img_name.rstrip('jpg') + 'txt'
    new_txt_name = str(name_idx).zfill(6) + '.txt'
    img = cv2.imread(src_dir+img_name)
    height, width, c = img.shape
    hratio = 0
    wratio = 0
    prob = random.choice(range(0, 10))
    hratio = random.choice(range(5, 10)) / 10.
    if prob < 7:
        wratio = hratio
    else:
        wratio = random.choice(range(5, 10)) / 10.
    scale_img = cv2.resize(img, (int(width*wratio), int(height*hratio)), interpolation=cv2.INTER_AREA)
    write_label(txt_name, new_txt_name, hratio, wratio)
    cv2.imwrite(dest_img_dir+str(name_idx).zfill(6)+'.jpg', scale_img)
    name_idx += 1
    #print hratio, wratio
    #break
    
    
    
    
    
