#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 14:18
# @Author  : MaHongTao
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        # return self.width * self.height
        return '100'


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


class Abd(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    __repr__ = __str__

    def __iter__(self):
        return self

    def __next__(self):
        return


print(Abd('mahongtao'))
print(Abd('mahongtao'))


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, item):
        a, b = 1, 1
        for i in range(item):
            a, b = b, a + b
        return a


for n in Fib():
    print(n)
print(Fib()[3])
#

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        if attr == 'grade':
            return '11'
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)

#
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, user ):
        return Chain('%s/%s' % (self._path, user))

    __repr__ = __str__

user = "michael"
path = Chain().users(user).repos

assert  "%s"%path == "/users/%s/repos"%(user)