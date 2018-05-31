import random
import linecache
import shutil

txt = open("random-select/label.txt", 'w')
resultList=random.sample(range(0,789),150)
for i in range(0, 150):
    theline = linecache.getline(r'ImageSets/Main/train.txt', resultList[i]).strip('\n')
    print(theline)
    txt.write(theline+'\n')
    shutil.copyfile(r'Annotations/'+theline+'.xml', r"random-select/Annotations/"+theline+'.xml')
    shutil.copyfile(r"JPEGImages/"+theline+'.png', r"random-select/JPEGImages/"+theline+'.png')
txt.close()