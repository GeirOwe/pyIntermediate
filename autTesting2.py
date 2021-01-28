#automated testing with pytest from separate TestClass
#defined in test_automation.py

import os

#start function
def square(x):
    return x * x
#end function

#start function
def inc(x):
    return x + 1
#end function

#this is initialized only when this program is run directly, not when it is called from another program
if __name__ == '__main__':
    os.system('clear')
    print('.. wake up geir owe ..\n')
    number = int(input('tall: '))
    sq = square(number)
    print('kvadratet av ',number, ' er ', sq, '\n')
    print('.. og økt med 1 så er tallet blitt til', inc(number))