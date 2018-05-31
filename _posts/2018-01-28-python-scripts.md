---
layout: post
title: python代码
categories: Material
tags: Python
author: zhuwei
description: 深度学习做检测时用到的一些制作数据集的python文件（代码）
---

### 1、图像增强（对颜色分量进行处理）		

			import os
			import cv2
			import numpy as np

			dir = r"JPEGImages/"
			list = os.listdir(dir)
			cnt =0

			for i in range(0, len(list)):
				print(list[i])
				img = cv2.imread(dir+list[i])
				img_tmp = img.copy()
				img2 = img.copy()
				img_tmp = img_tmp.dot((0.05, 0.35, 0.6))
				#print(img_tmp.shape)
				img[:,:,0] = img_tmp
				#img[:,:,1] = img_tmp
				#img[:,:,2] = img_tmp
				#print(img.shape)
				#cv2.imshow('img', img)
				#cv2.imshow('aug', img2)
				#cv2.waitKey(0)
				cv2.imwrite(r"aug/"+list[i], img)
				cnt = cnt + 1
			print(cnt)
    		
			
### 2、生成标签文件。将csv格式的文件存储的标签数据转换为固定格式的txt文件或者将数据处理后写入到新的csv格式文件		

			import csv
			import os

			dir = r"test-annotations-csv/"
			list = os.listdir(dir)

			flag = 0
			category = 'apple'
			top_left_x = 0
			top_left_y = 0
			bottom_right_x = 0
			bottom_right_y = 0

			txt = open("label.txt", 'w')

			for i in range(0,len(list)):  #len(list)
				img_file_name = list[i].rstrip('.csv') + '.png'
				print(img_file_name)
				path = os.path.join(dir,list[i])
				new_csv = open(r'aug_label_csv_test/'+list[i], 'w', newline='')
				writer = csv.writer(new_csv)
				writer.writerow(['#item', 'c-x', 'c-y', 'radius', 'label'])
				if os.path.isfile(path):
					out = open(path,'r')
					read_csv = csv.reader(out,dialect='excel')
					for line in read_csv:     #循环输出csv中的所有数据
						if flag == 0:
							flag = flag + 1
							continue
						flag = flag + 1
						#print(line)
						if line[4] == '1':
							category = 'apple'
							top_left_x = (int)(float(line[1]) + float(line[3])) if (int)(float(line[1]) + float(line[3])) < 307 else 307
							top_left_x = 308 - top_left_x
							top_left_y = (int)(float(line[2]) - float(line[3])) if (int)(float(line[2]) - float(line[3])) > 1 else 1
							bottom_right_x = (int)(float(line[1]) - float(line[3])) if (int)(float(line[1]) - float(line[3])) > 0 else 0
							bottom_right_x = 308 - bottom_right_x
							bottom_right_y = (int)(float(line[2]) + float(line[3])) if (int)(float(line[2]) + float(line[3])) < 202 else 202
							write_str = img_file_name + ' ' + category + ' ' + str(top_left_x) +' ' + str(top_left_y) + ' ' + str(bottom_right_x) + ' ' + str(bottom_right_y) + '\n'
							txt.write(write_str)
							c_x = float((top_left_x+bottom_right_x)/2)
							c_y = float((top_left_y+bottom_right_y)/2)
							radius = float((bottom_right_x+bottom_right_y-top_left_x-top_left_y)/4)
							writer.writerow([str(flag-2), str(c_x), str(c_y), str(radius), '1'])
					#print(flag)
					if flag == 1:
						print("no apples")
						os.exit()
					flag = 0
					out.close()
				new_csv.close()
			txt.close() 
			print(len(list))			
			
### 3、图像增强（水平翻转）		
			import os
			import cv2

			dir = r"test_images/"
			list = os.listdir(dir)
			cnt = 0

			for i in range(0,len(list)):  #len(list)
				img_file_name = list[i]
				print(img_file_name)
				img = cv2.imread(dir+img_file_name)
				new_img = cv2.flip(img, 1)
				cv2.imwrite(r"aug_images_test/"+img_file_name, new_img)
				cnt += 1
			print('all ', cnt)			
			
