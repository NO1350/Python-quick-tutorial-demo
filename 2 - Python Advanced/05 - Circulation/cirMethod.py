__author__ = 'crixalis'
# coding:utf-8
#!/usr/bin/env python
#在Python中，for循环后的in跟随一个序列的话，循环每次使用的序列元素，而不是序列的下标。
#range()实现下标对循环的控制,range函数中，分别定义上限，下限和每次循环的步长
S='abcdefghijk'
for i in range(0,len(S),2):
    print S[i]

#enumerate()函数，可以在每次循环中同时得到下标和元素：
for (index,char) in enumerate(S):
    print index
    print char

#zip()实现多个等长的序列，然后每次循环时从各个序列分别取出一个元素
ta=[1,2,3]
tb=[9,8,7]
tc=['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)
#zip()函数的功能，就是从多个列表中，依次各取出一个元素。每次取出的(来自不同列表的)元素合成一个元组，合并成的元组放入zip()返回的列表中。zip()函数起到了聚合列表的功能。


ta=[1,2,3]
tb=[9,8,7]

#cluster
zipped=zip(ta,tb)
print(zipped)

#decompose
na,nb=zip(*zipped)
print(na,nb)



