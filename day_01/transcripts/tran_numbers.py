Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Numbers
>>> 
>>> a = 5
>>> type(a)
<class 'int'>
>>> b = 1.4
>>> type(b)
<class 'float'>
>>> c = -5
>>> type(c)
<class 'int'>
>>> # --------------------------- Operators
>>> 
>>> # Arithmetic operators
>>> 
>>> x = a + c
>>> x
0
>>> x = a + 6
>>> x
11
>>> a - 5
0
>>> a - 3
2
>>> a * 4
20
>>> a / 4
1.25
>>> a % 4
1
>>> a // 4
1
>>> a // 2
2
>>> a ** 2
25
>>> a ** 3
125
>>> # Relational operators
>>> 
>>> True
True
>>> False
False
>>> None
>>> 
>>> a > 5 # Is a greater than 5?
False
>>> a < 5
False
>>> a == 5
True
>>> a <= 5
True
>>> a >= 5
True
>>> a != 5
False
>>> 
>>> a ** 2 == (c + 10) * (c + 10)
True
>>> 
>>> # Logical operators
>>> 
>>> a >= 5 and a**2 == 25
True
>>> a > 5 and a**2 == 25
False
>>> a > 5 or a**2 == 25
True
>>> not(a > 5) and a**2 == 25
True
>>> 
>>> 
>>> # ---------------------------- in-built functions
>>> 
>>> a = 8
>>> b = 14
>>> a - b
-6
>>> b - a
6
>>> abs(a - b)
6
>>> abs(b - a)
6
>>> a = 100
>>> type(a)
<class 'int'>
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> bin(a)
'0b1100100'
>>> 
>>> 
>>> s = '1234'
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> type(s)
<class 'str'>
>>> s1 = int(s)
>>> s2 = float(s)
>>> type(s1)
<class 'int'>
>>> type(s2)
<class 'float'>
>>> s1 * 4
4936
>>> s2 + 192
1426.0
>>> 
>>> 
>>> s = "3.14"
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '3.14'
>>> float(s)
3.14
>>> x = "4..56"
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: '4..56'
>>> float(x)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    float(x)
ValueError: could not convert string to float: '4..56'
>>> 
>>> 
>>> 
>>> s = "11101001"
>>> int(s)
11101001
>>> int(s, 2)
233
>>> 
>>> 
>>> a
100
>>> chr(a)
'd'
>>> ord('d')
100
>>> # -------------------- built in modules
>>> 
>>> sqrt(100)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    sqrt(100)
NameError: name 'sqrt' is not defined
>>> import math
>>> sqrt(100)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    sqrt(100)
NameError: name 'sqrt' is not defined
>>> math.sqrt(100)
10.0
>>> a = 90
>>> math.sin(a)
0.8939966636005579
>>> math.sin(a * 3.14/180)
0.9999996829318346
>>> math.sin(a * 3.14159/180)
0.9999999999991198
>>> math.sin(a * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> 
>>> 
>>> 
>>> import random
>>> random.randint(1, 100)
74
>>> random.randint(1, 100)
84
>>> random.randint(1, 100)
80
>>> random.randint(1, 100)
26
>>> random.randint(1, 100)
21
>>> random.randint(1, 100)
88
>>> # ------------------------ test
>>> 
>>> a = 10
>>> b = math.sqrt(a)
>>> a
10
>>> b
3.1622776601683795
>>> a == b*b
False
>>> a = float(a)
>>> a == b*b
False
>>> a
10.0
>>> b*b
10.000000000000002
>>> 
