print('Please enter the number you want to check if it is a factorial :')
n=int(input('n = '))

x=1
i=1
fact=False
while x <= n:
    if x == n:
        fact =True
    
    x *= i
    i += 1

if fact:
    print("\nYES it is a Factorial number!")
else:
    print("\nNO it is NOT a Factorial number!")