### 4、计算一幅图像三个颜色通道各自的平均值			

			import cv2
			import os
			import numpy as np

			dir = r'JPEGImages/'
			list = os.listdir(dir)

			R_sum = 0
			G_sum = 0
			B_sum = 0
			im_num = 0

			for im_name in list:
				im_num += 1
				img = cv2.imread(dir+im_name)
				imgr = img[:,:,2]
				imgg = img[:,:,1]
				imgb = img[:,:,0]
				R_sum += np.sum(imgr) / 308 / 202
				G_sum += np.sum(imgg) / 308 / 202
				B_sum += np.sum(imgb) / 308 / 202
				#print R_sum, G_sum, B_sum
			R_sum /= im_num
			G_sum /= im_num
			B_sum /= im_num
			print R_sum, G_sum, B_sum			
			
### 5、根据csv文件的标签数据在原图上画出标定框			
			
			import csv
			import os
			from PIL import Image, ImageDraw

			source_dir = r'apple/'
			dest_dir = r'apple-gt/'

			list = os.listdir(source_dir)
			for file_name in list:
				print file_name
				file_name_no_ext = file_name.rstrip('.png')
				img = Image.open(source_dir+file_name)
				draw = ImageDraw.Draw(img)
				csv_out = open(r'test-annotations-csv/'+file_name_no_ext+'.csv', 'r')
				read_csv = csv.reader(csv_out, dialect='excel')
				csv_line_num = 0
				for line in read_csv:
					if csv_line_num == 0:
						csv_line_num += 1
						continue
					xminT = (int)(float(line[1]) - float(line[3])) if (int)(float(line[1]) - float(line[3])) > 1 else 1
					yminT = (int)(float(line[2]) - float(line[3])) if (int)(float(line[2]) - float(line[3])) > 1 else 1
					xmaxT = (int)(float(line[1]) + float(line[3])) if (int)(float(line[1]) + float(line[3])) < 308 else 308
					ymaxT = (int)(float(line[2]) + float(line[3])) if (int)(float(line[2]) + float(line[3])) < 202 else 202
					draw.rectangle([xminT, yminT, xmaxT, ymaxT], outline=(0, 0, 255))
				csv_out.close()
				img.save(dest_dir+file_name)			
			
### 6、根据txt文件（保存了文件名）批量复制文件			
				
			import os
			import shutil

			dir = r'test-annotations-csv/'
			txt = open(r'ImageSets/Main/test.txt')
			lines = txt.readlines()
			for line in lines:
				line = line.strip('\r\n') + '.csv'
				print(line)
				shutil.copyfile(r'annotations-csv/'+line, dir + line)
			txt.close()			
			
### 7、随机读取txt文件中的若干行			
			
			import random
			import linecache
			import shutil

			txt = open("random-select/label.txt", 'w')
			resultList=random.sample(range(0,789),150)
			for i in range(0, 150):
				theline = linecache.getline(r'ImageSets/Main/train.txt', resultList[i]).strip('\n')
				print(theline)
				txt.write(theline+'\n')
				shutil.copyfile(r'Annotations/'+theline+'.xml', r"random-select/Annotations/"+theline+'.xml')
				shutil.copyfile(r"JPEGImages/"+theline+'.png', r"random-select/JPEGImages/"+theline+'.png')
			txt.close()			
			
### 8、读取txt文件			
			
			import os

			txt = open(r'test.txt')
			new_txt = open(r'test1.txt', 'w')
			lines = txt.readlines()
			#print lines.strip('\n')
			for line2 in lines:
				new_txt.write(line2.strip('\r\n')+'\n')
			txt.close()
			new_txt.close()			
			
### 9、读取csv文件			
			
			import csv
			import os
			import shutil


			dir = r"annotations-csv/"
			list = os.listdir(dir)

			flag = 0

			for i in range(0,len(list)):  #len(list)
				file_name_no_ext = list[i].rstrip('.csv')
				print(file_name_no_ext)
				path = os.path.join(dir,list[i])
				if os.path.isfile(path):
					out = open(path,'r')
					read_csv = csv.reader(out,dialect='excel')
					for line in read_csv:     #循环输出csv中的所有数据
						if flag == 0:
							flag = flag + 1
							continue
						flag = flag + 1
					if flag > 1:
						shutil.copyfile(path, r"all-have-apples/annotations-csv/"+file_name_no_ext+'.csv')
						shutil.copyfile(r"images/"+file_name_no_ext+'.png', r"all-have-apples/images/"+file_name_no_ext+'.png')
					flag = 0
					out.close()
			print(len(list))			
			
