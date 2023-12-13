#!/usr/bin/env python3

# this is the class Square
class Square:
    # specifying the attributes using __init__ 
    def __init__(self, size):
        # initializing a square instance
        # parameter - size
        # no type / value verification was used
        self.__size = size
    
    # getters
    def get_size(self):
        return self.__size
    
    # setter
    def set_size(self, value):
        self.__size = value

# Example usage:
square_instance = Square(5)
print(square_instance.get_size())  # Output: 5

square_instance.set_size(7)
print(square_instance.get_size())  # Output: 7
