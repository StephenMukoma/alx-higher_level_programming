#!/usr/bin/python3
""" This class represents a Rectangle """


class Rectangle:
    """ This class defines a Rectangle """
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attriute"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """Property setter for width"""
        if not isinstance(value, int):
            """Check if width value is an integer"""
            raise TypeError("width must be an integer")
        if value < 0:
            """Check if width is greater than 0"""
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Property setter for height"""
        if not isinstance(value, int):
            """Check if height value is an integer"""
            raise TypeError("height must be an integer")
        if value < 0:
            """ Check if height value is greater than or equal to zero """
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            """checks the value of width and height"""
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """converts rectangle to a string"""
        if self.width == 0 or self.height == 0:
            """check if string is empty"""
            return ""
        output = ""
        for i in range(self.__height):
            output += ("#" * self.__width)
            if i != self.__height - 1:
                output += "\n"
        return output

    def __repr__(self):
        """returns a string representation of the Rectangle object"""
        return 'Rectangle({}, {})'.format(str(self.width), str(self.height))

    def __del__(self):
        """Prints message when a rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -=1
