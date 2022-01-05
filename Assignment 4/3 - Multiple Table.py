print('Please enter table dimentions :')
n = int(input('N = '))
m = int(input('M = '))

table = []

for i in range(n):
    x = []
    for j in range(m):
        x.append((i+1)*(j+1))
    table.append(x)

for i in range(n):
    for j in range(m):
        print(table[i][j],end="\t")
    print()