#!/usr/bin/env python3
''' make the class Square.'''

class Square:
    '''state the attributes using __init__ '''
    def __init__(self, size):
        '''initialize a square instance'''
        '''parameter - size'''
        '''no type / value verification was used'''
        self.__size = size
    
    '''getters'''
    def get_size(self):
        return self.__size
    
    '''setter'''
    def set_size(self, value):
        self.__size = value
