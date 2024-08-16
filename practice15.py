Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums=[25,12,36,95,14]
>>> nums
[25, 12, 36, 95, 14]
>>> nums[0]
25
>>> nums[54\]
     
SyntaxError: unexpected character after line continuation character
>>> nums[54\]
     
SyntaxError: unexpected character after line continuation character
>>> nums[54]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    nums[54]
IndexError: list index out of range
>>> nums[4]
14
>>> 14
14
>>> nums[2]
36
>>> nums[2:]
[36, 95, 14]
>>> nums[-1]
14
>>> nums[-5]
25
>>> names=['Navin','Kiran','John']
>>> names
['Navin', 'Kiran', 'John']
>>> values=[9.5,'Navin',25]
>>> values
[9.5, 'Navin', 25]
>>> type(values)
<class 'list'>
>>> a=1
>>> type(a)
<class 'int'>
>>> mil=[nums,names]
>>> mil
[[25, 12, 36, 95, 14], ['Navin', 'Kiran', 'John']]
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45]
>>> nums.pop()
45
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend(29,12,14,36)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    nums.extend(29,12,14,36)
TypeError: extend() takes exactly one argument (4 given)
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> 