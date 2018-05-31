import os

txt = open(r'test.txt')
new_txt = open(r'test1.txt', 'w')
lines = txt.readlines()
#print lines.strip('\n')
for line2 in lines:
    new_txt.write(line2.strip('\r\n')+'\n')
txt.close()
new_txt.close()
