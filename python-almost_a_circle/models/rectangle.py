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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__width = value
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__width = value
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__width = value
        self.__y = value