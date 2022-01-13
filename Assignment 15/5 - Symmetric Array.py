print(".:: Symmetric Array ::.\n")
print("Please enter your Array :")
array = list(map(int, input("Array = ").split()))
#array = [1,2,3,2,1]
symmetric = True 
for i in range(len(array)):
    if array[i] != array[-i-1]:
        symmetric = False

if symmetric :
    print("\nThis array is symmetric")
else:
    print("\nThis array is NOT symmetric")