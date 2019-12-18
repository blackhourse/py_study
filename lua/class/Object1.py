#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:34
# @Author  : MaHongTao

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


a = Student('mahongtao', 100)
b = Student('wangwu', 99)
c = Student('lisi', 88)
print(a.print_score())
print(b.print_score())
print(c.print_score())
print(a.name)


# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self._gender = gender

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        if gender == 'female' or gender == 'male':
            self._gender = gender
        else:
            raise ValueError('error gender')


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败a!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'femgale':
        print('测试失败d!')
    else:
        print('测试成功!')


class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):
    # def run(self):
    #     print('Dog is running...')
    pass


class Cat(Animal):
    # def run(self):
    #     print('Cat is running...')
    pass


dog = Dog()
cat = Cat()
dog.run()
cat.run()