### 9、文件批量重命名（000001.*）			
			
			import os

			for i in range(1870 * 1 + 1, 1870 * 2 + 1):
				index = str(i).zfill(6)
				os.rename('camera4/period14_camera4/%d.png' % i, 'camera4/period14_camera4/%s.png' % index)   #重命名
			print('ok')
			#        print file.split('.')[-1]			
			
### 10、除去txt文件中的空行			
			
			import sys  

			f=open('tmp.txt', 'r')  
			fnew=open('_new.txt','w') #将结果存入新的文本中 
			lines =  f.readlines()
			for line in lines:   #对每一行先删除空格，\n等无用的字符，再检查此行是否长度为0  
				#print(":"+line)
				if line.strip():   
					fnew.write(line) 
			print('ok')
			f.close()  
			fnew.close() 			
			
### 11、opencv提取前景			
			
			import numpy as np
			import cv2

			#cap = cv2.VideoCapture('Video_001.avi')
			#cap = cv2.VideoCapture(0)
			kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
			fgbg = cv2.createBackgroundSubtractorMOG2(False)
			cv2.namedWindow("sourceImg")
			cv2.namedWindow("fgmask")
			count = 0
			for i in range(1, 23):
				frame = cv2.imread("ball_annotated/camera1_20080409T183943+02_frame%d.png" % (i))
				#ret, frame = cap.read()
				fgmask = fgbg.apply(frame)
				fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
				cv2.imshow('sourceImg', frame)
				cv2.imshow('fgmask', fgmask)
				#count = i % 10
				#if not count:
				cv2.imwrite("2.fg/camera1_20080409T183943+02_frame%d_fg.png" % (i), fgmask)
				k = cv2.waitKey(100) & 0xff
				#if k == 27:
					#break
			#cap.release()
			cv2.destroyAllWindows()			
			
### 12、xml文件转换成txt文件			
			
			#!/usr/bin/evn python
			# coding:utf-8
			import os

			try:
				import xml.etree.cElementTree as ET
			except ImportError:
				import xml.etree.ElementTree as ET
			import sys

			xml_dir = r"D:\Python\PythonProjects\333_xml"
			xml_paths = [os.path.join(xml_dir, f) for f in os.listdir(xml_dir) if
							 os.path.isfile(os.path.join(xml_dir, f)) and f.endswith(".xml")]

			strTemp = ''  # 将txt文件清空
			with open(os.path.join(xml_dir, "mytxt.txt"), "w") as f:
				f.write(str(strTemp))

			for xml_path in xml_paths:
				f = xml_path
				tree = ET.parse(f)  # 打开xml文档
				root = tree.getroot()  # 获得root节点
				print
				"*" * 10
				filename = root.find('filename').text
				#filename = filename[:-4]
				print
				filename

				########################################
				for size in root.findall('size'):  # 找到root节点下的size节点
					width = size.find('width').text  # 子节点下节点width的值
					height = size.find('height').text  # 子节点下节点height的值
					print
					width, height
				########################################

				for object in root.findall('object'):  # 找到root节点下的所有object节点
					name = object.find('name').text  # 子节点下节点name的值
					print
					name
					bndbox = object.find('bndbox')  # 子节点下属性bndbox的值
					xmin = bndbox.find('xmin').text
					ymin = bndbox.find('ymin').text
					xmax = bndbox.find('xmax').text
					ymax = bndbox.find('ymax').text
					print
					xmin, ymin, xmax, ymax

				strTemp=filename+'.png '+'basketball'+' '+str(xmin)+' '+str(ymin)+' '+str(xmax)+' '+str(ymax)+'\n'

				with open(os.path.join(xml_dir, "mytxt.txt"), "a") as f:
					f.write(str(strTemp))			
					
