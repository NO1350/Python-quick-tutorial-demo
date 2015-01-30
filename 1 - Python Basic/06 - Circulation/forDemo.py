__author__ = 'crixalis'
# coding:utf-8
#!/usr/bin/env python

for a in [3,4.4,'life']:
    print a


#range这个函数的功能是新建一个表。这个表的元素都是整数，从0开始，下一个元素比前一个大1， 直到函数中所写的上限 （不包括该上限本身）
#python3.2中range生成了一个iterator,要转换成list的类型，如list(range(10))
for a in range(10):
    print a**2

# 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作
for i in range(10):
    if i==2:
        continue
    print i

# break停止执行整个循环
for i in range(10):
    if i == 2:
        break
    print i