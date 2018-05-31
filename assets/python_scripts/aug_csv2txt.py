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

txt = open("label.txt", 'w')

for i in range(0,len(list)):  #len(list)
    img_file_name = list[i].rstrip('.csv') + '.png'
    print(img_file_name)
    path = os.path.join(dir,list[i])
    new_csv = open(r'aug_label_csv_test/'+list[i], 'w', newline='')
    writer = csv.writer(new_csv)
    writer.writerow(['#item', 'c-x', 'c-y', 'radius', 'label'])
    if os.path.isfile(path):
        out = open(path,'r')
        read_csv = csv.reader(out,dialect='excel')
        for line in read_csv:     #循环输出csv中的所有数据
            if flag == 0:
                flag = flag + 1
                continue
            flag = flag + 1
            #print(line)
            if line[4] == '1':
                category = 'apple'
                top_left_x = (int)(float(line[1]) + float(line[3])) if (int)(float(line[1]) + float(line[3])) < 307 else 307
                top_left_x = 308 - top_left_x
                top_left_y = (int)(float(line[2]) - float(line[3])) if (int)(float(line[2]) - float(line[3])) > 1 else 1
                bottom_right_x = (int)(float(line[1]) - float(line[3])) if (int)(float(line[1]) - float(line[3])) > 0 else 0
                bottom_right_x = 308 - bottom_right_x
                bottom_right_y = (int)(float(line[2]) + float(line[3])) if (int)(float(line[2]) + float(line[3])) < 202 else 202
                write_str = img_file_name + ' ' + category + ' ' + str(top_left_x) +' ' + str(top_left_y) + ' ' + str(bottom_right_x) + ' ' + str(bottom_right_y) + '\n'
                txt.write(write_str)
                c_x = float((top_left_x+bottom_right_x)/2)
                c_y = float((top_left_y+bottom_right_y)/2)
                radius = float((bottom_right_x+bottom_right_y-top_left_x-top_left_y)/4)
                writer.writerow([str(flag-2), str(c_x), str(c_y), str(radius), '1'])
        #print(flag)
        if flag == 1:
            print("no apples")
            os.exit()
        flag = 0
        out.close()
    new_csv.close()
txt.close() 
print(len(list))