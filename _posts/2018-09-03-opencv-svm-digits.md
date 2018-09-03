---
layout: post
title: 基于opencv3.4和SVM的手写数字识别
categories: Tutorial
tags: Opencv Text_recognition
author: zhuwei
description: 基于opencv3.4和SVM的手写数字识别
---

&emsp;&emsp;本文将使用opencv3.4和SVM识别手写数字，开发环境为vs2013和C++。			

### 数据集				

&emsp;&emsp;opencv安装文件夹的 “samples/data" 下预置了一张手写数字的图片，其包含了5000个 0至9 的手写数字，每个数字大小为20*20， 只需相应的格式进行分割就可得到相应的数据集。先在选定的文件夹里新建10个文件夹，分别以0至9命名，方便存放图片。以下是代码：			

	#include <opencv2/opencv.hpp>
    #include <iostream>

    using namespace std;
    using namespace cv;

    int main()
    {
        char ad[128] = { 0 };
        int  filename = 0, filenum = 0;
        Mat img = imread("D:/opencv-3.4.0/samples/data/digits.png");
        Mat gray;
        cvtColor(img, gray, CV_BGR2GRAY);
        int b = 20;
        int m = gray.rows / b;   //原图为1000*2000
        int n = gray.cols / b;   //裁剪为5000个20*20的小图块

        for (int i = 0; i < m; i++)
        {
            int offsetRow = i*b;  //行上的偏移量
            if (i % 5 == 0 && i != 0)
            {
                filename++;
                filenum = 0;
            }
            for (int j = 0; j < n; j++)
            {
                int offsetCol = j*b; //列上的偏移量
                sprintf_s(ad, "D:/实习/seg/datasets/cvSamplesDigits/%d/%d.jpg", filename, filenum++);
                //截取20*20的小块
                Mat tmp;
                gray(Range(offsetRow, offsetRow + b), Range(offsetCol, offsetCol + b)).copyTo(tmp);
                imwrite(ad, tmp);
            }
        }
        return 0;
    }			
    
成功运行之后，就会在每个文件夹下生成500张20*20的图片。			

### 训练				

下面是训练的代码：

	#include "stdafx.h"
    #include <stdio.h>  
    #include <time.h>  
    #include <opencv2/opencv.hpp>  
    #include <opencv/cv.h>  
    #include <iostream> 
    #include <opencv2/core/core.hpp>  
    #include <opencv2/highgui/highgui.hpp>  
    #include <opencv2/ml/ml.hpp>  
    #include <io.h>

    using namespace std;
    using namespace cv;
    using namespace ml;

    void getFiles(string path, vector<string>& files);
    void get_1(Mat& trainingImages, vector<int>& trainingLabels);
    void get_0(Mat& trainingImages, vector<int>& trainingLabels);

    int main()
    {
        //获取训练数据
        Mat classes;
        Mat trainingData;
        Mat trainingImages;
        vector<int> trainingLabels;
        get_1(trainingImages, trainingLabels);
        get_0(trainingImages, trainingLabels);
        Mat(trainingImages).copyTo(trainingData);
        trainingData.convertTo(trainingData, CV_32FC1);
        Mat(trainingLabels).copyTo(classes);
        //配置SVM训练器参数
        Ptr<SVM> svm = SVM::create();
        svm->setType(SVM::C_SVC);
        svm->setKernel(SVM::LINEAR);
        svm->setDegree(0);
        svm->setTermCriteria(TermCriteria(CV_TERMCRIT_ITER, 1000, 0.01));
        svm->setGamma(1);
        svm->setCoef0(0);
        svm->setC(1);
        svm->setNu(0);
        svm->setP(0);
        cout << "开始训练！！！" << endl;
        //训练
        svm->train(trainingData, cv::ml::ROW_SAMPLE, classes);
        //保存模型
        svm->save("../../svm.xml");
        cout << "训练好了！！！" << endl;
        return 0;
    }
    void getFiles(string path, vector<string>& files)
    {
        long long hFile = 0;
        struct _finddata_t fileinfo;
        string p;
        if ((hFile = _findfirst(p.assign(path).append("/*.jpg").c_str(), &fileinfo)) != -1)
        {
            do
            {
                if ((fileinfo.attrib &  _A_SUBDIR))
                {
                    if (strcmp(fileinfo.name, ".") != 0 && strcmp(fileinfo.name, "..") != 0)
                        getFiles(p.assign(path).append("/").append(fileinfo.name), files);
                }
                else
                {
                    files.push_back(p.assign(path).append("/").append(fileinfo.name));
                }
            } while (_findnext(hFile, &fileinfo) == 0);

            _findclose(hFile);
        }
    }
    void get_1(Mat& trainingImages, vector<int>& trainingLabels)
    {
        char * filePath = "D:/实习/seg/datasets/cvSamplesDigits/1";
        vector<string> files;
        getFiles(filePath, files);
        int number = files.size();
        for (int i = 0; i < number; i++)
        {
            Mat  SrcImage = imread(files[i].c_str(), 0);
            resize(SrcImage, SrcImage, Size(8, 16), (0, 0), (0, 0), INTER_AREA);
            SrcImage = SrcImage.reshape(1, 1);
            trainingImages.push_back(SrcImage);
            trainingLabels.push_back(1);
        }
    }
    void get_0(Mat& trainingImages, vector<int>& trainingLabels)
    {
        char * filePath = "D:/实习/seg/datasets/cvSamplesDigits/0";
        vector<string> files;
        getFiles(filePath, files);
        int number = files.size();
        for (int i = 0; i < number; i++)
        {
            Mat  SrcImage = imread(files[i].c_str(), 0);
            resize(SrcImage, SrcImage, Size(8, 16), (0, 0), (0, 0), INTER_AREA);
            SrcImage = SrcImage.reshape(1, 1);
            trainingImages.push_back(SrcImage);
            trainingLabels.push_back(0);
        }
    }			
    
