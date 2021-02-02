#more OOP
import os

#start class definition
class Car:
    def __init__(self):
        pass
        
    def set_name(self, brand):
        self.brand = brand

    def set_type(self, type):
        self.type = type

    def set_model(self, model):
        self.model = model

    def set_km(self, km):
        self.km = km

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.brand

    def get_type(self):
        return self.type

    def get_km(self):
        return self.km

    def get_model(self):
        return self.model
    
    def get_price(self):
        return self.price

#end class definition

#start function
def get_data_about_car(myCar):
    myCar.set_name('volvo')
    myCar.set_type('V90-T8')
    myCar.set_model(2018)
    myCar.set_km(27000)
    myCar.set_price(450000)
#end function

#start function
def print_data_about_car(myCar):
    print(myCar.get_name(), myCar.get_type(), myCar.get_model(), 'som er kjørt', 
            myCar.get_km(), ' koster ', myCar.get_price())
#end function

#start function
def clear_console():
    os.system('clear')
    print('----------------------------\n')
#end function

#start the programme
def main_module():
    clear_console()
    myCar = Car()
    get_data_about_car(myCar)
    print_data_about_car(myCar)
    print()
#end main programme

#test if this is the main programme, or if this code is imported into another main programme
if __name__ == '__main__':
    main_module()