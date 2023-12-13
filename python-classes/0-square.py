# the class Square

 
class Square:
    # specifying the attribute __init__ 
    def __init__(self, size):
        # initialize a square instance. parameter - size with no type / value verification was used
        
        self.__size = size
        
    
    # define the getter
   
    def get_size(self):
        return self.__size