### 测试			

下面是测试代码：				

	#include "stdafx.h"
    #include <stdio.h>  
    #include <time.h>  
    #include <opencv2/opencv.hpp>  
    #include <opencv/cv.h>  
    #include <iostream> 
    #include <opencv2/core/core.hpp>  
    #include <opencv2/highgui/highgui.hpp>  
    #include <opencv2/ml/ml.hpp>  
    #include <io.h>

    using namespace std;
    using namespace cv;
    using namespace ml;

    void getFiles(string path, vector<string>& files);

    int main()
    {
        int result = 0;
        char * filePath = "D:/ʵϰ/seg/datasets/test/0";
        vector<string> files;
        getFiles(filePath, files);
        int number = files.size();
        //cout << number << endl;
        string modelpath = "../../svm.xml";
        Ptr<SVM> svm = StatModel::load<SVM>(modelpath);
        for (int i = 0; i < number; i++)
        {
            Mat inMat = imread(files[i].c_str(), 0);
            //cout << files[i].c_str()<<endl;
            resize(inMat, inMat, Size(8, 16), (0, 0), (0, 0), INTER_AREA);
            Mat p = inMat.reshape(1, 1);
            p.convertTo(p, CV_32FC1);
            int response = (int)svm->predict(p);
            cout << response << endl;
            if (response == 1)
            {
                result++;
            }
        }
        //cout << result << endl;
        //getchar();
        return  0;
    }
    void getFiles(string path, vector<string>& files)
    {
        long long hFile = 0;
        struct _finddata_t fileinfo;
        string p;
        if ((hFile = _findfirst(p.assign(path).append("\\*").c_str(), &fileinfo)) != -1)
        {
            do
            {
                if ((fileinfo.attrib &  _A_SUBDIR))
                {
                    if (strcmp(fileinfo.name, ".") != 0 && strcmp(fileinfo.name, "..") != 0)
                        getFiles(p.assign(path).append("\\").append(fileinfo.name), files);
                }
                else
                {
                    files.push_back(p.assign(path).append("\\").append(fileinfo.name));
                }
            } while (_findnext(hFile, &fileinfo) == 0);
            _findclose(hFile);
        }
    }			
    
以上代码参考自：https://blog.csdn.net/chaipp0607/article/details/68067098/ ，在此表示感谢。他（她）的代码是早期opencv版本的，我改成了opencv3.4版本的。以上代码都经过了测试，只需修改对应路径。

