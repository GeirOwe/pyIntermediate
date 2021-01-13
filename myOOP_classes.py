#define object
class Wine():
    def __init__(self, name, wtype, characteristics, country, district, subdistrict, 
                    vintage, producer, price, drinkafter, drinkbefore, score, bottles, privatscore, grape):
        self.name = name
        self.wtype = wtype
        self.characteristics = characteristics
        self.country = country
        self.district = district
        self.vintage = vintage
        self.producer = producer
        self.price = price
        self.drinkafter = drinkafter
        self.drinkbefore = drinkbefore
        self.score = score
        self.bottles = bottles
        self.privatscore = privatscore
        self.grape = grape
    
    #the name of the wine
    def get_name(self):
        return self.name

    #the cost of the wine
    def get_price(self):
        return self.price
    
    #number of bottles of this wine
    def get_no_of_bottles(self):
        return self.bottles
#end class definition

#define class
class Cellar():
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.wineList = [] #contains all wine objects
    
    #the name of the Cellar
    def get_name(self):
        return self.name
    
    #number of bottles in cellar
    def get_no_of_bottles(self):
        bottles = 0
        #for all the wines in the wineList
        for wine in self.wineList:
            bottles += wine.get_no_of_bottles()
        return bottles

    #remaining capacity in Cellar
    def remain_capacity(self):
        totalBottles = 0
        for wine in self.wineList:
            totalBottles += wine.get_no_of_bottles()
        return self.max_capacity - totalBottles

    #add wine to cellar
    def add_wine(self, wine):
        if len(self.wineList) < self.max_capacity:
            self.wineList.append(wine)
            return True
        return False

    #calc avg price of all wines in cellar
    def avg_cost(self):
        cost = 0
        for wine in self.wineList:
            cost += wine.get_price()
        return cost // len(self.wineList)
#end class definition