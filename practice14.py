Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> x=2
>>> x+3
5
>>> y=3
>>> x+y
5
>>> x=9
>>> x+y
12
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x+10
19
>>> _+y
22
>>> name='youtube'
>>> name
'youtube'
>>> name+'rocks'
'youtuberocks'
>>> name'rocks'
SyntaxError: invalid syntax
>>> name[0]
'y'
>>> name[6]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[-1]
'e'
>>> name[-2]
'b'
>>> name[-7]
'y'
>>> name[0:2]
'yo'
>>> name[1:4]
'out'
>>> name[1:]
'outube'
>>> name[:4]
'yout'
>>> name[3:10]
'tube'
>>> name[0:3]='my'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name[0:3]='my'
TypeError: 'str' object does not support item assignment
>>> name[0]='R'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    name[0]='R'
TypeError: 'str' object does not support item assignment
>>> 'my'+name[3:]
'mytube'
>>> myname='Navin Reddy'
>>> len(myname)
11
>>> 