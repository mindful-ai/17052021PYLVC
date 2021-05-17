Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input()
834
'834'
>>> n = input()
23
>>> n
'23'
>>> n = input("Enter a number: ")
Enter a number: 45
>>> n
'45'
>>> n + 10
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    n + 10
TypeError: can only concatenate str (not "int") to str
>>> type(n)
<class 'str'>
>>> n = int(n)
>>> n + 10
55
>>> n = float(input("Enter a number:"))
Enter a number:45
>>> n
45.0
>>> n + 8
53.0
>>> 
