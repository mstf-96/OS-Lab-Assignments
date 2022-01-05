import math 
from os import system, name

def clear():
      if name == 'nt':
        _ = system('cls')
      else:
        _ = system('clear')

while True :

    print (".:: Calculator ::.")
    print("\nPlease choose one of the options and enter it's number :")
    print ("1. Sum")
    print ("2. Sub")
    print ("3. Mul")
    print ("4. Div")
    print ("5. Sin")
    print ("6. Cos")
    print ("7. Tan")
    print ("8. Cot")
    print ("9. Log")
    print ("0. Exit")
    opt = int(input('\nYour choice = '))
    while not ((0<=opt) and (opt<=9)):
        print("\nInvalid input ! . Please Choose one of the options and enter it's number :")
        opt = int(input('Your choice = '))

    if opt == 1 :
        a = float(input ("First number = "))
        b = float(input ("Second number = "))
        print(str(a)+' + '+str(b)+' = '+str(a+b))
    
    elif opt == 2 :
        a = float(input ("First number = "))
        b = float(input ("Second number = "))
        print(str(a)+' - '+str(b)+' = '+str(a-b))
    
    elif opt == 3 :
        a = float(input ("First number = "))
        b = float(input ("Second number = "))
        print(str(a)+' * '+str(b)+' = '+str(a*b))
    
    elif opt == 4 :
        a = float(input ("First number = "))
        b = float(input ("Second number = "))
        while b==0:
            print('\nCan NOT divide by 0 . please enter another number')
            b = float(input ("Second number = "))
        print(str(a)+' / '+str(b)+' = '+str(a/b))
    
    elif opt == 5 :
        a = float(input ("Angle in degrees = "))
        print('Sin('+str(a)+') = '+str(math.sin(math.radians(a))))

    elif opt == 6 :
        a = float(input ("Angle in degrees = "))
        print('Cos('+str(a)+') = '+str(math.cos(math.radians(a))))

    elif opt == 7 :
        a = float(input ("Angle in degrees = "))
        print('Tan('+str(a)+') = '+str(math.tan(math.radians(a))))

    elif opt == 8 :
        a = float(input ("Angle in degrees = "))
        print('Cot('+str(a)+') = '+str(1/math.tan(math.radians(a))))

    elif opt == 9 :
        a = float(input ("X = "))
        while a==0:
            print('X can Not be 0 enter another number')
            a = float(input ("X = "))
        b = float(input ("Base number = "))
        while b==1:
            print('Base can Not be 1 enter another number')
            b = float(input ("Base number = "))
        print('Log('+str(a)+') in Base '+str(b)+' = '+str(math.log(a, b)))
    
    elif opt==0:
        print('\nGoodbye !')
        break

    print('-----------------------------------------')
    input('Press ENTER to continue ... ')
    clear()
