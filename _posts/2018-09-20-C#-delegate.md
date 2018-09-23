---
layout: post
title: C#设置委托，两个form之间传值、多播委托：委托可以指向多个函数
categories: Tutorial
tags: C#
author: zhuwei
description: 设置委托，两个form之间传值、多播委托
---

                            
&emsp;&emsp;参考自[这里](https://blog.csdn.net/yanhuatangtang/article/details/72844065)				
form1:			

	Form1.cs
    namespace feiqiu
    {
        public partial class Form1 : Form
        {
            public Form1()
            {
                InitializeComponent();
            }

            private void button1_Click(object sender, EventArgs e)
            {
                Form2 for1 = new Form2(ShowMsg );
                for1.Show();
            }
            void ShowMsg(string st) //需要将这个方法传递到Form2中，使用委托在构造函数中实现
            {
                label1.Text =st;   //这样就可以在form2中有方法也有值，完成
            }
        }
    }					
    
form2:			

	Form2.cs
    namespace feiqiu
    {
        public delegate void DelTest(string str);
        public partial class Form2 : Form
        {
            public DelTest _dt;
            public Form2(DelTest del)
            {
                this._dt =del;
                InitializeComponent();
            }

            private void label1_Click(object sender, EventArgs e)
            {
                //_dt(textBox1.Text );
            }

            private void button1_Click(object sender, EventArgs e)
            {
                _dt(textBox1.Text);
            }
        }
    }			
    
委托可以实现多个方法同时实现:			

    namespace delegation2
    {
        public delegate void DelAdd1();

        class Program
        {
            static void Main(string[] args)
            {
                DelAdd1 d1 = Show1;
                d1 += Show2;
                d1 += Show3;
                d1 += Show4; //同时实现了Show1、Show2、Show3、Show4多个方法
                d1 -= Show2;//同时实现了Show1、Show3、Show4多个方法
                d1();

                Console.ReadKey();
            }
            public static void Show1()
            {
                Console.WriteLine("The delegate One");
            }
            public static void Show2()
            {
                Console.WriteLine("The delegate Two");
            }
            public static void Show3()
            {
                Console.WriteLine("The delegate Three");
            }
            public static void Show4()
            {
                Console.WriteLine("The delegate Four");
            }
            public static void Show5()
            {
                Console.WriteLine("The delegate Five");
            }
        }
    }



