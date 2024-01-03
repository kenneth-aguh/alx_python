'''Import the base module'''
from base import Base

'''
The Rectangle class inherits from the Base class
'''
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        '''call the super class with id'''
        super().__init__(id)
        '''assign each argument to the right attribute'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    '''width getter'''
    @property
    def width(self):
        return self.__width

    '''width setter'''
    @width.setter
    def width(self, value):
        self.__width = value

    '''height getter'''
    @property
    def height(self):
        return self.__height

    '''height setter'''
    @height.setter
    def height(self, value):
        self.__height = value

    '''x getter'''
    @property
    def x(self):
        return self.__x

    '''x setter'''
    @x.setter
    def x(self, value):
        self.__x = value

    ''' y getter'''
    @property
    def y(self):
        return self.__y

    '''y setter '''
    @y.setter
    def y(self, value):
        self.__y = value