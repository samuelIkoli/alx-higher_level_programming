#!/usr/bin/python3
"""
This module implements a square class
"""


class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size, end="\n")

    def __str__(self):
        if self.size == 0:
            return ""
        result = ""
        result += "\n" * self.position[1]
        for i in range(self.size):
            result += " " * self.position[0]
            result += "#" * self.size + "\n"
        return result[:-1]
        
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area() 