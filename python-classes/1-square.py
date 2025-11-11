#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a new Square with a given size.

        Args:
            size: The size of the square (no type or value checks here).
        """
        self.__size = size
