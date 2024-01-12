'''Import the base module'''
from models.base import Base

'''The Rectangle class inherits from the Base class.'''
class Rectangle(Base):
    ''' The class constructor (__init__) calls the super class 
    with the provided id and assigns the other arguments 
    (width, height, x, y) to the appropriate attributes'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''adding a layer of protection'''
        super().__init__(id)
    
        self.__width = width

        self.__height = height
        self.__x = x
        self.__y = y
    
    def __validate_integers(self, value, attribute_name):
        '''adding a layer of protection'''
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        
     
    def __validate_positives(self, value, attribute_name):
        '''adding a layer of protection'''
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    '''adding a layer of protection'''
    @property
    def width(self):
        '''adding a layer of protection'''
        return self.__width
    


    '''width setter -Using getters and setters provides a 
    way to validate and control the assignment of values to the attributes, 
    adding a layer of protection'''

    @width.setter
    def width(self, value):
        ''' and then calling those validation methods in the property setters'''
        self.__validate_integers(value, 'width')
        self.__validate_positives(value, 'width')
        self.__width = value

    '''height getter - Using getters and setters provides a 
    way to validate and control the assignment of values to the attributes, 
    adding a layer of protectionmm '''
    @property
    def height(self):
        '''adding a layer of protection'''
        return self.__height

    '''height setter - Using getters and setters provides a 
    way to validate and control the assignment of values to the attributes, 
    adding a layer of protection'''
    @height.setter
    def height(self, value):
        ''' and then calling those validation methods in the property setters'''
        self.__validate_integers(value, 'height')
        self.__validate_positives(value, 'height')
        self.__height = value

    '''x getter- Using getters and setters provides a 
    way to validate and control the assignment of values to the attributes, 
    adding a layer of protection'''
    @property
    def x(self):
        '''adding a layer of protection'''
        return self.__x

    '''x setter - Using getters and setters provides a 
    way to validate and control the assignment of values to the attributes, 
    adding a layer of protection'''
    @x.setter
    def x(self, value):
        ''' and then calling those validation methods in the property setters'''
        self.__validate_integers(value, 'x')
        self.__validate_positives(value, 'x')
        self.__x = value

    ''' y getter - Using getters and setters provides a 
    way to validate and control the assignment of values to the attributes, 
    adding a layer of protection'''
    @property
    def y(self):
        '''adding a layer of protection'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' and then calling those validation methods in the property setters'''
        self.__validate_integers(value, 'y')
        self.__validate_positives(value, 'y')
        self.__y = value