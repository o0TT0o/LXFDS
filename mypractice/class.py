#!/usr/bin/env python
# -*- coding:utf8 -*-
import functools
__author__ = 'qinting'

def logger(func):
    print func.__name__
    return func

class Animal(object):
    def __init__(self,kind='unknown',*args,**kw):
        self.__kind = kind

    def set_act(self,action='nothing',*args,**kw):
        self.__action = action

    def get_act(self):
        print '%s is %s'%(self.__kind,self.__action)
    def run(self):
        print 'Animal is running...'


class Cat(Animal):
    def yell(self):
        print 'Wangwangwangwang...'
    def run(self):
        print 'Cat is running...'
        
class Dog(Animal):
    def bark(self):
        print 'Miaomiaomiaomiao...'
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'
        
class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'

class SB(Animal):
    pass
        
def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == '__main__':
    cat = Cat(kind='cat')
    dog = Dog(kind='dog')
    cat.set_act(action='watching')
    dog.set_act(action='running')
    cat.get_act()
    dog.get_act()
    cat.yell()
    dog.bark()
    #偏函数
    isinstance_cat = functools.partial(isinstance,cat)
    print 'isinstance_cat(Cat) :',isinstance_cat(Cat)
    print 'isinstance_cat(Animal) :',isinstance_cat(Animal)
    print 'isinstance(animal,Cat) :',isinstance(Animal(),Cat)
    run_twice(Animal())
    run_twice(cat)
    run_twice(dog)
    run_twice(Tortoise())
    run_twice(SB())
