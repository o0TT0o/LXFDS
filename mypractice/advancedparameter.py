#!/usr/bin/env python
# -*- coding: utf-8 -*-

def person(*args, **kw):
    print 'b:', args, 'a:', kw

name = u'qinting'
age = 25
city = u'Shanghai'
job = u'Programmer'
base = [name,age]
advanse = {'city':city,'job':job}

#person(name,age,city=kw['city'],job=kw['job'])
person(*args,**kw)
