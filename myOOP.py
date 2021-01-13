#my oop
#les vinkjeller fil inn i ett objekt

import os
import pandas as pd
import csv
from myOOP_classes import Cellar 
from myOOP_classes import Wine

# read the CSV file into a dataframe
def read_data():
    df = pd.read_csv('vinkjeller.csv', sep=';', encoding = 'utf8')
    #and replace 'nan' with zero or space
    df['privatscore'] = df['privatscore'].fillna(0)
    return df
#end function

#start of program
if __name__ == '__main__':
    os.system('clear')
    print('----------------------------')
    print()

    cellar = Cellar('VINSKAPET', 70)    # prepare the wine cellar
    wineDF = read_data()                # get wines from the data base 
    wineList = []                       # the list will hold all wine objects in data base
    
    #create objects of all wines and add to the wine cellar
    for idx, row in wineDF.iterrows(): 
        #create the wine object
        wine = Wine(row['name'], row['type'], row['characteristics'], row['country'], row['district'], 
                    row['subdistrict'], row['vintage'], row['producer'], row['price'], row['drinkafter'],
                    row['drinkbefore'], row['score'], row['bottles'], row['privatscore'], row['grape'])
    
        #add wine to cellar and list of wines
        cellar.add_wine(wine)
        wineList.append(wine)

    # print info on first & last wine.
    # expect opus one & fontalloro to be printed
    print(wineList[0].get_name(), ' koster ', wineList[0].get_price(), ',-')
    print(wineList[-1].get_name(), ' koster ', wineList[-1].get_price(), ',-')
    print('Snittpris på de ', cellar.get_no_of_bottles(),  ' flaskene med vin i skapet er ', cellar.avg_cost(), ',-')
    print('Ledig kapasitet i ', cellar.get_name(), ' er ', cellar.remain_capacity())

    #the end
    print()