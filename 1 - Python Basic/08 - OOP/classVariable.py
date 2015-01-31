__author__ = '100068'
# coding:utf-8
# !/usr/bin/env python
#更改类变量属性是否影响其他对象(通过对象来修改类属性是危险的，这样可能会影响根据这个类定义的所有对象的这一属性！！)
class Human(object):
    Can_Talk = True
    Can_Walk = True
    Age = 0
    Name = ""

    def Say(self,msg):
        print "I am saying: "+msg

class Child(Human):
    def Cry(self):
        print "wa wa ...."

    def ShowAge(self):
        print self.Name, " is " , self.Age , "years old."

    def Grow(self,yr):
        self.Age = yr

Jerry = Child()
Jerry.Name = "Jerry"
Jerry.Age = 3
Jerry.Grow(4)
Jerry.ShowAge()

Daniel = Child()
Daniel.Name = "Daniel"
Daniel.Grow(1)
Daniel.ShowAge()

#immutable的(比如整数、字符串)。但如果属性是mutable的话(比如list)
"""
为什么immutable是可行的呢？原因是，在更改对象属性时，如果属性是immutable的，该属性会被复制出一个副本，存放在对象的__dict__中。你可以通过下面的方式查看：
print a.__class__.__dict__
print a.__dict__
注意到类中和对象中各有一个Age。一个为0， 一个为1。所以我们在查找a.Age的时候，会先查到对象的__dict__的值，也就是1。
但mutable的类属性，在更改属性值时，并不会有新的副本。所以更改会被所有的对象看到。

所以，为了避免混淆，最好总是区分类属性和对象的属性，而不能依赖上述的immutable属性的复制机制。
"""
#使用__init__初始化对象属性值是好习惯。
#如果是个可变类型的变量 那么赋值时传递的是引用修改的是同一块内存 如果是不可变类型的变量 赋值时 会重新开辟一块内存
"""
（通过对象来修改类属性是危险的，这样可能会影响根据这个类定义的所有对象的这一属性！！）
关于这一句，情况是这样的：
1、对象不能修改类的属性，只能修改自己的，也就是说，修改了之后对同类的其他对象没有影响；
2、动态修改类属性可以用类名.属性 = xxx来进行修改；
3、修改的类属性一般会影响所辖对象的属性，除非对象在此之前对该属性进行过修改。
"""