print('.:: WELCOME ::.')
print('\nPlease enter height in meter and weight in kilogram.')
w = float(input('Weight [kg] = '))
h = float(input('Height [meter] = '))
if 0<h and 0<w:
    bmi = w/(h*h)
    print('\nBMI = ' + str(bmi))
    if bmi<18.5 :
        print('Underweight')
    elif 18.5<= bmi and bmi<25 :
        print('Normal')
    elif 25<= bmi and bmi<30 :
        print('Overweight')
    elif 30<= bmi and bmi<35 :
        print('Obese')
    elif 35<= bmi :
        print('Extremely Obese')
else:
    print('[ERROR] : height and weight should be greater than 0 !')


