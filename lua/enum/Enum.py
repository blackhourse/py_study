#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 17:21
# @Author  : MaHongTao
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Sun
print(day1)
day2 = Weekday.Mon
print(day2)
print(day1 == day2)
print(Weekday(1))
for name, member in Weekday.__members__.items():
    print(name, '--', member)


# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
class Gender(Enum):
    Male = 0
    Female = 1


Gender = Enum('Gender', ('Male', 'Female'))


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


for sex, member in Gender.__members__.items():
    print(sex,Gender(member), '---', member)
