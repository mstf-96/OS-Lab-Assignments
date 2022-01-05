print('.:: WELCOME ::.')
print('\nPlease enter 3 numbers you want to check if they can make a triangle : ')
a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))

if 0<a and 0<b and 0<c and a<b+c and b<a+c and c<a+b:
    print('Yes these 3 numbers can make a Triangle.')
else:
    print('No these 3 numbers can not make a Triangle.')
