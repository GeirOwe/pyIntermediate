# closures
# closure is a nested function which has access to a free variable from an 
# enclosing function that has finished its execution. 
# Three characteristics of a Python closure are: 
# it is a nested function. it has access to # a free variable in outer scope. 
# it is returned from the enclosing function.

import os

# start class
class Fun:
    def __init__(self):
        return

    def inner(self):
        a = 2
        print('variable "a" from the inner function: ', a)
        return

    def outer(self, a):      
        self.inner()
        print('variable "a" from the outer function: ', a)
        return
#end class

# start function
def hilarious(x):
    #this is what is called closure - see expl at the top
    def inner_h():
        a = 2
        print('variable "a" from the inner function: ', a)
        print('variable "x" from the outer function: ', x)
    
    inner_h()
    return
# end function

# ---- start of program ----
os.system('clear')
print('      -- let the game begin! --')
print()

#call class
x = Fun()
x.outer(5)
print('      ..')

#call function
hilarious(5)
print('      ..')