Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> id(num)
1855977456
>>> name='navin'
>>> id(name)
67105216
>>> a=10
>>> b=a
\
>>> b
10
>>> a
10
>>> 1d(a)
SyntaxError: invalid syntax
>>> id(a)
1855977536
>>> id(b)
1855977536
>>> id(10)
1855977536
>>> k=10
>>> id(10)
1855977536
>>> id(k)
1855977536
>>> a=9
>>> id(a)
1855977520
>>> id(b)
1855977536
>>> k=a
>>> id(k)
1855977520
>>> b=8
>>> PI=3.14
>>> PI
3.14
>>> PI=3.15
>>> type(PI)
<class 'float'>
>>> 