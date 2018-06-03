---
layout: post
title: 基于深度学习目标检测算法faster-rcnn的行人检测系统
categories: Paper
tags: DeepLearning Detection Faster-rcnn
author: zhuwei
description: “A Faster RCNN-based Pedestrian Detection System”
---
# 论文组织结构       
## 摘要       
&emsp;&emsp;行人检测系统在自动驾驶中的应用。提出基于faster-rcnn的检测系统。说明实验结果。		
## 1. 介绍		
&emsp;&emsp;1. 研究背景、现状。现有方法的不足。2. 基于深度学习的检测研究方法，ImageNet、VOC。3. 简要介绍本文提出的算法（系统）。		
## 2. 相关工作		
&emsp;&emsp;1. 介绍现有的行人检测方法。2. 介绍基于CNN的模型。		
## 3. 行人检测系统		
### A. 模型概览： first stage, second stage, finally		
### B. 区域建议方法： 详细介绍了RPN		
### C. fast-rcnn： 介绍了ROI		
### D. detection tuning		
##  4. 实验结果		
&emsp;&emsp;1. Caltech Pedestrian Dataset. 2. 实施细节，四个训练阶段。3. 结果比较：与其他方法的错误率比较。4. 精度和效率分析。	  
## 5. 结论		
&emsp;&emsp;总结。		
# 主要算法		
&emsp;&emsp;faster-rcnn的一个具体应用。		
# 重要参考文献		
1. C. Szegedy et al., “Going deeper with convolutions,” in Proc. IEEE
Conf. on Computer Vision and Pattern Recognition, Boston, MA, Jun.
2015, pp. 1–9.		
2. K. He, Y. Zhang, S. Ren, and J. Sun, “Spatial pyramid pooling in
deep convolutional networks for visual recognition,” IEEE Trans. Pattern
Anal. Mach. Intell., vol. 37, no. 9, pp. 1904–1916, Sep. 2015.		

# 重要语句		
1. The system achieves good
performance and is faster than the well known and frequently
used methods in the literature.		

2. It will be
shown that PedFasterRCNN achieves good results compared
with state-of-the-art methods and is faster than these methods,
which makes it very suitable for real-time applications.		

3. The remainder of this paper is organized as follows. Section
2 provides a review of the related work on pedestrian detection.
Section 3 describes the proposed pedestrian detection system.
Some experimental results are given in Section 4, and finally
Section 5 provides a summary of the paper and possibilities
for future improvements.		


[论文原文](https://pan.baidu.com/s/1fH3WyIgS9R5O4JFq-iim4g)