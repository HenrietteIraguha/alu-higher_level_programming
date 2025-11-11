#!/usr/bin/python3
"""Class that defines a square with controlled size."""
class Square:
    def __init__(self, size=0):
        self.size = size
"""Initialize a new square with optional size."""
    @property
    def size(self):
        return self.__size
"""Retrieve the current size of the square."""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
"""Return the current area of the square."""
    def area(self):
        return self.__size ** 2
