Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SETS
>>> 
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'p', 'i', 's', 'm'}
>>> 
>>> 
>>> set("abcdefgh")
{'a', 'e', 'h', 'g', 'f', 'c', 'b', 'd'}
>>> 
>>> s1 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
>>> s1
{'a', 'e', 'h', 'g', 'f', 'c', 'b', 'd'}
>>> s1
{'a', 'e', 'h', 'g', 'f', 'c', 'b', 'd'}
>>> s1[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable
>>> type(s1)
<class 'set'>
>>> 
>>> 
>>> # ------------------------ operators
>>> 
>>> s1
{'a', 'e', 'h', 'g', 'f', 'c', 'b', 'd'}
>>> s2 = set("defghijkl")
>>> s2
{'e', 'h', 'g', 'j', 'k', 'i', 'f', 'd', 'l'}
>>> s1 | s2
{'a', 'e', 'h', 'g', 'f', 'c', 'j', 'k', 'i', 'b', 'd', 'l'}
>>> s1 & s2
{'e', 'h', 'g', 'f', 'd'}
>>> s1 ^ s2
{'a', 'b', 'c', 'j', 'k', 'i', 'l'}
>>> 
>>> 'a' in s1
True
>>> s1 + s2
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> 
>>> 
>>> # --------------------- functions
>>> 
>>> s1
{'a', 'e', 'h', 'g', 'f', 'c', 'b', 'd'}
>>> s1.add('x')
>>> s1
{'a', 'e', 'h', 'x', 'g', 'f', 'c', 'b', 'd'}
>>> s3 = {'y', 'z'}
>>> s1.update(s2)
>>> s1
{'a', 'e', 'h', 'x', 'g', 'f', 'c', 'j', 'k', 'i', 'b', 'd', 'l'}
>>> s1.update(s3)
>>> s1
{'a', 'e', 'y', 'h', 'x', 'g', 'f', 'c', 'j', 'z', 'k', 'i', 'b', 'd', 'l'}
>>> s1.add('a')
>>> s1
{'a', 'e', 'y', 'h', 'x', 'g', 'f', 'c', 'j', 'z', 'k', 'i', 'b', 'd', 'l'}
>>> 
>>> s1.remove('a')
>>> s1
{'e', 'y', 'h', 'x', 'g', 'f', 'c', 'j', 'z', 'k', 'i', 'b', 'd', 'l'}
>>> 
>>> 
>>> # ---------------------------------- force sorting
>>> 
>>> s
'mississippi'
>>> S1
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    S1
NameError: name 'S1' is not defined
>>> s1
{'e', 'y', 'h', 'x', 'g', 'f', 'c', 'j', 'z', 'k', 'i', 'b', 'd', 'l'}
>>> s1.sort()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s1.sort()
AttributeError: 'set' object has no attribute 'sort'
>>> sorted(s1)
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'x', 'y', 'z']
>>> s1
{'e', 'y', 'h', 'x', 'g', 'f', 'c', 'j', 'z', 'k', 'i', 'b', 'd', 'l'}
>>> 
>>> 
>>> 
>>> # -----------------------------------
>>> 
>>> 
>>> import random
>>> RN = []
>>> for i in range(100):
	RN.append(random.randint(1, 40))

	
>>> RN
[13, 16, 23, 8, 33, 16, 30, 25, 40, 28, 7, 37, 7, 10, 10, 13, 34, 31, 7, 18, 13, 9, 22, 6, 3, 26, 15, 40, 40, 6, 27, 13, 14, 11, 17, 9, 17, 33, 20, 38, 3, 32, 17, 22, 36, 36, 40, 25, 31, 1, 2, 29, 28, 24, 20, 6, 22, 30, 39, 26, 13, 28, 39, 25, 36, 25, 37, 38, 10, 14, 30, 27, 5, 35, 11, 36, 19, 37, 16, 16, 33, 1, 19, 13, 17, 7, 36, 29, 19, 19, 23, 15, 16, 37, 31, 9, 10, 35, 38, 29]
>>> len(RN)
100
>>> set(RN)
{1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40}
>>> len(set(RN))
37
>>> 
>>> LR = list(range(1, 41))
>>> LR
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
>>> LS = list(set(RN))
>>> LR
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
>>> LS
[1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
>>> 
>>> set(LR) ^ set(LS)
{4, 12, 21}
>>> 
