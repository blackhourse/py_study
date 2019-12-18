# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

name = ['jack', 'tom', 'joy']
age = [12, 13, 14]
people = {'jack': 12, 'tom': 13, 'joy': 14};
print(people)
print(people.get('tom'))
print(people.get('aa'))  # key不存在时 返回none
print('aa' in people)
print(people.get('aa'), -11)  # 指定 自定义的值

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
people.pop('joy')
print(people)

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。


# 要创建一个set，需要提供一个list作为输入集合：
s1 = set([1, 2, 3, 4])
print(s1)
s1.add(1)
print(s1)
s1.add(5)
print(s1)

s1.remove(4)
print(s1)

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
a.replace('a', 'A')
print(a)
