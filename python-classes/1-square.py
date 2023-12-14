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

    # getters
    def get_size(self):
        return self.__size
    
    # setter
    def set_size(self, value):
        self.__size = value        

# Example usage:
try:
    our_square = Square(2)
    print( our_square.get_size())  # Accessing private attribute indirectly
except Exception as e:
    print(e)