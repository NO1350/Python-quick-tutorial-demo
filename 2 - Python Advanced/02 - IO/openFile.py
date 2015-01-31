__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
#文本文件的读写主要通过open()所构建的文件对象来实现。
f=open("test.txt","r") # "r" 只读 "w" 写入
"""
文件对象的方法

读取：

content = f.read(N)          # 读取N bytes的数据

content = f.readline()       # 读取一行

content = f.readlines()      # 读取所有行，储存在列表中，每个元素是一行。


写入：

f.write('I like apple')      # 将'I like apple'写入文件



关闭文件：

f.close()

"""