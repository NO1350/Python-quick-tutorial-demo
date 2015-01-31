__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
#一个新的类，词典 (dictionary)。与列表相似，词典也可以储存多个元素。这种储存多个元素的对象称为容器(container)。
#不可变的对象可以作为键,值可以是任意对象.键和值两者一一对应。
#键的数据类型是不可变的数据类型，不仅是字符串，数字也可以
dic = {'tom':11,'sam':57,'lily':100}
print dic,type(dic)
#与表不同的是，词典的元素没有顺序。你不能通过下标引用元素。词典是通过键来引用。

print dic['tom']
dic['tom']= 30
print dic

#构建一个新的空的词典
dict= {}
print dict
#在词典中增添一个新元素的方法
dict['lilei'] = 99
print dict

#词典元素的循环调用(在循环中，dict的每个键，被提取出来，赋予给key变量。)
for key in dic:
    print dic[key]

#词典的常用方法
print dic.keys()           # 返回dic所有的键

print dic.values()         # 返回dic所有的值

print dic.items()          # 返回dic所有的元素（键值对）

print len(dic)             #len()查询词典中的元素总数。

del dic['tom']             # 删除 dic 的‘tom’元素
#del是Python中保留的关键字，用于删除对象。

print dic
dic.clear()                # 清空dic，dict变为{}
print dic