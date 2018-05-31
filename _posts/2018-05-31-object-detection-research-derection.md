---
layout: post
title: 目标检测可能的研究方向
categories: InformalEssay
tags: DeepLearning Detection
author: zhuwei
description: 关于目标检测的一些切入点
---

                            
&emsp;&emsp;此博客主要收集来自[知乎](https://www.zhihu.com/question/64861580)的问答。		

1.提升图像分辨率。 如果不考虑context， CNN能识别出物体大小不应小于20x20 pixels. 			

2.观察目标， 设定合适大小的context， 不宜太小或者太大。			

3.ROI pooling 会引入位置偏差， 物体越小， 偏差越明显。			

4.多引入一些low-level feature map，即做feature fusion。 小物体在高层的feature map上不能被很好表达。			

5.目标较小，建议作者用ROI Align 代替ROI pooling，ROI pooling在小物体上会带来较大误差，可以看看mask rcnn的分析			

6.把gt放大一点，加上上下文context，变相加大object,因为物体太小，上下文信息有助于找得更准			

7.如果对速度要求不高，考虑切图			

8.stride上考虑用一下hypernet(16cvpr)，降为8，速度会比较慢			

9.设置更合理的anchor size，避免出现“田”字，anchor没有覆盖中间的区域			
10.tiny faces, 上采样				

11.如果目标太小的话，不建议用图像检测的方案，试试分割可能效果更好			
12.FPN是否是一个值得尝试的方向？
