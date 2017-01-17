# -*- coding: utf8 -*-
import functools

#its a decorator
#   用装饰器打印变量
def logger(x): #先提取 logger 附带的参数，留下函数名继续传入
    def descorator(func): #函数在此传入
        @functools.wraps(func)
        def wrapper(*args,**kw): #这里传入 函数 需要的参数
            print "[call] ",func.__name__,", args ",x
            return func(*args,**kw) #组合函数及其参数一起返回出去
        return wrapper
    return descorator

print """
#闭包实验1：
# 参数 i 直接传入 子函数 f
"""
def count1():
    fs = []
    for i in range(1, 4):
        @logger(None)
        def f():
            print "[check] i =",i
            return i*i
        fs.append(f)
        print f.__name__ # because of @functools.wraps(func) ,print f ,else print wrapper
    return fs

for index,f in enumerate(count1()):
    print "count1.F%s result = %s\n"%(index,f())
print "[说明] 如上可以看出，闭包的内部变量的值为运行完所有循环后的结果，如果直接用f计算参数，会导致取值为循环最终结果  3"



print """
#闭包实验2：
# 参数 i 经过函数 fun_for_args 传递后转为 j 再被子函数 f 使用
"""
def count2():
    fs = []
    for i in range(1, 4):
        @logger(i)
        def fun_for_args(j):
            @logger(j)
            def f():
                print "[check] i =",i
                return j*j
            return f
        fs.append(fun_for_args(i)) #这里的变量赋值是关键
    return fs

for index,f in enumerate(count2()):
    print "count1.F%s result = %s funname = %s\n"%(index,f(),count2.__name__)
print "[说明] 如上可以看出，闭包的内部变量的值被函数 fun_for_args 获取并保存，传递给 f 时的值为 1 2 3。未被单独保存的变量 i 的值 仍为循环的最终结果 3"


