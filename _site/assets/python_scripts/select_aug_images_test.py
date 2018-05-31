import random
import shutil
import os

list = os.listdir(r'aug_label_csv/')
for i in range(0, 150):
    image_name = list[i].rstrip('.csv')+'.png'
    shutil.copyfile(r'aug_label_csv/'+list[i], r"aug_label_csv_test/"+list[i])
    shutil.copyfile(r"aug_images/"+image_name, r"aug_images_test/"+image_name)