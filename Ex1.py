# Exercises ch 1

import os

#Iterate over lists
print('Iterate over lists')
myList = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
sum = 0
for x in myList:
    if i>0:
        sum = myList[i] + myList[i-1]
    else:
        sum = sum + x
    i = i +1
print(sum)
print()

#Iterate over sets
mySet = set('12345678')
print('Iterate over Set')
sum = 0
for x in mySet:
    sum = sum + int(x)
print(sum)
print()

#Iterate over tuples
myTuple = (1, 2, 3, 4, 5, 6, 7, 8)
print('Iterate over tuple')
i = 0
sum = 0
for x in myTuple:
    if i>0:
        sum = myTuple[i] + myTuple[i-1]
    else:
        sum = sum + x
    i = i +1
print(sum)
print()

#Iterate over strings
myString = '12345678'
print('Iterate over string')
i = 0
sum = 0
for x in myString:
    if i>0:
        sum = int(myString[i]) + int(myString[i-1])
    else:
        sum = sum + int(x)
    i = i +1
print(sum)
print()

# Iterate over dicts using raw iteration, over dict.keys and dict.items
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
svar = input('Iterate over dict: ')
if svar.upper() == 'Y':
    i = 0
    sum = 0
    print('key : value')
    for key in myDict:
        print(key, ': ', myDict[key])
    print('keys')
    for key in myDict.keys():
        print(key)
    print('values')
    for value in myDict.values():
        print(value)
    print('items')
    for item in myDict.items():
        print(item)
else:
    os.system('clear')

#Iterate over dict.items with tuple unpacking. 
for k, v in myDict.items():
    print(k, v)

# What happens when you use zip(*dict.items())?
print(myDict.items())
#print(zip(*myDict.items())) #it returns the zip object adress

# Create a class whose instances are iterable using __getitem__. 
# Raise IndexError when you have no more items.
class Dictionary:
    def __init__(self):
        self.dictionary = {'a' : 1, 'b' : 2, 'c': 3}

    def __getitem__(self,key):
        try:
            xKey = self.dictionary[key]
        except IndexError:
            raise StopIteration
        return xKey

    def __iter__(self):
        return iter(self.dictionary)

a = Dictionary()
for i in a:
    print(i, end = " ")