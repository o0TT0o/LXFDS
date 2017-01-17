#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_err():
    fs = []
    for i in range(1, 4):
        print 'DBG i = %s'%i
        def f():
            return i*i
        fs.append(f)
        print 'DBG fs = %s'%fs
    return fs


def count():
    fs = []
    for i in range(1, 4):
        print 'DBG i = %s'%i
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
        print 'DBG fs = %s'%fs
    return fs


f1, f2, f3 = count()
print f1(),f1
print f2(),f2
print f3(),f3

f1, f2, f3 = count_err()
print f1(),f1
print f2(),f2
print f3(),f3
