---
layer: post
title: 给文件夹里的图片创建用于caffe的文件列表
categories:  Tutorial
tags: file
author: zhuwei
description: 创建文件名列表
---
&emsp;&emsp;caffe创建自己的数据集时，首先要生成训练和验证用的图片文件名和对应标签的txt文件，train.txt和val.txt,如：52306.jpg 2。下面这个代码就是用于创建这个文件的。  

	#!/usr/bin/env sh
	DATA=path/to/imagenet/2
	MY=data/my_data/2

	echo "Create train.txt..."
	rm -rf $MY/train.txt
	for i in 3 4 5 6 7 
	do
	find $DATA/train/ -name $i*.jpg | cut -d '/' -f 6 | sed "s/$/ $i/">>$MY/train.txt
	done
	echo "Create val.txt..."
	rm -rf $MY/val.txt
	for i in 3 4 5 6 7
	do
	find $DATA/test/ -name $i*.jpg | cut -d '/' -f 6 | sed "s/$/ $i/">>$MY/val.txt
	done
	echo "All done"  

&emsp;&emsp;其中两点需要说明一下，1、：cut -d '/' -f 6，这个命令中，-d表示分隔符，-f表示选取哪个字段，因为find得到的是包含路径的文件名，而我们只需要文件名，所以需要选取特定字段。在我参考的blog中，是 -f4-5，这个是不对的。2、for循环中的3 4 5 6 7表示标签。[原文链接](http://http://www.cnblogs.com/denny402/p/5083300.html)  
