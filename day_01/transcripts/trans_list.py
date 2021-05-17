Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS
>>> 
>>> L = ['red', 'green', 'blue', 1, 3, 4.5, max, min, [1,2,3]]
>>> L
['red', 'green', 'blue', 1, 3, 4.5, <built-in function max>, <built-in function min>, [1, 2, 3]]
>>> type(L)
<class 'list'>
>>> 
>>> # -------------------- mutability
>>> 
>>> L[2]
'blue'
>>> L[2] = "yellow"
>>> L
['red', 'green', 'yellow', 1, 3, 4.5, <built-in function max>, <built-in function min>, [1, 2, 3]]
>>> L[-1]
[1, 2, 3]
>>> L[-1][2]
3
>>> L[-1][3] = 4
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    L[-1][3] = 4
IndexError: list assignment index out of range
>>> L[-1][2] = 4
>>> L
['red', 'green', 'yellow', 1, 3, 4.5, <built-in function max>, <built-in function min>, [1, 2, 4]]
>>> L[1]
'green'
>>> L[1][2] = 'x'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    L[1][2] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ------------------------ accessing values
>>> 
>>> L[0]
'red'
>>> L[-1]
[1, 2, 4]
>>> L[3:5]
[1, 3]
>>> L[-5:-3]
[3, 4.5]
>>> L[::-1]
[[1, 2, 4], <built-in function min>, <built-in function max>, 4.5, 3, 1, 'yellow', 'green', 'red']
>>> 
>>> 
>>> # ----------------------- replacing values
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> L[1] = ['black', 'white']
>>> L
['red', ['black', 'white'], 'blue']
>>> 
>>> L = ['red', 'yellow', 'blue']
>>> L[1:2]
['yellow']
>>> L[1:2] = ['black', 'white']
>>> L
['red', 'black', 'white', 'blue']
>>> 
>>> # ---------------------- operators
>>> 
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> len(L)
4
>>> L
['red', 'black', 'white', 'blue']
>>> 'red' in L
True
>>> type(L) is list
True
>>> del L[2]
>>> L
['red', 'black', 'blue']
>>> 
>>> # --------------------- add elements to the list
>>> 
>>> L
['red', 'black', 'blue']
>>> L.append("yellow")
>>> L
['red', 'black', 'blue', 'yellow']
>>> L.append("orange")
>>> L
['red', 'black', 'blue', 'yellow', 'orange']
>>> L.insert(2, "white")
>>> L
['red', 'black', 'white', 'blue', 'yellow', 'orange']
>>> L.insert(0, "golden")
>>> L
['golden', 'red', 'black', 'white', 'blue', 'yellow', 'orange']
>>> 
>>> L1 = ["maroon", "cyan", "pink"]
>>> L.extend(L1)
>>> L
['golden', 'red', 'black', 'white', 'blue', 'yellow', 'orange', 'maroon', 'cyan', 'pink']
>>> 
>>> 
>>> L = ['golden', 'red', 'black', 'white', 'blue', 'yellow', 'orange']
>>> L1
['maroon', 'cyan', 'pink']
>>> L + L1
['golden', 'red', 'black', 'white', 'blue', 'yellow', 'orange', 'maroon', 'cyan', 'pink']
>>> L
['golden', 'red', 'black', 'white', 'blue', 'yellow', 'orange']
>>> L1
['maroon', 'cyan', 'pink']
>>> 
>>> 
>>> # ------------------- removing element
>>> 
>>> L
['golden', 'red', 'black', 'white', 'blue', 'yellow', 'orange']
>>> L.pop()
'orange'
>>> L
['golden', 'red', 'black', 'white', 'blue', 'yellow']
>>> L.pop(1)
'red'
>>> L
['golden', 'black', 'white', 'blue', 'yellow']
>>> 
>>> "blue" in L
True
>>> L.remove("blue")
>>> L
['golden', 'black', 'white', 'yellow']
>>> 
>>> del L[2]
>>> del
SyntaxError: invalid syntax
>>> L
['golden', 'black', 'yellow']
>>> 
>>> # ----------------------- search for element
>>> 
>>> L
['golden', 'black', 'yellow']
>>> L.count("black")
1
>>> "black" in L
True
>>> L.index("black")
1
>>> # ---------------------- re-arranging elements
>>> 
>>> L = ["zebra", "monkey", "ant"]
>>> L[::-1]
['ant', 'monkey', 'zebra']
>>> reversed(L)
<list_reverseiterator object at 0x000001C5A72BEDD8>
>>> list(reversed(L))
['ant', 'monkey', 'zebra']
>>> L
['zebra', 'monkey', 'ant']
>>> L.reverse()
>>> L
['ant', 'monkey', 'zebra']
>>> 
>>> 
>>> L = ['golden', 'red', 'black', 'white', 'blue', 'yellow']
>>> sorted(L)
['black', 'blue', 'golden', 'red', 'white', 'yellow']
>>> L
['golden', 'red', 'black', 'white', 'blue', 'yellow']
>>> L.sort()
>>> L
['black', 'blue', 'golden', 'red', 'white', 'yellow']
>>> L.sort(reverse=True)
>>> L
['yellow', 'white', 'red', 'golden', 'blue', 'black']
>>> 
>>> # -------------------- iteration
>>> 
>>> for item in L:
	print(item)

	
