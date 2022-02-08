#test loops
import os
import csv

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

def do_loops():    
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

class Car():
    def __init__(self, brand, vintage, price):
        self.brand = brand
        self.vintage = vintage
        self.price = price
        return

    def get_brand(self):
        return self.brand

    def get_vintage(self):
        return self.vintage

    def get_price(self):
        return self.price
    
    def set_mileage(self, mileage):
        self.mileage = mileage
        return 
    
    def get_mileage(self):
        return self.mileage

#create Car object and add to list of Car objects
def create_car(brand, vintage, price, carObjList):
    carObj = Car(brand, vintage, price)
    carObjList.append(carObj)
    return carObjList

def store_data(carObjList):
    filename = 'cars.csv'
    header = ['Merke', 'Årgang', 'Pris', 'Kmstand']
    #data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
    #build datarows
    data = []
    i = 0
    while i < len(carObjList):
        datarow = []
        datarow.append(carObjList[i].get_brand())
        datarow.append(carObjList[i].get_vintage())
        datarow.append(carObjList[i].get_price())
        datarow.append(carObjList[i].get_mileage())
        data.append(datarow)
        i += 1

    #store data in a csv file
    with open(filename, 'w', newline="") as file:
        csvwriter = csv.writer(file) # 2. create a csvwriter object
        csvwriter.writerow(header) # 4. write the header
        csvwriter.writerows(data) # 5. write the rest of the data

    return

def do_objects():
    #keep all Car objects in a List
    carObjList = []
    #ceate new Car objects
    carObjList = create_car('macan', '2017', '660000', carObjList)
    carObjList = create_car('i3', '2018', '300000', carObjList)
    
    #get / set some info on Car objects
    carObjList[1].set_mileage('38000')
    carObjList[0].set_mileage('75000')
    print('pris ', carObjList[0].get_brand(), ': ', carObjList[0].get_price())
    print('km ', carObjList[1].get_brand(), ': ', carObjList[1].get_mileage())

    #store the data
    store_data(carObjList)
    return

def read_cars_from_file():
    file = open("cars.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    #print(header)
    #add cars to a list of Car objects
    carObjList = []
    for row in csvreader:
        carObjList = create_car(row[0],row[1], row[2], carObjList)
    file.close()
    
    #get / set some info on Car objects
    carObjList[1].set_mileage('38000')
    carObjList[0].set_mileage('75000')
    print('pris ', carObjList[0].get_brand(), ': ', carObjList[0].get_price())
    print('km ', carObjList[1].get_brand(), ': ', carObjList[1].get_mileage())
    print()

    return

#let's start
if __name__ == '__main__':
    empty()
    #do_loops()
    #do_objects()
    read_cars_from_file()
