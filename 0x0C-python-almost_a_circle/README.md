# 0x0C. Python - Almost a circle

20180520 - This purpose of this assignment was to review previously covered Python concepts such as import, exceptions, class, attributes, getter/setter, class method, static method, inheritance, unittest, read/write file

### models/base.py, models/__init__.py
first class Base that defines private class attribute __nb_objects = 0 
class constructor: def __init__(self, id=None):  
This class is the base for all other classes in this project  

### models/rectangle.py
Rectangle class that inherits from Base and includes:  
setters and getters for private instance attributes:  
def __init__(self, width, height, x=0, y=0, id=None):  
__width - width
__height - height
__x - x
__y - y
setters and getters should have validation for type and value
area method that returns the area
display method that prints the rectangle, accounting for x,y shift
updated __str__ method that returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
update method: update(self, *args, **kwargs)  
That updates the arguments to attributes

### models/square.py
inherits from Rectangle
def __init__(self, size, x=0, y=0, id=None):

### main/
contains main files for project