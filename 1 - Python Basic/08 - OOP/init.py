__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
class Bird(object):
    have_feather=True
    way_of_reproduction='egg'
    def move(self,dx,dy):
        position=[0,0]
        position[0]=position[0]+dx
        position[1]=position[1]+dy
        return position

class happyBird(Bird):
    def __init__(self,more_words):
        print 'We are happy birds.',more_words

summer=happyBird('Happy,Happy!')

#__init__()是一个特殊方法(special method).特殊方法的特点是名字前后有两个下划线
#创建对象时，Python会自动调用这个方法。这个过程也叫初始化。

