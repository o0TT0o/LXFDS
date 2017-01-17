#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 读入 =》【解码】 =》 处理 =》 【编码】 =》 输出

import sys

print u'你好冒险者，我是穆，请问你是'
name = u''
name = raw_input(u"请输入你的姓名:").decode(sys.stdin.encoding)                                                         #无论系统读入还是文件读入，都先转成unicode
print u'[DBG] sys.stdin.encoding=%s'%sys.stdin.encoding
print name
target = open(r'C:\Users\qinting\Documents\LXF_python\tmp.txt','w')
target.write(name.encode('utf-8'))                                                                                     #写出文件时，把字符串转为指定格式，建议utf-8
target.close()
print u'[DBG] name=%s'%name
print u'[DBG] len(name)=%s'%(len(name))
print u'%s你好，真是一个不错的名字，欢迎来到%s' %(name,u"法兰城")                                                        #字符串传给print打印时，用unicode就行
