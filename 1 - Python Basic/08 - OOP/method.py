__author__ = '100068'
#-*-coding:utf-8-*-
# !/usr/bin/env python
#子类对父类函数的调用,定义和调用类函数，静态函数和实例函数
class a():
    a_1=0
    a_2='aaa'
    #classmethod
    @classmethod
    def d(self,a):
        print(a+"a1a2a3")

    def c(self,a):
        print(a+"11111")

    @staticmethod
    def b(a):
        print(a+"2222")

x=a()
x.c('d')

a.d("c")

a.b('bb')

class r(a):
    r_1=111
    r_2='rrrr'

rr=r()
rr.c('r22222')

r.d('r11111')

