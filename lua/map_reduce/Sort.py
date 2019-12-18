# 假设我们用一组tuple表示学生名字和成绩：
# 请用sorted()对上述列表分别按名字排序：


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def name_score(t):
    def getName(t):
        return t[0]

    def getScore(t):
        return t[1]

    return sorted(t, key=getName)


print(name_score(L))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def paixi(t):
    def by_name(t):
        return t[0]

    def by_core(t):
        return t[1]

    # return sorted(t, key=by_name, reverse=True)
    return sorted(t, key=by_core)


print(paixi(L))


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = list(count())
print(f1)
print(f2)
print(f3)


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    s = [0]

    def counter():
        s[0] = s[0] + 1
        return s[0]

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(),

    (), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(filter(lambda x: x % 2 == 1, range(1, 10))))
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


print(now())
