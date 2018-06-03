---
layout: post
title: 阅读过的几篇目标检测论文小记
categories: Paper
tags: DeepLearning Detection
author: zhuwei
description: 几篇目标检测方面的论文的阅读收获
---

&emsp;&emsp;1、[Improve object detection via a multi-feature and multi-task CNN model](https://pan.baidu.com/s/1fH3WyIgS9R5O4JFq-iim4g)  
主要贡献：多特征（多个卷积层作为ROI）、多任务（检测、分割）以及定义新的重叠损失函数，提高了小目标检测精度，在voc数据集上测试。        
&emsp;&emsp;2、[Graphic logo detection with deep region-based convolutional networks](https://pan.baidu.com/s/1fH3WyIgS9R5O4JFq-iim4g)   
主要贡献：a.数据集：[FlickrLogo-32 dataset](http://www.multimedia-computing.de/flickrlogos/)   b.组合不同的CNN模型和fast rcnn，并使用了迁移学习   c.使用K-means方法对训练数据进行聚类，设置超参数。  d.改变fast rcnn参数：anchor scales, ratios  
       	
&emsp;&emsp;2、[Forward Vehicle Detection Based on Incremental Learning and Fast R-CNN](https://pan.baidu.com/s/1fH3WyIgS9R5O4JFq-iim4g)   
主要贡献：a.数据集：[ KITTI dataset](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d)  b.训练模型：fast rcnn与不同的cnn模型         
&emsp;&emsp;3、[CityPersons-A Diverse Dataset for Pedestrian Detection](https://pan.baidu.com/s/1fH3WyIgS9R5O4JFq-iim4g)    
主要贡献：数据集：[CityPerson](https://bitbucket.org/shanshanzhang/citypersons)