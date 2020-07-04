'''Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.'''


names = ['ram','shyam']
for name in names:
    if name == 'John':
        print('John is in name list')
    else:
        print('Not Found')