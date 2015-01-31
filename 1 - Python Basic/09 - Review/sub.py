__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
class superList(list):
#    def __sub__(self, b, c):
    def jian(self,b,c):
        a = self[:]
        b = b[:]  #表元素的引用
        c = c[:]

        while len(b) > 0 or len(c) > 0:
            if len(b) > 0:
                element_b = b.pop()
                if element_b in a:
                    a.remove(element_b)
            if len(c) > 0:
                element_c = c.pop()
                if element_c in a:
                    a.remove(element_c)

        return a

a = superList([1,2,3,5])
b = superList([3,2])
c = superList([1,4,2])


print a.jian(b,c)