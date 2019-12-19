#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 17:47
# @Author  : MaHongTao
# @desc  ： 系统工具类

from datetime import datetime, timedelta

#  获取当前日期和时间
nowtime = datetime.now()
print(nowtime)
print(type(nowtime))  # datetime 的类型

# 获取指定日期和时间
s = datetime(2018, 1, 1, 12, 59, 59)
print(s)
print(s.timestamp())
#  datetime 转 时间戳  datetime.timestamp()
print(datetime.now().timestamp())

# 时间戳 转 datetime
print(s.fromtimestamp(1514782799.0))

# 字符串转 datetime
str = '2019-1-1 12:22:33'
abc = datetime.strptime(str, '%Y-%m-%d %M:%H:%S')
print(abc)

# datetime 转str
now = datetime.now()
timeStr = now.strftime('%a,%b %M:%H:%S')
print(timeStr)

# datetime  加减   + ——   timedelta(args[])  参数可以传递  时分秒  天
s = datetime(2018, 1, 1, 12, 59, 59)
print(s)
# s1 = s + timedelta(minutes=1)
s1 = s + timedelta(seconds=1)
s1 = s + timedelta()
print(s1)
