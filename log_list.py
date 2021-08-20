Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota','honda','izusu']
>>> garage
['toyota', 'honda', 'izusu']
>>> import pprint
>>> pprint(garage)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pprint(garage)
TypeError: 'module' object is not callable
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'honda', 'izusu', 'suzuki']
>>> print(garage[2])
izusu
>>> find('isuzu',garage)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    find('isuzu',garage)
NameError: name 'find' is not defined
>>> garage.remove('honda')
>>> garage
['toyota', 'izusu', 'suzuki']
>>> garage
['toyota', 'izusu', 'suzuki']
>>> garage
['toyota', 'izusu', 'suzuki']
>>> for i in garage:
	print(i)

	
toyota
izusu
suzuki
>>> garage.insert(1,'benz')
>>> garage
['toyota', 'benz', 'izusu', 'suzuki']
>>> del garage[2]
>>> garage
['toyota', 'benz', 'suzuki']
>>> garage[-1]
'suzuki'
>>> garage[-2]
'benz'
>>> mycar = garage.pop(-1)
>>> mycar
'suzuki'
>>> mycar = garage.pop()
>>> 
>>> mycar
'benz'
>>> garage
['toyota']
>>> garage = ['toyota','benz','suzuki']
>>> garage[1] ='tesla'
>>> garage
['toyota', 'tesla', 'suzuki']
>>> print(len(garage))
3
>>> users = ['z','r','t','b','n','p']
>>> users.sort()
>>> print(user)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(user)
NameError: name 'user' is not defined
>>> print(users)
['b', 'n', 'p', 'r', 't', 'z']
>>> users.sort(reverse = True)
>>> print(users)
['z', 't', 'r', 'p', 'n', 'b']
>>> print(sorted(users))
['b', 'n', 'p', 'r', 't', 'z']
>>> users
['z', 't', 'r', 'p', 'n', 'b']
>>> users = ['z','r','t','b','n','p']
>>> print(sorted(user),reverse=Ture)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(sorted(user),reverse=Ture)
NameError: name 'user' is not defined
>>> print(sorted(user),reverse=True)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(sorted(user),reverse=True)
NameError: name 'user' is not defined
>>> print(sorted(user,reverse=True))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(sorted(user,reverse=True))
NameError: name 'user' is not defined
>>> print(sorted(users,reverse=True))
['z', 't', 'r', 'p', 'n', 'b']
>>> users.reverse()
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> users.reverse()
>>> for u in users:
	print(u)

	
z
r
t
b
n
p
>>> users.reverse()
>>> for u in users:
	print(u)

	
p
n
b
t
r
z
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> users.reverse()
>>> for u in sorted(users):
	print(u)

	
b
n
p
r
t
z
>>> for u in users:
	print('สวัสดี',u)
	print('สวัสดี'+u)

	
สวัสดี z
สวัสดีz
สวัสดี r
สวัสดีr
สวัสดี t
สวัสดีt
สวัสดี b
สวัสดีb
สวัสดี n
สวัสดีn
สวัสดี p
สวัสดีp
>>> for u in users:
	print('สวัสดี '+u)

	
สวัสดี z
สวัสดี r
สวัสดี t
สวัสดี b
สวัสดี n
สวัสดี p
>>> 