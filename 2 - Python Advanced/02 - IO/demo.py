__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
fp = open('record.txt', 'rb')

content = fp.read(5)
cnt = fp.readline()
cnt2 = fp.readlines()

print(content, cnt, cnt2)    #我的是python3

fp.close()

f = open('test.txt','a')
f.write("aaaaa")
f.close()

t = open('test.txt','r')
print t.read()

"""
'b' --> binary 二进制
'r' --> read 读取
'w' --> write 写
'a' --> append 追加

于是: 'rb'就是 以二进制的形式读取文件

注:
'w' 和 'a'的区别:
'w'模式下, 如果文件不存在, 会创建这个文件; 如果文件存在, 则将其覆盖
'a'模式下, 打开一个文件用于追加, 也就是说, 文件指针将会指向文件的结尾; 当然, 如果这个文件不存在, 也是会创建这个文件的.

至于 '+', 这个好理解.
'r+' --> 'wr'
'w+' --> 'wr'

原来是 read, 多了一个 '+', 就又可以read, 又可以write了;
同样, 原来是 write, 多了一个'+', 就又可以 write, 又可以 read了.

可以看下这个:
https://docs.python.org/2/library/functions.html#open
"""