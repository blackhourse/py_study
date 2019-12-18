#  过滤函数


def abc(n):
    if n % 2 == 0:
        return n


a = list(filter(abc, [1, 2, 3, 4, 5, 6, 7, 8]))
print(a)


def not_empty(s):
    return s and s.strip


b = list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))
print(b)


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 20:
        print(n)
    else:
        break