### 13、图像数据增强方法			
		
			# -*- coding:utf-8 -*-  
			"""数据增强 
			   1. 翻转变换 flip 
			   2. 随机修剪 random crop 
			   3. 色彩抖动 color jittering 
			   4. 平移变换 shift 
			   5. 尺度变换 scale 
			   6. 对比度变换 contrast 
			   7. 噪声扰动 noise 
			   8. 旋转变换/反射变换 Rotation/reflection 
			   author: XiJun.Gong 
			   date:2016-11-29 
			"""  

			from PIL import Image, ImageEnhance, ImageOps, ImageFile  
			import numpy as np  
			import random  
			import threading, os, time  
			import logging  
			import cv2  
			logger = logging.getLogger(__name__)  
			ImageFile.LOAD_TRUNCATED_IMAGES = True  


			class DataAugmentation:  
				""" 
				包含数据增强的八种方式 
				"""  


				def __init__(self):  
					pass  

				@staticmethod  
				def openImage(image):  
					return Image.open(image, mode="r")  

				@staticmethod  
				def randomRotation(image, mode=Image.BICUBIC):  
					""" 
					 对图像进行随机任意角度(0~360度)旋转 
					:param mode 邻近插值,双线性插值,双三次B样条插值(default) 
					:param image PIL的图像image 
					:return: 旋转转之后的图像 
					"""  
					random_angle = np.random.randint(1, 360)  
					return image.rotate(random_angle, mode)  
					#return image.rotate(180, mode)  

				@staticmethod  
				def randomFlip(image):  
					#图像翻转（类似于镜像，镜子中的自己）  
					#FLIP_LEFT_RIGHT,左右翻转  
					#FLIP_TOP_BOTTOM,上下翻转  
					#ROTATE_90, ROTATE_180, or ROTATE_270.按照角度进行旋转，与randomRotate()功能类似  
					return image.transpose(Image.FLIP_LEFT_RIGHT)  

				@staticmethod  
				def Tranform(image):  
					#t图像变换  
					#im.transform(size, method, data) ⇒ image  

					#im.transform(size, method, data, filter) ⇒ image  
					#1：image.transform((300,300), Image.EXTENT, (0, 0, 300, 300))   
					#   变量data为指定输入图像中两个坐标点的4元组(x0,y0,x1,y1)。  
					#   输出图像为这两个坐标点之间像素的采样结果。  
					#   例如，如果输入图像的(x0,y0)为输出图像的（0，0）点，(x1,y1)则与变量size一样。  
					#   这个方法可以用于在当前图像中裁剪，放大，缩小或者镜像一个任意的长方形。  
					#   它比方法crop()稍慢，但是与resize操作一样快。  
					#2：image.transform((300,300), Image.AFFINE, (1, 2,3, 2, 1,4))  
					#   变量data是一个6元组(a,b,c,d,e,f)，包含一个仿射变换矩阵的第一个两行。  
					#   输出图像中的每一个像素（x，y），新值由输入图像的位置（ax+by+c, dx+ey+f）的像素产生，  
					#   使用最接近的像素进行近似。这个方法用于原始图像的缩放、转换、旋转和裁剪。  
					#3: image.transform((300,300), Image.QUAD, (0,0,0,500,600,500,600,0))  
					#   变量data是一个8元组(x0,y0,x1,y1,x2,y2,x3,y3)，它包括源四边形的左上，左下，右下和右上四个角。  
					#4: image.transform((300,300), Image.MESH, ())  
					#   与QUAD类似，但是变量data是目标长方形和对应源四边形的list。  
					#5: image.transform((300,300), Image.PERSPECTIVE, (1,2,3,2,1,6,1,2))  
					#   变量data是一个8元组(a,b,c,d,e,f,g,h)，包括一个透视变换的系数。  
					#   对于输出图像中的每个像素点，新的值来自于输入图像的位置的(a x + b y + c)/(g x + h y + 1),  
					#   (d x+ e y + f)/(g x + h y + 1)像素，使用最接近的像素进行近似。  
					#   这个方法用于原始图像的2D透视。  
					return image.transform((300,300), Image.EXTENT, (0, 0, 300, 300))  

				@staticmethod  
				def randomCrop(image):  
					""" 
					对图像随意剪切,考虑到图像大小范围(68,68),使用一个一个大于(36*36)的窗口进行截图 
					:param image: PIL的图像image 
					:return: 剪切之后的图像 

					"""  
					image_width = image.size[0]  
					image_height = image.size[1]  
					crop_win_size = np.random.randint(40, 68)  
					random_region = (  
						(image_width - crop_win_size) >> 1, (image_height - crop_win_size) >> 1, (image_width + crop_win_size) >> 1,  
						(image_height + crop_win_size) >> 1)  
					return image.crop(random_region)  

				@staticmethod  
				def randomColor(image):  
					""" 
					对图像进行颜色抖动 
					:param image: PIL的图像image 
					:return: 有颜色色差的图像image 
					"""  
					random_factor = np.random.randint(0, 31) / 10.  # 随机因子  
					color_image = ImageEnhance.Color(image).enhance(random_factor)  # 调整图像的饱和度  
					random_factor = np.random.randint(10, 21) / 10.  # 随机因子  
					brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor)  # 调整图像的亮度  
					random_factor = np.random.randint(10, 21) / 10.  # 随机因1子  
					contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor)  # 调整图像对比度  
					random_factor = np.random.randint(0, 31) / 10.  # 随机因子  
					return ImageEnhance.Sharpness(contrast_image).enhance(random_factor)  # 调整图像锐度  

				@staticmethod  
				def randomGaussian(image, mean=0.2, sigma=0.3):  
					""" 
					 对图像进行高斯噪声处理 
					:param image: 
					:return: 
					"""  

					def gaussianNoisy(im, mean=0.2, sigma=0.3):  
						""" 
						对图像做高斯噪音处理 
						:param im: 单通道图像 
						:param mean: 偏移量 
						:param sigma: 标准差 
						:return: 
						"""  
						for _i in range(len(im)):  
							im[_i] += random.gauss(mean, sigma)  
						return im  

					# 将图像转化成数组  
					img = np.asarray(image)  
					img.flags.writeable = True  # 将数组改为读写模式  
					width, height = img.shape[:2]  
					img_r = gaussianNoisy(img[:, :, 0].flatten(), mean, sigma)  
					img_g = gaussianNoisy(img[:, :, 1].flatten(), mean, sigma)  
					img_b = gaussianNoisy(img[:, :, 2].flatten(), mean, sigma)  
					img[:, :, 0] = img_r.reshape([width, height])  
					img[:, :, 1] = img_g.reshape([width, height])  
					img[:, :, 2] = img_b.reshape([width, height])  
					return Image.fromarray(np.uint8(img))  

				@staticmethod  
				def saveImage(image, path):  
					image.save(path)  


			def makeDir(path):  
				try:  
					if not os.path.exists(path):  
						if not os.path.isfile(path):  
							# os.mkdir(path)  
							os.makedirs(path)  
						return 0  
					else:  
						return 1  
				except Exception, e:  
					print str(e)  
					return -2  


			def imageOps(func_name, image, des_path, file_name, times=5):  
				#funcMap = {"randomRotation": DataAugmentation.randomRotation,  
				#           "randomCrop": DataAugmentation.randomCrop,  
				#           "randomColor": DataAugmentation.randomColor,  
				#           "randomGaussian": DataAugmentation.randomGaussian  
				#           "randomFlip":DataAugmentation.randomFlip,  
				#           }  
				funcMap = {  
						   "Tranform":DataAugmentation.Tranform  
						   }  
				if funcMap.get(func_name) is None:  
					logger.error("%s is not exist", func_name)  
					return -1  

				for _i in range(0, times, 1):  
					new_image = funcMap[func_name](image)  
					DataAugmentation.saveImage(new_image, os.path.join(des_path, func_name + str(_i) + file_name))  


			#opsList = {"randomFlip","randomRotation", "randomCrop", "randomColor", "randomGaussian"}  
			opsList = { "Tranform"}  

			def threadOPS(path, new_path):  
				""" 
				多线程处理事务 
				:param src_path: 资源文件 
				:param des_path: 目的地文件 
				:return: 
				"""  
				if os.path.isdir(path):  
					img_names = os.listdir(path)  
				else:  
					img_names = [path]  
				for img_name in img_names:  
					print img_name  
					tmp_img_name = os.path.join(path, img_name)  
					if os.path.isdir(tmp_img_name):  
						if makeDir(os.path.join(new_path, img_name)) != -1:  
							threadOPS(tmp_img_name, os.path.join(new_path, img_name))  
						else:  
							print 'create new dir failure'  
							return -1  
							# os.removedirs(tmp_img_name)  
					elif tmp_img_name.split('.')[1] != "DS_Store":  
						# 读取文件并进行操作  
						image = DataAugmentation.openImage(tmp_img_name)  
						threadImage = [0] * 5  
						_index = 0  
						for ops_name in opsList:  
							threadImage[_index] = threading.Thread(target=imageOps,  
																   args=(ops_name, image, new_path, img_name,))  
							threadImage[_index].start()  
							_index += 1  
							time.sleep(0.2)  


			if __name__ == '__main__':  
				threadOPS("D:\datasets\dataArgument\JPEGImages",  
						  "D:\datasets\dataArgument\Dealed_JPEGImages")  		
						  
