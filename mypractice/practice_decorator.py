#!/usr/bin/env python
# -*- coding: utf8 -*-

def decorator_log(func):
    def wrapper(*args,**kwargs):
        print 'fun.__name__:',func.__name__
        return func(*args,**kwargs)
    return wrapper


def logged(func):
    def with_logging(*args, **kwargs):
        print func.__name__ + " was called"
        return func(*args, **kwargs)
    return with_logging

@logged
@logged
@logged
def write_log(logcontent):
    print 'logcontent:',logcontent
    return None


if __name__ == '__main__':
    result = 'I want to print a log.'

    print 'result:',result

    #result = write_log('I want to print a log with a function.')

    write_log = logged(write_log)
    result = write_log('I want to print a log and function name with a function.')