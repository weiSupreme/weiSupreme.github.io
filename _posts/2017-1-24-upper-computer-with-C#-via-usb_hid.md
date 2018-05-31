---
layout: post
title: C#上位机之USB_Hid通信
categories:  Tutorial
tags: C# 上位机
author: zhuwei
description: C#编写usb_hid协议上位机（用于匿名无人机飞控）
---


       最近在写上位机，用到了hid通信，在网上查找了很多资料，终于通信成功。其中也遇到了一些问题，在此说明一下，希望可以帮到有需要的朋友。
---
        我是在网上找到了一个例程，将其移植了一下。开始接收数据没问题，但是发送数据一直不成功，只有在一次性发送到数据大于64个字节是才会发送，而且接收下位机发送回来的相同的数据也不对。折磨了我好几天，终于在谷歌上搜到了相关信息。原来hid的report是有固定格式的。发送数据的时候，数组第一个byte是hid 的report id，一般是0；数组第二个byte是要发送的数据的长度。同样的，接收到的数据，缓冲区里第一个byte是id,，也就是0；第二个byte是接收到的数据的长度。我在网上搜索到的例程中并不是这样的，他直接把缓冲区的数据全当作是接收到的数据，发送的时候也是直接发送数据，没有按照report的格式，所以导致我通信不成功。一开始接收数据时，由于下位机发送到数据是有固定格式的，所以没有分离出id和数据长度也没有影响。
       附件里是我修改过的例程，并且也多次测试过，发送和接收都没有问题，有需要的朋友可以下载参考。我这里再单独提一下这个report的问题。
---
接收数据：

        private void ReadCompleted(IAsyncResult iResult)
        {
            byte[] readBuff = (byte[])(iResult.AsyncState);
            try
            {
                hidDevice.EndRead(iResult);//读取结束,如果读取错误就会产生一个异常
                byte[] reportData = new byte[readBuff.Length - 2];  ////////////////////////////////////////////第一个byte是id，第二个byte是数据长度，所以从readbuff[2]开始才是真正接收到的数据
                for (int i = 2; i < readBuff.Length; i++)
                    reportData[i - 2] = readBuff[i];
                report e = new report(readBuff[0], reportData);
                OnDataReceived(e); //发出数据到达消息
                BeginAsyncRead();//启动下一次读操作
            }
            catch (IOException)//读写错误,设备已经被移除
            {
                EventArgs ex = new EventArgs();
                OnDeviceRemoved(ex);//发出设备移除消息
                CloseDevice();
            }
        }
发送数据：

        internal string WriteUSBHID(string sendValue)
        {
            try
            {
                //byte[] array = { 0xF5, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01 };
                byte[] array = System.Text.ASCIIEncoding.Default.GetBytes(sendValue);
                byte[] arr = new byte[outputReportLength]; ////////////////////////////////////////////////////////////这里注意：要发送的arr数组大小必须是outputReportLength
                arr[0] = 0x00;   /////////////////////////////////////第一个是id
                arr[1] = (byte)array.Length;////////////////////////////////第二个是数据长度
                for (int i = 2; i < array.Length + 2; i++)
                {
                    arr[i] = array[i - 2];
                }
                hidDevice.Write(arr, 0, arr.Length);  ///////////////////////////////原例程是直接发送array数组，导致通信失败
                return sendValue;
            }
            catch (Exception e) {
                return e.Message ;
            }
        }
---
       最后，感谢原例程的作者，还要感谢伟大的谷歌（我是输入英文查找的。百度上搜索的都是你抄我，我抄你的，没有人讲这个问题，也不知道是就我一个人遇到了，还是大家解决了不屑说又或者太保守不想告诉别人，唉！吐槽一下，请勿见怪。）
         再附上百度云链接：链接：http://pan.baidu.com/s/1qYIZXrY 密码：85hq  ；链接：http://pan.baidu.com/s/1kU6cE0Z 密码：g8r2