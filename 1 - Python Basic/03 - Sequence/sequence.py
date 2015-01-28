__author__ = 'crixalis'
# coding:utf-8
#!/usr/bin/env python
"""
sequence(序列)是一组有顺序的元素的集合

(严格的说，是对象的集合，但鉴于我们还没有引入“对象”概念，暂时说元素)

序列可以包含一个或多个元素，也可以没有任何元素。

我们之前所说的基本数据类型，都可以作为序列的元素。元素还可以是另一个序列，以及我们以后要介绍的其他对象。
"""

#序列有两种：tuple（定值表； 也有翻译为元组） 和 list (表)
s1=(2,1.3,'love',5.6,9,12,False)   #s1是一个tuple
s2=[True,5,'smile']                #s2是一个list
print s1,type(s1)
print s2,type(s2)

#tuple和list的主要区别在于，一旦建立，tuple的各个元素不可再变更，而list的各个元素可以再变更。

#一个序列作为另一个序列的元素
s3=[1,[3,4,5]]
#空序列
s4=[]
print s3
print s4




