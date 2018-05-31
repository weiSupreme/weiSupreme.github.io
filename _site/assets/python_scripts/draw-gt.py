import csv
import os
from PIL import Image, ImageDraw

source_dir = r'apple/'
dest_dir = r'apple-gt/'

list = os.listdir(source_dir)
for file_name in list:
    print file_name
    file_name_no_ext = file_name.rstrip('.png')
    img = Image.open(source_dir+file_name)
    draw = ImageDraw.Draw(img)
    csv_out = open(r'test-annotations-csv/'+file_name_no_ext+'.csv', 'r')
    read_csv = csv.reader(csv_out, dialect='excel')
    csv_line_num = 0
    for line in read_csv:
        if csv_line_num == 0:
            csv_line_num += 1
            continue
        xminT = (int)(float(line[1]) - float(line[3])) if (int)(float(line[1]) - float(line[3])) > 1 else 1
        yminT = (int)(float(line[2]) - float(line[3])) if (int)(float(line[2]) - float(line[3])) > 1 else 1
        xmaxT = (int)(float(line[1]) + float(line[3])) if (int)(float(line[1]) + float(line[3])) < 308 else 308
        ymaxT = (int)(float(line[2]) + float(line[3])) if (int)(float(line[2]) + float(line[3])) < 202 else 202
        draw.rectangle([xminT, yminT, xmaxT, ymaxT], outline=(0, 0, 255))
    csv_out.close()
    img.save(dest_dir+file_name)
