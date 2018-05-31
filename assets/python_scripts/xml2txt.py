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

