Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = [0, 1, 2, 3, 4, 5, 6]
>>> 
>>> for n in L:
	print(n, n**2, n**3)

	
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
>>> L = ['red', 'green', 'blue']
>>> for item in L:
	print(item)

	
red
green
blue
>>> for c in "python":
	print(c, end=' ')

	
p y t h o n 
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(30, 50))
[30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> list(range(1, 100, 7))
[1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]
>>> list(range(100, 1, -5))
[100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
>>> 
>>> 
>>> for i in range(10):
	print(i, i**2)

	
0 0
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
>>> 
