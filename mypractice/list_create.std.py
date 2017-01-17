Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print [x for x in range(0,10)]
SyntaxError: invalid syntax
>>> [x for x in range(0,10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x for x in range(0,10) if x%2 == 0]
[0, 2, 4, 6, 8]
>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    [s.lower() for s in L]
  File "<pyshell#4>", line 1, in <listcomp>
    [s.lower() for s in L]
AttributeError: 'int' object has no attribute 'lower'
>>> [s.lower() for s in L if isinstance(s,str)]
['hello', 'world', 'apple']
>>> 
