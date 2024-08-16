Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup=(21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1]=3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1]=3
TypeError: 'tuple' object does not support item assignment
>>> s={22,25,14,21,5}
>>> s
{5, 14, 21, 22, 25}
>>> s={25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> 