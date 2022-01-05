print('Please enter the number you want to check if it is an Armstrong number :')
n = input('n = ')
digits = len(n)

x = 0

for i in range(digits):
    x += int(n[i]) ** digits

if x == int(n):
    print('\nYES it is an Armstrong number!')
else:
    print('\nNO it is NOT an Armstrong number!')


