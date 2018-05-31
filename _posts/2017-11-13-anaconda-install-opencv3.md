---
layer: post
title: anaconda 安装opencv3
categories:  Tutorial
tags: opencv
author: zhuwei
description: 安装opencv
---
　　安装好opencv3.2，anacaonda, caffe后，发现不能使用opencv, import cv2失败，应该是由于安装caffe后修改了路径，于是用anaconda重新安装了opencv3,解决了不能导入的问题。   
　　打开终端，执行命令：   
 ```
　　　　conda install --channel https://conda.anaconda.org/menpo opencv3
```

　　验证：
  
		python　　　
		import cv2
		
　　应该不会报错了