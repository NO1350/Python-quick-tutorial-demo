#coding=utf-8


"""
什么是循环对象
循环对象是这样一个对象，它包含有一个next()方法(__next__()方法，在python 3x中)， 这个方法的目的是进行到下一个结果，而在结束一系列结果之后，举出StopIteration错误。

当一个循环结构（比如for）调用循环对象时，它就会每次循环的时候调用next()方法，直到StopIteration出现，for循环接收到，就知道循环已经结束，停止调用next()。
"""


for line in open("test.txt"):
    print line

#open()返回的实际上是一个循环对象，包含有next()方法。而该next()方法每次返回的就是新的一行的内容，到达文件结尾时举出StopIteration。这样，我们相当于手工进行了循环。
#在这里，for结构自动调用next()方法，将该方法的返回值赋予给line。循环知道出现StopIteration的时候结束。

"""
相对于序列，用循环对象的好处在于：不用在循环还没有开始的时候，就生成好要使用的元素。所使用的元素可以在循环过程中逐次生成。这样，节省了空间，提高了效率，编程更灵活。
"""

"""
迭代器
从技术上来说，循环对象和for循环调用之间还有一个中间层，就是要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。但从逻辑层面上，常常可以忽略这一层，所以循环对象和迭代器常常相互指代对方。
"""

"""
生成器
生成器(generator)的主要目的是构成一个用户自定义的循环对象。

生成器的编写方法和函数定义类似，只是在return的地方改为yield。生成器中可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield。生成器自身又构成一个循环器，每次循环使用一个yield返回的值。
"""

def gen():
    a=100
    yield a
    a=a*8
    yield a
    yield 1000

for i in gen():
    print i


def gen1():
    for i in range(4):
        yield i
#又可以写成生成器表达式(Generator Expression)
G=[x for x in range(4)]
print G

"""
表推导(list comprehension)是快速生成表的方法。表推导的机制实际上是利用循环对象
"""
L1=[]
for x in range(10):
    L1.append(x**2)
print L1
#表推导方式
L2=[x**2 for x in range(10)]
print L2

x1=[1,3,5]
y1=[9,12,13]
L=[x**2 for (x,y) in zip(x1,y1) if y>10]
print L

