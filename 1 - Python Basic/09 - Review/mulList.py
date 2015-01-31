__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
#乘法运算符重载
class mulList(list):
    def __mul__(self, b):
        result=[]
        a=self[:]
        c=b[:]
        if len(a)>=len(c):
            for i in range(len(c)):
                result.append(a[i]*b[i])
        else:
            for i in range(len(a)):
                result.append(a[i]*b[i])

        return result

print mulList([1,2,3]) * mulList([3,4])