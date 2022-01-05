print('.:: WELCOME ::.')
print("\nPlease enter circle's radius")
r = float(input('R = '))
pi = 3.14

if 0<r :
    p = 2*pi*r
    a = pi*r**2
    print('\nPerimeter = ' + str(p))
    print('Area = ' + str(a))
else:
    print("[ERROR] : Circle's radius should be greater than 0 !")