yellow
white
red
golden
blue
black
>>> 
>>> for item in L:
	print(item.ljust(10), '--> ', str(len(item)))

	
yellow     -->  6
white      -->  5
red        -->  3
golden     -->  6
blue       -->  4
black      -->  5
>>> for item in L:
	print(item.ljust(10), '--> ', len(item))

	
yellow     -->  6
white      -->  5
red        -->  3
golden     -->  6
blue       -->  4
black      -->  5
>>> for item in L:
	print(item.ljust(10) + '--> ' + len(item))

	
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    print(item.ljust(10) + '--> ' + len(item))
TypeError: can only concatenate str (not "int") to str
>>> for item in L:
	print(item.ljust(10) + '--> ' + str(len(item)))

	
yellow    --> 6
white     --> 5
red       --> 3
golden    --> 6
blue      --> 4
black     --> 5
>>> 
>>> for item in L:
	print(item.upper(), end=' ')

	
YELLOW WHITE RED GOLDEN BLUE BLACK 
>>> 
>>> # ---------------------- copy lists
>>> 
>>> L
['yellow', 'white', 'red', 'golden', 'blue', 'black']
>>> L1 = L
>>> L
['yellow', 'white', 'red', 'golden', 'blue', 'black']
>>> L1
['yellow', 'white', 'red', 'golden', 'blue', 'black']
>>> L1.append("orange")
>>> L1[-3] = "pink"
>>> L1
['yellow', 'white', 'red', 'golden', 'pink', 'black', 'orange']
>>> L
['yellow', 'white', 'red', 'golden', 'pink', 'black', 'orange']
>>> 
>>> 
>>> from copy import deepcopy
>>> from copy import deepcopy
>>> 
>>> 
>>> # import copy
>>> # copy.deepcopy()
>>> 
>>> L2 = deepcopy(L)
>>> L
['yellow', 'white', 'red', 'golden', 'pink', 'black', 'orange']
>>> L2
['yellow', 'white', 'red', 'golden', 'pink', 'black', 'orange']
>>> L2.append("maroon")
>>> L2
['yellow', 'white', 'red', 'golden', 'pink', 'black', 'orange', 'maroon']
>>> L
['yellow', 'white', 'red', 'golden', 'pink', 'black', 'orange']
>>> 
>>> 
>>> 
>>> from math import sqrt, sin, radians
>>> sqrt(144)
12.0
>>> sin(radians(90))
1.0
>>> dir(math)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    dir(math)
NameError: name 'math' is not defined
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> import copy
>>> dir(copy)
['Error', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_copy_dispatch', '_copy_immutable', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', 'copy', 'deepcopy', 'dispatch_table', 'error']
>>> 
