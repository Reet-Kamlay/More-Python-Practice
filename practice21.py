Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=2.5
>>> type(num)
<class 'float'>
>>> num=5
>>> type(num)
<class 'int'>
>>> num=6+9j
>>> type(num)
<class 'complex'>
>>> a=5.6
>>> b=int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k=float(b)
>>> k
5.0
>>> k=6
>>> c=complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> bool=b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> int(True)
1
>>> int(False)
0
>>> 1st=[25,36,45,12]
SyntaxError: invalid syntax
>>> lst=[25,36,45,12]
>>> type(lst)
<class 'list'>
>>> s={25,36,45,15,12,25}
>>> s
{36, 12, 45, 15, 25}
>>> type(s)
<class 'set'>
>>> t=(25,36,4,57,12)
>>> type(t)
<class 'tuple'>
>>> str="navin"
>>> type(str)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range(10))
<class 'range'>
>>> d={'Navin':'Samsung','rahul':'Iphone','kiran';'oneplus'}
SyntaxError: invalid syntax
>>> d={'navin':'samsung','rahul':'Iphone','kiran':'oneplus'}
>>> d
{'navin': 'samsung', 'rahul': 'Iphone', 'kiran': 'oneplus'}
>>> d.keys(d)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d.keys(d)
TypeError: keys() takes no arguments (1 given)
>>> d.keys()
dict_keys(['navin', 'rahul', 'kiran'])
>>> d.values()
dict_values(['samsung', 'Iphone', 'oneplus'])
>>> d['rahul']
'Iphone'
>>> d.get('kiran')
'oneplus'
>>> 