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

    def area(self):
        return self.__size**2
    

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# Example usage:
try:
    square_instance = Square(5)
    print("Size:", square_instance.get_size())
    print("Area:", square_instance.area())
    square_instance.my_print()
except Exception as e:
    print(e)