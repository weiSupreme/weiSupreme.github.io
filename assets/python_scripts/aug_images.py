import os
import cv2

dir = r"test_images/"
list = os.listdir(dir)
cnt = 0

for i in range(0,len(list)):  #len(list)
    img_file_name = list[i]
    print(img_file_name)
    img = cv2.imread(dir+img_file_name)
    new_img = cv2.flip(img, 1)
    cv2.imwrite(r"aug_images_test/"+img_file_name, new_img)
    cnt += 1
print('all ', cnt)