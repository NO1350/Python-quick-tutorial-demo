__author__ = 'crixalis'
#coding:utf-8
#!/usr/bin/env python
a=10
print a   #Python的变量不需要声明，不需要删除，可以直接回收适用
print type(a)  #内置函数type(), 用以查询变量的类型。
print a,type(a) #print后跟多个输出，以逗号分隔。

b=10 #int整型
b=1.3 #float 浮点数
b=True #真值(True/false)
b="Hello!" #字符串

a=3-2j
b=2+1j
print a+b

for a in range(10):  #for是把iterator生成的值赋予给a，然后再使用a，因此不用声明
    print a

print
a=-1/5
print a