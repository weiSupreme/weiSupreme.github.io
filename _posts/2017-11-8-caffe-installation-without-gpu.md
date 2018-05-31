---
layout: post
title: caffe的安装步骤（无GPU版）
categories:  Tutorial
tags: DeepLearning caffe
author: zhuwei
description: 安装深度学习框架caffe
---
1、安装anconda:   
　　系统python版本最好留在2.7，到anconda官网下载anaconda2，按照官网步骤安装（其实就一行语句：bash anaconda***.sh）

- - -

        设置anaconda环境变量：
            sudo gedit /etc/environment
        在文件里加上“ :/(anaconda_dir)/anconda/bin  ”（anaconda_dir是你安装anaconda的根目录）

- - -

2、安装opencv3.2:   
去官网下载opencv的zip包，不要按照某些网站或博客说的一个一个的安装依赖包，很容易出错。
	
        下载好了之后，解压zip包，打开终端，进入opencv文件夹，执行命令：
			mkdir build
			cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .
       （如果没安装cmake,先安装cmake：sudo apt-get install cmake）
			make -j4
		      make install
		测试是否安装成功
			python
			import cv2
		    cv2.__version__
	   显示版本号，则安装成功。如果显示 no module named cv2，执行：
		    sudo apt-get install python-opencv
	   或者：
			pip install opencv-python
	   是opencv-python还是python-opencv,自己试一下，我也忘了。再次测试，如无意外，会显示版本号，说明安装成功。

- - -

3、安装caffe依赖包

		执行以下命令：
			sudo apt-get install git
			sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev 		libhdf5-serial-dev protobuf-compiler
			sudo apt-get install --no-install-recommends libboost-all-dev
			sudo apt-get install libatlas-base-dev
			sudo apt-get install python-dev
			sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
			
必须全部安装，中间如有错误，根据终端错误信息自行解决，我遇到的几个问题都是某些文件下载不了，update或upgrade一下就好了

- - -

4、安装Caffe

- - -

    4.1、下载源码
            sudo apt-get install git（如果已经安装git则不要再次安装）
            git clone https://github.com/bvlc/caffe.git
    4.2、配置make文件
            cd caffe/
            cp Makefile.config.example Makefile.config
            gedit Makefile.config
    或者
            vi Makefile.config
    修改宏：
            CPU_ONLY :=1（去掉前面的注释#即可，后同）
            USE_OPENCV :=1
            USE_LEVELDB :=1
            USE_LMDB :=1
            OPENCV_VERSION :=2
            #CUDA_DIR :=/USR/LOCAL/cuda
    修改python链接：
            ANACONDA_HOME := $(HOME)/anaconda2 #这个是你anaconda所在路径
            PYTHON_INCLUDE := $(ANACONDA_HOME)/include \
                 $(ANACONDA_HOME)/include/python2.7 \
                 $(ANACONDA_HOME)/lib/python2.7/site-packages/numpy/core/include \
            PYTHON_LIB := $(ANACONDA_HOME)/lib
    再把原来同样的内容注释掉。
    还需要在库目录这一项加入路径/usr/lib/x86_64-linux-gnu

            # Whatever else you find you need goes here.
            INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include 
            LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu
	4.3、编译：
            cd caffe
            mkdir build
            cd build
            cmake ..
            cd ..
            make
            make install
            make runtest
    如果中间几个命令有错误，make clean，重新执行，在camke ..之后，cd到caffe文件夹在执行make命令
    如果最后有错误，一般是anaconda的libstdc++.so.6缺少GLIBCXX,执行：
        	sudo apt-get install lib64stdc++6
    这个命令将会安装最新的libstdc++文件，libstdc++.so.6.xxx，执行：
            cd /usr/lib64
            cp libstdc++.so.6.xxx /anaconda_dir/anaconda2/lib
            cd /anaconda_dir/anaconda2/lib
            rm -rf libstdc++.so.6
            sudo ln -s libstdcc.so.6.xxx libstdc++.so.6
    再执行make runtest，一般就可以了。
	4.4、python导入caffe，执行：
            python
            import caffe
    如果有错误，一般是no module named caffe，需要设置caffe的变量路径，执行：
        	sudo gedit /etc/profile
    在文件最后加上：
            export PYTHONPATH=/caffe_dir/caffe/python:$PYTHONPATH
            source /etc/profile
  caffe_dir是你的caffe安装根目录。

至此，大功告成！！！



















