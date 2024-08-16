Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data={1:'Navin',2:'Kiran',4:'Harsh'}
>>> data
{1: 'Navin', 2: 'Kiran', 4: 'Harsh'}
>>> data[4]
'Harsh'
>>> data[1]
'Navin'
>>> data[3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[3]
KeyError: 3
>>> data.get(1)
'Navin'
>>> data.get(3)
>>> print(data.get(3))
None
>>> data.get(1)
'Navin'
>>> data.get(1,'Not Found')
'Navin'
>>> data.get(3,'Not Found')
'Not Found'
>>> keys=['Navin','Kiran','Harsh']
>>> values=['Python','Java','JS']
>>> data=dict(zip(keys,values))
>>> data
{'Navin': 'Python', 'Kiran': 'Java', 'Harsh': 'JS'}
>>> data['Kiran']
'Java'
>>> data['Monika']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data['Monika']
KeyError: 'Monika'
>>> data['Monika']='CS'
>>> data
{'Navin': 'Python', 'Kiran': 'Java', 'Harsh': 'JS', 'Monika': 'CS'}
>>> del data['Harsh']
>>> data
{'Navin': 'Python', 'Kiran': 'Java', 'Monika': 'CS'}
>>> 