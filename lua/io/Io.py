#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 15:01
# @Author  : MaHongTao
import json
import os

file = open('C:/Users/Administrator/Desktop/新建文本文档.txt', 'rb')

print(file.read())

s = os.name
print(s)
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
