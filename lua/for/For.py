# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来

lista = ['A', 'b', 'c', 'd']
for a in lista:
    print(a)

#  循环累加
sum = 0
numa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for na in numa:
    sum += na
print(sum)

# range()  生成连续的数字  也可以指定开始数字
numb = range(0, 11);
print(numb)
sumb = 0
for na in numb:
    print(na)
    sumb += na
print(sumb)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 5
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 练习 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']

L = ['Bart', 'Lisa', 'Adam']
for a in L:
    print('HELLO,', a)

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
