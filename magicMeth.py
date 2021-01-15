# The magic methods are used to construct and initialise new objects, they help us 
# retrieve an object as a dictionary, they are used to delete an object amongst other 
# operations. They are used when the + operator is invoked, or even when we want to represent an 
# object as a string. This implies that magic methods are intended to be private 
# methods. It also means that the caller of an object should not invoke the method 
# directly as the method is intended to be invoked by the class internally that has 
# the magic method.
# However, we can override the magic methods to provide our own custom functionality.

class Human:
    def __init__(self, id, name, addresses=[], maps={}):
        self.id = id
        self.name = name
        self.addresses = addresses
        self.maps = maps

    # We can override the dir() method by overriding the __dir__() method in the class. 
    def __dir__(self):
        return list(filter(lambda x: not x.startswith('_'), object.__dir__(self)))
    
    # The __str__() method is executed when we want to print an object in a printable format. 
    def __str__(self):
        return f'id={self.id}. name={self.name}'

#start of programme
import os
os.system('clear')

human = Human(1, 'Geir Owe', ['Sandestien', 'Sola'], {'Rogaland':2, 'Norge':3})
print(human)
human = Human(2, 'Ronja', ['Fyllingen', 'Bergen'], {'Hordaland':1, 'Norge':3}).__dict__
print(human)

# We can override the dir() method by overriding the __dir__() method in the class.
print(dir(human))

#print(dir(human))
#output: 
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', 
# 'addresses', 'id', 'maps', 'name'] --> expect for these attributes, the rest are magic methods.
# we are used to override __int__(), not so much the others

# The purpose of outlining the key magic methods is for us to understand whether we want to override 
# these methods in our custom classes to enrich the applications.