#automated testing with doctest
import os

#start function
def square(x):
    '''
    Tar square av ett tall dvs x2, x i andre

    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x * x
#end function

#main program
def start_main():
    number = int(input('tall:'))
    sq = square(number)
    print('kvadratet av ',number, ' er ', sq)

#this is initialized only when this program is run directly, not when it is called from another program
if __name__ == '__main__':
    os.system('clear')
    print('.. wake up geir owe ..\n')
    import doctest, autTesting
    doctest.testmod(autTesting)
    start_main()