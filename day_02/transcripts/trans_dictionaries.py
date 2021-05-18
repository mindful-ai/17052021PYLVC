Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # DICTIONARIES
>>> 
>>> L = ["Anil", 35, "oracle", "india"]
>>> L[0]
'Anil'
>>> L[3]
'india'
>>> L[2]
'oracle'
>>> L.insert(2, "software engineer")
>>> L
['Anil', 35, 'software engineer', 'oracle', 'india']
>>> L[0]
'Anil'
>>> L[2]
'software engineer'
>>> 
>>> 
>>> # --> "name":"anil", "age":35, "company":"oracle", "country":india
>>> # --> "job":"software engineer"
>>> 
>>> D = {"name":"anil", "age":35, "company":"oracle", "country":"india"}
>>> D
{'name': 'anil', 'age': 35, 'company': 'oracle', 'country': 'india'}
>>> D["name"]
'anil'
>>> D["age"]
35
>>> D["country"]
'india'
>>> 
>>> 
>>> D["job"]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    D["job"]
KeyError: 'job'
>>> D["job"] = "Software engineer"
>>> D
{'name': 'anil', 'age': 35, 'company': 'oracle', 'country': 'india', 'job': 'Software engineer'}
>>> D["age"] = 36
>>> D
{'name': 'anil', 'age': 36, 'company': 'oracle', 'country': 'india', 'job': 'Software engineer'}
>>> D[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    D[0]
KeyError: 0
>>> D.pop("age")
36
>>> D
{'name': 'anil', 'company': 'oracle', 'country': 'india', 'job': 'Software engineer'}
>>> 
>>> 
>>> D1 = {"dob":"19-09-1999", "addr":"new orleans"}
>>> D.update(D1)
>>> D
{'name': 'anil', 'company': 'oracle', 'country': 'india', 'job': 'Software engineer', 'dob': '19-09-1999', 'addr': 'new orleans'}
>>> 
>>> D.setdefault("name")
'anil'
>>> D.setdefault("hobbies", ['cricket', 'music'])
['cricket', 'music']
>>> D
{'name': 'anil', 'company': 'oracle', 'country': 'india', 'job': 'Software engineer', 'dob': '19-09-1999', 'addr': 'new orleans', 'hobbies': ['cricket', 'music']}
>>> D.["hobbies"].append("painting")
SyntaxError: invalid syntax
>>> D["hobbies"].append("painting")
>>> D
{'name': 'anil', 'company': 'oracle', 'country': 'india', 'job': 'Software engineer', 'dob': '19-09-1999', 'addr': 'new orleans', 'hobbies': ['cricket', 'music', 'painting']}
>>> 
>>> 
>>> "name" in D
True
>>> 
>>> # ---------------------------------------------
>>> 
>>> D.keys()
dict_keys(['name', 'company', 'country', 'job', 'dob', 'addr', 'hobbies'])
>>> D.values()
dict_values(['anil', 'oracle', 'india', 'Software engineer', '19-09-1999', 'new orleans', ['cricket', 'music', 'painting']])
>>> D.items()
dict_items([('name', 'anil'), ('company', 'oracle'), ('country', 'india'), ('job', 'Software engineer'), ('dob', '19-09-1999'), ('addr', 'new orleans'), ('hobbies', ['cricket', 'music', 'painting'])])
>>> 
>>> 
>>> for item in D.items():
	print(item)

	
('name', 'anil')
('company', 'oracle')
('country', 'india')
('job', 'Software engineer')
('dob', '19-09-1999')
('addr', 'new orleans')
('hobbies', ['cricket', 'music', 'painting'])
>>> 
>>> for key, value in D.items():
	print(key, ' --------> ', value)

	
name  -------->  anil
company  -------->  oracle
country  -------->  india
job  -------->  Software engineer
dob  -------->  19-09-1999
addr  -------->  new orleans
hobbies  -------->  ['cricket', 'music', 'painting']
>>> for key, value in D.items():
	print(key.ljust(10), ' | ', value)

	
name        |  anil
company     |  oracle
country     |  india
job         |  Software engineer
dob         |  19-09-1999
addr        |  new orleans
hobbies     |  ['cricket', 'music', 'painting']
>>> 
>>> 
>>> # ----------------------------- tabular data
>>> 
>>> # name  |  age  | company
>>> # anil  |   35  |  oracle
>>> # sunil |   36  |  infosys
>>> 
>>> r1 = {"name":"anil", "age":35, "company":"oracle"}
>>> r2 = {"name":"sunil", "age":36, "company":"infosys"}
>>> tab = {"anil":r1, "sunil":r2}
>>> tab
{'anil': {'name': 'anil', 'age': 35, 'company': 'oracle'}, 'sunil': {'name': 'sunil', 'age': 36, 'company': 'infosys'}}
>>> tab['anil']['company']
'oracle'
>>> tab['sunil']['company']
'infosys'
>>> 
