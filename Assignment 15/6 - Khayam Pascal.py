print(".:: Khayam Pascal ::.\n")
print("Please enter N :")
n = int(input("N = "))
khayam = [[1]]

for i in range(1,n):
    array = [1]
    for j in range(len(khayam[i-1])-1):
        array.append(khayam[i-1][j] + khayam[i-1][j+1])
    array.append(1)
    khayam.append(array)

print("\nKhayam :\n")

for i in range(0,n):
    for j in range(len(khayam[i])):
        print(khayam[i][j],end="\t")
    print()
