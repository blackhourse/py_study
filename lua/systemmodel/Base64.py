#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 14:19
# @Author  : MaHongTao
# Base64是一种用64个字符来表示任意二进制数据的方法。
#
# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。
#
# Base64的原理很简单，首先，准备一个包含64个字符的数组：
#
# ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
# 然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
#
# base64-encode
#
# 这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。
#
# 所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。
#
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
import base64

strToEccode = base64.b64encode(b'hello,world')
print('字符串 转base64 %s' % strToEccode)
s = base64.b64decode(b'aGVsbG8sd29ybGQ=')
print(s)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

b = base64.urlsafe_b64encode(b'hello')
print(b)
print(b)

# 请写一个能处理去掉=的base64解码函数：


def safe_base64_decode(s):
    if len(s) % 4 == 0:  # 判断参数长度是否整除4

        if isinstance(s, str):  # 整除了但是有可能传入的参数是字符串，而不是byte类型

            s = s.encode(s)  # 转换为byte类型

        b = base64.b64decode(s)  # 进行解码

    else:

        k = len(s) % 4

        if isinstance(s, str):  # 不能整除4且传入的参数为字符串，那么就需要对字符串进行类型转换

            for i in range(k):  # 根据余数，使用for循环需要补多少个'='

                s = s + '='

                s = s.encode()  # 转换为byte类型

        else:

            for i in range(k):
                s = s + b'='

        b = base64.b64decode(s)

    return b


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')

assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')

print('ok')


