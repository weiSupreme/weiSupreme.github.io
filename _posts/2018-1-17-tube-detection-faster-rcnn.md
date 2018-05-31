---
layout: post
title: 基于faster-rcnn的纸管缺陷检测
categories: Paper
tags: DeepLearning Detection Faster-rcnn
author: zhuwei
description: “A Faster-RCNN Based Chemical Fiber Paper Tube Defect Detection Method”
---
# 论文组织结构       
## 摘要       
&emsp;&emsp;简要介绍了相关问题研究现状，本文的主要工作以及实验结果,给出结论。		
## 1. 介绍		
&emsp;&emsp;介绍论文背景，介绍相关缺陷检测算法，阐述他们的优缺点。引出论文主题：纸管缺陷检测。介绍CNN，提出基于faster-rcnn的检测方法。	 
## 2. 图像采集系统		
&emsp;&emsp;主要介绍图像采集和检测系统。		
## 3. 缺陷检测方法		
&emsp;&emsp;介绍了现有方法存在的不足以及faster-rcnn的优势。	   
### A. regiion proposal network： 介绍faster-rcnn的区域建议网络。		
### B. The Struct of Faster-RCNN： 介绍faster-rcnn的结构		
##  4. 实验设计和结果		
### A. 检测数据集		
&emsp;&emsp;介绍数据集以及检测的难点。		
### B. 实验结果		
&emsp;&emsp;1. 基于faster-rcnn的实验结果，包括训练时间、准确率以及召回率。2. 与传统方法的实验结果进行比较：SIFT特征、SVM分类器。论述优缺点。		
## 5. 结论		
&emsp;&emsp;本文算法的优势以及不足和需要改进的地方。		
# 主要算法		
&emsp;&emsp;使用faster-rcnn进行了纸管缺陷检测，并与传统方法进行了比较。没有对算法提出改进，是对faster-rcnn的一个具体应用。		
# 重要参考文献		
1. D. Eigen, J. Rolfe, R. Fergus. Understanding deep architectures using a
recursive convolutional network[R]. arXiv:1312.1847v2, 2014		
2. Girshick R, Donahue J, Darrell T, et al. Region-Based Convolutional
Networks for Accurate Object Detection and Segmentation[J]. IEEE
Transactions on Pattern Analysis & Machine Intelligence, 2016,
38(1):142-158.		

# 重要语句		

1. However, in the process of the paper tube
production, due to the production-level, the scene environmentand other factors, it is easy to make the surface scratches, holes,joints and other defects.		

2. With the development of deep learning in recent years, people have found a way to let the computer simulate the
human brain to perceive the visual signal mechanism, and then design a deep network to achieve the visual function.		
3. In this paper, a quick defect detection method is designed
and implemented.	  

4. These methods have proven their effectiveness in
long-term applications, but still have a lot of breakthrough
space, there are several shortcomings:		

5. However, Faster-RCNN method also has somgthing
insufficient that need to be improved in future studies.		

[论文原文](/assets/paper/A Faster-RCNNBasedChemicalFiberPaperTubeDefectDetectionMethod.pdf)