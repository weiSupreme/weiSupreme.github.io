---
layout: post
title: 改变faster-rcnn中的anchors数量和尺寸
categories: Tutorial
tags: DeepLearning Detection Faster-rcnn
author: zhuwei
description: 改变faster-rcnn中的anchors数量和尺寸
---
&emsp;&emsp;我们使用faster-rcnn时，可能需要根据我们自己检测的目标来定制rpn的anchors的尺寸和数量，本篇文章详细介绍了改变anchors的尺寸和数量的过程。     
# anchors参数介绍     
&emsp;&emsp;anchor主要有三个参数： base_size, ratios, scales. 其中base_size是anchor的基本尺寸；ratios决定anchor的长宽比，但不改变面积；scales是放大比例，同时放大或缩小长和宽。修改anchors，也就是修改这三个参数。至于修改成什么样，看自己实际的情况。如果不明白这三个参数的作用，请自行百度。。。    
# 修改参数    
## 三个layers文件    
### lib/rpn/generate_anchors.py    
&emsp;&emsp;在这个文件中，我们关注generate_anchors函数，函数定义中设定了以上三个参数的默认值，我们通过修改这三个默认值，就可以修改anchors的数量和尺寸了。*需要注意的是，如果是修改base_size，除了在这个文件中修改，可能还要在lib/fast_rcnn/config.py中修改anchors的最小尺寸, RPN_MIN_SIZE；如果修改ratios，只在这个文件中修改就可以了；如果修改scales，除了这个文件，还要在另外两个文件中修改。*     
### lib/rpn/anchor_target_layer.py, proposal_layer     
&emsp;&emsp;在这两个文件中，在setup函数里找到这个语句：anchor_scales = layer_params.get('scales', (8, 16， 32))，把scales改成和generate_anchors里的scales一样就可以了。    
		
        如果修改了anchors数量，还需要改下面六个网络定义文件      
        
## 网络定义文件（.prototxt、.pt文件）    
### 四个训练阶段的网络定义文件（models/pascal_voc/ZF/，*train.pt)      
&emsp;&emsp;这四个文件中，修改与rpn有关的层的参数。1. rpn_cls_score层中，num_output=anchors数量x2；2.rpn_bbox_pred层中，num_output=anchors数量x4。     
### 两个测试阶段的网络定义文件（models/pascal_voc/ZF/，*test.pt）     
&emsp;&emsp;在这两个文件中，有三个地方要修改。1. rpn_cls_score层中，num_output=anchors数量x2；2.rpn_bbox_pred层中，num_output=anchors数量x4；3.rpn_cls_prob_reshape层中，reshape_param { shape { dim: 0 dim: 18 dim: -1 dim: 0 } }第二个dim后的参数为anchors数量x2，对应修改。    

		以上就是整个的修改过程了。
