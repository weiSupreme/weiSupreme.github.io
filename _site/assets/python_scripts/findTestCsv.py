import os
import shutil

dir = r'test-annotations-csv/'
txt = open(r'ImageSets/Main/test.txt')
lines = txt.readlines()
for line in lines:
    line = line.strip('\r\n') + '.csv'
    print(line)
    shutil.copyfile(r'annotations-csv/'+line, dir + line)
txt.close()