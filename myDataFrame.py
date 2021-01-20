# practicing dataframe w pandas and numpy

import pandas as pd
import numpy as np
import os

# ----------------------------------------
#start of the main part of the programme
# ----------------------------------------
os.system('clear')
print('\n ------- wake up gary owen ------- \n')

#use pandas to read the csv file into a DataFrame
polls = pd.read_csv('data/covid_concern_polls_adjusted.csv', low_memory=False)
pollsagg = polls[['very', 'somewhat', 'not_very', 'not_at_all']].agg('mean')
print('how concerned are americans about covid-19?\n') 
print(pollsagg)
print('\ndeltakere i spørreundersøkelsen: ', int(polls['samplesize'].sum()), '\n')
#confPolls = polls[polls['very'] > 40]
#print(confPolls.head())
#print()
#for i, v in snitt.items():
#    print(i, float("{:.2f}".format(v)))

print('\n ------- over til vin og TOPPLISTEN -------\n')
#over til vin
vin = pd.read_csv('data/vinkjeller.csv', sep=';', encoding = 'utf8')
#and replace 'nan' with zero or space
#vin['privatscore'] = vin['privatscore'].fillna(0)
#print(vin.head())
#       subset some rows
drikkNu = vin[(vin['bottles'] > 0) & (vin['drinkafter'] <= 2021)]
drikkNu = drikkNu.sort_values(['score', 'privatscore'], ascending=[False, False])
print(drikkNu, '\n')

#lag en liste
vinListe = []
for idx, row in drikkNu.iterrows():
    vinListe.append(row['name'])

#list comprehension
[print(x) for x in vinListe]