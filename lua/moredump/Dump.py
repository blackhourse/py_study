#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 16:13
# @Author  : MaHongTao
import os
from multiprocessing import Process

pid = os.getppid()
print('pid: %s' % pid)


# c = os.fork()


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

print('hello,%s %s %s' % ('fa' ,21,'ddddddd'))
print("My name is %s and weight is %d kg!" % ('Zara', 21))
