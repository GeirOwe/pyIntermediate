# decorators

import os

def logging(func):
    def wrapper():
        msgB = func()
        print(msgB.upper())
        msgA = 'a timestamp has been added to the log'
        return msgA
    return wrapper

@logging
def do_an_event():
    msgB = 'event performed .......'
    return msgB

os.system('clear')
print('\n ------- wake up gary owen ------- \n')

print(do_an_event())
