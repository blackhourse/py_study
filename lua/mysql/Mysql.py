#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 17:21
# @Author  : MaHongTao


import mysql.connector

# 注意把password设为你的root口令:
conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password='123456', database='pig')

# conn = mysql.connector.connect(user='root', password='123456', database='pig')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
