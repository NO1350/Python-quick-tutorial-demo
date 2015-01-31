__author__ = '100068'
# coding:utf-8
#!/usr/bin/env python
#Python使用类(class)和对象(object)，进行面向对象（object-oriented programming，简称OOP）的编程。
#面向对象的最主要目的是提高程序的重复使用性。
#在人类认知中，会根据属性相近把东西归类，并且给类别命名。
#当括号中为object时，说明这个类没有父类（到头了）
class Bird(object):
    have_feather=True
    way_of_reproduction='egg'
    def move(self,dx,dy):
        position=[0,0]
        position[0]=position[0]+dx
        position[1]=position[1]+dy
        return position

summer=Bird()
print 'after move:',summer.move(5,8)
#对属性的引用是通过 对象.属性（object.attribute） 的形式实现的。
#对象=属性+方法（行为）

#继承(inheritance)通过继承制度，我们可以减少程序中的重复信息和重复语句.因此，面向对象提高了程序的可重复使用性。
class Chicken(Bird):
    way_of_move='walk'
    possible_in_KFC=True

class Oriole(Bird):
    way_of_move='fly'
    possible_in_KFC=False

summer = Chicken()
print summer.have_feather
print summer.way_of_move
print summer.move(5,8)

"""
Summary
将东西根据属性归类 ( 将object归为class )

方法是一种属性，表示动作

用继承来说明父类-子类关系。子类自动具有父类的所有属性。

self代表了根据类定义而创建的对象。



建立对一个对象： 对象名 = 类名()

引用对象的属性： object.attribute
"""

"""
参数不一定必须是self，可以指定为任何名字的参数，取为sel、this、it等等都可以，python中原意是为：类中的方法第一个参数必须是调用该方法的对象本身，由于大家都习惯用self，所以很多教材都说必须用self，这种说法是不准确的。

"""