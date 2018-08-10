---
layout: post
title: halcon ocr字符识别与训练
categories: Tutorial
tags: Halcon Text_Recognition
author: zhuwei
description: 使用halcon实现字符识别与训练
---

                            
&emsp;&emsp;训练图片：
				![](/assets/images/halcon_test_image.png)
       		
识别结果：
			![](/assets/images/halcon_ocr_result.png)			
            
&emsp;&emsp;训练代码：				

    *读取图片
    read_image (Image, 'D:/github/CodeRecognition/test.png')
    *反转图片，使前景为白色，便于处理
    invert_image (Image, ImageInvert)
    *使用阈值分割，提取前景
    threshold (ImageInvert, Region, 128, 255)
    *计算连通域
    connection (Region, ConnectedRegions)
    *选择符合要求的区域，即字符
    select_shape (ConnectedRegions, SelectedRegions, 'area', 'and', 150, 99999)
    *排序
    sort_region (SelectedRegions, SortedRegions, 'first_point', 'true', 'column')
    *训练****************
    *计算字符个数
    count_obj (SortedRegions, Number)
    *创建训练文件******
    *标签
    words:=['2','0','1','7']
    TrainFile:='D:/github/CodeRecognition/testWords.trf'
    dev_set_check('~give_error') 
    delete_file(TrainFile) 
    dev_set_check('~give_error')
    *生成训练文件
    for i:=1 to Number by 1 
        select_obj(SortedRegions, SingleWord, i) 
        append_ocr_trainf(SingleWord,Image,words[i-1],TrainFile) 
    endfor
    *训练ocr
    FontFile:='D:/github/CodeRecognition/testWords.omc'
    *读取训练文件
    read_ocr_trainf_names(TrainFile, CharacterNames, CharacterCount)
    NumHidden:=400
    *自己创建神经网络分类器
    *create_ocr_class_mlp (10, 20, 'constant', 'default', CharacterNames, NumHidden, 'none', 10, 42, OCRHandle)
    *这里采用halcon预训练模型；第二次及以后训练先将文件名改为FontFile，调用已训练的参数继续训练
    read_ocr_class_mlp('HandWritten_0-9.omc', OCRHandle)
    *训练
    trainf_ocr_class_mlp (OCRHandle, TrainFile, 200, 1, 0.01, Error, ErrorLog)
    *保存参数到自己命名的文件
    write_ocr_class_mlp(OCRHandle, FontFile) 
    *释放内存
    clear_ocr_class_mlp(OCRHandle)
    			
&emsp;&emsp;识别代码：				

    read_image (Image, 'D:/github/CodeRecognition/test.png')
    invert_image (Image, ImageInvert)
    threshold (ImageInvert, Region, 128, 255)
    connection (Region, ConnectedRegions)
    select_shape (ConnectedRegions, SelectedRegions, 'area', 'and', 150, 99999)
    sort_region (SelectedRegions, SortedRegions, 'first_point', 'true', 'column')
    *计算每一个字符区域中心
    area_center (SortedRegions, Area, Row, Column)
    FontFile:='D:/github/CodeRecognition/testWords.omc'
    *读取已训练好的参数
    read_ocr_class_mlp(FontFile, OCRHandle)
    *识别
    do_ocr_multi_class_mlp (SortedRegions, Image, OCRHandle, RecNum, Confidence)
    *显示在屏幕上
    set_display_font (3600, 27, 'mono', 'true', 'false')
    for i := 0 to |RecNum| - 1 by 1
        disp_message (3600, RecNum[i], 'image', Row[i],Column[i], 'white', 'false')
    endfor			
