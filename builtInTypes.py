# get to know the python built-in-types
# https://docs.python.org/3/library/stdtypes.html

import os
os.system('clear')
print(' here we go')
print('------------\n')

# check out: x in y
x = 'hets'
s = 'es'
if s in x:
    print(s, ' is in ', x)
else:
    print(s, ' is NOT in ', x)
print()

#helper function to add a space betwen each char
def add_space(xOrigin):
    pos = 0
    end = len(xOrigin) 
    xModified = []
    while pos < end:
        xModified.append(xOrigin[pos] + ' ')
        pos = pos +1
    return xModified
#end function

#split
myList2 = add_space(x)
myList = x.split()
print('from string "%(param)s" to list: ' % {'param': x} , myList, ' & ', myList2)

#.. and concatnate
y = ''
myString = y.join(myList)
myString2 = y.join(myList2)
print('.. and back from list to a string: ', myString, ' & ', myString2)

# print formatted
#the % operator (modulo). This is also known as the string formatting or 
# interpolation operator. Given "format % values" (where "format" is a string), 
# % conversion specifications in format are replaced with zero or more 
# elements of values. 
print()
print('print f.o.m. andre til tredje bokstav av "%(param)s": ' % {'param': x}, 
    '"...',x[1:3], '..."' )
print()