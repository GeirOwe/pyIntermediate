# error handling and exceptions

import os
from os import path

#start function
def count_lines_in_file(filename : str) -> int:
    return len(open(filename, 'r').readlines())
#end function

#start function
def int_divide(a: int, b:int) -> int:
    if b == 0:
        return 0  # ?? ... that's not correct‽
    return a//b
#end function

#ok let's go!
os.system('clear')
print()

#the file
xFile = 'day12019_puzzle_input.txt'

#find the number of rows in the file
if path.exists(xFile):
    # between line 1 and 3, the file could be deleted, the filesystem unmounted
    wc = count_lines_in_file(xFile)
    print('antall rader i filen er ', wc)

#the floor division // rounds the result down to the nearest whole number
left = int_divide(5, 2)
print(left)

#exception handling
def throwing(n):
    value = float('inf')
    try:
        value = 5/n
    except ZeroDivisionError:
        print('Division by zero')
    else:
        print('Divided successfully')
    finally:
        print('Returning', value)
    return value

result = throwing(3)