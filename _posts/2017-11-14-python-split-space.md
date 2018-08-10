---
layer: post
title: 用python合并Txt文档中的空格
categories:  Tutorial
tags: File Python
author: zhuwei
description: txt文档的操作
---
&emsp;对txt文档中每一行中的连续多个空格合并为一个空格，以下是代码：

	f = open('row_val.txt')
	nf = open('val.txt', 'w')
	done = 0
	while not done:
		line = f.readline()
		if line != '':
			str = ' '.join(line.split())
			nf.write(str+'\n')
		else:
			done = 1
	f.close()
	nf.close()