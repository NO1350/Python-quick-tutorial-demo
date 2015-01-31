__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
#对list的sub函数添加对"-"的定义 而“+”运算符定义了add函数
#根据自己的目的，将原本不存在的运算增加在对象上
class superList(list):
    def __sub__(self, b):
        a=self[:] # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象
        b=b[:]
        while len(b)>0:
            element_b=b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1,2,3]) - superList([3,4])

"""
>>>print nl.count(5)       # 计数，看总共有多少个5

>>>print nl.index(3)       # 查询 nl 的第一个3的下标

>>>nl.append(6)            # 在 nl 的最后增添一个新元素6

>>>nl.sort()               # 对nl的元素排序

>>>print nl.pop()          # 从nl中去除最后一个元素，并将该元素返回。

>>>nl.remove(2)            # 从nl中去除第一个2

>>>nl.insert(0,9)          # 在下标为0的位置插入9

总之，list是一个类。每个列表都属于该类。
"""