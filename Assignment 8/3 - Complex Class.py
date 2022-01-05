class Complex:

    def __init__(self,real=0,imaginary=0):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self,other):
        if not isinstance(other, Complex):
            raise TypeError
        result = Complex()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result
    
    def __sub__(self,other):
        if not isinstance(other, Complex):
            raise TypeError
        result = Complex()
        result.real = self.real - other.real
        result.imaginary = self.imaginary - other.imaginary
        return result
    
    def __mul__(self,other):
        if not isinstance(other, Complex):
            raise TypeError
        result = Complex()
        result.real = self.real * other.real - self.imaginary * other.imaginary
        result.imaginary = self.real * other.imaginary + self.imaginary * other.real
        return result
    
    def __truediv__(self,other):
        if not isinstance(other, Complex):
            raise TypeError
        result = Complex()
        result.real = (self.real * other.real + self.imaginary * other.imaginary) / (other.real**2 + other.imaginary**2)
        result.imaginary = (self.imaginary * other.real - self.real * other.imaginary)  / (other.real**2 + other.imaginary**2)
        return result
    
    def __str__(self):
        if self.real==0 and self.imaginary != 0:
            str(self.imaginary) + '(i)'
        if self.imaginary < 0:
            return str(self.real) + ' - ' + str(abs(self.imaginary)) + '(i)'
        elif self.imaginary == 0:
            return str(self.real)
        elif self.imaginary > 0:
            return str(self.real) + ' + ' + str(abs(self.imaginary)) + '(i)'

#-------------------------------------------------------------------
    
def get_complex():
    r = float(input('Real = '))
    i = float(input('Imaginary = '))
        
    return Complex(r,i)

#-------------------------------------------------------------------

while True:
    print('.:: Complex Numbers ::.\n')
    print('1. Add \n2. Subtract \n3. Multiply\n4. Division\n5. Exit')
    opt=int(input('Your choice = '))
    
    while not (1 <= opt <=5):
        print('Please enter a number between 1 and 5 !')
        opt=int(input('Your choice = '))
    
    if opt==5:
        print('\nGoodbye !\n')
        break

    print('\nEnter Complex Number 1 :')
    a = get_complex()
    print(a)
    print('\nEnter Complex Number 2 :')
    b = get_complex()
    print(b)
        
    if opt==1 :
        print('('+str(a)+') + ('+str(b)+') = '+ str(a + b))
    elif opt==2:
        print('('+str(a)+') - ('+str(b)+') = '+ str(a - b))
    elif opt==3:
        print('('+str(a)+') * ('+str(b)+') = '+ str(a * b))
    elif opt==4:
        print('('+str(a)+') / ('+str(b)+') = '+ str(a / b))
    input('\nPress ENTER to Continue...\n')