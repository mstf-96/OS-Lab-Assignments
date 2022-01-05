print('.:: Checking if an array is sorted in ascending order ::.')
print('\nPlease enter your numbers with a space between them and then press Enter :')
nums = input('Array = ')
array = nums.split(' ')
n = len(array)
sorted=True

i = 1
while i < n:
    if int(array[i-1])>int(array[i]):
        sorted = False
        break
    i += 1

if sorted :
    print("\nYES this array is sorted in ascending order")
else :
    print("\nNO this array is NOT sorted in ascending order")
