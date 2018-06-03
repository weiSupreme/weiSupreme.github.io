---
layout: post
title: 基于深度学习的rcnn用于小目标检测的一些改进
categories: Paper
tags: DeepLearning Detection Faster-rcnn
author: zhuwei
description: “R-CNN for Small Object Detection”
---
# 论文组织结构       
## 摘要       
&emsp;&emsp;说明现有检测方法的不足：难以检测小目标。提出本文的算法：a context model and a small region proposal generator.		
## 1. 介绍		
&emsp;&emsp;介绍现有方法的不足以及小目标检测的困难。提出算法。1.1 现有方法、数据集准备。1.2 贡献。		
## 2. 小物体数据集		
&emsp;&emsp;介绍自己的小物体数据集。从coco和SUN数据集中选取较小的物体的类，如鼠标、电话等。		
## 3. rcnn		
&emsp;&emsp;介绍rcnn。		
### 3.1 生成小的proposal。		
&emsp;&emsp;存在的问题：rpn生成的anchors太大。选用小的anchors：16,40,100.把rpn网络接到conv4_3之后。		
### 3.2 上采样		
### 3.3 上下文		
&emsp;&emsp;
##  4. 实验设计和结果		
&emsp;&emsp;
## 5. 结论		
&emsp;&emsp;
# 主要算法		
&emsp;&emsp;
# 重要参考文献		

# 重要语句		


[论文原文](https://pan.baidu.com/s/1fH3WyIgS9R5O4JFq-iim4g)