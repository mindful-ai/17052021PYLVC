Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS
>>> 
>>> s = "computer"
>>> type(s)
<class 'str'>
>>> 
>>> # --------------------- Accessing characters
>>> # Subscripting: [index], [start:end], [start:end:interval]
>>> 
>>> s[0]
'c'
>>> s[3]
'p'
>>> s[-1]
'r'
>>> s[-2]
'e'
>>> s[-5]
'p'
>>> s[3:5]
'pu'
>>> s[3:6]
'put'
>>> s[1:4]
'omp'
>>> s[-5:-3]
'pu'
>>> s[-5:-2]
'put'
>>> s[0:4]
'comp'
>>> s[:4]
'comp'
>>> s[5:]
'ter'
>>> s[:]
'computer'
>>> s[1:6]
'omput'
>>> s[1:6:2]
'opt'
>>> s[::2]
'cmue'
>>> s[::-1]
'retupmoc'
>>> # ---------------------------- immutability
>>> 
>>> s
'computer'
>>> s[0]
'c'
>>> s[-1]
'r'
>>> s[0] = 'B'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s[0] = 'B'
TypeError: 'str' object does not support item assignment
>>> 
>>> # ---------------------------- Operators
>>> 
>>> 'py' + 'thon'
'python'
>>> 'py' * 5
'pypypypypy'
>>> s
'computer'
>>> len(s)
8
>>> 'p' in s
True
>>> 'a' in s
False
>>> 'put' in s
True
>>> type(s) is str
True
>>> a = 10
>>> type(a) is int
True
>>> type(a) is str
False
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s1 = 'apples'
>>> s2 = 'Apples'
>>> s1 == s2
False
>>> s1 == s2.lower()
True
>>> 
>>> # ------------------------------------ in-built functions for strings
>>> 
>>> # case
>>> 
>>> s
'computer'
>>> s.upper()
'COMPUTER'
>>> s.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> s.title()
'Computer'
>>> 
>>> text = "This is a text"
>>> text.capitalize()
'This is a text'
>>> text.title()
'This Is A Text'
>>> 
>>> 
>>> len(s)
8
>>> # Querying
>>> 
>>> '1234'.isdigit()
True
>>> '1234'.isalnum()
True
>>> 'abc123'.isalnum()
True
>>> 'a23'.isdigit()
False
>>> 'asd'.isalpha()
True
>>> '   '.isspace()
True
>>> 'asd'.islower()
True
>>> 'asd'.isupper()
False
>>> 'asd'.istitle()
False
>>> 'Asd'.istitle()
True
>>> 
>>> 
>>> # searching
>>> 
>>> s
'computer'
>>> 'put' in s
True
>>> s.find('put')
3
>>> s.count('put')
1
>>> x = 'mississippi'
>>> x.count('ss')
2
>>> x.find('ss')
2
>>> 
>>> # modifying a string
>>> 
>>> ip = '192-168-2-1'
>>> ip.replace('-','.')
'192.168.2.1'
>>> ip
'192-168-2-1'
>>> newip = ip.replace('-', '.')
>>> newip
'192.168.2.1'
>>> ip
'192-168-2-1'
>>> txt = "one one was a race horse, two two was one too."
>>> x = txt.replace("one", "three", 2)
>>> x
'three three was a race horse, two two was one too.'
>>> 
>>> 
>>> # -------
>>> 
>>> t = '   14,500 '
>>> t.strip()
'14,500'
>>> t.lstrip()
'14,500 '
>>> t.rstrip()
'   14,500'
>>> 
>>> t.strip().replace(',','')
'14500'
>>> 0.13 * int(t.strip().replace(',',''))
1885.0
>>> 
>>> t
'   14,500 '
>>> 
>>> # ------------
>>> 
>>> s
'computer'
>>> s.ljust(20)
'computer            '
>>> s.rjust(20,'>')
'>>>>>>>>>>>>computer'
>>> 
>>> # ---------
>>> 
>>> site = "www.google.com"
>>> site.startswith('https')
False
>>> site.endswith('com')
True
>>> 
>>> # ---------
>>> 
>>> text = 'mary had a little lamb'
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> L = text.split()
>>> type(L)
<class 'list'>
>>> 
>>> L
['mary', 'had', 'a', 'little', 'lamb']
>>> '-'.join(L)
'mary-had-a-little-lamb'
>>> 
