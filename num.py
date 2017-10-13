# -*- coding:utf8 -*-
''' Create on "2017/10/13 16:23"
    _author_="zhao ling"
    Poject: 数值计算层
 '''
# 全部用面向对象的方法实现
class number(object):
    ''' add '''
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def __str__(self): #  What uses?
        self.name = 'add'