#!/usr/bin/env python3
''' make the class Square.'''

class Square:
    '''state the attributes using __init__'''
    def __init__(self, size=0):
        '''initialize a square instance'''
        '''parameter - size'''
        '''no type / value verification was used'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        '''Check if is less than 0'''
        if size < 0:
            raise ValueError("size must be >= 0")  
        
        '''Set the size attribute'''
        self.__size = size

    '''public instance method to return current square area'''
    def area(self):
        return self.__size**2