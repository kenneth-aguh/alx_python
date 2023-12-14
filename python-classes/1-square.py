#!/usr/bin/env python3

class Square:
    def __init__(self, size=0):
        # Check if is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        # Check if is less than 0
        if size < 0:
            raise ValueError("size must be >= 0")
        
        # Set the size attribute
        self.__size = size