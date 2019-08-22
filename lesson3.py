Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = "John"
>>> print(x)
5
>>> print(y)
John
>>> x = 4 # x is of type int
>>> x = "Sally" # x is now of type str
>>> print(x)
Sally
>>> x = "John"
>>> # is the same as
>>> x = 'John'
>>> x = "John"
>>> print(x)
John
>>> #double quotes are the same as single quotes:
>>> x = 'John'
>>> print(x)
John
>>> x, y, z = "Orange", "Banana", "Cherry"
>>> print(x)
Orange
>>> print(y)
Banana
>>> print(z)
Cherry
>>> x = y = z = "Orange"
>>> print(x)
Orange
>>> print(y)
Orange
>>> print(z)
Orange
>>> X = "awesome"
>>> print("Python is " + X)
Python is awesome
>>> x = "Python is "
>>> y = "awesome"
>>> z = x + y
>>> print(z)
Python is awesome
>>> x = 5
>>> y = 10
>>> print(x + y)
15
>>> x = 5
>>> y = "John"
>>> print(x + y)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(x + y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
