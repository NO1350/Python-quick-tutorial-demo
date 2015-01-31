__author__ = 'crixalis'
# coding:utf-8
#!/usr/bin/env python
#参数传递

#位置传递
def f(a,b,c):
    return a+b+c

print(f(1,2,3))


#关键字传递(根据每个参数的名字传递参数），关键字并不用遵守位置的对应关系。
print(f(c=3,b=2,a=1))
#关键字传递可以和位置传递混用。但位置参数要出现在关键字参数之前
print(f(1,c=3,b=2))



#参数默认值,定义参数时赋值，如果该参数最终没有被传递值，将使用该默认值
def f(a,b,c=10):
    return a+b+c

print(f(3,2))
print(f(3,2,1))

#包裹传递
def func(*name):
    print type(name)
    print name

func(1,4,6)
func(5,6,7,1,2,3)
#在func的参数表中，所有的参数被name收集，根据位置合并成一个元组(tuple)，这就是包裹位置传递
#为了提醒Python参数，name是包裹位置传递所用的元祖名，在name前加*号。或是用字典作为包裹位置传递所用的字典，在参数名前加**号

def func(**dict):
    print type(dict)
    print dict

func(a=1,b=9)
func(m=2,n=1,c=11)


#解包裹(*和**在调用的时候使用)
def func(a,b,c):
    print a,b,c

args=(1,3,4)
func(*args)
#在传递tuple时，让tuple的每一个元素对应一个位置参数,将args拆成分散的三个元素，分别传递给ａ,b,c

dict={'a':1,'b':2,'c':3}
func(**dict)
#在传递词典dict时，让词典的每个键值对作为一个关键字传递给func


"""
混合

在定义或者调用参数时，参数的几种传递方式可以混合。但在过程中要小心前后顺序。基本原则是，先位置，再关键字，再包裹位置，再包裹关键字，并且根据上面所说的原理细细分辨。



注意：请注意定义时和调用时的区分。包裹和解包裹并不是相反操作，是两个相对独立的过程。


"""
