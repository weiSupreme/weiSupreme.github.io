---
layer: post
title: 在caffe框架下使用cifar10例程预测自己的图片
categories:  Tutorial
tags: DeepLearning caffe
author: zhuwei
description: 基于cifar10数据集的图片预测
---
&emsp; 使用caffe/examples/cifar10_full模型进行图片的训练。准备好cifar10分类的图片，任意尺寸都行，将图片和代码存放在cifar10/predict文件夹下，运行代码，即可预测。   
&emsp; 以下是代码：

	import caffe
	import numpy as np
	import cv2

	MODEL_FILE = '../cifar10_full.prototxt'
	PRETRAINED = '../cifar10_full_iter_10000.caffemodel'
	IMAGE_FILE = 'plane1.jpg'

	img = cv2.imread(IMAGE_FILE)
	if img.shape != [32, 32]:
			img2 = cv2.resize(img, (32, 32))
			img = img2.reshape(32, 32, -1)
	else:
			img = img.reshape(32, 32, -1)
	'''        
	img = caffe.io.load_image(IMAGE_FILE)
	img = caffe.io.resize_image(input_image, (32, 32)) * 255.0
	tmp = img
	tmp[:,:,0] = img[:,:,2]
	tmp[:,:,2] = img[:,:,0]
	img = tmp
	'''
	input_image = img
	print input_image.shape
	print input_image

	net = caffe.Net(MODEL_FILE, PRETRAINED, caffe.TEST)
	caffe.set_mode_cpu()
	res = net.forward_all(data = np.asarray([input_image.transpose(2, 0, 1)]))
	prediction = res['prob'][0]
	label = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'}
	print prediction
	print 'predicted class:', label[prediction.argmax()]

&emsp;有几点要注意一下：   
&emsp;1、caffe模型使用的彩色图片的通道是BGR，而python得到的图像是RGB，需要手动进行通道转换。opencv读出的数据直接就是BGR的，不需要自己进行转换。   
&emsp;2、此模型使用的数据范围是0-255，而caffe.io.load_image得到的是0-1，需要进行转换（io.py中说明了），opencv得到的数据就是0-255的，不需要再进行转换  &emsp;以上两点可以与前面的手写数字识别的代码比较一下，尤其是数据的值域。