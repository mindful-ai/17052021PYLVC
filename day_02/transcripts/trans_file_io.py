Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILES
>>> # text files
>>> # f = open(filename, mode)
>>> # mode -> r, w, a, b
>>> # f.close()
>>> # read(), readline(), readlines()
>>> # write(), writeline()
>>> # tell() and seek()
>>> 
>>> path = "C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\sample.txt"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = "c:\data\text\read\note.dat"
>>> print(path)
c:\data	extead
ote.dat
>>> path = r"c:\data\text\read\note.dat"
>>> print(path)
c:\data\text\read\note.dat
>>> path = r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\sample.txt"
>>> f = open(path, "r")
>>> f.read()
'Data sampling is a statistical analysis \ntechnique used to select, manipulate and \nanalyze a representative subset of data points \nto identify patterns and trends in the larger \ndata set being examined.'
>>> f.readline()
''
>>> f.tell()
206
>>> f.seek(0)
0
>>> f.readline()
'Data sampling is a statistical analysis \n'
>>> f.readline()
'technique used to select, manipulate and \n'
>>> f.readline()
'analyze a representative subset of data points \n'
>>> f.read(10)
'to identif'
>>> f.seek(0)
0
>>> f.readlines()
['Data sampling is a statistical analysis \n', 'technique used to select, manipulate and \n', 'analyze a representative subset of data points \n', 'to identify patterns and trends in the larger \n', 'data set being examined.']
>>> 
>>> f.close()
>>> path = r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\sample2.txt"
>>> f = open(path, "w")
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\\sample2.txt' mode='w' encoding='cp1252'>
>>> f.write("SAMPLE \n")
8
>>> f.close()
>>> f = open(path, "w")
>>> f.close()
>>> f = open(path, "a")
>>> f.writelines(['Data sampling is a statistical analysis \n', 'technique used to select, manipulate and \n', 'analyze a representative subset of data points \n', 'to identify patterns and trends in the larger \n', 'data set being examined.'])
>>> f.close()
>>> 
