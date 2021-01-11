# trying out lambdas

import os
os.system('clear')

# a list of tuples
tuples = [(1, 'x'), (3, 'a'), (66, 'k'), (2, 'b')]
print('the list of tuples')
print(tuples, '\n')

# lambda ='single expression function' with an implicit retrn statement
# lambda = is an inline function without the 'def'
# but, be CAREFUL - lambdas can mak the code hard to read
xSort = sorted(tuples, key=lambda z: z[1], reverse=False)
print('hele listen - tuples er sortert på char: ', xSort, '\n')
#[(3, 'a'), (2, 'b'), (66, 'k'), (1, 'x')] 
#The sorted() function returns a sorted list of the specified iterable object.
#sorted(iterable, key=key, reverse=reverse)

#another case where lambda should not be used
result2 = sorted([x[0] for x in tuples])
print('kun tallene, sortert: ', result2, '\n')
#[1, 2, 3, 66] 

#another case where lambda should not be used
result = [x for x in range(10) if x % 2 == 0]
#print(result, '\n')
#[0, 2, 4, 6, 8] 