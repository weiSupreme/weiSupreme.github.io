---
layout: post
title: ubuntu16.04下caffe的安装步骤（CPU only，无GPU版）
categories:  Tutorial
tags: DeepLearning caffe
author: zhuwei
description: 安装深度学习框架caffe
---
1、安装anconda:   	

- - -

        强烈建议不要使用anaconda配置caffe，各种问题！！！
        强烈建议不要使用anaconda配置caffe，各种问题！！！
        强烈建议不要使用anaconda配置caffe，各种问题！！！
    需要什么包，直接下载。如果网速比较慢，可以到国内的镜像源网站下载。

- - -

2、安装opencv3.2:   

	
        到国内镜像源网站下载相应的opencv-python.whl包，使用pip安装即可。一般不推荐自己编译opencv，速度慢，组件多。

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
   
            推荐使用ccmake进行编译，ccmake可以将配置选项可视化，不需要手动配置make文件。如果安装cpu版的caffe，只需将CPU-ONLY置ON即可。如果安装GPU版的，在安装了cuda和cudnn后只需将CPU-ONLY置OFF（默认已经打开了cuudnn），直接生成配置文件并退出即可。
            sudo apt-get install cmake-curses-gui
     安装完后，到对应文件夹运行ccmake，见4.3。出来ccmake gui界面后，按c出来配置选项，然后选择要配置的选项，按enter可进行编辑。再按c重新生成配置选项，按g生成配置文件并退出。如果出现camke warnings,可以忽略，按e退出即可。如果出现cmake errors，则需要根据提示信息修改相应文件，重新配置。
            
4.3、编译：

            cd caffe
            mkdir build
            cd build
            ccmake ..
            make
            make install
            make runtest
    如果中间几个命令有错误，make clean，重新执行。		
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



















