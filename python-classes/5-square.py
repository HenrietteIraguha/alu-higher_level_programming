#!/usr/bin/python3


class Square:
"""Class that defines a square."""
    def __init__(self, size=0):
        self.size = size
"""Initialize a new square with optional size."""
    @property
    def size(self):
        return self.__size
"""Retrieve the current size of the square."""
    @size.setter
    def size(self, value):
"""Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
        """Return the current area of the square."""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
