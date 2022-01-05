print('.:: Converting Time to Seconds ::.')
print('\nPlease enter Time in this format hours:minutes:seconds')
time = input('Time = ')
a = time.split(':')

result = int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2])

print('Result = '+ str(result))