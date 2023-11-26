#some code snippets from the beginning python book
import os

#start function
def clear_console():
    os.system('clear')
    print('----------------------------\n')
#end function

#start the programme
def main_module():
    clear_console()
    print('\n')
#end main programme

#test if this is the main programme, or if this code is imported into another main programme
if __name__ == '__main__':
    main_module()