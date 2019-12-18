# 自定义函数

sum = 0


def aaa(x):
    if x <= 0:
        return -x;
    else:
        return x;


# print(aaa(10))


# 空函数   也可以用于 todo
def nothing():
    pass


# 返回多个值
def cal(wid, hig, long):
    s1 = wid + hig + long
    s2 = wid * hig * long
    return s1, s2


a, b = cal(1, 2, 5)
print(a)
print(b)


def cal2(x, y):
    s = 1
    while y > 0:
        y = y - 1
        s = s * x
    return s;


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 3))
print(cal2(5, 3))


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())
a = add_end([1, 2, 3])
print(a)
b = add_end(['x', 'y', 'z'])
print(b)


# 111111
def product(x, y, *a):
    return x * y


# print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))


# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


# 递归函数
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(10))


def facter(x, y):
    if x == 1:
        return y
    return facter(x - 1, x * y)


def a(x):
    return facter(x, 1)


print(a(100))

print(facter(10,1))


# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b)
        print(a, '-->', c)
        hanoi(n-1, b, a, c)


print(hanoi(3, 'a', 'b', 'c'))
