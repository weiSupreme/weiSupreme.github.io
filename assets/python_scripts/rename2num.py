import os

dir = r"train_annotations-csv/"
list = os.listdir(dir)
ind = 2000

for i in range(0,len(list)):  #len(list)
    img_file_name_no_ext = list[i].rstrip('.csv')
    print(img_file_name_no_ext)
    new_name_no_ext = str(ind).zfill(6)
    os.rename(dir+list[i], dir+new_name_no_ext+'.csv')
    os.rename(r"aug_images/"+img_file_name_no_ext+'.png', r"aug_images/"+new_name_no_ext+'.png')
    os.rename(r"train_images/"+img_file_name_no_ext+'.png', r"train_images/"+new_name_no_ext+'.png')
    ind += 1
print(ind-2000)