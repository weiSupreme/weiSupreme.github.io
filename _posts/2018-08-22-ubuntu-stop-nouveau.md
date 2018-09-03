---
layout: post
title: ubuntu禁用nouveau重启无法进入系统
categories: Tutorial
tags: DeepLearning
author: zhuwei
description: 解决禁用nouveau驱动后无法进入ubuntu系统的问题
---

                            
&emsp;&emsp;安装英伟达驱动时，一般需要禁用自带nouveau驱动，按如下命令操作：					

	sudo vim /etc/modprobe.d/blacklist-nouveau.conf			

添加如下内容：				

    blacklist nouveau				
    options nouveau modeset=0				
    
保存后更新：			

	sudo update-initramfs -u
    	
然后接着安装英伟达驱动。			

&emsp;&emsp;若安装英伟达驱动失败或直接重启，则会出现无法进入系统的情况，此时需要进入ubuntu recovery模式修复。首先重启进入recovery模式的root命令行，先挂载系统可读写：		

	mount -o remount,rw /			
    
然后删除先前创建的文件：			

	rm -f /etc/modprobe.d/blacklist-nouveau.conf		
    
删除后再重启就能进入系统了。这样做相当于恢复了自带nouveau驱动。				

&emsp;&emsp;接下来继续辛苦地安装英伟达驱动吧！！！
