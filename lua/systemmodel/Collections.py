#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 10:27
# @Author  : MaHongTao

# collections是Python内建的一个集合模块，提供了许多有用的集合类。
from collections import namedtuple, deque, defaultdict, Counter

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
#
# 可以验证创建的Point对象是tuple的一种子类：
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
x = p.x
y = p.y
z = '11'
print('a:%s,b:%s,z:%s' % (x, y, z))

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

q = deque(['5', '28', '34'])
q.append('x')
print(q)
q.appendleft('y')
print(q)
for n in q:
    print(n)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# dd = defaultdict['a', 'd', 'c']
dd = defaultdict(lambda: 'N/A')
dd['key1'] = '123'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#
# 如果要保持Key的顺序，可以用OrderedDict：
dict1 = dict([('key1', 1), ('key2', 2), ('key3', 3)])
print(dict1)

d = dict([('a', 1), ('b', 2), ('c', 3)])

print(d)

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：


c = Counter()
print('c:%s' % c.items())
for ch in 'hello,world':
    c[ch] = c[ch] + 1

print(c)  #Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ',': 1, 'w': 1, 'r': 1, 'd': 1})