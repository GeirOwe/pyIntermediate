# Excerise 2
# Write a program that reads input from the user until the user 
# types an integer. In case the user types a single q, the program should quit.

#exception handling Class
class Xeption:
    def __init__(self):
        return

    def check_if_int(self, xInput):
        value = 5
        sum = 0
        try:
            sum = value + int(xInput)        # Type Error hvis xInput ikke er en int
        except ValueError:
            print('Value error - kun integer aksepteres')
        except TypeError:
            print('Type error, convert input to int in code')
        else:
            print('inputs is integer as expected')
        finally:
            print('The input: ', xInput)
        return xInput
#end class

# get input from user
xInput = input('enter integer or "q" for quit: ')

# check if integer
while xInput.lower() != 'q':
    print('not "q" yet .....')
    thisClass = Xeption()
    thisClass.check_if_int(xInput)
    xInput = input('enter integer or "q" for quit: ')
