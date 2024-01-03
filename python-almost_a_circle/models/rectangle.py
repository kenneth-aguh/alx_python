'''Import the base module'''
from models.base import Base

'''
The Rectangle class inherits from the Base class.
'''
class Rectangle(Base):
    ''' The class constructor (__init__) calls the super class 
    with the provided id and assigns the other arguments 
    (width, height, x, y) to the appropriate attributes'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''call the super class with id'''
        super().__init__(id)
        '''assign each argument to the right attribute'''
        self.width = width
        '''assign each argument to the right attribute'''
        self.height = height
        '''assign each argument to the right attribute'''
        self.x = x
        '''assign each argument to the right attribute'''
        self.y = y
    '''creating separate methods for integer validation'''
    def __validate_integers(self, value, attribute_name):
        '''lets state the condition for validation'''
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
    '''creating separate methods for positives validation'''
    def __validate_positives(self, value, attribute_name):
        '''lets state the condition for validation'''
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    '''width getter - Using getters and setters provides a way to validate and 
    control the assignment of values to the attributes, 
    adding a layer of protection'''
    @property
    def width(self):
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
        return self.__y

    '''y setter -Using getters and setters provides a 
    way to validate and control the assignment of values to the attributes, 
    adding a layer of protection'''
    @y.setter
    def y(self, value):
        ''' and then calling those validation methods in the property setters'''
        self.__validate_integers(value, 'y')
        self.__validate_positives(value, 'y')
        self.__y = value