Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for c in "python":
	print(c)

	
p
y
t
h
o
n
>>> for item in ["red", "green", "blue"]:
	print(item)

	
red
green
blue
>>> T = ("red", "green", "blue")
>>> for item in sorted(T):
	print(t.upper())

	
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    print(t.upper())
NameError: name 't' is not defined
>>> for item in sorted(T):
	print(item.upper())

	
BLUE
GREEN
RED
>>> S = set("abcdef")
>>> for elem in S:
	print(elem, end=' ')

	
d e c f b a 
>>> 
>>> D = {"name":"anil", "age":35, "company":"oracle"}
>>> for item in D:
	print(item)

	
name
age
company
>>> for item in D.keys():
	print(item)

	
name
age
company
>>> for value in D.value():
	print(value)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    for value in D.value():
AttributeError: 'dict' object has no attribute 'value'
>>> for value in D.values():
	print(value)

	
anil
35
oracle
>>> 
>>> D1 = {}
>>> D
{'name': 'anil', 'age': 35, 'company': 'oracle'}
>>> for key,value in D.items():
	D1.setdefault(value, key)

	
'name'
'age'
'company'
>>> D1
{'anil': 'name', 35: 'age', 'oracle': 'company'}
>>> 
>>> D
{'name': 'anil', 'age': 35, 'company': 'oracle'}
>>> D.setdefault("country", "india")
'india'
>>> D.items()
dict_items([('name', 'anil'), ('age', 35), ('company', 'oracle'), ('country', 'india')])
>>> 
>>> 
>>> 
>>> 
>>> # ----------------- while loop
>>> 
>>> i = 0
>>> while i < 10:
	print(i ** 2, '*'*i+1)
	i += 1

	
Traceback (most recent call last):
  File "<pyshell#50>", line 2, in <module>
    print(i ** 2, '*'*i+1)
TypeError: can only concatenate str (not "int") to str
>>> while i < 10:
	print(i**2, '*'*(i+1))
	i += 1

	
0 *
1 **
4 ***
9 ****
16 *****
25 ******
36 *******
49 ********
64 *********
81 **********
>>> while i < 10:
	print('*'*(i+1))
	i += 1

	
>>> i = 0
>>> while i < 10:
	print('*'*(i+1))
	i += 1

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> 
>>> # ----------------------------------- Loop control statement
>>> 
>>> for i in range(1, 11):
	print(i, end=' ')

	
1 2 3 4 5 6 7 8 9 10 
>>> for i in range(1, 11):
	if(i % 2 == 0 and i % 3 == 0):
		break
	print(i, end=' ')

	
1 2 3 4 5 
>>> for i in range(1, 11):
	if(i % 2 == 0 and i % 3 == 0):
		continue
	print(i, end=' ')

	
1 2 3 4 5 7 8 9 10 
>>> 
>>> # ---------------------------------- Loop else block
>>> 
>>> 
