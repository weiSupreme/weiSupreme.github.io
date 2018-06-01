import os

src_txt = open('Englabel.txt')
txt_read = src_txt.readlines()
map_txt = open('map.txt', 'w')
idx = 1

for line in txt_read:
    line_split = line.split(':')
    name = line_split[1].rstrip('\n')
    write_str = 'item' + ' ' + '{' + '\n'
    write_str += '  ' + 'name:' + ' ' + '"' + name + '"' + '\n'
    write_str +=  '  ' + 'label:' + ' ' + str(idx) + '\n'
    write_str +=  '  ' + 'display_name:' + ' ' + '"' + name + '"' + '\n'
    write_str += '}' + '\n'
    idx += 1
    map_txt.write(write_str)
    #break
src_txt.close()
map_txt.close()