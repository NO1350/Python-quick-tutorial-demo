__author__ = 'crixalis'
# coding:utf-8
#!/usr/bin/env python
#函数目的是提高程序的重复可用性
def square_sum(a,b):
    c=a**2+b**2
    return c
#Python的函数允许不返回值，也就是不用return
"""
在Python中，当程序执行到return的时候,程序将停止执行函数内余下的语句。return并不是必须的，当没有
return,或者return后面没有返回值时，函数将自动返回None.None是Python中的一个特别的数据类型，用来表示什么都没有，
相当于Ｃ中的NULL。None多用于关键字参数传递的默认值。
"""

