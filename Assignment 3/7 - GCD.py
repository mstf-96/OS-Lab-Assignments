print(".:: Greatest Common Divisor ::.")
print("\nPlease enter two non zero numbers :")
a = int(input('First number = '))
while a==0:
    print('number can not be 0 !')
    a = int(input('First number = '))

b = int(input('Second number = '))
while b==0:
    print('number can not be 0 !')
    b = int(input('Second number = '))

min = min(abs(a),abs(b))
gcd=1

for i in range(min , 0 , -1):
    if(a % i==0)and (b % i==0):
        gcd=i
        break

print("\nGCD("+ str(a)+" , "+str(b)+") =",gcd)

