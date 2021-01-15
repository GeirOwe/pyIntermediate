# A program’s control flow is the order in which the program’s code executes. 
# The control flow of a Python program is regulated by conditional statements, 
# loops, and function calls. This section covers the if statement and for and 
# while loops; functions are covered later in this chapter. Raising and handling 
# exceptions also affects control flow.

import os
os.system('clear')
print(' ........ wake up gary o .......')
print()

# good ways to iterate over key and values in a dictionary
myDict = {'opus one':1, 'esprit de chevalier':6, 'fontodi':7}
for key, value in myDict.items():
    print(key, ' - ', value)
print('')
#myDict[key] = value
myDict['fontalloro'] = 0
# .. or like this ... same result
for key in myDict.keys():
    print(key, ' - ', myDict[key])
print('')

#lists
myList = ['opus one', 'esprit de chevalier', 'fontodi']
x = 0
while x < len(myList):
    print(myList[x])
    x += 1
myList.append('fontalloro')
print(myList[-1])
print('')

