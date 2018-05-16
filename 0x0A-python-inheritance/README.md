#0x0A. Python - Inheritance

20180515 - This purpose of this assignment was to introduce Inheritance in Python

### 0-lookup.py
a function that returns the list of available attributes and methods of an object

### 1-my_list.py, tests/1-my_list.txt
a class MyList that inherits from list  
test cases to test the class

### 2-is_same_class.py
a function that returns True if the object is exactly an instance of the specified class ; otherwise False

### 3-is_kind_of_class.py
a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False

### 4-inherits_from.py
a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False

### 5-base_geometry.py
an empty class BaseGeometry

### 6-base_geometry.py
class BaseGeometry with:  
Public instance method: def area(self): that raises an Exception with the message area() is not implemented

### 7-base_geometry.py, tests/7-base_geometry.txt
class BaseGeometry with:  
Public instance method: def area(self): that raises an Exception with the message area() is not implemented  
Public instance method: def integer_validator(self, name, value): that validates value
test cases to test public instance method

### 8-rectangle.py
a class Rectangle that inherits from BaseGeometry  
Instantiation with width and height: def __init__(self, width, height):

### 9-rectangle.py
a class Rectangle that inherits from BaseGeometry  
Instantiation with width and height: def __init__(self, width, height):
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

### 10-square.py
a class Square that inherits from Rectangle (9-rectangle.py):  
Instantiation with size: def __init__(self, size):
the area() method must be implemented

### 11-square.py
a class Square that inherits from Rectangle (9-rectangle.py):
Instantiation with size: def __init__(self, size):
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>