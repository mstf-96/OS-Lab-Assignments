print('Please enter table dimentions :')
n = int(input('N = '))
m = int(input('M = '))
a=[]

for i in range(n):
    if i % 2 == 0:
        s = '#*' * (m//2)
        if m % 2 == 1:
            s+='#'
    else :
        s = '*#' * (m//2)
        if m % 2 == 1:
            s+='*'
    
    a.append(s)

for i in range(n):
    print(a[i])
