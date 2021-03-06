---
layer: post
title: 在caffe框架下进行手写数字的预测，mnist
categories: Tutorial
tags: DeepLearning caffe
author: zhuwei
description: mnist数据集使用及预测
---
　　本文主要讲解如何用caffe已训练好的模型进行手写数字的预测。准备：1、数字图片。任意尺寸，可以是彩色，也可以是灰度的。如果是灰度的，把下面代码里的彩色转灰度的代码去掉就行。2、已训练好的模型。例如：lenet_iter_10000.caffemodel
  
　　预测的步骤比较简单，主要是读取图片、构建网络、前向传播。其中最关键的就是读取图片了。一开始我使用的caffe进行读取图片：caffe.io.load_image(),但是预测结果都是错的，目前还没有发现是什么原因引起的。改用opencv进行读取就对了。代码是根据github上一个例程修改的，这是源代码的链接：[caffe-mnist-test](http://github.com/9crk/caffe-mnist-test)
  
　　下面直接给出代码：
  
        #predict.py
        import os
        import caffe
        import numpy as np
        import cv2
		
        caffe_root = caffe_dir（替换自己的Caffe根目录）

        MODEL_FILE = caffe_root+'examples/mnist/lenet.prototxt'
        PRETRAINED = caffe_root+'examples/mnist/lenet_iter_10000.caffemodel'
        IMAGE_FILE = caffe_root+'examples/mnist/test/8.bmp'

        img = cv2.imread(IMAGE_FILE)
        if img.shape != [28, 28]:
                img2 = cv2.resize(img, (28, 28))
                img = img2.reshape(28, 28, -1)
        else:
                img = img.reshape(28, 28, -1)
        input_image = 1.0 - img / 255.0
        
        print input_image.shape
        print input_image
        input_image = np.dot(input_image, np.transpose([0.3, 0.59, 0.11]))（如果原图是灰度图片，则不需要这步）
        input_image = input_image[:,:,np.newaxis]（如果读取的数据尺寸就是[28,28,1],则不需要此步骤）

        #img = caffe.io.load_image(IMAGE_FILE, color=False)
        net = caffe.Net(MODEL_FILE, PRETRAINED, caffe.TEST)
        caffe.set_mode_cpu()
        res = net.forward_all(data = np.asarray([input_image.transpose(2, 0, 1)]))
        prediction = res['prob'][0]
        print 'predicted class:', prediction.argmax()
		
　　执行以下命令进行预测：
  
	    cd caffe_root
	    python predict.py
	
　　路径都对的话，就会输出正确的预测分类了。
  
　　很庆幸，找到问题根源了。原来caffe.io.load_image()读取到的图片数据0代表黑色，255(1）代表白色，而进行预测的时候，必须反过来，0表示白色，1表示黑色，前面代码中的1-img/255正是这个原因。
