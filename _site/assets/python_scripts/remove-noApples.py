import csv
import os
import shutil


dir = r"annotations-csv/"
list = os.listdir(dir)

flag = 0

for i in range(0,len(list)):  #len(list)
    file_name_no_ext = list[i].rstrip('.csv')
    print(file_name_no_ext)
    path = os.path.join(dir,list[i])
    if os.path.isfile(path):
        out = open(path,'r')
        read_csv = csv.reader(out,dialect='excel')
        for line in read_csv:     #循环输出csv中的所有数据
            if flag == 0:
                flag = flag + 1
                continue
            flag = flag + 1
        if flag > 1:
            shutil.copyfile(path, r"all-have-apples/annotations-csv/"+file_name_no_ext+'.csv')
            shutil.copyfile(r"images/"+file_name_no_ext+'.png', r"all-have-apples/images/"+file_name_no_ext+'.png')
        flag = 0
        out.close()
print(len(list))