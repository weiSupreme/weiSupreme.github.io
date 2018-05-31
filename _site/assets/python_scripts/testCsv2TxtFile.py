import csv
import os


dir = r"test-annotations-csv/"
list = os.listdir(dir)

flag = 0
category = 'apple'
top_left_x = 0
top_left_y = 0
bottom_right_x = 0
bottom_right_y = 0

#txt = open("label.txt", 'w')

for i in range(0,len(list)):  #len(list)
    img_file_name = list[i].rstrip('.csv') + '.png'
    print(img_file_name)
    path = os.path.join(dir,list[i])
    if os.path.isfile(path):
        out = open(path,'r')
        read_csv = csv.reader(out,dialect='excel')
        for line in read_csv:     #循环输出csv中的所有数据
            txt = open(r'test-label/'+list[i].rstrip('.csv')+'.txt', 'w')
            if flag == 0:
                flag = flag + 1
                continue
            flag = flag + 1
            #print(line)
            if line[4] == '1':
                category = 'apple'
                top_left_x = (int)(float(line[1]) - float(line[3])) if (int)(float(line[1]) - float(line[3])) > 1 else 1
                top_left_y = (int)(float(line[2]) - float(line[3])) if (int)(float(line[2]) - float(line[3])) > 1 else 1
                bottom_right_x = (int)(float(line[1]) + float(line[3])) if (int)(float(line[1]) + float(line[3])) < 308 else 308
                bottom_right_y = (int)(float(line[2]) + float(line[3])) if (int)(float(line[2]) + float(line[3])) < 202 else 202
                write_str = str(top_left_x) +' ' + str(top_left_y) + ' ' + str(bottom_right_x) + ' ' + str(bottom_right_y) + '\n'
                txt.write(write_str)
        #print(flag)
        if flag == 1:
            print("no apples")
            os.exit()
        flag = 0
        out.close()
        txt.close() 
print(len(list))