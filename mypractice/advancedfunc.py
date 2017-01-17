#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

'''
map
'''
inputeng = ['adam', 'LISA', 'barT']
print map(lambda x: x.upper(),inputeng)

'''
reduce
'''
numlist = [1,2,3,4,5,6,7,8,9]
print reduce(lambda x,y:x*y,numlist)


'''
filter
'''
def is_prime(n):
    #print n
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print filter(is_prime,range(1,101))

'''
sorted
'''
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
