print('数组的基本操作')
classmates = ['a', 'b', 'c', 'd', 'e']

classmates2 = ['a',]
print(classmates2)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])

print(classmates[-1])  # 倒数第一个  可以用 -1  取值
print(classmates[-2])
print(classmates[-5])
##########


classmates.append('niko')
print(classmates)

# classmates.clear()  # 清楚所有元素
print(classmates)
a = classmates.copy()  # 复制数组
print(a)
print(classmates)

print(classmates.count('g'))  # count 统计出  数字元素为  g 的个数
s = ['n']
s.extend(classmates)  # 数组继承
print(s)

print(classmates.index('c'))
# classmates.insert(0,'b')  # 相当于替换
print(classmates)
print("11")
classmates.pop(-1)  # 移除指定位置数据
print(classmates)
# classmates.append(s)  # 数组里的 对象也可以是数组
print(classmates)
# classmates.reverse()
print(classmates)
# classmates.sort('1', '1')  # 排序
print(classmates)


A =  classmates.__contains__('b')
print(A)



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


C = (1)
print(C)














