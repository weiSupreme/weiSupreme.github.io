import os
import shutil

cnt = 0
f = open(r"ImageSets/Main/"+"train.txt")
lines = f.readlines()
for line in lines:
    print(line)
    file_name_no_ext = line.strip('\n')
    shutil.copyfile(r"annotations-csv/"+file_name_no_ext+'.csv', r"train_annotations-csv/"+file_name_no_ext+'.csv')
    shutil.copyfile(r"images/"+file_name_no_ext+'.png', r"train_images/"+file_name_no_ext+'.png')
    cnt = cnt + 1
f.close()
print(cnt)