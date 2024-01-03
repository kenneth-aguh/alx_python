'''
This class can serve as the base class for other classes in your project,
managing the id attribute in a consistent way across different classes

'''

class Base:
    # private class attribute
    __nb_objects = 0

    '''
    The __init__ method (class constructor) initializes the instance 
    with a provided id or increments __nb_objects and assigns 
    the new value to the id attribute if id is not provided.
    '''

    def __init__(self, id=None):
        # class constructor
        if id is not None:
            '''assign the public instance attribute id with 
            the argument value'''
            self.id = id
        else:
            '''increment __nb_objects and assign the new value to the 
            public instance attribute id'''
            Base.__nb_objects += 1
            self.id = Base.__nb_objects