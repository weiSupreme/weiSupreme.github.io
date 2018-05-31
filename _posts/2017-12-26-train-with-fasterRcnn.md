---
layer: post
title: 创建VOC2007格式数据集用于训练faster-rcnn
categories:  Tutorial
tags: DeepLearning caffe Detection Faster-rcnn
author: zhuwei
description: 创建自己的数据集
---
&emsp;&emsp;转载：[创建自己的VOC2007格式的数据集](http://weiSupreme.github.io/assets/note/generate-voc2007-for-fasterRcnn.pdf) (the link of original blog [click here](http://blog.csdn.net/sinat_30071459/article/details/50723212))
        
&emsp;&emsp;转载：[用faster-rcnn训练自己的数据集](http://weiSupreme.github.io/assets/note/train-ownData-fasterRcnn.pdf)  (the link of original blog [click here](http://blog.csdn.net/sinat_30071459/article/details/51332084))
       
&emsp;&emsp;[点这里下载用于制作标签的LabeilImage](/assets/note/object_labelImg-master.zip)
       
&emsp;&emsp;[点这里下载用于制作xml文件的工具](/assets/note/tools-for-generate-datastes.zip)
     

问题解决：
&emsp;&emsp;1、修改faster-rcnn默认的图片格式和目标种类![](/assets/note/faster-rcnn-jpg-class.png)

&emsp;&emsp;2、'module' has no attribute 'text_format'![](/assets/note/faster-rcnn-protobuf-txt-format-error.png)

&emsp;&emsp;3、ValueError: total size of new array must be unchanged
![](/assets/note/faster-rcnn-data-odd.png)
      
&emsp;&emsp;4、KeyError: max_overlaps  (IndexError: list index out of range):&emsp;删除data下的2个cache文件夹

