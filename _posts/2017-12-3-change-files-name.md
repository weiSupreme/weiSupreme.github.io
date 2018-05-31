---
layout: post
title:  批量修改文件名
categories:  Tutorial
tags: file python
author: zhuwei
description: 修改某文件夹下的所有/部分文件名
---

### 说明
&emsp;&emsp;本代码适合用来批量修改文件名，可以命名全新的名字，也可以在旧文件名上修改，根据自己的需要对代码做适量改动。注意：此种方法读取的文件不是按文件名的排列顺序的，会有乱序的情况，所以如果要对顺序排列好的文件进行顺序命名，读取文件的时候需要一定的判断。

### 代码    
    import os
    src_dir = r"period14_camera1_fgimproved"   #源文件夹
    name_trip = '_improved'       #文件名要除去的部分：camera1_20080409T183943+02_frame1_name_trip
    new_name_att = 'improved.png'    #新的名称：camera1_20080409T183943+02_frame1_new_name_att
    src_paths = [os.path.join(src_dir, f) for f in os.listdir(src_dir)]
    for src_path in src_paths:
        print(src_path)
        src_filename = os.path.basename(src_path)
        src_filename_no_ext = os.path.splitext(src_filename)[0] #去掉了扩展名的文件名
        src_filename_no_ext = src_filename_no_ext.rstrip(name_trip) #rstrip去掉右边的，lstrip去掉左边的
        print(src_filename_no_ext)
        src_new_name = src_filename_no_ext + new_name_att
        print(src_new_name)
        os.rename(src_path,os.path.join(src_dir,src_new_name))   #重命名
    print('ok')
