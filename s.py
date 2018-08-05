Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x,y,z = (3,4,5)
>>> my_tuple = (3,4,5)
>>> print(x+y+z)
12
>>> print(my_tuple+my_tuple)
(3, 4, 5, 3, 4, 5)
>>> print(x*3)
9
>>> print(my_tuple*3)
(3, 4, 5, 3, 4, 5, 3, 4, 5)
>>> print(my_tuple[0]==x)
True
>>> print(x[0])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(x[0])
TypeError: 'int' object is not subscriptable
>>> my_tuple[0]=17
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    my_tuple[0]=17
TypeError: 'tuple' object does not support item assignment
>>> print(my_tuple)
(3, 4, 5)
>>> x=17
>>> print(x)
17
>>> number = 2
>>> while number in range(2):
	print(number)
	
