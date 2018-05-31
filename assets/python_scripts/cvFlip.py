import os
import cv2

src_dir = "select2000/"
flag = 0
if flag == 1:
    name_idx = 0
    dest_img_dir = "horizontalFlip/image/"
    dest_txt_dir = "horizontalFlip/txt/"
else:
    name_idx = 3000
    dest_img_dir = "verticalFlip/image/"
    dest_txt_dir = "verticalFlip/txt/"

img_list = os.listdir(src_dir)

def write_label(old_name, new_name, flag, img_height, img_width):
    old_obj = open(src_dir+old_name)
    new_obj = open(dest_txt_dir+new_name, 'w')
    old_txt = old_obj.read()
    
    
    writeline_str = ''
    gt_split = old_txt.split('\n')
    for gt_line in gt_split:
        gt_ind = gt_line.split(',')
        cordiante_str = []
        if len(gt_ind) > 8:
            if flag == 1:
                for i in range(0, 7, 2):
                    cordiante_str.append(str(img_width-1-float(gt_ind[i])))
                    #print len(cordiante_str)
                writeline_str = cordiante_str[0] + ',' + gt_ind[1] + ',' + cordiante_str[1] + ',' + gt_ind[3] + ',' + cordiante_str[2] + ',' + gt_ind[5] + ',' + cordiante_str[3] + ',' + gt_ind[7] + ',' + gt_ind[8] + '\n'
            else:
                for i in range(1, 8, 2):
                    cordiante_str.append(str(img_height-1-float(gt_ind[i])))
                writeline_str = gt_ind[0] + ',' + cordiante_str[0] + ',' + gt_ind[2] + ',' + cordiante_str[1] + ',' + gt_ind[4] + ',' + cordiante_str[2] + ',' + gt_ind[6] + ',' + cordiante_str[3] + ',' + gt_ind[8] + '\n'
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
    #print height, width
    #break
    flip_img = []
    if flag == 1:
        flip_img = cv2.flip(img, 1)
    else:
        flip_img = cv2.flip(img, 0)
    write_label(txt_name, new_txt_name, flag, height, width)
    cv2.imwrite(dest_img_dir+str(name_idx).zfill(6)+'.jpg', flip_img)
    name_idx += 1
    
    
    
    
    
