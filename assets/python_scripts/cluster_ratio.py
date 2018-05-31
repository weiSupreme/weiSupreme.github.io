# coding: utf-8

import os
import random
import numpy as np

######## read all boxes
train = open('train.txt', 'r')
train_read = train.readlines()
box_wh = []

for train_line in train_read:
    txt_name = train_line.rstrip('\n') + '.txt'   #annotations_txt:  width height channel \n  xmin ymin xmax ymax
    #print(txt_name)
    txt = open('annotations_txt/'+txt_name, 'r')
    txt_read = txt.readlines()
    flag = 0
    for line in txt_read:
        if flag == 0:
            flag = 1
            continue
        line = line.split(' ')
        xmin = float(line[0])
        ymin = float(line[1])
        xmax = float(line[2])
        ymax = float(line[3])
        box_wh.append([xmax-xmin, ymax-ymin])

def distance(box, centroid):
    return (abs(box[0]-centroid[0])+abs(box[1]-centroid[1]))

def cluster_aspect_ratio(box, anchor_num):
    ########## cluster
    print('clustering aspec ratios ******************************************************')
    box_cnt = len(box)
    boxes = []
    for p in range(box_cnt):
        boxes.append([box[p][0]/box[p][1], box[p][1]/box[p][0]])
    centroids = []
    centroids_last = []
    boxes_c_a = []
    boxes_c_d = []
    boxes_c_cnt = np.zeros(anchor_num)
    rand_k = random.sample(range(0, box_cnt), anchor_num)
    for i in range(0, anchor_num):
        width = boxes[rand_k[i]][0]
        height = boxes[rand_k[i]][1]
        centroids.append([width, height])
        centroids_last.append([0, 0])

    flag = 0
    cluster_cnt = 1
    while not flag:
        #print('clustering', cluster_cnt)
        flag_cnt = 0
        boxes_c_cnt = np.zeros(anchor_num)
        boxes_c_a = []                  #生成数组
        boxes_c_d = []
        for n in range(0, anchor_num):
            boxes_c_a.append([])
            boxes_c_d.append([])
        #print(boxes_c_d)    
        for i in range(0, box_cnt):
            dist = []
            for j in range(0, anchor_num):
                dist.append(distance(boxes[i], centroids[j]))
            min_dist_idx = dist.index(min(dist))
            boxes_c_a[min_dist_idx].append(boxes[i])
            boxes_c_cnt[min_dist_idx] += 1
            boxes_c_d[min_dist_idx].append(min(dist))
        for k in range(0, anchor_num):
            #print(centroids[k])
            centroids[k] = np.sum(boxes_c_a[k], axis=0)/(float(boxes_c_cnt[k]))
            if centroids[k][0] == centroids_last[k][0] and centroids[k][1] == centroids_last[k][1]:
                flag_cnt += 1
            centroids_last[k] = centroids[k]
        if flag_cnt == anchor_num:
            flag = 1
            #print('********************min  max************************')
            #for m in range(0, anchor_num):
             #   print('min', boxes_c_a[m][boxes_c_d[m].index(min(boxes_c_d[m]))])
              #  print('max', boxes_c_a[m][boxes_c_d[m].index(max(boxes_c_d[m]))])
            #print('********************min  max************************')
        cluster_cnt += 1
    print('********************centroids************************')
    write_flag = 0
    for l in range(0, anchor_num):
        print(centroids[l], boxes_c_cnt[l])
        if write_flag:
            txt_name = str(int(centroids[l][0])) + '_' + str(int(centroids[l][1])) + '.txt'
            txt = open(txt_name, 'w')
            for p in range(int(boxes_c_cnt[l])):
                txt.write(str(boxes_c_a[l][p][0]) + ' ' + str(boxes_c_a[l][p][1]) + '\n')
            txt.close()
    print('clustering aspec ratios ******************************************************')

cluster_aspect_ratio(box_wh, 6)
    
    
    
    
    
    
    
    
    
    
    
    

