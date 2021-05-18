Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Tuples
>>> 
>>> L = ["red", "green", "blue"]
>>> type(L)
<class 'list'>
>>> T = ("red", "green", "blue")
>>> type(T)
<class 'tuple'>
>>> 
>>> L[0]
'red'
>>> L[0] = "orange"
>>> L
['orange', 'green', 'blue']
>>> T[0]
'red'
>>> T[0] = "orange"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    T[0] = "orange"
TypeError: 'tuple' object does not support item assignment
>>> L.append("red")
>>> L
['orange', 'green', 'blue', 'red']
>>> T.append("Red")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    T.append("Red")
AttributeError: 'tuple' object has no attribute 'append'
>>> 
>>> 
>>> 
>>> 
>>> # --------------------- interconversion functions
>>> 
>>> L
['orange', 'green', 'blue', 'red']
>>> TL = tuple(L)
>>> TL
('orange', 'green', 'blue', 'red')
>>> TL[0] = "red"
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    TL[0] = "red"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> LT = list(TL)
>>> LT
['orange', 'green', 'blue', 'red']
>>> LT[0] = "pink"
>>> LT
['pink', 'green', 'blue', 'red']
>>> TL
('orange', 'green', 'blue', 'red')
>>> TL = tuple(LT)
>>> Tl
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Tl
NameError: name 'Tl' is not defined
>>> TL
('pink', 'green', 'blue', 'red')
>>> L
['orange', 'green', 'blue', 'red']
>>> 
>>> # --------------------------- operators
>>> 
>>> T
('red', 'green', 'blue')
>>> TL
('pink', 'green', 'blue', 'red')
>>> T +TL
('red', 'green', 'blue', 'pink', 'green', 'blue', 'red')
>>> T + L
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    T + L
TypeError: can only concatenate tuple (not "list") to tuple
>>> 
>>> T * 3
('red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue')
>>> 
>>> "red" in T + TL
True
>>> type(T) is tupel
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    type(T) is tupel
NameError: name 'tupel' is not defined
>>> type(T) is tuple
True
>>> 
>>> len(T + TL)
7
>>> 
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> L
['orange', 'green', 'blue', 'red']
>>> del L[0]
>>> L
['green', 'blue', 'red']
>>> 
>>> TL
('pink', 'green', 'blue', 'red')
>>> del TL
>>> TL
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    TL
NameError: name 'TL' is not defined
>>> 
>>> 
>>> # --------------------------- mutable element in tuple
>>> 
>>> T = ("red", "green", "blue", ["white"])
>>> T[0] = "green"
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    T[0] = "green"
TypeError: 'tuple' object does not support item assignment
>>> T[-1]
['white']
>>> T[-1] = " ["black"]
SyntaxError: invalid syntax
>>> T[-1] = ["black"]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    T[-1] = ["black"]
TypeError: 'tuple' object does not support item assignment
>>> T[-1].append("black")
>>> T
('red', 'green', 'blue', ['white', 'black'])
>>> 
>>> 
>>> # ------------------------------- functions
>>> 
>>> T
('red', 'green', 'blue', ['white', 'black'])
>>> 
>>> T = ('red', 'green', 'blue')
>>> reversed(T)
<reversed object at 0x000001F62956CCF8>
>>> list(reversed(T))
['blue', 'green', 'red']
>>> sorted(T)
['blue', 'green', 'red']
>>> 
>>> # T.sort() and T.reverse() is not allowed as they try to make in-place
>>> # changes
>>> 
>>> T.sort()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    T.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> 
>>> T = list(T)
>>> T.sort()
>>> T
['blue', 'green', 'red']
>>> T = tuple(T)
>>> T
('blue', 'green', 'red')
>>> 
>>> # The above show making forced changes on tuples
>>> 
>>> T
('blue', 'green', 'red')
>>> 
>>> # ---------- searching
>>> 
>>> T.count("blue")
1
>>> T.index("blue")
0
>>> 
>>> 
>>> # ------ iterations
>>> 
>>> for item in T:
	print(item)

	
blue
green
red
>>> 
>>> # ------------------------------- unpacking a tuple
>>> 
>>> T
('blue', 'green', 'red')
>>> r, g, b = T
>>> r
'blue'
>>> g
'green'
>>> b
'red'
>>> 
>>> L
['green', 'blue', 'red']
>>> a, b, c = L
>>> a
'green'
>>> b
'blue'
>>> c
'red'
>>> 
>>> x,y = T
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    x,y = T
ValueError: too many values to unpack (expected 2)
>>> 

>>> T = ('blue', 'green', 'red', "yellow", "golden")
>>> x, y, *z = T
>>> x
'blue'
>>> y
'green'
>>> z
['red', 'yellow', 'golden']
>>> type(z)
<class 'list'>
>>> 
