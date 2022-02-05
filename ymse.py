#test loops
import os

#clear the console and start the programme
def empty():
    os.system('clear')
    print(' ... Start the engine! ...')
    print()
    return

#normall loop
def normal_loop(y):
    sq = []
    for x in range(y):
        sq.append(x**2)
    return sq

#looping thru list comprehension
def list_comp(y):
    sq = [x**2 for x in range(y)]
    return sq 

def do_main():    
    #no of iterations
    iter = 10
    
    #normal loop
    sq = normal_loop(iter)
    print('normal loop        -> ', sq)
    
    #list comprehension
    sqX = list_comp(iter)
    print('list comprehension -> ', sqX)
    
    print('')
    return

#let's start
if __name__ == '__main__':
    empty()
    do_main()