#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 11:06
# @Author  : MaHongTao


# ?实现Web应用程序的WSGI处理函数：
def applocation(envi, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>hello,world</h1>']