### 14、从一个VOC数据集创建多个训练子集（只改变训练样本的数量）					

			import random 
			import linecache
			import shutil
			import os

			source_txt_dir = r'ImageSets/Main/'
			source_annotations_dir = r'Annotations/'
			source_images_dir = r'JPEGImages/'
			dest_root_dir = r'manyDatasets/'

			for image_num in range(50, 751, 50):

				#create dir
				one_dataset_dir = dest_root_dir + str(image_num)
				Annotations_dir = one_dataset_dir+'/Annotations/'
				ImageSets_dir_up = one_dataset_dir+'/ImageSets/'
				ImageSets_dir = one_dataset_dir+'/ImageSets/Main/'
				JPEGImages_dir = one_dataset_dir+'/JPEGImages/'

				is_exist_dir = os.path.exists(one_dataset_dir)  #dataset dir
				if not is_exist_dir:
					os.mkdir(one_dataset_dir)
				is_exist_dir = os.path.exists(Annotations_dir)  #Annotations dir
				if not is_exist_dir:
					os.mkdir(Annotations_dir)
				is_exist_dir = os.path.exists(ImageSets_dir_up)  #ImageSets dir
				if not is_exist_dir:
					os.mkdir(ImageSets_dir_up)
					is_exist_dir = os.path.exists(ImageSets_dir)  #ImageSets dir
				if not is_exist_dir:
					os.mkdir(ImageSets_dir)
				is_exist_dir = os.path.exists(JPEGImages_dir)  #JPEGImages dir
				if not is_exist_dir:
					os.mkdir(JPEGImages_dir)

				#create new train.txt trainval.txt
				new_train = open(ImageSets_dir+'train.txt', 'w')
				new_trainval = open(ImageSets_dir+'trainval.txt', 'w')

				#read source train.txt
				result_list = random.sample(range(1, 789), image_num)  #image_num
				for i in range(0, image_num):
					file_name_no_ext = linecache.getline(source_txt_dir+'train.txt', result_list[i]).rstrip('\r\n')
					print file_name_no_ext

					#write train.txt
					new_train.write(file_name_no_ext+'\n')
					new_trainval.write(file_name_no_ext+'\n')

					#copy annotations file
					shutil.copyfile(source_annotations_dir+file_name_no_ext+'.xml', Annotations_dir+file_name_no_ext+'.xml')
					#copy images
					shutil.copyfile(source_images_dir+file_name_no_ext+'.png', JPEGImages_dir+file_name_no_ext+'.png')

				new_train.close()
				#write test.txt
				source_test = open(source_txt_dir+'test.txt', 'r')
				new_test = open(ImageSets_dir+'test.txt', 'w')
				lines = source_test.readlines()
				for line in lines:
					new_test.write(line.rstrip('\r\n')+'\n')
					#copy annotations file
					shutil.copyfile(source_annotations_dir+line.rstrip('\r\n')+'.xml', Annotations_dir+line.rstrip('\r\n')+'.xml')
					#copy images
					shutil.copyfile(source_images_dir+line.rstrip('\r\n')+'.png', JPEGImages_dir+line.rstrip('\r\n')+'.png')
				source_test.close()
				new_test.close()

				#write val.txt
				source_val = open(source_txt_dir+'val.txt', 'r')
				new_val = open(ImageSets_dir+'val.txt', 'w')
				lines = source_val.readlines()
				for line in lines:
					new_val.write(line.rstrip('\r\n')+'\n')
					#copy annotations file
					shutil.copyfile(source_annotations_dir+line.rstrip('\r\n')+'.xml', Annotations_dir+line.rstrip('\r\n')+'.xml')
					#copy images
					shutil.copyfile(source_images_dir+line.rstrip('\r\n')+'.png', JPEGImages_dir+line.rstrip('\r\n')+'.png')
				source_val.close()
				new_val.close()

				val = open(ImageSets_dir+'val.txt', 'r')
				lines = val.readlines()
				for line in lines:
					new_trainval.write(line.rstrip('\r\n')+'\n')    #copy val to trainval
				val.close()
				new_trainval.close()				
				