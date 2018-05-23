#!/usr/bin/python3
"""
module defines square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class defines Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer method
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return id x/y - size
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.__size))

    @property
    def size(self):
        """getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        Args:
            value (int): value for size
        """
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """updates attributes:
        args:
            *args: argument list
            **kwargs: keyword dictionary of arguments
        """
        list = ["id", "size", "x", "y"]
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass
        elif kwargs:
            for key, value in kwargs.items():
                if key in list:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of a Square
        """
        dictionary = dict(self.__dict__)
        for key in dictionary:
            new_key = key.replace("_Rectangle__", "")
            new_key2 = new_key.replace("_Square__", "")
            dictionary[new_key2] = dictionary.pop(key)
        return dictionary
