print('.:: Fibonacci Sequence ::.')
n = int(input('\nN = '))

fib=[0,1]

for i in range(2,n):
    x = fib[i-1] + fib[i-2]
    fib.append(x)

fib = tuple(fib)

print()
for i in range(n):
    print(fib[i],end='\t')
