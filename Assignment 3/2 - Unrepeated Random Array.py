import random
print('Please enter the length of array :')
n = int(input('N = '))
array=[]
i =0
while True:
    x = random.randint(-5*n,5*n)
    if x not in array:
        array.append(x)
        i+=1
    
    if i>=n:
        break

print("random array =",array)

