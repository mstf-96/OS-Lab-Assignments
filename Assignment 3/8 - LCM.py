print(".:: Least Common Multiple ::.")
print("\nPlease enter two non zero numbers :")
a = int(input('First number = '))
while a==0:
    print('number can not be 0 !')
    a = int(input('First number = '))

b = int(input('Second number = '))
while b==0:
    print('number can not be 0 !')
    b = int(input('Second number = '))

max = max(abs(a),abs(b))
min = min(abs(a),abs(b))
lcm = max
for i in range(max , max * min +1 , max):
    if (i % a ==0 )and (i % b ==0 ):
        lcm = i
        break


print("\nLCM("+ str(a)+" , "+str(b)+") =",lcm)