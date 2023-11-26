#some code snippets from the beginning python book
import os
import matplotlib.pyplot as plt

#start function
def clear_console():
    os.system('clear')
    print('----------------------------\n')
#end function

#a database in a form of a dict
def create_dict():
    people = {
        'alice': {
            'phone': '2341',
            'addr': 'foo drive 23'
        },
         'beth': {
            'phone': '9102',
            'addr': 'bar street 42'
        },
         'cecil': {
            'phone': '3158',
            'addr': 'baz avenue 90'
        }
    }
    return people

def create_labels():
    labels = {
        'phone': 'phone number',
        'addr': 'adress'
        }
    return labels 

def do_some_dict():
    #a database in a form of a dict
    people = create_dict()
    labels = create_labels()
    name = input('name: ').lower()
    request = input('phone number(p) or adress(a)? ')
    #use the input to find the correct data
    key = request
    if request == 'p': key = 'phone'
    if request == 'a': key = 'addr'

    #use get to find the data
    person = people.get(name, {})
    label = labels.get(key, key)
    result = person.get(key, 'not available')
    print("{}'s {} is {}.".format(name, label, result))

    for k, v in people.items():
        print(k, 'corresponds to', v)
    return

def do_fibonacci():
    #generate the fibonacci sequence with y numbers
    y = int(input('hvor mange tall i fibonacci sequence: '))
    fib_seq_list = []
    fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
    fib_seq = (fib(i) for i in range(y))
    for number in fib_seq:
        fib_seq_list.append(number)

    # presenter resultat som ett pyplot
    # x akse
    x = list(range(y))
    #foreta plot
    plt.plot(x, fib_seq_list, marker='o', linestyle='-')
    #tittel
    plt.title('fibonacci by geirowe')
    #show plot
    plt.show
    return

#start the programme - useful icons {} []
def main_module():
    clear_console()
    do_some_dict()
    #do_fibonacci()
    print('\n')
#end main programme

#test if this is the main programme, or if this code is imported into another main programme
if __name__ == '__main__':
    main_module()