#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 11:09
# @Author  : MaHongTao

# 编写一个server.py，负责启动WSGI服务器，加载application()函数：
from wsgiref.simple_server import make_server

from lua.web.hello import applocation

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, applocation)
print('Server Http port is 8000')
httpd.serve_forever()
