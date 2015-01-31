__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
class Human(object):
    def __init__(self,input_gender):
        self.gender=input_gender
    def printGender(self):
        print self.gender

hanmeimei=Human('female')# 这里，'female'作为参数传递给__init__()方法的input_gender变量。
print hanmeimei.gender
hanmeimei.printGender()


"""
Summary
通过self调用类属性

__init__(): 在建立对象时自动执行

类属性和对象的性质的区别
"""