Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> E = []
>>> for n in range(30, 81):
	if(n % 2 == 0):
		E.append(n)

		
>>> E
[30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80]
>>> 
>>> E = [x for x in range(30, 81) if x % 2 == 0]
>>> E
[30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80]
>>> 
>>> # COMPREHENSIONS
>>> # You can create a comprehension in any collection
>>> 
>>> # [<expr> <loop> <condition>]
>>> 
>>> L = [1, 3, 5, 8, 10]
>>> L2 = [i**2 for i in L]
>>> L2
[1, 9, 25, 64, 100]
>>> L3 = [(i, i**2, i**3) for i in L]
>>> L3
[(1, 1, 1), (3, 9, 27), (5, 25, 125), (8, 64, 512), (10, 100, 1000)]
>>> 
>>> 
>>> L = ["red", "green", "blue", "yellow"]
>>> D = { s:len(s) for s in L }
>>> D
{'red': 3, 'green': 5, 'blue': 4, 'yellow': 6}
>>> 
>>> 
>>> 
>>> L = [ (x,y) for x in range(10) for y in range(10) if x + y == 9]
>>> L
[(0, 9), (1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1), (9, 0)]
>>> 
>>> 
>>> L = [1, 3, 5, 8, 10]
>>> L1 = [1, 3, 25, 8, 100]
>>> 
>>> L2 = [x for x in L if x % 5 == 0]
>>> L2
[5, 10]
>>> L2 = [x**2 for x in L if x % 5 == 0]
>>> L2
[25, 100]
>>> L3 = [x**2 if x % 5 == 0 else x for x in L]
>>> L3
[1, 3, 25, 8, 100]
>>> 
>>> 
>>> # ---------------- prime numbers
>>> 
>>> N = 7
>>> rems = [ N % n != 0  for n in range(2, N)]
>>> rems
[True, True, True, True, True]
>>> L = [0, 1, 1, 0]
>>> all(L)
False
>>> any(L)
True
>>> 
>>> prime = all[ N % n != 0  for n in range(2, N)]
SyntaxError: invalid syntax
>>> prime = all([ N % n != 0  for n in range(2, N)])
>>> prime
True
>>> N = 10
>>> prime = all([ N % n != 0  for n in range(2, N)])
>>> prime
False
>>> bool
<class 'bool'>
>>> prime = bool([ N % n != 0  for n in range(2, N)])
>>> prime
True
>>> all
<built-in function all>
>>> bool(10)
True
>>> bool(0)
False
>>> bool(-1)
True
>>> L
[0, 1, 1, 0]
>>> bool(L)
True
>>> L = [0, 0, 0]
>>> bool(L)
True
>>> bool([])
False
>>> 
