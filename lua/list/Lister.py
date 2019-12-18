import os

names = ['ma', 'tang', 'wang']
for name in names:
    print(name)

r = []
i = 3
range(3)
for i in range(3):
    r.append(names[i])
print(r)

names[0:2]
print(names[0:9])
print(names[:3])
print(names[:-1])
print(names[-1])
print(names[-1:])
print(names[-1: -2])

L = list(range(10))
print(L)

# str = 'ABCDEFG'
# print(str[:2])
print('ABCDEFG'[:3])
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
str2 = 'avbbfdgfagaga'
print(str2[1:-1])
print(str2[1:])
print(str2[:1])


def trim(st):
    if st[:1] == ' ':
        return trim(st[1:])
    elif st[-1:] == ' ':
        return trim(st[:-1])
    else:
        return st


a = trim(' hello world ')
print(a)


def FinMaxAndmin(L):
    if L == []:
        return (None, None)
    else:
        b = c = L[0]
        for n in L:
            if b < n:
                b = n
            if c > n:
                c = n
        return (c, b)


L = [10, 20, 3, 4]
print(FinMaxAndmin(L))

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

print([x + y for x in ['A', 'B', 'C'] for y in ['X', 'Y', 'Z']])
print([d for d in os.listdir('C:\\')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

list1 = ['Hello', 'World', 18, 'Apple', None]
list2 = [item.lower() for item in list1 if isinstance(item, str)]
print(list2)

print([a.lower() for a in list1 if isinstance(a, str)])
