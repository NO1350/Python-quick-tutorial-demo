__author__ = 'crixalis'
# coding:utf-8
#!/usr/bin/env python

#range()
S='abcdefghijk'
for i in range(0,len(S),2):
    print S[i]

#enumerate()
for (index,char) in enumerate(S):
    print index
    print char

