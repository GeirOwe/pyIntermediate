#a bit more OOP practice
import os

#start class
class GolfBane():
    def __init__(self, name, hull):
        self.name = name,
        self.hull = hull
    
    #the name of the golf course
    def get_name(self):
        return self.name
    
    #the name of the golf course
    def get_hull(self):
        return self.hull
#class end

#start function
def clear_console():
    os.system('clear')
    print('----------------------------\n')
#end function

#function start
def prepare_golfbaner():
    baneListe = []                       # the list will hold all wine objects in the data base
    endaEnBane = True
    while endaEnBane:
        nyBane = input('golf bane: ')
        if nyBane.upper() == 'Q':
            endaEnBane = False
        else:
            hull = str(input('antall hull: '))
            bane = GolfBane(nyBane, hull)
            baneListe.append(bane)
    return baneListe
#function end

#start the programme
def main_module():
    clear_console()
    baneListe = prepare_golfbaner()
    print(baneListe[0].get_name(), ' har ', baneListe[0].get_hull(), ' hull.')
#end main programme

#test if this is the main programme, or if this code is imported into another main programme
if __name__ == '__main__':
    main_module()