# def f(x):
#     return x * x
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
a = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def normalize(name):
    return name.title()


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

