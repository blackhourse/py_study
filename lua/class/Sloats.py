#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 13:58
# @Author  : MaHongTao
from types import MethodType


class Student(object):
    pass


s = Student()

s.name = 'adfa'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给当前实例绑定一个方法， 只对当前这个实例 生效
s.age = 25
print(s.age)


# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Perple(object):
    __slots__ = ('name', 'age')


a = Perple()
a.name = 'niko'
a.age = 25
# a.sex = 1             报错
